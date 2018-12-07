import json
import os

import pytest


def test_not_found_404(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert rv.status_code == 404
    assert b'404 Not Found' in rv.data


def test_update_task(client):
    data = {
        'title': 'test_task_creation'
    }

    rv = client.post('/api/v1/tasks', data=json.dumps(data))
    assert rv.status_code == 200
    created = json.loads(rv.data)

    data = {
        'title': 'test_task_update_id_works',
    }

    rv = client.post('/api/v1/tasks/%s' % str(created['id']), data=json.dumps(data))
    assert rv.status_code == 200
    assert json.loads(rv.data)['title'] == data['title']


def test_delete_non_existent(client):
    data = {
        'id': 'not_existent'
    }
    rv = client.delete('/api/v1/tasks/%s' % str(data['id']))
    assert rv.status_code == 404


def test_create_list_and_delete_task(client):
    data = {
        'title': 'test_task_creation'
    }

    rv = client.post('/api/v1/tasks', data=json.dumps(data))
    assert rv.status_code == 200
    data = json.loads(rv.data)

    rv = client.get('/api/v1/tasks')
    assert rv.status_code == 200
    assert data['id'] in json.loads(rv.data)['tasks']

    rv = client.delete('/api/v1/tasks/%s' % str(data['id']))
    assert rv.status_code == 200

    rv = client.get('/api/v1/tasks')
    assert rv.status_code == 200
    assert data['id'] not in json.loads(rv.data)['tasks']
