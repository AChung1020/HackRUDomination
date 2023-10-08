import pandas as pd
from collections import defaultdict
import csv
import json

class readingData:

    def __init__(self, currentIngredients):

        # self.nutrients = pd.read_csv('nutrients_csvfile.csv')
        # self.allIngredientsInARecipe = pd.read_pickle('allIngredientsInARecipe.pkl')
        # self.actual_ingredients = pd.read_pickle('actual_ingredients.pkl')
        # self.ingredientsToRecipes = pd.read_pickle('ingredientsToRecipes.pkl')
        self.recipe_map = pd.read_pickle('realRecipesMap.pkl')
        self.recipesForEachIngredient = pd.read_pickle('realIngredientsMap.pkl')
        self.nutrients = pd.read_csv('food.csv')
        self.currentIngredients = currentIngredients

        self.meats = {"beef": 1, "chicken": 1, "pork": 1, "lamb": 1, "turkey": 1, "duck": 1, "goose": 1, "quail": 1, "rabbit": 1, "venison": 1, "bison": 1, "buffalo": 1, "elk": 1, "moose": 1, "emu": 1, "ostrich": 1, "kangaroo": 1, "alligator": 1, "turtle": 1, "frog": 1, "escargot": 1, "snail": 1, "bear": 1, "boar": 1, "caribou": 1, "reindeer": 1, "pheasant": 1, "squab": 1, "rabbit": 1, "squirrel": 1, "bear": 1, "boar": 1, "caribou": 1, "reindeer": 1, "pheasant": 1, "squab": 1, "rabbit": 1, "squirrel": 1, "bear": 1, "boar": 1, "caribou": 1, "reindeer": 1, "pheasant": 1, "squab": 1, "rabbit": 1, "squirrel": 1, "bear": 1, "boar": 1, "caribou": 1, "reindeer": 1, "pheasant": 1, "squab": 1, "rabbit": 1, "squirrel": 1, "bear": 1, "boar": 1, "caribou": 1, "reindeer": 1, "pheasant": 1, "squab": 1, "rabbit": 1, "squirrel": 1, "bear": 1, "boar": 1, "caribou": 1, "reindeer": 1, "pheasant": 1, "squab": 1, "cod": 1, "fish": 1, "crab": 1, "mussels": 1, "octopus": 1, "shrimp":1, "prawns": 1}
        self.carbs = {"rice": 1, "bread": 1, "pasta": 1, "potatoes": 1}
        self.obviousSpices = {"salt": 1, "pepper": 1, "water": 1, "olive oil": 1, "flour": 1, "sugar": 1, "soy sauce": 1, "vinegar": 1}
        
        self.nutritionallyDenseFoods = pd.read_pickle('nutrientMap.pkl')
        self.bestIngredientRecipes = pd.read_pickle("bestIngredientsRecipes.pkl")
        # self.nutritionallyDenseFoods = defaultdict(list)
        # self.recipesWithFoods = defaultdict(list)
        self.ingredientMap = {}
        for i in self.currentIngredients:
            self.ingredientMap[i.upper()] = 1
        

    def getNutritonalInformation(self):
        
        information = [0 for element in range(len(self.nutritionallyDenseFoods))]

        val = "Data.Alpha Carotene,Data.Ash,Data.Beta Carotene,Data.Beta Cryptoxanthin,Data.Carbohydrate,Data.Cholesterol,Data.Choline,Data.Fiber,Data.Kilocalories,Data.Lutein and Zeaxanthin,Data.Lycopene,Data.Manganese,Data.Niacin,Data.Pantothenic Acid,Data.Protein,Data.Refuse Percentage,Data.Retinol,Data.Riboflavin,Data.Selenium,Data.Sugar Total,Data.Thiamin,Data.Water,Data.Fat.Monosaturated Fat,Data.Fat.Polysaturated Fat,Data.Fat.Saturated Fat,Data.Fat.Total Lipid,Data.Household Weights.1st Household Weight,Data.Household Weights.1st Household Weight Description,Data.Household Weights.2nd Household Weight,Data.Household Weights.2nd Household Weight Description,Data.Major Minerals.Calcium,Data.Major Minerals.Copper,Data.Major Minerals.Iron,Data.Major Minerals.Magnesium,Data.Major Minerals.Phosphorus,Data.Major Minerals.Potassium,Data.Major Minerals.Sodium,Data.Major Minerals.Zinc,Data.Vitamins.Vitamin A - IU,Data.Vitamins.Vitamin A - RAE,Data.Vitamins.Vitamin B12,Data.Vitamins.Vitamin B6,Data.Vitamins.Vitamin C,Data.Vitamins.Vitamin E,Data.Vitamins.Vitamin K"

        val = val.split(",")
        
        # Get all the recipes that contain the current ingredients

        # keys = self.nutritionallyDenseFoods.keys()

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
                # information[27] += float(data[val[27]])
                information[28] += float(data[val[28]])
                # information[29] += float(data[val[29]])
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

        possibleRecipes = {}

        for i in self.recipe_map.keys():
            ingredients = self.recipe_map[i]
            totalIngredientsMatch = 0
            totalOfPassedInMatch = 0
            val = True
            for j in ingredients:
                if j.upper() in self.ingredientMap or j in self.obviousSpices:
                    if j.upper() in self.ingredientMap:
                        totalOfPassedInMatch += 1
                    if j in self.meats or j in self.carbs:
                        totalIngredientsMatch += 2
                    else:
                        totalIngredientsMatch += 1
                elif j in self.meats:
                    val = False
                    break
                elif j in self.carbs:
                    val = False
                    break
            if not(val):
                continue
            if ((totalIngredientsMatch/len(ingredients)) > 0.5):
                possibleRecipes[i] = ingredients
        
        return possibleRecipes
    
    def determineAdditionalRecipes(self):
        
        areasToImprove = self.determineAreasToImprove()

        recipes = defaultdict(list)

        for i in range(len(areasToImprove)):
            if i == 5:
                break
            ingredients = self.nutritionallyDenseFoods[areasToImprove[i]]
            for j in ingredients:
                if recipes[i] > 2:
                    break
                possibleRecipes = self.bestIngredientRecipes[j]
                recipes[i].append(possibleRecipes[0])
                continue
        
        print(recipes)
            
                
            



readingData = readingData(['beef', 'cheese', 'tomatoes', 'onions'])
# print(readingData.determineAdditionalRecipes())



