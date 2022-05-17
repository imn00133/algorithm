# https://www.hackerrank.com/contests/kakao-adtech-devday-1st-codejam/challenges/challenge-3412
# Solved Date: 22.04.14.

s = int(input())

arr = ["P", "R", "R",
       "P", "P", "P",
       "R", "P", "P",
       "P", "R", "P", # 11

       "S", "S", "R",
       "P", "P", "S",
       "P", "S", "S",
       "S", "P", "P", # 23

       "R", "R", "R",
       "R", "S", "P",
       "P", "S", "S",
       "P", "R", "S", # 35

       "R", "R", "P",
       "R", "P", "R",
       "R", "S", "S",
       "S", "S", "S", # 47

       "S", "S", "P",
       "S", "P", "R",
       "R", "S", "S",
       "S", "S", "S",
       ]

print(arr[s])
