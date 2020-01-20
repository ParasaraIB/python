# === if ===

# define variables
room = 'kit'
area = 14.0
# if statement for room
if room == 'kit' :
    print('Looking around in the kithcen.')
# if statement for area
if area > 15 :
    print('big place!')

# === add else ===

# if-else construct for room
if room == 'kit' :
    print('looking around in the kitchen.')
else :
    print('looking around elsewhere.')
# if else construct for area
if area > 15 :
    print('big place!')
else :
    print('pretty small.')

# === customize further: elif ===

# define variables
room = 'bed'
area = 14.0

# if-elif-else construct for room
if room == 'kit' :
    print('looking around in the kitchen.')
elif room == 'bed' :
    print('looking around in the bedroom.')
else :
    print('looking around elsewhere.')
# if-elif-else construct for area
if area > 15 :
    print('big place!')
elif area > 10 :
    print('medium size, nice!')
else :
    print('pretty small.')
