# === Random float ===

# import numpy
import numpy as np
# set the seed
np.random.seed(123)
# generate and print random float
print(np.random.rand())

# === Roll the dice ===

# use randint() to simulate a dice
print(np.random.randint(1, 7))
# use randint() again
print(np.random.randint(1, 7))

# === Determine your next move ===

# set the seed
np.random.seed(123)
# starting step
step = 50
# roll the dice
dice = np.random.randint(1, 7)
# finish the control construct
if dice <= 2 :
    step = step - 1
elif dice > 2 and dice < 6 :
    step = step + 1
else :
    step = step + np.random.randint(1, 7)
# print out the dice and step
print(dice)
print(step)

# == The next step ===

# set the seed
np.random.seed(123)
# initialize random walk
random_walk = [0]
# for loop which runs 100 times
for x in range(100) :
    # set step: last element in random_walk
    step = random_walk[-1]
    # roll the dice
    dice = np.random.randint(1, 7)
    # determine the next step
    if dice <= 2 :
        step = step - 1
    elif dice <= 5 :
        step = step + 1
    else :
        step = step + np.random.randint(1, 7)
    # append next_step to random_walk
    random_walk.append(step)
# print random_walk
print(random_walk)

# === How long can you go? ===

# set the seed
np.random.seed(123)
# initialize random_walk
random_walk = [0]
# for loop which runs 100 times
for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1, 7)
    if dice <= 2 :
        # use max to make sure that the step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5 :
        step = step + 1
    else :
        step = step + np.random.randint(1, 7)
    # append next step to random_walk
    random_walk.append(step)
# print random_walk
print(random_walk)

# === Visualize the walk ===

# import matplotlib.pyplot
import matplotlib.pyplot as plt
# plot random_walk
plt.plot(random_walk)
# show the plot
plt.show()
plt.clf

# === Simulate multiple walks ===

# set the seed
np.random.seed(123)
# initialize all_walks
all_walks = []
# simulate random walk 10 times
for i in range(10) :
    # code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2 :
            step = max(0, step - 1)
        elif dice <= 5 :
            step = step + 1
        else :
            step = step + np.random.randint(1, 7)
        random_walk.append(step)
    # append random_walk to all_walks
    all_walks.append(random_walk)
# print all_walks
print(all_walks)

# === Visualize all walks ===

# set the seed
np.random.seed(123)
# intialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2 :
            step = max(0, step - 1)
        elif dice <= 5 :
            step = step + 1
        else :
            step = step + np.random.randint(1, 7)
        random_walk.append(step)
    all_walks.append(random_walk)
# convert all_walks to numpy array
np_aw = np.array(all_walks)
# plot np_aw and show
plt.plot(np_aw)
plt.show()
# clear the figure
plt.clf()
# transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)
# plot and show
plt.plot(np_aw_t)
plt.show()
plt.clf()

# === Implement clumsiness ===

# set the seed
np.random.seed(123)
# simulate random walk 250 times
all_walks = []
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2 :
            step = max(0, step - 1)
        elif dice <= 5 :
            step = step + 1
        else :
            step = step + np.random.randint(1, 7)
        # implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)
# create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()
plt.clf()

# === Plot the distribution ===

# simlulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2 :
            step = max(0, step - 1)
        elif dice <= 5 :
            step = step + 1
        else :
            step = step + np.random.randint(1, 7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)
# create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
# select last row from np_aw_t : ends
ends = np_aw_t[-1, :]
# plot histogram of ends, display plot
plt.hist(ends)
plt.show()

# === Calculate the odds ===

# make an array which check the comparison for each end step
ends_60 = ends >= 60
# calculate the number of end step that greater than or equal to 60
n_ends_60 = (len(ends[ends_60 == True]))
# divide the result of calculation with the number of random walks
print(n_ends_60 / 500)
