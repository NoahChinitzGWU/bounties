# CDF-Histogram Bounty
# Forked from https://github.com/twood02/bounties
# Authors: Connor Burnett, Noah Chinitz, Aaron Hill

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')

graph_type = input("For histogram, type h. For CDF, type c.\n")

if graph_type == "h":
    min = input("Please enter a minimum value:\n")
    max = input("Please enter a maximum value:\n")
    bin_size = input("Please enter a bin size:\n")
# elif graph_type == "c":
else:
    print("That was not an option")

column_names = ["Grades"]
df = pd.read_csv('~/Bounties/bounties/cdf-histogram/grades.txt', delimiter = "\n", names = column_names)
print(df)

# np.random.seed(seed=42)
# data_points = 1000

# df = pd.DataFrame(data=list(zip(np.random.choice(["Math", "English"], size=data_points),
#                                 np.random.beta(15, 10, size=data_points),
#                                 np.random.beta(30, 4, size=data_points))),
#             columns=['Major', 'Test1', 'Test2'])

# df.head()

# pd.DataFrame.hist(column="test")
# pd.DataFrame.plot(kind='hist')
# pd.DataFrame.plot.hist()

df.hist(column="Grades")