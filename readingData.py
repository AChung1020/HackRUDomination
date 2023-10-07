import pandas as pd
from collections import defaultdict
import csv

class readingData:

    def __init__(self, recipesDataset, ingredientsDataset, currentIngredients):
        self.recipesDF = pd.read_csv(recipesDataset)
        self.ingredientsDF = pd.read_csv(ingredientsDataset)
        self.currentIngredients = currentIngredients
        self.nutritionallyDenseFoods = defaultdict(list)
        self.recipesWithFoods = defaultdict(list)
        self.recipes = {}

    def getNutritonalInformation(self):
        currentIngredientsMap = {}
        for i in self.currentIngredients:
            currentIngredientsMap[i] = 1
        
        information = [0 for i in range(6)]
        
        # Get all the recipes that contain the current ingredients
        for name, data in self.recipesDF.iterrows():
            currIngredient = data['food']
            if currIngredient not in currentIngredientsMap:
                continue
            else:
                information[0] += data['calories']
                information[1] += data['protein']
                information[2] += data['fat']
                information[3] += data['Sat.fat']
                information[4] += data['Fiber']
                information[5] += data['Carbs']
        
        return information
    
    def populateNutritionallyDenseFoods(self):
        
        def populateProtein():
            self.nutritionallyDenseFoods["protein"].append("chicken")
            self.nutritionallyDenseFoods["protein"].append("beef")
            self.nutritionallyDenseFoods["protein"].append("pork")
            self.nutritionallyDenseFoods["protein"].append("fish")
            self.nutritionallyDenseFoods["protein"].append("egg")
            self.nutritionallyDenseFoods["protein"].append("tofu")
            self.nutritionallyDenseFoods["protein"].append("beans")
            
        def populateCarbs():
            self.nutritionallyDenseFoods["carbs"].append("rice")
            self.nutritionallyDenseFoods["carbs"].append("bread")
            self.nutritionallyDenseFoods["carbs"].append("pasta")
            self.nutritionallyDenseFoods["carbs"].append("potato")
            self.nutritionallyDenseFoods["carbs"].append("corn")

        def populateFiber():
            self.nutritionallyDenseFoods["fiber"].append("broccoli")
            self.nutritionallyDenseFoods["fiber"].append("spinach")
            self.nutritionallyDenseFoods["fiber"].append("carrots")
            self.nutritionallyDenseFoods["fiber"].append("kale")
            self.nutritionallyDenseFoods["fiber"].append("avocado")

        def populateVitamins():
            self.nutritionallyDenseFoods["vitamins"].append("orange")
            self.nutritionallyDenseFoods["vitamins"].append("apple")
            self.nutritionallyDenseFoods["vitamins"].append("banana")
            self.nutritionallyDenseFoods["vitamins"].append("grapes")
        
        def populateFats():
            self.nutritionallyDenseFoods["fats"].append("avocado")
            self.nutritionallyDenseFoods["fats"].append("cheese")
            self.nutritionallyDenseFoods["fats"].append("nuts")
            self.nutritionallyDenseFoods["fats"].append("olive oil")

        populateCarbs()
        populateFats()
        populateFiber()
        populateFats()
        populateProtein()
        populateVitamins()

    def determineAreasToImprove(self):
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
        for name, data in self.recipesDF.iterrows():
            currIngredient = data['food']
            self.recipesWithFoods[currIngredient].append(data['recipe'])


    



