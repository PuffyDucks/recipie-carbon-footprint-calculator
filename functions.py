
import pandas as pd

# return only target ingrediants as a df
def get_ingredients(ingredients, df):

    target_ingredients = pd.DataFrame(columns=df.columns)

    for i in ingredients:
        if i in df['Food product'].values:
            target_ingredients = target_ingredients.append(df.loc[df['Food product']==i])

    return target_ingredients

# return only emissions as a df
def get_emissions(target_ingredients):

    ingredients_emissions = target_ingredients[['Food product', 'Total from Land to Retail']]
    return ingredients_emissions

# get total emissions of meal
def get_total_emissions(ingredients_emissions):

    print(type(ingredients_emissions))

    total_emissions = ingredients_emissions['Total from Land to Retail'].sum()
    return total_emissions


def main():

    # import data into df
    df = pd.read_csv("/Users/claire/Documents/Projects/recipe_emissions/Food_Product_Emissions.csv")

    # get specific ingredients
    ingredients = {"Apples", "Bananas"}
    target_ingredients = get_ingredients(ingredients, df)

    # get specific ingredients emissions
    ingredients_emissions = get_emissions(target_ingredients)

    # get total emissions
    total_emissions = get_total_emissions(ingredients_emissions)
    print(total_emissions)
    

if __name__ == '__main__':
    main()