from flask import Flask, jsonify, request

from flask_cors import CORS

from foodRecognition import determineOutcomes

import readingData

import os

import configparser

filePath = os.path.expanduser(".aws/credentials")

config = configparser.ConfigParser()
config.read(filePath)

os.environ["AWS_ACCESS_KEY_ID"] = config.get("default", "aws_access_key_id")
os.environ["AWS_SECRET_ACCESS_KEY"] = config.get("default", "lMSYln/abaT84ml/2cBMaPYXVr/h7bMiZvgltl8Z")

app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "http://localhost:5000"}})
CORS(app, origins=["http://localhost:3000", "http://localhost:5000"])
ingredientsData = None

@app.route('/data', methods={'GET'})
def get_data():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/imageRetrieval', methods={'POST'})
def getImage():
    imageURL = request.data
    values = determineOutcomes(imageURL)
    print(imageURL)
    print(values)
    # Figure out what values returns as
    # ingredientsData = readingData(values)
    return jsonify("Received your image!")

@app.route('/valuesRetrieval', methods={'POST'})
def getValues():
    values = request.json['ingredients']
    ingredientsData = readingData(values)
    return f"Received your ingredients!"
    

@app.route('/nutritionalData', methods={'GET'})
def get_nutritionalInformation():
    map = jsonify(ingredientsData.determineAdditionalRecipes())
    map["importantVitaminInfo"] = ingredientsData.getNutritionalInformation()
    return jsonify(map)

@app.route('/necessaryVitamins', methods = {'GET'})
def get_vitamins():
    value = jsonify(ingredientsData.determineAreasToImprove())
    # return value


@app.route('/possibleRecipes', methods = {'GET'})
def get_recipes():
    return jsonify(ingredientsData.populateRecipes())

# @app.route('/vitaminRecipes')
# def get_vitaminRecipes():
#     return jsonify(ingredientsData.determineAdditionalRecipes())

if __name__ == '__main__':
    app.run(debug = True, port = 5000)


        