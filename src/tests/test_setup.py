
def test_redis_connection(flask_app):
    storage = flask_app.extensions['redis']

    storage.set('test', 'ok')
    assert storage.get('test') == 'ok'
    storage.delete('test')

