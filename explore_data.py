# Explore the data
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("movie_metadata.csv")
df.head()