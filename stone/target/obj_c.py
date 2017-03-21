from __future__ import absolute_import, division, print_function, unicode_literals

from contextlib import contextmanager

from stone.data_type import (
    is_list_type,
    is_struct_type,
    is_union_type,
    is_nullable_type,
    is_user_defined_type,
    is_void_type,
    unwrap_nullable,
)
from stone.generator import CodeGenerator
from stone.target.obj_c_helpers import (
    fmt_camel_upper,
    fmt_class,
    fmt_class_prefix,
    fmt_import,
)


stone_warning = """\
///
/// Copyright (c) 2016 Dropbox, Inc. All rights reserved.
///
/// Auto-generated by Stone, do not modify.
///

"""

# This will be at the top of the generated file.
base_file_comment = """\
{}\
""".format(stone_warning)


undocumented = '(no description).'


comment_prefix = '/// '


class ObjCBaseGenerator(CodeGenerator):
    """Wrapper class over Stone generator for Obj C logic."""
    # pylint: disable=abstract-method

    @contextmanager
    def block_m(self, class_name):
        with self.block('@implementation {}'.format(class_name), delim=('', '@end'), dent=0):
            self.emit()
            yield

    @contextmanager
    def block_h_from_data_type(self, data_type, protocol=None):
        assert is_user_defined_type(data_type), \
            'Expected user-defined type, got %r' % type(data_type)

        if not protocol:
            extensions = []
            if data_type.parent_type and is_struct_type(data_type):
                extensions.append(fmt_class_prefix(data_type.parent_type))
            else:
                if is_union_type(data_type):
                    # Use a handwritten base class
                    extensions.append('NSObject')
                else:
                    extensions.append('NSObject')

            extend_suffix = ' : {}'.format(
                ', '.join(extensions)) if extensions else ''
        else:
            base = fmt_class_prefix(data_type.parent_type) if (
                data_type.parent_type and not is_union_type(data_type)) else 'NSObject'
            extend_suffix = ' : {} <{}>'.format(base, ', '.join(protocol))
        with self.block('@interface {}{}'.format(
                fmt_class_prefix(data_type), extend_suffix), delim=('', '@end'), dent=0):
            self.emit()
            yield

    @contextmanager
    def block_h(self, class_name, protocol=None, extensions=None, protected=None):
        if not extensions:
            extensions = ['NSObject']

        if not protocol:
            extend_suffix = ' : {}'.format(', '.join(extensions))
        else:
            extend_suffix = ' : {} <{}>'.format(
                ', '.join(extensions), fmt_class(protocol))

        base_interface_str = '@interface {}{} {{' if protected else '@interface {}{}'
        with self.block(base_interface_str.format(
                class_name, extend_suffix), delim=('', '@end'), dent=0):
            if protected:
                with self.block('', delim=('', '')):
                    self.emit('@protected')
                    for field_name, field_type in protected:
                        self.emit('{} _{};'.format(field_type, field_name))
                self.emit('}')
            self.emit()
            yield

    @contextmanager
    def block_init(self):
        with self.block('if (self)'):
            yield
        self.emit('return self;')

    @contextmanager
    def block_func(self, func, args=None, return_type='void', class_func=False):
        args = args if args is not None else []
        modifier = '-' if not class_func else '+'
        base_string = '{} ({}){}:{}' if args else '{} ({}){}'
        signature = base_string.format(modifier, return_type, func, args)
        with self.block(signature):
            yield

    def _get_imports_m(self, data_types, default_imports):
        """Emits all necessary implementation file imports for the given Stone data type."""
        if not isinstance(data_types, list):
            data_types = [data_types]

        import_classes = default_imports

        for data_type in data_types:
            import_classes.append(fmt_class_prefix(data_type))

            if data_type.parent_type:
                import_classes.append(fmt_class_prefix(data_type.parent_type))

            if is_struct_type(data_type) and data_type.has_enumerated_subtypes():
                for _, subtype in data_type.get_all_subtypes_with_tags():
                    import_classes.append(fmt_class_prefix(subtype))

            for field in data_type.all_fields:
                data_type, _ = unwrap_nullable(field.data_type)

                # unpack list
                while is_list_type(data_type):
                    data_type = data_type.data_type

                if is_user_defined_type(data_type):
                    import_classes.append(fmt_class_prefix(data_type))

        if import_classes:
            import_classes = list(set(import_classes))
            import_classes.sort()

        return import_classes

    def _get_imports_h(self, data_types):
        """Emits all necessary header file imports for the given Stone data type."""
        if not isinstance(data_types, list):
            data_types = [data_types]

        import_classes = []

        for data_type in data_types:

            if is_user_defined_type(data_type):
                import_classes.append(fmt_class_prefix(data_type))

            for field in data_type.all_fields:
                data_type, _ = unwrap_nullable(field.data_type)

                # unpack list
                while is_list_type(data_type):
                    data_type = data_type.data_type

                if is_user_defined_type(data_type):
                    import_classes.append(fmt_class_prefix(data_type))

        import_classes = list(set(import_classes))
        import_classes.sort()

        return import_classes

    def _generate_imports_h(self, import_classes):
        import_classes = list(set(import_classes))
        import_classes.sort()

        for import_class in import_classes:
            self.emit('@class {};'.format(import_class))

        if import_classes:
            self.emit()

    def _generate_imports_m(self, import_classes):
        import_classes = list(set(import_classes))
        import_classes.sort()

        for import_class in import_classes:
            self.emit(fmt_import(import_class))

        self.emit()

    def _generate_init_imports_h(self, data_type):
        self.emit('#import <Foundation/Foundation.h>')
        self.emit()
        self.emit('#import "DBSerializableProtocol.h"')

        if data_type.parent_type and not is_union_type(data_type):
            self.emit(fmt_import(fmt_class_prefix(data_type.parent_type)))

        self.emit()

    def _get_namespace_route_imports(self,
                                     namespace,
                                     include_route_args=True,
                                     include_route_deep_args=False):
        result = []

        def _unpack_and_store_data_type(data_type):
            data_type, _ = unwrap_nullable(data_type)
            if is_list_type(data_type):
                while is_list_type(data_type):
                    data_type = data_type.data_type

            if not is_void_type(data_type) and is_user_defined_type(data_type):
                result.append(data_type)

        for route in namespace.routes:
            if include_route_args:
                data_type, _ = unwrap_nullable(route.arg_data_type)
                _unpack_and_store_data_type(data_type)
            elif include_route_deep_args:
                data_type, _ = unwrap_nullable(route.arg_data_type)
                if is_union_type(data_type) or is_list_type(data_type):
                    _unpack_and_store_data_type(data_type)
                elif not is_void_type(data_type):
                    for field in data_type.all_fields:
                        data_type, _ = unwrap_nullable(field.data_type)
                        if (is_struct_type(data_type) or
                                is_union_type(data_type) or
                                is_list_type(data_type)):
                            _unpack_and_store_data_type(data_type)

            _unpack_and_store_data_type(route.result_data_type)
            _unpack_and_store_data_type(route.error_data_type)

        return result

    def _cstor_name_from_fields(self, fields):
        """Returns an Obj C appropriate name for a constructor based on
        the name of the first argument."""
        if fields:
            return self._cstor_name_from_field(fields[0])
        else:
            return 'init'

    def _cstor_name_from_field(self, field):
        """Returns an Obj C appropriate name for a constructor based on
        the name of the supplied argument."""
        return 'initWith{}'.format(fmt_camel_upper(field.name))

    def _cstor_name_from_fields_names(self, fields_names):
        """Returns an Obj C appropriate name for a constructor based on
        the name of the first argument."""
        if fields_names:
            return 'initWith{}'.format(fmt_camel_upper(fields_names[0][0]))
        else:
            return 'init'

    def _struct_has_defaults(self, struct):
        """Returns whether the given struct has any default values."""
        return [f for f in struct.all_fields if f.has_default or is_nullable_type(f.data_type)]
