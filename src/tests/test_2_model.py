import pytest

from src.model.todo_task import TodoTask


def test_load_save(flask_app):
    storage = flask_app.extensions['redis']
    a = TodoTask("test_task", storage=storage)
    a.save()
    test_id = a.id
    a = None
    a = TodoTask.load(test_id, storage)

    assert test_id == a.id
    assert "test_task" == a.title
    assert a.status == TodoTask.STATUS.OPEN


def test_load_not_existent(flask_app):
    storage = flask_app.extensions['redis']

    with pytest.raises(Exception, message="Expecting task to be not existent"):
        a = TodoTask.load("not_existent", storage)
        print(a.id)


def test_status_change(flask_app):
    storage = flask_app.extensions['redis']
    a = TodoTask("test_task", storage)
    test_id = a.id
    assert a.status == TodoTask.STATUS.OPEN

    a.set_status(TodoTask.STATUS.DONE)
    assert a.status == TodoTask.STATUS.DONE

    a.save()
    b = TodoTask.load(test_id, storage)
    assert a.status == b.status


def test_parenting(flask_app):
    storage = flask_app.extensions['redis']
    a = TodoTask("test_task_1", storage)
    b = TodoTask("test_task_2", storage)
    a_id = a.id
    b_id = b.id

    a.save()
    b.save()

    a.set_parent(b_id)

    a = TodoTask.load(a_id, storage)
    b = TodoTask.load(b_id, storage)

    assert a.parent_id == b.id


def test_create_list_delete(flask_app):
    storage = flask_app.extensions['redis']

    current_list = storage.smembers(TodoTask.LIST_PREFIX)
    for each in current_list:
        TodoTask.delete(each, storage)

    a = TodoTask("test_task_1", storage)
    a.save()

    current_list = storage.smembers(TodoTask.LIST_PREFIX)
    assert len(current_list) == 1

    for each in current_list:
        TodoTask.delete(each, storage)

    current_list = storage.smembers(TodoTask.LIST_PREFIX)
    assert len(current_list) == 0
