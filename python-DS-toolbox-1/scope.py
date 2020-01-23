# === Understanding scope ===

# define num
num = 5
# define function 1
def func1() :
    num = 3
    print(num)
# define function 2
def func2() :
    global num
    double_num = num * 2
    num = 6
    print(double_num)
# call function 1
func1()
# call function 2
func2()
# recall num
print(num)

# === Global scope ===

# create a string: team
team = 'sunda empire'
# define change_team()
def change_team() :
    """Change the value of the global variable team."""
    # use team in global scope
    global team
    # change the value of team in global team: team
    team = 'universal keraton'
# print team
print(team)
# call change_team()
change_team()
# print team
print(team)

# === Python's built-in scope ===

# import builtins module
import builtins
# recognize that there is no 'array' in builtins module
print(dir(builtins))
