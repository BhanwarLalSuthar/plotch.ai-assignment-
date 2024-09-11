 #5. Implement a group_by_owners function that:
#Accepts a dictionary containing the file owner name for each file name.
#Returns a dictionary containing a list of file names for each owner #name, in any order.

def group_by_owners(files):
    owners_dict = {}

    for file, owner in files.items():
        # If the owner is already in the dictionary, append the file
        if owner in owners_dict:
            owners_dict[owner].append(file)
        else:
            # If the owner is not in the dictionary, create a new entry
            owners_dict[owner] = [file]

    return owners_dict

files = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 
output = group_by_owners(files)
print(output)

#the group_by_owners function should return 
# output = {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.