# Generated by BabelSDK

import json
import os
from collections import OrderedDict
from bottle import (
    HTTPResponse,
    request,
    response,
    route,
    run,
)

def segmentation_response(header, body, *segments):
    """Constructs HTTP headers and body for a segmentation response."""
    response_json = []

    for segment in segments:
        response_json.append(segment)

    if len(response_json) == 1:
        response_json = response_json[0]

    if header:
        response.headers['Dropbox-API-Result'] = json.dumps(response_json)
        if body:
            return open(os.path.dirname(os.path.abspath(__file__)) + '/v2_server.babelt.py')
    else:
        # Manually convert json to a string because bottle only dumps json for
        # dicts, and not lists.
        response.content_type = 'application/json'
        return json.dumps(response_json)

@route('/2/files/folder-list', method=['POST'])
def files_folder_list():
    return segmentation_response(
        False,
        False,
        OrderedDict([('id', 'abc456'), ('id_rev', 3), ('path', '/Photos'), ('path_rev', 20), ('modified', 'Sat, 28 Jun 2014 18:23:21'), ('is_deleted', False), ('shared_folder', OrderedDict([('id', 'sf123')])), ('contents', [{'file': OrderedDict([('id', 'xyz123'), ('id_rev', 2), ('path', '/Photos/flower.jpg'), ('path_rev', 19), ('modified', 'Sat, 28 Jun 2014 18:23:21'), ('is_deleted', False), ('size', 1234), ('mime_type', 'image/jpg'), ('shared_folder', OrderedDict([('id', 'sf123')])), ('media_info', {'photo': OrderedDict([('time_taken', 'Sat, 28 Jun 2014 18:23:21'), ('lat_long', None)])})])}])]),
    )

@route('/2/files/info', method=['POST'])
def files_info():
    return segmentation_response(
        False,
        False,
        {'file': OrderedDict([('id', 'xyz123'), ('id_rev', 2), ('path', '/Photos/flower.jpg'), ('path_rev', 19), ('modified', 'Sat, 28 Jun 2014 18:23:21'), ('is_deleted', False), ('size', 1234), ('mime_type', 'image/jpg'), ('shared_folder', OrderedDict([('id', 'sf123')])), ('media_info', {'photo': OrderedDict([('time_taken', 'Sat, 28 Jun 2014 18:23:21'), ('lat_long', None)])})])},
    )

@route('/2/files/download', method=['GET', 'POST'])
def files_download():
    return segmentation_response(
        True,
        True,
        OrderedDict([('id', 'xyz123'), ('id_rev', 2), ('path', '/Photos/flower.jpg'), ('path_rev', 19), ('modified', 'Sat, 28 Jun 2014 18:23:21'), ('is_deleted', False), ('size', 1234), ('mime_type', 'image/jpg'), ('shared_folder', OrderedDict([('id', 'sf123')])), ('media_info', {'photo': OrderedDict([('time_taken', 'Sat, 28 Jun 2014 18:23:21'), ('lat_long', None)])})]),
    )

@route('/2/files/upload', method=['POST'])
def files_upload():
    return segmentation_response(
        True,
        False,
        OrderedDict([('id', 'xyz123'), ('id_rev', 2), ('path', '/Photos/flower.jpg'), ('path_rev', 19), ('modified', 'Sat, 28 Jun 2014 18:23:21'), ('is_deleted', False), ('size', 1234), ('mime_type', 'image/jpg'), ('shared_folder', OrderedDict([('id', 'sf123')])), ('media_info', {'photo': OrderedDict([('time_taken', 'Sat, 28 Jun 2014 18:23:21'), ('lat_long', None)])})]),
    )

@route('/2/files/delta', method=['POST'])
def files_delta():
    return segmentation_response(
        False,
        False,
        OrderedDict([('reset', False), ('cursor', 'xyz123'), ('has_more', True), ('entries', [{'file': OrderedDict([('id', 'xyz123'), ('id_rev', 2), ('path', '/Photos/flower.jpg'), ('path_rev', 19), ('modified', 'Sat, 28 Jun 2014 18:23:21'), ('is_deleted', False), ('size', 1234), ('mime_type', 'image/jpg'), ('shared_folder', OrderedDict([('id', 'sf123')])), ('media_info', {'photo': OrderedDict([('time_taken', 'Sat, 28 Jun 2014 18:23:21'), ('lat_long', None)])})])}])]),
    )

@route('/2/files/longpolldelta', method=['POST'])
def files_longpoll_delta():
    return segmentation_response(
        False,
        False,
        OrderedDict([('changes', False), ('backoff', 60)]),
    )

@route('/2/files/thumbnail', method=['POST'])
def files_thumbnail():
    return segmentation_response(
        True,
        True,
        OrderedDict([('id', 'xyz123'), ('id_rev', 2), ('path', '/Photos/flower.jpg'), ('path_rev', 19), ('modified', 'Sat, 28 Jun 2014 18:23:21'), ('is_deleted', False), ('size', 1234), ('mime_type', 'image/jpg'), ('shared_folder', OrderedDict([('id', 'sf123')])), ('media_info', {'photo': OrderedDict([('time_taken', 'Sat, 28 Jun 2014 18:23:21'), ('lat_long', None)])})]),
    )

@route('/2/files/revisions', method=['POST'])
def files_revisions():
    return segmentation_response(
        False,
        False,
        {'no example': 'no example'},
    )

@route('/2/files/restore', method=['POST'])
def files_restore():
    return segmentation_response(
        False,
        False,
        OrderedDict([('id', 'xyz123'), ('id_rev', 2), ('path', '/Photos/flower.jpg'), ('path_rev', 19), ('modified', 'Sat, 28 Jun 2014 18:23:21'), ('is_deleted', False), ('size', 1234), ('mime_type', 'image/jpg'), ('shared_folder', OrderedDict([('id', 'sf123')])), ('media_info', {'photo': OrderedDict([('time_taken', 'Sat, 28 Jun 2014 18:23:21'), ('lat_long', None)])})]),
    )

@route('/2/files/search', method=['POST'])
def files_search():
    return segmentation_response(
        False,
        False,
        OrderedDict([('has_more', False), ('results', [{'file': OrderedDict([('id', 'xyz123'), ('id_rev', 2), ('path', '/Photos/flower.jpg'), ('path_rev', 19), ('modified', 'Sat, 28 Jun 2014 18:23:21'), ('is_deleted', False), ('size', 1234), ('mime_type', 'image/jpg'), ('shared_folder', OrderedDict([('id', 'sf123')])), ('media_info', {'photo': OrderedDict([('time_taken', 'Sat, 28 Jun 2014 18:23:21'), ('lat_long', None)])})])}])]),
    )

@route('/2/files/preview', method=['POST'])
def files_preview():
    return segmentation_response(
        True,
        True,
        OrderedDict([('id', 'xyz123'), ('id_rev', 2), ('path', '/Photos/flower.jpg'), ('path_rev', 19), ('modified', 'Sat, 28 Jun 2014 18:23:21'), ('is_deleted', False), ('size', 1234), ('mime_type', 'image/jpg'), ('shared_folder', OrderedDict([('id', 'sf123')])), ('media_info', {'photo': OrderedDict([('time_taken', 'Sat, 28 Jun 2014 18:23:21'), ('lat_long', None)])})]),
    )

@route('/2/files/copy', method=['POST'])
def files_copy():
    return segmentation_response(
        False,
        False,
        OrderedDict([('id', 'xyz123'), ('id_rev', 2), ('path', '/Photos/flower.jpg'), ('path_rev', 19), ('modified', 'Sat, 28 Jun 2014 18:23:21'), ('is_deleted', False), ('size', 1234), ('mime_type', 'image/jpg'), ('shared_folder', OrderedDict([('id', 'sf123')])), ('media_info', {'photo': OrderedDict([('time_taken', 'Sat, 28 Jun 2014 18:23:21'), ('lat_long', None)])})]),
    )

@route('/2/files/move', method=['POST'])
def files_move():
    return segmentation_response(
        False,
        False,
        OrderedDict([('id', 'xyz123'), ('id_rev', 2), ('path', '/Photos/flower.jpg'), ('path_rev', 19), ('modified', 'Sat, 28 Jun 2014 18:23:21'), ('is_deleted', False), ('size', 1234), ('mime_type', 'image/jpg'), ('shared_folder', OrderedDict([('id', 'sf123')])), ('media_info', {'photo': OrderedDict([('time_taken', 'Sat, 28 Jun 2014 18:23:21'), ('lat_long', None)])})]),
    )

@route('/2/files/folder-create', method=['POST'])
def files_folder_create():
    return segmentation_response(
        False,
        False,
        OrderedDict([('id', 'xyz123'), ('id_rev', 2), ('path', '/Photos/flower.jpg'), ('path_rev', 19), ('modified', 'Sat, 28 Jun 2014 18:23:21'), ('is_deleted', False), ('size', 1234), ('mime_type', 'image/jpg'), ('shared_folder', OrderedDict([('id', 'sf123')])), ('media_info', {'photo': OrderedDict([('time_taken', 'Sat, 28 Jun 2014 18:23:21'), ('lat_long', None)])})]),
    )

@route('/2/files/delete', method=['POST'])
def files_delete():
    return segmentation_response(
        False,
        False,
        OrderedDict([('id', 'xyz123'), ('id_rev', 2), ('path', '/Photos/flower.jpg'), ('path_rev', 19), ('modified', 'Sat, 28 Jun 2014 18:23:21'), ('is_deleted', False), ('size', 1234), ('mime_type', 'image/jpg'), ('shared_folder', OrderedDict([('id', 'sf123')])), ('media_info', {'photo': OrderedDict([('time_taken', 'Sat, 28 Jun 2014 18:23:21'), ('lat_long', None)])})]),
    )

@route('/2/users/info', method=['POST'])
def users_info():
    return segmentation_response(
        False,
        False,
        OrderedDict([('display_name', 'Jon Snow'), ('account_id', '314159'), ('email', 'jsnow@westeros.com'), ('country', 'US'), ('referral_link', 'https://db.tt/ZITNuhtI'), ('is_paired', True), ('quota', OrderedDict([('quota', 1000000), ('normal', 1000), ('shared', 500), ('datastores', 42)])), ('team', OrderedDict([('name', 'Acme, Inc.')]))]),
    )


run(host='localhost', port=8080, debug=True, reloader=True)