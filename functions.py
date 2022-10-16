
import pandas as pd

# return only target ingrediants as a df
def get_ingredients(ingredients, df):

    target_ingredients = pd.DataFrame(columns=df.columns)

    for i in ingredients:
        if i in df['Food product'].values:
            target_ingredients = target_ingredients.append(df.loc[df['Food product']==i])
        else:
            print(i + " is not in the database")

    return target_ingredients

# return ingredient emissions as a dict
def get_emissions(target_ingredients):

    ingredients_emissions = target_ingredients.set_index('Food product').to_dict()['Total from Land to Retail']
    return ingredients_emissions

# get total emissions of meal
def get_total_emissions(ingredients_emissions):

    print(type(ingredients_emissions))

    total_emissions = sum(ingredients_emissions.values())
    return total_emissions

# get percent of total emissions of each ingredient as a dict
def get_percentages(ingredients_emissions, total_emissions):

    percent_total_emissions = {}
    
    for i in ingredients_emissions.keys():
        percent_total_emissions[i] = ingredients_emissions[i]/total_emissions

    return percent_total_emissions

def main():

    # import data into df
    df = pd.read_csv("/Users/claire/Documents/Projects/recipe_emissions/Food_Product_Emissions.csv")

    # get specific ingredients
    ingredients = {"Apples", "Bananas", "Palm Oil", "Tofu", "test"}
    target_ingredients = get_ingredients(ingredients, df)

    # get specific ingredients emissions
    ingredients_emissions = get_emissions(target_ingredients)
    print(ingredients_emissions)

    # get total emissions
    total_emissions = get_total_emissions(ingredients_emissions)
    print(total_emissions)

    # get percent total emissions for each ingredient
    percent_total_emissions = get_percentages(ingredients_emissions, total_emissions)
    print(percent_total_emissions)

if __name__ == '__main__':
    main()
