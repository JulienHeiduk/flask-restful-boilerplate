from flask import Flask
from flask_restful import Api
from controllers import helloController
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

# infos
api.add_resource(helloController.HelloController, '/api/hello')
api.add_resource(helloController.InfoController, '/')

# Ml
api.add_resource(machinelearning.classification,'/ml')

if __name__ == '__main__':
    app.run(debug=True)
