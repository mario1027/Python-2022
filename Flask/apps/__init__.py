from flask import Flask
from importlib import import_module


def register_blueprints(app):
    for module_name in ['routes']:
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def create_app(config):
    app=Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    register_blueprints(app)
    return app