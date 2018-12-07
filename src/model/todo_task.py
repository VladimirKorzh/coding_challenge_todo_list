import uuid


class TodoTask:
    class STATUS:
        OPEN = 'OPEN'
        DONE = 'DONE'

    LIST_PREFIX = 'tasks:list'
    TASK_PREFIX = 'task:%s'

    def __init__(self, title, storage, parent_id=0, status=STATUS.OPEN, id=None):
        if id is None:
            self.id = TodoTask.TASK_PREFIX % str(uuid.uuid4())
        else:
            self.id = id

        self.storage = storage

        self.title = title
        self.status = status
        self.parent_id = parent_id

    @staticmethod
    def load(id, storage):
        if storage.hexists(id, 'title'):
            values = storage.hgetall(id)
            return TodoTask(**values, storage=storage)
        else:
            raise Exception('Task with id: %s does not exist' % id)

    @staticmethod
    def delete(id, storage):
        if storage.sismember(TodoTask.LIST_PREFIX, id):
            storage.srem(TodoTask.LIST_PREFIX, id)
            storage.delete(id)
        else:
            raise Exception("No task with id: %s found" % str(id))

    def save(self):
        data = {'id': self.id, 'title': self.title, 'status': self.status, 'parent_id': self.parent_id}
        self.storage.hmset(self.id, data)
        self.storage.sadd(TodoTask.LIST_PREFIX, self.id)

    def set_status(self, _status):
        # Quick and dirty way to get all the possible keys from a class
        allowed = [x for x in TodoTask.STATUS.__dict__.keys() if not x.startswith("__")]

        if _status in allowed:
            self.status = _status
            self.save()
        else:
            raise Exception('Wrong status provided,'
                            ' please provide a valid one. Allowed values: ' + ', '.join(allowed))

    def set_parent(self, new_parent_id):

        if new_parent_id is not None:
            # check for the existence of a new parent
            new_parent = TodoTask.load(new_parent_id, self.storage)
        else:
            new_parent_id = 0

        # set the parent reference
        self.parent_id = new_parent_id
        self.save()
