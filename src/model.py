import pandas as pd

def make_dataset():
    try:
        master_data = pd.read_csv('../data/master.csv')
    except:
        number = [i for i in range(174)]
        datasets = [pd.read_csv('data/recipe.csv')]
        for k in number:
            trial = pd.read_csv(f'data/recipe_cuisine_recipe_info{k}.csv')
            datasets.append(trial)
        master_data = pd.concat(datasets).drop_duplicates()
        master_data.to_csv('data/master.csv', index=False)
    return master_data

def read_dataset():
    # master_data = pd.read_csv('../data/master.csv')
    master_data = make_dataset()
    X_dataset = master_data[['name', 'recipe_category']].copy()
    Y_dataset = master_data[['recipe_cuisine']]
    X = []
    Y = []
    recipe_items = set()
    count = 0
    cuisine_type = set()
    for name, items in zip(X_dataset['name'], X_dataset['recipe_category']):
        temp = str(items).split("$")
        for i in temp:
            recipe_items.add(i)
        temp.append(name)
        tempstr = ""
        for i in temp:
            tempstr = tempstr + i + " "
        cuisines = Y_dataset['recipe_cuisine'][count]
        temp = str(cuisines).split("$")
        for j in temp:
            if len(j.strip()):
                cuisine_type.add(j.strip())
                Y.append(j)
                X.append(tempstr)
    return X, Y
