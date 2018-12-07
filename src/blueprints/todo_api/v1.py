import json
import pprint

from dicttoxml import dicttoxml
from flask import Blueprint, current_app, request

from src.model.todo_task import TodoTask

api = Blueprint("TodoApiv1", __name__)


# Quick way to decorate all the views within a blueprint
@api.before_request
def before_request():
    pass


def dynamic_response_format(response):
    # who knows maybe someone would actually need the xml output
    if request.args.get('xml'):
        response = dicttoxml(response, custom_root="response", attr_type=False)

    # useful for manual checking of the returned values,
    # especially in postman
    elif request.args.get('plaintext'):
        response = pprint.pformat(response)

    # defaults to JSON output
    elif request.args.get('json') or True:
        response = json.dumps(response)

    return response


@api.route('/tasks', methods=['GET'])
def list_tasks():
    storage = current_app.extensions['redis']
    data = {
        "tasks": list(storage.smembers(TodoTask.LIST_PREFIX))
    }

    return dynamic_response_format(data), 200


@api.route('/tasks', methods=['POST'])
def create_task():
    return update_task(None)


@api.route('/tasks/<id>', methods=['POST'])
def update_task(id):
    try:
        data = json.loads(request.data)
        task = TodoTask(storage=current_app.extensions['redis'], **data)
        task.save()

        return dynamic_response_format({
            'id': task.id, 'title': task.title, 'status': task.status
        }), 200

    except Exception as e:
        return dynamic_response_format({'error': str(e)}), 404


@api.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    try:
        TodoTask.delete(id, storage=current_app.extensions['redis'])
        return 'ok', 200
    except Exception as e:
        return dynamic_response_format({'error': str(e)}), 404

