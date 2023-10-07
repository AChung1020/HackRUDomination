import pandas as pd

class readingData:

    def __init__(self, recipesDataset, ingredientsDataset, currentIngredients):
        self.recipesDF = pd.read_csv(recipesDataset)
        self.ingredientsDF = pd.read_csv(ingredientsDataset)
        self.currentIngredients = currentIngredients

    def getNutritonalInformation(self):
        currentIngredientsMap = {}
        for i in self.currentIngredients:
            currentIngredientsMap[i] = 1
        
        information = []
        
        # Get all the recipes that contain the current ingredients
        for name, data in self.recipesDF.iterrows():
            currIngredient = data['ingredients']
            if currIngredient not in currentIngredientsMap:
                continue
            else:


