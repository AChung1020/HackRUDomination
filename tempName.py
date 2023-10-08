from flask import Flask, jsonify, request

from flask_cors import CORS

from foodRecognition import determineOutcomes

from readingData import readingData

import os

import configparser

import json

filePath = os.path.expanduser(".aws/credentials")

config = configparser.ConfigParser()
config.read(filePath)

# os.environ["AWS_ACCESS_KEY_ID"] = config.get("default", "aws_access_key_id")
# os.environ["AWS_SECRET_ACCESS_KEY"] = config.get("default", "lMSYln/abaT84ml/2cBMaPYXVr/h7bMiZvgltl8Z")

app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "http://localhost:5000"}})
CORS(app, origins=["http://localhost:3000", "http://localhost:5000"])
ingredientsData = readingData()

@app.route('/data', methods={'GET'})
def get_data():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/imageRetrieval', methods={'POST'})
def getImage():
    ingredientsData = readingData()
    file = request.files['file']
    if file:
        image_data = file.read()
        values = determineOutcomes(image_data)
        # print(values._ListFieldsItemKey)
        actualValues = []
        count = 0
        for i in str(values.ListFields()[2][1]).split("concepts"):
            if count == 0:
                count += 1
                continue
            else:
                val = i.strip()
                lines = val.strip().split('\n')
                name = lines[2].split(":")[1][1:].strip()
                value = lines[3].split(":")[1][1:]
                if float(value) >= 0.6:
                    name = name[1:-1]
                    if name in ingredientsData.recipesForEachIngredient:
                        actualValues.append(name)
        # values = jsonify(str(values))['data']

        # for j in values:
        #     if j in ingredientsData.recipesForEachIngredient:
        #         actualValues.append(j)
        ingredientsData.changeIngredients(actualValues)
        
    # ingredientsData = readingData(["apple", "banana", "orange"])
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


        