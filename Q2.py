#  #2. count the occurrences of a particular element in the list and output highest occurring element

days = ['sun','mon','mon','tue','wed','thu','fri','sat','mon','thu',]

# 1st method use dictionary 
count_with_name = {}
# Count the occurrences of each element in the list
for i in days:
  if i in count_with_name:
    #   day in already in count_with_name , increase the count
    count_with_name[i]+=1
  else:
    #   day entites not in count_with_name , create new entite and initialize with 1
    count_with_name[i] = 1
# Find the element with the highest occurrence
max_item = None
highest_occu = -1
for item,value in count_with_name.items():
    if value> highest_occu:
        highest_occu = value
        max_item = item
print([max_item, highest_occu])


# 2nd method is use in bulid fucntion Counter
def highest_occurrence(days):
    # Create an empty dictionary to store occurrences
    occurrence_count = {}
    
    # Count the occurrences of each element in the list
    for day in days:
        if day in occurrence_count:
            occurrence_count[day] += 1
        else:
            occurrence_count[day] = 1
    
    # Find the element with the highest occurrence
    max_element = None
    max_count = 0
    
    for day, count in occurrence_count.items():
        if count > max_count:
            max_element = day
            max_count = count
    
    return max_element, max_count

# Example usage
element, occurrences = highest_occurrence(days)
print(element,occurrences)