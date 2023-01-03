langages = {
    "javascript": "tu est un devellopeur web",
    "python": "tu es un developpeur IA",
    "java": "tu es un developpeur logiciel",
    "reactjs": "tu es un developpeur mobile",
}


def Developpeur(lang):
    if lang.lower() in langages:
        return langages[lang.lower()]
    else:
        return "un jour, je serai le meilleur developpeur..."


print(Developpeur("javascript"))
print(Developpeur("python"))
print(Developpeur("java"))
print(Developpeur("reactjs"))
print(Developpeur("mama"))
