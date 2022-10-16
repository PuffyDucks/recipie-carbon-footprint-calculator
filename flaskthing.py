from flask import Flask, redirect, url_for, render_template, request
from functions import *

app = Flask(__name__)
df = pd.read_csv("Food_Product_Emissions.csv")


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        ingredients = {}
        #sets ingredient to the input value from textbox
        ingredient = request.form["userinput"]
        if len(ingredient) == 0:
            return render_template("index.html", total_emissions=0, text="", foods=0, emissions=0)
        #adds the ingredient to the dictionary so it can be a parameter for get_ingredients
        ingredients[ingredient] = ""
        ingredients = convert_dictionary(ingredients)
        found_ingredients = get_ingredients(ingredients, df)
        found_ingredients_html = found_ingredients.to_html(index=False)
        print(found_ingredients_html)
        emissions = get_emissions(found_ingredients)
        total_emissions = get_total_emissions(emissions)

        # arrays for javascript to make piechart
        foodsList = get_foods_only(found_ingredients)
        emissionsList = get_emissions_only(found_ingredients)

        #working on trying to pass other info (feed, farm, processing, transport, etc) into index.html
        ingredient_list = dictionary_to_list(ingredient)
        target_ingredients = get_ingredients(ingredient_list, df)
        more_info = []
        for x in target_ingredients:
            more_info.append(x)

        #this is where you pass the parameters into index.html
        return render_template("index.html", total_emissions=total_emissions,  table=found_ingredients_html, text=ingredient, foods=foodsList, emissions=emissionsList)

    else:
        return render_template("index.html")

@app.route("/<test>")
def user(test):
    return f"<h1>{test}</h1>"



if __name__ == ("__main__"):
    app.run(debug=True)


    app.run()
    # ingredients = {"Apples": ""}
    # target_ingredients = get_ingredients(ingredients, df)
    # print(target_ingredients)
    # {"Apples, Bananas": }

