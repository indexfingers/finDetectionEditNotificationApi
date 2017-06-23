import os

from flask import Flask
from flask_restful import  Api

from resources.finDetectionEditNotification import FinDetectionEditNotification, FinDetectionEditNotifications

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ben'
api = Api(app)


# @app.before_first_request
# def create_tables():
#     db.create_all()


api.add_resource(FinDetectionEditNotification, '/finDetectionEditNotification/<string:annotationId>')
api.add_resource(FinDetectionEditNotifications, '/finDetectionEditNotifications')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
