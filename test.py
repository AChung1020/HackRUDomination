import pandas as pd
from collections import defaultdict
import json


def test():

    # map = checkOpen()

    # ingredients = ["chicken", "eggs", "milk", "yogurt", "squash"]

    # IngredientsWithRecipes = pd.read_pickle('ingredientsToRecipes.pkl')

    # recipeMap = pd.read_pickle('recipe_map.pkl')

    # ingredientMap = pd.read_pickle('actual_ingredients.pkl')
    # ingredientToID = pd.read_pickle('IDToIngredient.pkl')

    # for i in ingredients:
    #     if i not in ingredientToID:
    #         print(i)
    #         continue
    #     Id = ingredientToID[i]
    #     print(Id)
    #     print(ingredientMap[Id])
    #     print(recipesWithIngredients.keys())
    #     print(recipesWithIngredients[Id])

    # pd.to_pickle(IDToIngredient, 'IDToIngredient.pkl')

    # for i in ingredients:
    #     # if i not in ingredientMap:
    #     #     print(i)
    #     #     continue
    #     print(recipesWithIngredients[i])

    # recipes = pd.read_pickle('recipe_map.pkl')
    ingredientMap = pd.read_pickle('actual_ingredients.pkl')

    # ingredientsToRecipes = defaultdict(list)

    recipesIngredients = defaultdict(list)

    df = pd.read_csv('PP_recipes.csv')

    for i, data in df.iterrows():
        ingredients = data['ingredient_tokens']
        recipeId = data['id']
        ingredients = json.loads(ingredients)
        for j in ingredients:
            for k in j:
                if k not in ingredientMap:
                    continue
                else:
                    recipesIngredients[recipeId].append(ingredientMap[k])
    pd.to_pickle(recipesIngredients, 'allIngredientsInARecipe.pkl')

    # ingredientMap = pd.read_pickle(file)

    # actualIngredients = {}

    # for i, data in ingredientMap.iterrows():
    #     actualIngredients[data['id']] = data['raw_ingr']

    # pd.to_pickle(actualIngredients, 'actual_ingredients.pkl')
    # df = pd.read_csv('PP_recipes.csv')

    # print(df.head(5))


def checkOpen():
    file = open('actual_ingredients.pkl', 'rb')
    value = pd.read_pickle(file)
    return value


def returnRecipes(currentIngredients):
    possibleRecipes = []
    recipeMap = pd.read_pickle('recipe_map.pkl')
    ingredientMap = {}
    for i in currentIngredients:
        ingredientMap[i] = 1
    allIngredientsInARecipe = pd.read_pickle('allIngredientsInARecipe.pkl')
    for i in allIngredientsInARecipe.keys():
        data = allIngredientsInARecipe[i]
        total = 0
        for j in data:
            if j in ingredientMap:
                total += 1
            if total >= len(currentIngredients):
                possibleRecipes.append(recipeMap[i])
                break
        if (total >= len(data)) or (total / len(data)) > 0.8:
            possibleRecipes.append(recipeMap[i])

    return possibleRecipes


def test2():

    recipeMap = pd.read_pickle('recipe_map.pkl')


# def getNutritonalInformation(currentIngredients):

#     nutrients = pd.read_csv('food.csv')

#     ingredientMap = {}

#     for i in currentIngredients:
#         ingredientMap[i.upper()] = 1

#     information = [0 for i in range(50)]

#     # Get all the recipes that contain the current ingredients
#     for name, data in nutrients.iterrows():
#         currIngredient = data['Category']
#         if currIngredient not in ingredientMap:
#             continue
#         else:
#             information[0] += float(data['Data.Alpha Carotene'])
#             information[1] += float(data['Data.Ash'])
#             information[2] += float(data['Data.Beta Carotene'])
#             information[3] += float(data['Data.Beta Cryptoxanthin'])
#             information[4] += float(data['Data.Carbohydrate'])
#             information[5] += float(data['Carbs'])

#     return information

# getNutritonalInformation(["chicken", "eggs", "milk", "yogurt", "squash"])

def getBestNutrients():

    val = "Data.Alpha Carotene,Data.Ash,Data.Beta Carotene,Data.Beta Cryptoxanthin,Data.Carbohydrate,Data.Cholesterol,Data.Choline,Data.Fiber,Data.Kilocalories,Data.Lutein and Zeaxanthin,Data.Lycopene,Data.Manganese,Data.Niacin,Data.Pantothenic Acid,Data.Protein,Data.Refuse Percentage,Data.Retinol,Data.Riboflavin,Data.Selenium,Data.Sugar Total,Data.Thiamin,Data.Water,Data.Fat.Monosaturated Fat,Data.Fat.Polysaturated Fat,Data.Fat.Saturated Fat,Data.Fat.Total Lipid,Data.Household Weights.1st Household Weight,Data.Household Weights.1st Household Weight Description,Data.Household Weights.2nd Household Weight,Data.Household Weights.2nd Household Weight Description,Data.Major Minerals.Calcium,Data.Major Minerals.Copper,Data.Major Minerals.Iron,Data.Major Minerals.Magnesium,Data.Major Minerals.Phosphorus,Data.Major Minerals.Potassium,Data.Major Minerals.Sodium,Data.Major Minerals.Zinc,Data.Vitamins.Vitamin A - IU,Data.Vitamins.Vitamin A - RAE,Data.Vitamins.Vitamin B12,Data.Vitamins.Vitamin B6,Data.Vitamins.Vitamin C,Data.Vitamins.Vitamin E,Data.Vitamins.Vitamin K"

    val = val.split(",")

    nutrients = pd.read_csv('food.csv')

    nutrients.sort_values(by=[val[0]], inplace=True, ascending=False)

    AlphaCarotene = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[1]], inplace=True, ascending=False)

    Ash = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[2]], inplace=True, ascending=False)

    BetaCarotene = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[3]], inplace=True, ascending=False)

    BetaCryptoxanthin = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[4]], inplace=True, ascending=False)

    Carbohydrate = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[5]], inplace=True, ascending=False)

    Cholesterol = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[6]], inplace=True, ascending=False)

    Choline = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[7]], inplace=True, ascending=False)

    Fiber = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[8]], inplace=True, ascending=False)

    Kilocalories = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[9]], inplace=True, ascending=False)

    LuteinandZeaxanthin = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[10]], inplace=True, ascending=False)

    Lycopene = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[11]], inplace=True, ascending=False)

    Manganese = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[12]], inplace=True, ascending=False)

    Niacin = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[13]], inplace=True, ascending=False)

    PantothenicAcid = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[14]], inplace=True, ascending=False)

    Protein = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[15]], inplace=True, ascending=False)

    RefusePercentage = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[16]], inplace=True, ascending=False)

    Retinol = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[17]], inplace=True, ascending=False)

    Riboflavin = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[18]], inplace=True, ascending=False)

    Selenium = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[19]], inplace=True, ascending=False)

    SugarTotal = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[20]], inplace=True, ascending=False)

    Thiamin = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[21]], inplace=True, ascending=False)

    Water = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[22]], inplace=True, ascending=False)

    MonosaturatedFat = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[23]], inplace=True, ascending=False)

    PolysaturatedFat = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[24]], inplace=True, ascending=False)

    SaturatedFat = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[25]], inplace=True, ascending=False)

    TotalLipid = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[26]], inplace=True, ascending=False)

    HouseholdWeights1stHouseholdWeight = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[27]], inplace=True, ascending=False)

    HouseholdWeights1stHouseholdWeightDescription = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[28]], inplace=True, ascending=False)

    HouseholdWeights2ndHouseholdWeight = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[29]], inplace=True, ascending=False)

    HouseholdWeights2ndHouseholdWeightDescription = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[30]], inplace=True, ascending=False)

    Calcium = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[31]], inplace=True, ascending=False)

    Copper = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[32]], inplace=True, ascending=False)

    Iron = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[33]], inplace=True, ascending=False)

    Magnesium = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[34]], inplace=True, ascending=False)

    Phosphorus = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[35]], inplace=True, ascending=False)

    Potassium = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[36]], inplace=True, ascending=False)

    Sodium = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[37]], inplace=True, ascending=False)

    Zinc = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[38]], inplace=True, ascending=False)

    VitaminA_IU = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[39]], inplace=True, ascending=False)

    VitaminA_RAE = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[40]], inplace=True, ascending=False)

    VitaminB12 = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[41]], inplace=True, ascending=False)

    VitaminB6 = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[42]], inplace=True, ascending=False)

    VitaminC = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[43]], inplace=True, ascending=False)

    VitaminE = set(nutrients['Category'].head(10).tolist())

    nutrients.sort_values(by=[val[44]], inplace=True, ascending=False)

    VitaminK = set(nutrients['Category'].head(10).tolist())

    nutrientMap = {}
    nutrientMap["AlphaCarotene"] = AlphaCarotene
    nutrientMap["Ash"] = Ash
    nutrientMap["BetaCarotene"] = BetaCarotene
    nutrientMap["BetaCryptoxanthin"] = BetaCryptoxanthin
    nutrientMap["Carbohydrate"] = Carbohydrate
    nutrientMap["Cholesterol"] = Cholesterol
    nutrientMap["Choline"] = Choline
    nutrientMap["Fiber"] = Fiber
    nutrientMap["Kilocalories"] = Kilocalories
    nutrientMap["LuteinandZeaxanthin"] = LuteinandZeaxanthin
    nutrientMap["Lycopene"] = Lycopene
    nutrientMap["Manganese"] = Manganese
    nutrientMap["Niacin"] = Niacin
    nutrientMap["PantothenicAcid"] = PantothenicAcid
    nutrientMap["Protein"] = Protein
    nutrientMap["RefusePercentage"] = RefusePercentage
    nutrientMap["Retinol"] = Retinol
    nutrientMap["Riboflavin"] = Riboflavin
    nutrientMap["Selenium"] = Selenium
    nutrientMap["SugarTotal"] = SugarTotal
    nutrientMap["Thiamin"] = Thiamin
    nutrientMap["Water"] = Water
    nutrientMap["MonosaturatedFat"] = MonosaturatedFat
    nutrientMap["PolysaturatedFat"] = PolysaturatedFat
    nutrientMap["SaturatedFat"] = SaturatedFat
    nutrientMap["TotalLipid"] = TotalLipid
    nutrientMap["HouseholdWeights1stHouseholdWeight"] = HouseholdWeights1stHouseholdWeight
    nutrientMap["HouseholdWeights1stHouseholdWeightDescription"] = HouseholdWeights1stHouseholdWeightDescription
    nutrientMap["HouseholdWeights2ndHouseholdWeight"] = HouseholdWeights2ndHouseholdWeight
    nutrientMap["HouseholdWeights2ndHouseholdWeightDescription"] = HouseholdWeights2ndHouseholdWeightDescription
    nutrientMap["Calcium"] = Calcium
    nutrientMap["Copper"] = Copper
    nutrientMap["Iron"] = Iron
    nutrientMap["Magnesium"] = Magnesium
    nutrientMap["Phosphorus"] = Phosphorus
    nutrientMap["Potassium"] = Potassium
    nutrientMap["Sodium"] = Sodium
    nutrientMap["Zinc"] = Zinc
    nutrientMap["VitaminA_IU"] = VitaminA_IU
    nutrientMap["VitaminA_RAE"] = VitaminA_RAE
    nutrientMap["VitaminB12"] = VitaminB12
    nutrientMap["VitaminB6"] = VitaminB6
    nutrientMap["VitaminC"] = VitaminC
    nutrientMap["VitaminE"] = VitaminE
    nutrientMap["VitaminK"] = VitaminK

    pd.to_pickle(nutrientMap, 'nutrientMap.pkl')


def test3():

    nutrientMap = pd.read_pickle('nutrientMap.pkl')
    print(nutrientMap)

def test4(currentIngredients):

    nutritionallyDenseFoods = pd.read_pickle('nutrientMap.pkl')

    nutrients = pd.read_csv('food.csv')
        
    information = [0 for element in range(len(nutritionallyDenseFoods))]

    val = "Data.Alpha Carotene,Data.Ash,Data.Beta Carotene,Data.Beta Cryptoxanthin,Data.Carbohydrate,Data.Cholesterol,Data.Choline,Data.Fiber,Data.Kilocalories,Data.Lutein and Zeaxanthin,Data.Lycopene,Data.Manganese,Data.Niacin,Data.Pantothenic Acid,Data.Protein,Data.Refuse Percentage,Data.Retinol,Data.Riboflavin,Data.Selenium,Data.Sugar Total,Data.Thiamin,Data.Water,Data.Fat.Monosaturated Fat,Data.Fat.Polysaturated Fat,Data.Fat.Saturated Fat,Data.Fat.Total Lipid,Data.Household Weights.1st Household Weight,Data.Household Weights.1st Household Weight Description,Data.Household Weights.2nd Household Weight,Data.Household Weights.2nd Household Weight Description,Data.Major Minerals.Calcium,Data.Major Minerals.Copper,Data.Major Minerals.Iron,Data.Major Minerals.Magnesium,Data.Major Minerals.Phosphorus,Data.Major Minerals.Potassium,Data.Major Minerals.Sodium,Data.Major Minerals.Zinc,Data.Vitamins.Vitamin A - IU,Data.Vitamins.Vitamin A - RAE,Data.Vitamins.Vitamin B12,Data.Vitamins.Vitamin B6,Data.Vitamins.Vitamin C,Data.Vitamins.Vitamin E,Data.Vitamins.Vitamin K"

    val = val.split(",")
    
    # Get all the recipes that contain the current ingredients

    keys = nutritionallyDenseFoods.keys()

    ingredientMap = {}
    
    for i in currentIngredients:
        ingredientMap[i.upper()] = 1

    for name, data in nutrients.iterrows():
        currIngredient = data['Category']
        if currIngredient not in ingredientMap or ingredientMap[currIngredient] == 0:
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
            ingredientMap[currIngredient] = 0
    return information

print(test4(["chicken", "eggs", "milk", "yogurt", "squash"]))

    # def populateNutritionallyDenseFoods(self):
        
    #     def populateProtein():
    #         self.nutritionallyDenseFoods["protein"].append("chicken")
    #         self.nutritionallyDenseFoods["protein"].append("beef")
    #         self.nutritionallyDenseFoods["protein"].append("pork")
    #         self.nutritionallyDenseFoods["protein"].append("fish")
    #         self.nutritionallyDenseFoods["protein"].append("egg")
    #         self.nutritionallyDenseFoods["protein"].append("tofu")
    #         self.nutritionallyDenseFoods["protein"].append("beans")
            
    #     def populateCarbs():
    #         self.nutritionallyDenseFoods["carbs"].append("rice")
    #         self.nutritionallyDenseFoods["carbs"].append("bread")
    #         self.nutritionallyDenseFoods["carbs"].append("pasta")
    #         self.nutritionallyDenseFoods["carbs"].append("potato")
    #         self.nutritionallyDenseFoods["carbs"].append("corn")

    #     def populateFiber():
    #         self.nutritionallyDenseFoods["fiber"].append("broccoli")
    #         self.nutritionallyDenseFoods["fiber"].append("spinach")
    #         self.nutritionallyDenseFoods["fiber"].append("carrots")
    #         self.nutritionallyDenseFoods["fiber"].append("kale")
    #         self.nutritionallyDenseFoods["fiber"].append("avocado")

    #     def populateVitamins():
    #         self.nutritionallyDenseFoods["vitamins"].append("orange")
    #         self.nutritionallyDenseFoods["vitamins"].append("apple")
    #         self.nutritionallyDenseFoods["vitamins"].append("banana")
    #         self.nutritionallyDenseFoods["vitamins"].append("grapes")
        
    #     def populateFats():
    #         self.nutritionallyDenseFoods["fats"].append("avocado")
    #         self.nutritionallyDenseFoods["fats"].append("cheese")
    #         self.nutritionallyDenseFoods["fats"].append("nuts")
    #         self.nutritionallyDenseFoods["fats"].append("olive oil")

    #     populateCarbs()
    #     populateFats()
    #     populateFiber()
    #     populateFats()
    #     populateProtein()
    #     populateVitamins()


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



