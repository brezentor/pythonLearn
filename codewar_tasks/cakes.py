def cakes(recipe, available):
    res = []
    r = 0
    for i in recipe:
        if ((available.get(i) == None) or (recipe.get(i) > available.get(i))):
            return 0
        else:
            r = available.get(i) // recipe.get(i)
            res.append(r)
    res.sort(reverse=True)
    return res[-1]

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))


