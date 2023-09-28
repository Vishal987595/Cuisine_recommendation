from model import read_dataset
import re

special_character_remover = re.compile('[/(){}\[\]\|@,:]') 
extra_symbol_remover = re.compile('[^-9a-z #+_]')

def clean_recipe(text):
   text = special_character_remover.sub('', text) 
   text = extra_symbol_remover.sub('', text)
   # Removing the stopwords
   return text

def take_input():
    recipe_name = input("Enter recipe name:").lower()
    recipe = input("Enter the recipe: ").lower()
    clean_recipe(recipe)
    predictions = []
    return predictions
if __name__ == "__main__":
    read_dataset()
    take_input()