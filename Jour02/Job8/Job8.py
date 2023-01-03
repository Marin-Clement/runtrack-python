legumes = {
    "hiver": "carotte, topinambour, endive",
    "ete": "artichaut, aubergine,navet",

}
fruits = {
    "hiver": "orange, mandarine et kiwi",
    "ete": "Poire, fraise, cassis",
}


def FruitSeason(type, saison):
    if type == "fruits":
        return fruits[saison]
    elif type == "legumes":
        return legumes[saison]
    else:
        return "error 404"



print(FruitSeason("fruits", "ete"))
print(FruitSeason("fruits", "hiver"))
print(FruitSeason("legumes", "ete"))
print(FruitSeason("legumes", "hiver"))
print(FruitSeason("efe", "hiver"))
