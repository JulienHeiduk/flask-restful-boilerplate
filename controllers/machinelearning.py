from flask_restful import Resource
import pandas as pd

class classification(Resource):

    def get(self):
        return {"response" : "hello get"} 
