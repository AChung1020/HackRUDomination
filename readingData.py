import pandas as pd
from collections import defaultdict
import csv

class readingData:

    def __init__(self, currentIngredients):

        self.nutrients = pd.read_csv('nutrients_csvfile.csv')
        self.allIngredientsInARecipe = pd.read_pickle('allIngredientsInARecipe.pkl')
        self.actual_ingredients = pd.read_pickle('actual_ingredients.pkl')
        self.ingredientsToRecipes = pd.read_pickle('ingredientsToRecipes.pkl')
        self.recipe_map = pd.read_pickle('recipe_map.pkl')
        self.currentIngredients = currentIngredients
        self.nutritionallyDenseFoods = defaultdict(list)
        self.recipesWithFoods = defaultdict(list)
        self.ingredientMap = {}
        for i in self.currentIngredients:
            self.ingredientMap[i] = 1
        

    def getNutritonalInformation(self):
        
        information = [0 for i in range(6)]
        
        # Get all the recipes that contain the current ingredients
        for name, data in self.nutrients.iterrows():
            currIngredient = data['Food']
            if currIngredient not in self.ingredientMap:
                continue
            else:
                information[0] += float(data['Calories'])
                information[1] += float(data['Protein'])
                information[2] += float(data['Fat'])
                information[3] += float(data['Sat.Fat'])
                information[4] += float(data['Fiber'])
                information[5] += float(data['Carbs'])
        
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


readingData = readingData(['chicken', 'Rice', 'Broccoli'])
print(readingData.getNutritonalInformation())



