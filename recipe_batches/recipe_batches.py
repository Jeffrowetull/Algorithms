#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  if ingredients.keys() != recipe.keys():
        return 0
  batches = 0
  recipe = list(recipe.values())
  ingredients = list(ingredients.values())
  x = [i//r for i,r in zip(ingredients,recipe)]
  batches = min(x)
  return batches
                          


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 200, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))