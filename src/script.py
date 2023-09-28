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
    recipe_name = input("Enter recipe name:").lower()
    recipe = input("Enter the recipe: ").lower()
    clean_recipe(recipe)
    lr = Pipeline([('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LogisticRegression())
    ])
    lr.fit(X, y)
    ans = lr.predict(recipe+recipe_name)
    print(ans)
    return
if __name__ == "__main__":
    X, y = read_dataset()
    take_input(X, y)