from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
base_url = "https://fintual.cl/api/"
conceptual_assets = {}

class ConceptualAssetList(Resource):
    def get(self):
        query = {}
        assets = requests.get(base_url + "conceptual_assets", params=query)
        return assets.json()['data']

class RealAsset(Resource):
    def get(self, real_asset_id):
        query = {}
        assets = requests.get(base_url + "real_assets/" + real_asset_id, params=query)
        return assets.json()['data']

class ConceptualAssetRealAssets(Resource):
    def get(self, asset_id):
        query = {}
        assets = requests.get(base_url + "conceptual_assets/" + asset_id + "/real_assets", params=query)
        return assets.json()['data']

class RealAssetRateofChange(Resource):
    def get(self, asset_id):
        query={'from_date': request.args['start_date'], 'to_date': request.args['start_date']}
        start_value = requests.get(base_url + "real_assets/" + asset_id + "/days", params=query).json()
        query = {
            'from_date': request.args['end_date'], 'to_date': request.args['end_date']}
        end_value = requests.get(base_url + "real_assets/" + asset_id + "/days", params=query).json()

        print(len(start_value['data']))
        print(len(end_value['data']))

        if len(start_value['data']) > 0 and len(end_value['data']) > 0:
            start_value = start_value['data'][0]['attributes']['price']
            end_value = end_value['data'][0]['attributes']['price']
            rateOfChange = round((end_value - start_value), 2)
            return rateOfChange
        return 'No se encontraron registros de precio para los datos ingresados.'

# API Resources
api.add_resource(ConceptualAssetList, "/conceptual_assets")
api.add_resource(ConceptualAssetRealAssets, "/conceptual_assets/<asset_id>/real_assets")
api.add_resource(RealAssetRateofChange, "/real_assets/<asset_id>/days")
api.add_resource(RealAsset, "/real_assets/<real_asset_id>")

if __name__ == "__main__":
    app.run(debug=True)