from flask_restful import Resource
import pandas as pd
import os

class classification(Resource):

    def get(self):
        dirpath = os.getcwd()
        return dirpath 
