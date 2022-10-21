import pathlib
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import seaborn as sns

new_path = pathlib.Path.home() / "Downloads"
os.chdir(new_path)

titanic = pd.read_csv("titanicV2020.csv")
#titanic.head(10)