import pandas as pd
from collections import defaultdict
import csv

class readingData:

    def __init__(self, currentIngredients):

        # self.nutrients = pd.read_csv('nutrients_csvfile.csv')
        self.allIngredientsInARecipe = pd.read_pickle('allIngredientsInARecipe.pkl')
        self.actual_ingredients = pd.read_pickle('actual_ingredients.pkl')
        self.ingredientsToRecipes = pd.read_pickle('ingredientsToRecipes.pkl')
        self.recipe_map = pd.read_pickle('recipe_map.pkl')
        self.nutrients = pd.read_csv('food.csv')
        self.currentIngredients = currentIngredients

        self.nutritionallyDenseFoods = pd.read_pickle('nutrientMap.pkl')

        # self.nutritionallyDenseFoods = defaultdict(list)
        self.recipesWithFoods = defaultdict(list)
        self.ingredientMap = {}
        for i in self.currentIngredients:
            self.ingredientMap[i.upper()] = 1
        

    def getNutritonalInformation(self):
        
        information = [0 for element in range(len(self.nutritionallyDenseFoods))]

        val = "Data.Alpha Carotene,Data.Ash,Data.Beta Carotene,Data.Beta Cryptoxanthin,Data.Carbohydrate,Data.Cholesterol,Data.Choline,Data.Fiber,Data.Kilocalories,Data.Lutein and Zeaxanthin,Data.Lycopene,Data.Manganese,Data.Niacin,Data.Pantothenic Acid,Data.Protein,Data.Refuse Percentage,Data.Retinol,Data.Riboflavin,Data.Selenium,Data.Sugar Total,Data.Thiamin,Data.Water,Data.Fat.Monosaturated Fat,Data.Fat.Polysaturated Fat,Data.Fat.Saturated Fat,Data.Fat.Total Lipid,Data.Household Weights.1st Household Weight,Data.Household Weights.1st Household Weight Description,Data.Household Weights.2nd Household Weight,Data.Household Weights.2nd Household Weight Description,Data.Major Minerals.Calcium,Data.Major Minerals.Copper,Data.Major Minerals.Iron,Data.Major Minerals.Magnesium,Data.Major Minerals.Phosphorus,Data.Major Minerals.Potassium,Data.Major Minerals.Sodium,Data.Major Minerals.Zinc,Data.Vitamins.Vitamin A - IU,Data.Vitamins.Vitamin A - RAE,Data.Vitamins.Vitamin B12,Data.Vitamins.Vitamin B6,Data.Vitamins.Vitamin C,Data.Vitamins.Vitamin E,Data.Vitamins.Vitamin K"

        val = val.split(",")
        
        # Get all the recipes that contain the current ingredients

        keys = self.nutritionallyDenseFoods.keys()

        for name, data in self.nutrients.iterrows():
            currIngredient = data['Category']
            if currIngredient not in self.ingredientMap:
                continue
            else:
                information[0] += float(data[val[0]])
                information[1] += float(data[val[1]])
                information[2] += float(data[val[2]])
                information[3] += float(data[val[3]])
                information[4] += float(data[val[4]])
                information[5] += float(data[val[5]])
                information[6] += float(data[val[6]])
                information[7] += float(data[val[7]])
                information[8] += float(data[val[8]])
                information[9] += float(data[val[9]])
                information[10] += float(data[val[10]])
                information[11] += float(data[val[11]])
                information[12] += float(data[val[12]])
                information[13] += float(data[val[13]])
                information[14] += float(data[val[14]])
                information[15] += float(data[val[15]])
                information[16] += float(data[val[16]])
                information[17] += float(data[val[17]])
                information[18] += float(data[val[18]])
                information[19] += float(data[val[19]])
                information[20] += float(data[val[20]])
                information[21] += float(data[val[21]])
                information[22] += float(data[val[22]])
                information[23] += float(data[val[23]])
                information[24] += float(data[val[24]])
                information[25] += float(data[val[25]])
                information[26] += float(data[val[26]])
                information[27] += float(data[val[27]])
                information[28] += float(data[val[28]])
                information[29] += float(data[val[29]])
                information[30] += float(data[val[30]])
                information[31] += float(data[val[31]])
                information[32] += float(data[val[32]])
                information[33] += float(data[val[33]])
                information[34] += float(data[val[34]])
                information[35] += float(data[val[35]])
                information[36] += float(data[val[36]])
                information[37] += float(data[val[37]])
                information[38] += float(data[val[38]])
                information[39] += float(data[val[39]])
                information[40] += float(data[val[40]])
                information[41] += float(data[val[41]])
                information[42] += float(data[val[42]])
                information[43] += float(data[val[43]])
                information[44] += float(data[val[44]])
        return information

    def determineAreasToImprove(self):

        # Edit this to return the areas to improve

        information = self.getNutritonalInformation()
        areasToImprove = []
        if information[1] < 50:
            areasToImprove.append("protein")
        if information[2] < 50:
            areasToImprove.append("fat")
        if information[4] < 50:
            areasToImprove.append("fiber")
        if information[5] < 50:
            areasToImprove.append("carbs")
        areasToImprove.append("vitamins")

        return areasToImprove
    
    def populateRecipes(self):

        # return recipes with the current ingredients

        possibleRecipes = []

        for i in self.allIngredientsInARecipe.keys():
            data = self.allIngredientsInARecipe[i]
            total = 0
            for j in data:
                if j in self.ingredientMap:
                    total += 1
            if total >= len(data) - 1 or (total / len(data)) > 0.8:
                possibleRecipes.append(i)
        
        return possibleRecipes


# readingData = readingData(['chicken', 'Rice', 'Broccoli'])
# print(readingData.getNutritonalInformation())



