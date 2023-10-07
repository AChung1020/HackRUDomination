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

    val = "Data.Alpha Carotene","Data.Ash","Data.Beta Carotene","Data.Beta Cryptoxanthin","Data.Carbohydrate","Data.Cholesterol","Data.Choline","Data.Fiber","Data.Kilocalories","Data.Lutein and Zeaxanthin","Data.Lycopene","Data.Manganese","Data.Niacin","Data.Pantothenic Acid","Data.Protein","Data.Refuse Percentage","Data.Retinol","Data.Riboflavin","Data.Selenium","Data.Sugar Total","Data.Thiamin","Data.Water","Data.Fat.Monosaturated Fat","Data.Fat.Polysaturated Fat","Data.Fat.Saturated Fat","Data.Fat.Total Lipid","Data.Household Weights.1st Household Weight","Data.Household Weights.1st Household Weight Description","Data.Household Weights.2nd Household Weight","Data.Household Weights.2nd Household Weight Description","Data.Major Minerals.Calcium","Data.Major Minerals.Copper","Data.Major Minerals.Iron","Data.Major Minerals.Magnesium","Data.Major Minerals.Phosphorus","Data.Major Minerals.Potassium","Data.Major Minerals.Sodium","Data.Major Minerals.Zinc","Data.Vitamins.Vitamin A - IU","Data.Vitamins.Vitamin A - RAE","Data.Vitamins.Vitamin B12","Data.Vitamins.Vitamin B6","Data.Vitamins.Vitamin C","Data.Vitamins.Vitamin E","Data.Vitamins.Vitamin K"

    val.split(",")

    nutrients = pd.read_csv('food.csv')

    nutrients.sort_values(by=[val[0]], inplace=True, ascending=False)

    AlphaCarotene = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[1]], inplace=True, ascending=False)

    Ash = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[2]], inplace=True, ascending=False)

    BetaCarotene = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[3]], inplace=True, ascending=False)

    BetaCryptoxanthin = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[4]], inplace=True, ascending=False)

    Carbohydrate = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[5]], inplace=True, ascending=False)

    Cholesterol = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[6]], inplace=True, ascending=False)

    Choline = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[7]], inplace=True, ascending=False)

    Fiber = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[8]], inplace=True, ascending=False)

    Kilocalories = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[9]], inplace=True, ascending=False)

    LuteinandZeaxanthin = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[10]], inplace=True, ascending=False)

    Lycopene = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[11]], inplace=True, ascending=False)

    Manganese = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[12]], inplace=True, ascending=False)

    Niacin = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[13]], inplace=True, ascending=False)

    PantothenicAcid = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[14]], inplace=True, ascending=False)

    Protein = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[15]], inplace=True, ascending=False)

    RefusePercentage = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[16]], inplace=True, ascending=False)

    Retinol = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[17]], inplace=True, ascending=False)

    Riboflavin = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[18]], inplace=True, ascending=False)

    Selenium = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[19]], inplace=True, ascending=False)

    SugarTotal = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[20]], inplace=True, ascending=False)

    Thiamin = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[21]], inplace=True, ascending=False)

    Water = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[22]], inplace=True, ascending=False)

    MonosaturatedFat = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[23]], inplace=True, ascending=False)

    PolysaturatedFat = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[24]], inplace=True, ascending=False)

    SaturatedFat = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[25]], inplace=True, ascending=False)

    TotalLipid = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[26]], inplace=True, ascending=False)

    HouseholdWeights1stHouseholdWeight = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[27]], inplace=True, ascending=False)

    HouseholdWeights1stHouseholdWeightDescription = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[28]], inplace=True, ascending=False)

    HouseholdWeights2ndHouseholdWeight = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[29]], inplace=True, ascending=False)

    HouseholdWeights2ndHouseholdWeightDescription = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[30]], inplace=True, ascending=False)

    Calcium = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[31]], inplace=True, ascending=False)

    Copper = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[32]], inplace=True, ascending=False)

    Iron = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[33]], inplace=True, ascending=False)

    Magnesium = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[34]], inplace=True, ascending=False)

    Phosphorus = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[35]], inplace=True, ascending=False)

    Potassium = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[36]], inplace=True, ascending=False)

    Sodium = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[37]], inplace=True, ascending=False)

    Zinc = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[38]], inplace=True, ascending=False)

    VitaminA_IU = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[39]], inplace=True, ascending=False)

    VitaminA_RAE = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[40]], inplace=True, ascending=False)

    VitaminB12 = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[41]], inplace=True, ascending=False)

    VitaminB6 = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[42]], inplace=True, ascending=False)

    VitaminC = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[43]], inplace=True, ascending=False)

    VitaminE = nutrients['Category'].head(10).tolist()

    nutrients.sort_values(by=[val[44]], inplace=True, ascending=False)

    VitaminK = nutrients['Category'].head(10).tolist()

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


getBestNutrients()