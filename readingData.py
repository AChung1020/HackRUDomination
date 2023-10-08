import pandas as pd
from collections import defaultdict
import csv
import json


class readingData:

    def __init__(self, currentIngredients = []):

        # self.nutrients = pd.read_csv('nutrients_csvfile.csv')
        # self.allIngredientsInARecipe = pd.read_pickle('allIngredientsInARecipe.pkl')
        # self.actual_ingredients = pd.read_pickle('actual_ingredients.pkl')
        # self.ingredientsToRecipes = pd.read_pickle('ingredientsToRecipes.pkl')
        self.recipe_map = pd.read_pickle('realRecipesMap.pkl')
        self.recipesForEachIngredient = pd.read_pickle('realIngredientsMap.pkl')
        self.nutrients = pd.read_csv('food.csv')
        self.currentIngredients = currentIngredients

        self.meats = {"beef": 1, "chicken": 1, "pork": 1, "lamb": 1, "turkey": 1, "duck": 1, "goose": 1, "quail": 1, "rabbit": 1, "venison": 1, "bison": 1, "buffalo": 1, "elk": 1, "moose": 1, "emu": 1, "ostrich": 1, "steak": 1, "alligator": 1, "turtle": 1, "frog": 1, "escargot": 1, "snail": 1, "bear": 1, "boar": 1, "caribou": 1, "reindeer": 1, "pheasant": 1, "squab": 1, "rabbit": 1, "squirrel": 1, "bear": 1, "boar": 1, "caribou": 1, "reindeer": 1, "pheasant": 1, "squab": 1, "rabbit": 1,
                      "squirrel": 1, "bear": 1, "boar": 1, "caribou": 1, "reindeer": 1, "pheasant": 1, "squab": 1, "rabbit": 1, "squirrel": 1, "bear": 1, "boar": 1, "caribou": 1, "reindeer": 1, "pheasant": 1, "squab": 1, "rabbit": 1, "squirrel": 1, "bear": 1, "boar": 1, "caribou": 1, "reindeer": 1, "pheasant": 1, "squab": 1, "rabbit": 1, "squirrel": 1, "bear": 1, "boar": 1, "caribou": 1, "reindeer": 1, "pheasant": 1, "squab": 1, "cod": 1, "fish": 1, "crab": 1, "mussels": 1, "octopus": 1, "shrimp": 1, "prawns": 1}
        self.carbs = {"rice": 1, "bread": 1, "pasta": 1, "potatoes": 1}
        self.obviousSpices = {"salt": 1, "pepper": 1, "water": 1,
                              "olive oil": 1, "flour": 1, "sugar": 1, "soy sauce": 1, "vinegar": 1}

        self.nutritionallyDenseFoods = pd.read_pickle('nutrientMap.pkl')
        self.bestIngredientRecipes = pd.read_pickle(
            "bestIngredientsRecipes.pkl")
        
        print(self.bestIngredientRecipes['BREAD'])

        self.actualNamesOfVitamins = pd.read_pickle(
            "actualNamesOfVitamins.pkl")

        # print(self.actualNamesOfVitamins["Protein"])

        # self.imageURLs = {
        #     "CARROT": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUVFRIWEhUVFhQYHBgYGRYcGBkWFhUVGBUaGhoWGBYcIS4lHB4rIRgYJjgmKzAxNTU1GiQ7QDszPy40NTEBDAwMEA8QHxISHzQsJSQ0NDQ0MTE0NDE0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NP/AABEIALcBEwMBIgACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAABAUCAwYBB//EADoQAAIBAgMFBQYEBAcAAAAAAAABAgMRBCExBRJBUWEGInGBsRMyQpGh0VJywfAjU4LhFDNikqLS8f/EABoBAQADAQEBAAAAAAAAAAAAAAACBAUDAQb/xAAyEQACAQMDAQUHAgcAAAAAAAAAAQIDBBESITFBImFxkfAFMlGBobHRE+EUFSNCQ1LB/9oADAMBAAIRAxEAPwD7MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaq1aMFeTsjxtJZYNoPD09AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4YSqJWu0r6DIPZySTb0Rz+18YtW1bgv3xJW1cbburPp16mnZ2y95qpVV7+7F8uq5GdVqSrT/AE4cL1n8d5JLBK2LUnKEd5WglZOWc5u/vckumfiWp4el+EdMcEQAa6dRSvutO2Ts72fIkDYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARsViVBc3wX3PcXiFCN3rwXNnMYrFvNu7bK9euqey5LFCg6j7jPaOMlL3peC4LwRUf4iWfedujZjUrbxhTln52MapUc5ZybUaCjDTg6fZVq0rzS7tnb8T5nQnJbBuqyS0abfRW+9jrTWs8OnnBiXNNU6mFwACJjajUd2PvTe7HpfWXkrssylpWTgaKuJlarKLSjFOMb6OfFvonb6lV2VhGHtIQ35Xe9OpK1t7hZLnd5GraeKT3aVP3Y5c96XPrn6kxN0oRoUf8AOlm3+G+rZQVTVU1dI/Vvovt4IljCOgBhTVkk3dpLPn1MzRIgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8Z6Vu1MUordvm9ei/uRlLSskoxcnhFXtTFXk3nbSPhzOfxFRtkzH4rVJlfF3MOvUcpH0FtS0R4PIQuboQSvfyM4xsrkfEV1GLcnZI48Hb3jqOzFG+/Ua17i8Fm/0+R0R82wm2KiSUJSjFcFJrz1LfZ/aCcZJVHvR4/iiuafHzNK3u6cYqD8zLubOrKTmvI7I5va2N7zs87NR6ResvF+hJ2jtiKgnDvb2lvV9Ohx2Lxc73ne8nrxVxeV8rRB+LM+MH1LbBV4xbm1dxdoR/FLn4R9bHR7JwTinOpnVnnJ8k8939/oU3ZnZ7k1Vmu7HKC4XXHwXqdWTs6T0qT+X58fh3HkmegAvkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXUmopt6I5bH4m7cm839Oha7axNrRv1f6I5XFVW3yXIzrytjsmnY0c9p9TTUndsUbXz0PLc+J7NK1v3cy1zk1nxhGVSaXEoMXVdSVl7qfzfMm46okrReb15pciBTlutcuPVcQzpTSRMwbtk+PqWEcuvLr/wCr0KmpXS3Wv2jesUpLimeLY8ks7llTxUrWgm3e26tbvki52f2dlUkp4h2jwh8TXJvh6+BQ7CxyjXhOV1FX3na/wtac72Ooq9p4vKnHzk7Px3V9y7b/AKOM1H8jIu7epKr/AE489eh0NOCikopJLJJZJJcDYcVW25Wb96y6JKxgtqVf5k/ne/zLf8fSTwk/ocf5fVxltevkdwDnNmbcbajVtnkpaZ8N77lpitpwgnbvPktL/m0LELinKOpPYq1aM6ctMieDmanaCTvbch43k/PgRJbfqfzYr+hfc5SvKUSGlnYg5CPaGpwqU5eMXH6q5f7Jx3toKUt1SV1JJ3Szyz6onSuqdR6Y8nji0WAALB4AAAAAAAAAAAAAAAAAAAAADTXqqMXJ8Pq+RoxePhDJu75cvEpMbipSTlveHJeRXq14x2XJ3pUJT3eyIm0KzlJtv+75Fcsz2pN3abVv3mYRa0MactTyzdhDRHCM52irlbjsVuq/HRePM2YzFKEZSk1ZfXocvi9oObbfH6dCK7RYhDqTPb2bbd+fXqRcRjM01wNNHDznwsub+xZ4bZ0VZ6vm+DPXhcnTGCLTU5pWjbq8ixw+DWW823++BKpUUbo2RycsnrMoxUEuRsqSSW9FeBrm7prgYxVlYasrBz0m6GIvqrMyo1Xo+HE0GbIpvkSiibTaV75Pnwa4EmNdOLTay9CtlK+WvB/oWmwtmxrymp727BLR2u23k35FiipTnpj1M68iv0m/gVWKlHhKKK2W8r2lFp63v9D6RDs9hkrezv1cpX+dzViOzGGkrez3XwcZSTXzbRcdjU5yjH1o4CE0/eXTKx2nY+MdybjKTd4pppK1lfLN3WfQrcT2SqU3vUJRqJZ7sklL692X0Ljs9g1b2kqPsaibi0t6MWra7jdl5C2oThV7S9dzPJPY6AAGqQAAAAAAAAAAAAAAAABhOSSbeSAPW+ZTbQ2qllHLrxfgatq7WVnFaepymNxd+Jl3V6l2YGlaWTn2pEzE43PrzJGIe6rcik2ZF1KsVbKL3nytFp+ti02hUblZaGfGb0uT6mlOCjNRXQit3Z5WaS1Nrikr8Sm2nX3u5Hwk+nIgdoLU9is2lN1pWTbprRL4ucn0NuFwEVZpJEmhh1FE2EEeub4LGy2NVPDW0N27b9RGXA8kyBHk84mbWZ4npce0seYGTJIzilxNPtjXKqe4Im+c0tDF1CM5tuyzbySWbb8C72f2ar1N11Eqcdby9635NU/Gx0hSnU2isnKpWp0vfZCw8JSajFOUnolzO72Ls72MLO2+85Phfkui+5nsrZVOhFqCd3bek85St6LoWJs2tqqO75+xh3V263ZXu/cAAuFIAAAAAAAAAAAAAAAAAAAGFSooq7dkG8ASmkrvJHP7X2nF2UW0l5X8TTtja2qXkjmcVjW9XYx7y9W8IGtZ2TfbkZ4rEXbzKivXu7LN8Es22SsJRqVm91WitZPReHN9C3wlClSu4Xc1rKWvlyM6NJy3ka7nGmsLd+ufWTDZFCUITcotSk9H+FdeGry8DdGF82tCRWqd2N9Wr+FyFi8RuQ6vTxsdZtZwuEVU3Jt9WyNtPENRcYPvP6IradCyT4v1NsIt5y1Zuja1n+2QyXF2FhGunCxsRrnVSNLrnmEeZ6kiclcw9oiRh9j4mo+7Smk/il3VbxkXeE7GSavWqJPgore+bdvQswtasuI+exWqXdGHMvLc5mVTJm7C4OpVdqcJT6pd1eMnkvNnebP7OUKS93fl+KdpfJWsi3hBJWSSXJKy+Rbp+z/935FGp7TX9i8/wcNgeydaT/iuNOPK6lL5LL6l1huyeHjnLem+rsvlGx0Nj0twtKUemfEo1LyvN7yx4EXDYKnTVqcIx8Ek/nqSgCytisAAAAAAAAAAAAAAAAAAAAAAeXKraG2IwVo5vnwX3OdSrGnHVJk4U5TeIom4rFRpq8n5HLbV2q5PJ6aLgQdo7TlK92zRT2TXqK8ounDVyn3br/THVmNXuqlw3CmtvXJrULSFFaqjWSFiMTnrdvzd+VkTMHsre79e6Xww0b/Nb0JdOlTo+4ry4zebfnw8ER6+Jb45FVKEHmW7LznKaxDZfHr+xtnibJKKUUslFaJEVtyklzfqzS5meAbc436+jPNTk9yehQi2izqcW+BT4me83fTTyLDaNa1orxf6ehqweyq9fOnG0X8cu7HXhxfkdIwlN4XJxjONOOqbwQN/g+BtwuBq1nalCUlpvWtFeMnkdfs/stShnV/iS14xin+VPPzL6nTUUkkklokrJeCNClYP/I/kilW9pLims97OOw/Yltp1qtlxjCOf+9/Y6HZ+w6FGzhTW8vil3pfN6eRaAvU6FOn7qM+rc1avvS+R5Y9AOxwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKPbleomowjJpq94pvPRp20Kins5SzrTUFyXfl52ukdXi6G/CUb23la+tvIoJ9n6iXdqRl4px9LmZdW8pVNSjq8X9On3NC3rRUNLlpfhz89/sQ8RSoQt7KN2vjldyvzSeS8iLPGzfvSbJctiYj8Kf9UfpdmNHs/iHruL80v+qZSlSuJPaDXctkXYzoRXamn3t5f/AEq6lZvXQ0Nl9LsvW4VKf/L7EvC9lILOrOUuke6vnq/oI2NdvdeZN3tvBbPyOR3lfPiTNmbPqN+0UJKEU25NWTVrZX18juMNsehDONOF+bW8/mzfjl/Cqfll6FqPs7TFuT6Pgqz9p6npgufiU2zdi0pWqzW83pF+4t3K9uOnE6GxD2WrUoeD9WTTQt4qNOOOqRnV5uU3l8cAAHY5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHlj0AAAAAGqsrxkuj9DaDxrIIuz3elT/LH0JR4j0RWlJfA9k8tv4gAHp4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAf//Z",
        #     "PEPPERS": "data:image/jpeg;base64,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",
        #     "PUMPKIN": ""
        # }

        # self.nutritionallyDenseFoods = defaultdict(list)
        # self.recipesWithFoods = defaultdict(list)
        self.ingredientMap = {}
        for i in self.currentIngredients:
            self.ingredientMap[i.upper()] = 1

    def changeIngredients(self, currentIngredients):
        self.currentIngredients = currentIngredients
        self.ingredientMap = {}
        for i in self.currentIngredients:
            self.ingredientMap[i.upper()] = 1

    def getNutritionalInformation(self):

        information = [0 for element in range(
            len(self.nutritionallyDenseFoods))]

        val = "Data.Alpha Carotene,Data.Ash,Data.Beta Carotene,Data.Beta Cryptoxanthin,Data.Carbohydrate,Data.Cholesterol,Data.Choline,Data.Fiber,Data.Kilocalories,Data.Lutein and Zeaxanthin,Data.Lycopene,Data.Manganese,Data.Niacin,Data.Pantothenic Acid,Data.Protein,Data.Refuse Percentage,Data.Retinol,Data.Riboflavin,Data.Selenium,Data.Sugar Total,Data.Thiamin,Data.Water,Data.Fat.Monosaturated Fat,Data.Fat.Polysaturated Fat,Data.Fat.Saturated Fat,Data.Fat.Total Lipid,Data.Household Weights.1st Household Weight,Data.Household Weights.1st Household Weight Description,Data.Household Weights.2nd Household Weight,Data.Household Weights.2nd Household Weight Description,Data.Major Minerals.Calcium,Data.Major Minerals.Copper,Data.Major Minerals.Iron,Data.Major Minerals.Magnesium,Data.Major Minerals.Phosphorus,Data.Major Minerals.Potassium,Data.Major Minerals.Sodium,Data.Major Minerals.Zinc,Data.Vitamins.Vitamin A - IU,Data.Vitamins.Vitamin A - RAE,Data.Vitamins.Vitamin B12,Data.Vitamins.Vitamin B6,Data.Vitamins.Vitamin C,Data.Vitamins.Vitamin E,Data.Vitamins.Vitamin K"

        val = val.split(",")

        # Get all the recipes that contain the current ingredients

        # keys = self.nutritionallyDenseFoods.keys()

        for name, data in self.nutrients.iterrows():
            currIngredient = data['Category']
            if currIngredient.upper() not in self.ingredientMap:
                continue
            else:
                information[0] += float(data[val[0]])
                information[1] += float(data[val[1]])
                information[2] += float(data[val[2]])
                information[3] += float(data[val[3]])
                information[4] += float(data[val[4]])
                # information[5] += float(data[val[5]])
                information[6] += float(data[val[6]])
                information[7] += float(data[val[7]])
                # information[8] += float(data[val[8]])
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

        information = self.getNutritionalInformation()

        print(information)

        areasToImprove = []
        val = "Data.Alpha Carotene,Data.Ash,Data.Beta Carotene,Data.Beta Cryptoxanthin,Data.Carbohydrate,Data.Cholesterol,Data.Choline,Data.Fiber,Data.Kilocalories,Data.Lutein and Zeaxanthin,Data.Lycopene,Data.Manganese,Data.Niacin,Data.Pantothenic Acid,Data.Protein,Data.Refuse Percentage,Data.Retinol,Data.Riboflavin,Data.Selenium,Data.Sugar Total,Data.Thiamin,Data.Water,Data.Fat.Monosaturated Fat,Data.Fat.Polysaturated Fat,Data.Fat.Saturated Fat,Data.Fat.Total Lipid,Data.Household Weights.1st Household Weight,Data.Household Weights.1st Household Weight Description,Data.Household Weights.2nd Household Weight,Data.Household Weights.2nd Household Weight Description,Data.Major Minerals.Calcium,Data.Major Minerals.Copper,Data.Major Minerals.Iron,Data.Major Minerals.Magnesium,Data.Major Minerals.Phosphorus,Data.Major Minerals.Potassium,Data.Major Minerals.Sodium,Data.Major Minerals.Zinc,Data.Vitamins.Vitamin A - IU,Data.Vitamins.Vitamin A - RAE,Data.Vitamins.Vitamin B12,Data.Vitamins.Vitamin B6,Data.Vitamins.Vitamin C,Data.Vitamins.Vitamin E,Data.Vitamins.Vitamin K"
        val = val.split(",")
        # print(val)

        if information[14] < 50:  # Protein
            areasToImprove.append((val[14])[5:])
        if information[0] < 216:  # Alpha Carotene
            areasToImprove.append((val[0])[5:])
        if information[1] < 50:  # Ash
            areasToImprove.append((val[1])[5:])
        if information[2] < 150:  # Beta Carotene
            areasToImprove.append((val[2])[5:])
        if information[38] < 10000:  # Vitamins.Vitamin A - IU
            areasToImprove.append((val[38])[14:])
        if information[39] < 700:  # Vitamins.Vitamin A - RAE
            areasToImprove.append((val[39])[14:])
        if information[40] < 0.002:  # Vitamins.Vitamin B12
            areasToImprove.append((val[40])[14:])
        if information[41] < 0.010:  # Vitamins.Vitamin B6
            areasToImprove.append((val[41])[14:])
        if information[42] < 10.0:  # Vitamins.Vitamin C
            areasToImprove.append((val[42])[14:])
        if information[43] < 1.0:  # Vitamins.Vitamin E
            areasToImprove.append((val[43])[14:])
        if information[44] < 610:  # Vitamins.Vitamin K
            areasToImprove.append((val[44])[14:])
        if information[3] < 200:  # Beta Cryptoxanthin
            areasToImprove.append((val[3])[5:])
        if information[4] < 800:  # Carbohydrate
            areasToImprove.append((val[4])[5:])
        # if information[5] < 0:  # Cholestrol
        #     areasToImprove.append((val[5])[5:])
        if information[6] < 400:  # Choline
            areasToImprove.append((val[6])[5:])
        if information[7] < 20:  # Fiber
            areasToImprove.append((val[7])[5:])
        # if information[8] < 1000:  # Kilocalories
        #     areasToImprove.append((val[8])[5:])
        if information[9] < 10:  # Lutein and Zeaxanthin
            areasToImprove.append((val[9])[5:])
        if information[10] < 6:  # Lycopene
            areasToImprove.append((val[10])[5:])
        if information[11] < 1.5:  # Manganese
            areasToImprove.append((val[11])[5:])
        if information[12] < 1.0:  # Niacin
            areasToImprove.append((val[12])[5:])
        if information[13] < 0.5:  # Pantothenic Acid
            areasToImprove.append((val[13])[5:])
        # if information[15] < 50:  # Refuse Percentage
        #     areasToImprove.append((val[15])[5:])
        if information[16] < 0:  # Retinol
            areasToImprove.append((val[16])[5:])
        if information[17] < 1:  # Riboflavin
            areasToImprove.append((val[17])[5:])
        if information[18] < 1.0:  # Selenium
            areasToImprove.append((val[18])[5:])
        # if information[19] < 0:  # Sugar Total
        #     areasToImprove.append((val[19])[5:])
        if information[20] < 0.01:  # Thiamin
            areasToImprove.append((val[20])[5:])
        if information[21] < 0:  # Water
            areasToImprove.append((val[21])[9:])
        if information[22] < 0.010:  # Fat.Monounsaturated Fat
            areasToImprove.append((val[22])[9:])
        if information[23] < 0.100:  # Fat.Polyunsaturated Fat
            areasToImprove.append((val[23])[9:])
        # if information[24] < 1.00:  # Fat.Saturated Fat
        #     areasToImprove.append((val[24])[5:])
        if information[25] < 1.0:  # Fat.Total Lipid
            areasToImprove.append((val[25])[9:])
        # if information[26] < 0:  # Household Weights.1st Household Weight
        #     areasToImprove.append((val[26])[5:])
        # if information[27] < 0:  # Household Weights.1st Household Weight Description
        #     areasToImprove.append((val[27])[5:])
        # if information[28] < 0:  # Household Weights.2nd Household Weight
        #     areasToImprove.append((val[28])[5:])
        # if information[29] < 0:  # Household Weights.2nd Household Weight Description
        #     areasToImprove.append((val[29])[5:])
        if information[30] < 20:  # Major Minerals.Calcium
            areasToImprove.append((val[30])[20:])
        if information[31] < 0.200:  # Major Minerals.Copper
            areasToImprove.append((val[31])[20:])
        if information[32] < 1.0:  # Major Minerals.Iron
            areasToImprove.append((val[32])[20:])
        if information[33] < 300:  # Major Minerals.Magnesium
            areasToImprove.append((val[33])[20:])
        if information[34] < 100:  # Major Minerals.Phosphorus
            areasToImprove.append((val[34])[20:])
        if information[35] < 1000:  # Major Minerals.Potassium
            areasToImprove.append((val[35])[20:])
        if information[36] < 1000:  # Major Minerals.Sodium
            areasToImprove.append((val[36])[20:])
        if information[37] < 3:  # Major Minerals.Zinc
            areasToImprove.append((val[37])[20:])

        areasToImproveMap = {}

        # print(areasToImprove)

        for i in range(len(areasToImprove)):
            if areasToImprove[i] in self.actualNamesOfVitamins:
                areasToImprove[i] = self.actualNamesOfVitamins[areasToImprove[i]]
            ingredients = []
            for j in self.nutritionallyDenseFoods[areasToImprove[i]]:
                if j.lower() not in self.recipesForEachIngredient:
                    continue
                ingredients.append(j)
                if len(ingredients) > 2:
                    break
            if i == 6:
                break
            areasToImproveMap[areasToImprove[i]] = ingredients
        return areasToImproveMap

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
            if not (val):
                continue
            if ((totalIngredientsMatch/len(ingredients)) > 0.5):
                possibleRecipes[i] = ingredients

        return possibleRecipes

    def determineAdditionalRecipes(self):

        areasToImprove = self.determineAreasToImprove()
        areasToImprove = list(areasToImprove.keys())

        recipes = defaultdict(list)
        # print(self.actualNamesOfVitamins.keys())

        for i in range(len(areasToImprove)):
            if i == 5:
                break
            if areasToImprove[i] in self.actualNamesOfVitamins:
                areasToImprove[i] = self.actualNamesOfVitamins[areasToImprove[i]]
            ingredients = self.nutritionallyDenseFoods[areasToImprove[i]]
            for j in ingredients:
                if len(recipes[i]) > 2:
                    break
                possibleRecipes = self.bestIngredientRecipes[j]
                if (len(possibleRecipes) > 0):
                    recipes[areasToImprove[i]].append(possibleRecipes[0])
                continue

        return recipes


# Create an instance of the readingData class (assuming readingData is a class)
# data_instance = readingData([])

# Call the determineAreasToImprove method and store the result in a variable
# result = data_instance.determineAdditionalRecipes()

# Now, you can print the result
# print(result)
