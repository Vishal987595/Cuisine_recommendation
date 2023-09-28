from model import read_dataset
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline   
import re

special_character_remover = re.compile('[/(){}\[\]\|@,:]') 
extra_symbol_remover = re.compile('[^-9a-z #+_]')

def clean_recipe(text):
   text = special_character_remover.sub('', text) 
   text = extra_symbol_remover.sub('', text)
   # Removing the stopwords
   return text

def take_input(X, y):
    # recipe_name = input("Enter recipe name:").lower()
    # recipe = input("Enter the recipe: ").lower()
    recipe = "4 tablespoons olive oil $ 1 large onion, diced (about 2 cups) $ 3 stalks celery, diced (about 1 1/2 cups) $ 3 large carrots, peeled and cut in rounds $ 1/2 teaspoon ground turmeric $ 1 teaspoon ground cumin $ 1/2 to 1 teaspoon harissa or dried red chile flakes, plus more for serving $ Salt to taste $ 1 bunch parsley, chopped (about 1 1/2 cups/75 grams), divided $ 1 bunch cilantro, chopped (about 1 1/2 cups/75 grams), divided $ 1 (15-ounce/425-gram) can tomatoes, crushed, or 2 cups (450 grams) tomato sauce $ 7 cups (1 2/3 liters) chicken or vegetable stock $ 1 cup (200 grams) dried chickpeas, soaked overnight and cooked or 1 (15-ounce/425-gram) can chickpeas, drained $ 1 cup (370 grams) green lentils $ 1 teaspoon freshly ground black pepper $ 2 tablespoons all-purpose unbleached flour $ 1 large egg $ Juice of 2 lemons (about 1/4 cup) $ "
    clean_recipe(recipe)
    lr = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', LogisticRegression())])
    lr.fit(X, y)
    ans = lr.predict([recipe])
    print(ans)
    return
if __name__ == "__main__":
    X, y = read_dataset()
    take_input(X, y) 