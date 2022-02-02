# question: From a dict, how can we print the Key whose value is maximum ??


Tv = {'BreakingBad':100, 'GameOfThrones':12, 'mirzapur' : 88}
 
Keymax = max(Tv, key= lambda x: Tv[x])
print(Keymax)