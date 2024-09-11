# 3. Merge dictionaries a and b. The resultant dict must contain all items of 
# both dicts. If key is common then the value of key in resultant dict 
# must be the sum of value in a and b.
a = {'x': 1, 'y': 2, 'z': 3}
b = {'a': 4, 'b': 5, 'y': 6}
def dictMerge(a, b):
    # for merge both dictionaries create one empty result dictionary
  result = {}
  
#   first add one dict all elements and value in result dict
  for i in a:
    result[i]= a[i]
    
#  now iterate in b dict
  for i in b:
    if i in result:
        # element of b inside result dict already have , increase that count
      result[i] += b[i]
    #   element not in result dict , create new key and value initilize with b dict value
    else:
      result[i] = b[i]
      
  return result
  
print(dictMerge(a, b))
