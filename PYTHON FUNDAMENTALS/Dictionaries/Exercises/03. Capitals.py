countries = input().split(", ")
capitals = input().split(", ")

result_dict = dict(zip(countries, capitals))

for country, capital in result_dict.items():
    print(f"{country} -> {capital}")