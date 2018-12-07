import os

from flask import Flask

from src.services.redis import redis_init


def create_app():
    # create and configure the app
    application = Flask(__name__, instance_relative_config=False)

    # ensure the instance folder exists
    try:
        os.makedirs(application.instance_path)
    except OSError:
        pass

    # load default configuration
    application.config.from_pyfile(os.path.join('.', 'config/default.cfg'), silent=False)

    # load environment overrides
    application.config.from_envvar('OVERRIDE_CONFIG_PATH', silent=True)

    # import the api
    from src.blueprints.todo_api import v1

    # register it with a custom prefix to allow serving multiple versions
    # of the same API within the same container
    application.register_blueprint(v1.api, url_prefix='/api/v1')
    return application


if __name__ == '__main__':
    app = create_app()
    redis_init(app)
    app.run(host=app.config.get('FLASK_HOST'), port=app.config.get('FLASK_PORT'))
