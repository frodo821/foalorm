from foalorm.orm import db_session
from flask import request

def _enter_session():
    session = db_session()
    request.foalorm_session = session
    session.__enter__()

def _exit_session(exception):
    session = getattr(request, 'foalorm_session', None)
    if session is not None:
        session.__exit__(exc=exception)

class FoalORM(object):
    def __init__(self, app=None):
        self.app = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.app.before_request(_enter_session)
        self.app.teardown_request(_exit_session)