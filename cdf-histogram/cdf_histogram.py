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

df.hist(column="Grades")