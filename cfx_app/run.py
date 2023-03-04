from app.authentication import app1 as authentication_app, db
from app.article import app2 as article_app, db2

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple


application = DispatcherMiddleware(authentication_app, {'/app2': article_app})


if __name__ == '__main__':

    with authentication_app.app_context():
        db.create_all()
    with article_app.app_context():
        db2.create_all()

    # authentication_app.run('localhost', 5001)
    # article_app.run('localhost', 5001)
    run_simple('localhost', 5000, application)
