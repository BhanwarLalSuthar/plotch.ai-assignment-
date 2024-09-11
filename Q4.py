#   #4. Return the Item with highest value count
items = [{'Delhi': 3}, {'Mumbai': 9}, {'Goa': 7}, {'Gujrat': 4}] 
def highest_count(items):
    max_item = None
    max_value = float('-inf')

    # Iterate through each dictionary in the list
    for item in items:
        for key, value in item.items():
            if value > max_value:
                max_value = value
                max_item = item
    
    return max_item

print(highest_count(items))
# #Output: Mumbai
