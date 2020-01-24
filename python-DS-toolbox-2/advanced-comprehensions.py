# === Using conditionals in comprehensions (1)===

# create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# create list comprehensions: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]
# print the new list
print(new_fellowship)

# === Using conditionals in comprehensions (2)===

# create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# create a list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]
# print the new list
print(new_fellowship)

# === Dict comprehension ===

# create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# create a dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}
# print the new dictionary
print(new_fellowship)
