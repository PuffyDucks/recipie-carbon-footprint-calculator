
import pandas as pd

# return only target ingredients as a df #param list, csv returns dataframe of only ingredient
def get_ingredients(ingredients, df):

    target_ingredients = pd.DataFrame(columns=df.columns)

    for i in ingredients:
        if i in df['Food product'].values:
            target_ingredients = target_ingredients.append(df.loc[df['Food product']==i])
        else:
            print(i + " is not in the database")

    target_ingredients = target_ingredients.drop(['Unit of GHG Emissions'], axis=1)
    return target_ingredients

# return ingredient emissions as a dict #takes data frame returns dictionary values are emissions
def get_emissions(target_ingredients):

    ingredients_emissions = target_ingredients.set_index('Food product').to_dict()['Total from Land to Retail']
    return ingredients_emissions

# get total emissions of meal #returns float input is dictionary
def get_total_emissions(ingredients_emissions):

    total_emissions = sum(ingredients_emissions.values())
    return round(total_emissions, 3)

# get percent of total emissions of each ingredient as a dict #param dictionary returns percentage
def get_percentages(ingredients_emissions, total_emissions):

    percent_total_emissions = {}
    
    for i in ingredients_emissions.keys():
        percent_total_emissions[i] = ingredients_emissions[i]/total_emissions

    return percent_total_emissions


#the user input returns a single dictionary key (ex: {"Bananas, Apple"}), so this converts it into {"Bananas", "Apples"}
def convert_dictionary(dictionary):
    list = []
    done_dictionary = {}
    for x in dictionary:
        list.append(x)
    splitlist = list[0].split(",")
    count = 0
    for x in splitlist:
        splitlist[count] = x.strip();
        count += 1
    for x in splitlist:
        print(x)
        done_dictionary[x] = ""
    return(done_dictionary)

def dictionary_to_list(dictionary):
    list = []
    for x in dictionary:
        list.append(x)
    splitlist = list[0].split(",")
    count = 0
    for x in splitlist:
        splitlist[count] = x.strip()
        count += 1
    return(splitlist)

def get_emissions_only(target_ingredients):
    emissions_only = []
    emissions_only = list(target_ingredients['Total from Land to Retail'])
    return emissions_only

def get_foods_only(target_ingredients):
    foods_only = []
    foods_only = list(target_ingredients['Food product'])
    return foods_only

def main():

    # import data into df
    df = pd.read_csv("Food_Product_Emissions.csv")

    # get specific ingredients
    ingredients = ("Apples", "Bananas", "Palm Oil", "Tofu", "test")
    target_ingredients = get_ingredients(ingredients, df)

    # get specific ingredients emissions
    ingredients_emissions = get_emissions(target_ingredients)

    # get total emissions
    total_emissions = get_total_emissions(ingredients_emissions)

    # get percent total emissions for each ingredient
    percent_total_emissions = get_percentages(ingredients_emissions, total_emissions)

    testdict = {"Apples, Bananas,Mango"}
    print(target_ingredients)
    print(dictionary_to_list(testdict))

if __name__ == '__main__':
    main()
