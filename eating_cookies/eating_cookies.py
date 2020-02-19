#!/usr/bin/python

import sys
import itertools
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  arr = [1,2,3]
  combo_arr=[]
  for x in range(100):
        combo_arr.extend(
          [
            combo for combo in itertools.combinations_with_replacement(arr,x)
              if sum(combo) == n
          ]
        )
  print(combo_arr)
  ways = 0
  for x in combo_arr:
        if x.count(x[0]) != len(x):
              ways += len(list(dict.fromkeys(list(itertools.permutations(x)))))
        else:
              ways += 1
  return ways

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')