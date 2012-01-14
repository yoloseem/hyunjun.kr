from flask import Flask, Module


def create_module(*args, **kwargs):
    module = Module(*args, **kwargs)
    return module


def auto_register_modules(app):
    import web
    for modname in web.__modules__:
        __import__("{0}.{1}".format(web.__name__, modname))
        module = getattr(web, modname)
        module.app.super_app = app
        app.register_module(module.app)


def create_app(__name__=__name__):
    app = Flask(__name__)
    auto_register_modules(app)
    return app
