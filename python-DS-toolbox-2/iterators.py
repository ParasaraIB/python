# === Using enumerate ===

# create a list of strings: mutants
mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde']
# create a list of tuples:
mutant_list = list(enumerate(mutants))
# print the list of tuples
print(mutant_list)
# unpack and print the tuple pairs
for index1, value1 in enumerate(mutants) :
    print(index1, value1)
# change the start index
for index2, value2 in enumerate(mutants, 1) :
    print(index2, value2)

# === Using zip ===

# create lists
mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde']
aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']
# create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))
# print the list of tuples
print(mutant_data)
# create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)
# print the zip object
print(mutant_zip)
# unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip :
    print(value1, value2, value3)

# === Using * and zip to 'unzip' ===

# create tuples of strings
mutants = tuple(mutants)
powers = tuple(powers)
# create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)
# print the tuples in z1 by unpacking with *
print(*z1)
# re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)
# 'unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)
# check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)
