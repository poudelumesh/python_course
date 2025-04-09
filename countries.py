countries = [{"name": "nepal",
             "population": 29_626_045,
             "name": "france",
             "population": 66_625_247,
             "name": "bhutan",
             "population": 795_468,}]
biggest_country = countries[0]
for country in countries:
    print(f"Name: {country["name"]} - population: {country["population"]:,}")
    if country["population"] > biggest_country["population"]:
        biggest_country = country

    print(f"The biggest country is {biggest_country["name"]} with a population of {biggest_country["population"]:,}")

