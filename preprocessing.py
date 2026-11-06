import pandas as pd                     # Read and work with tabular data
import numpy as np                      # Numerical operations
import matplotlib.pyplot as plt         # Graphs and visualizations

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("phishing_features.csv")

