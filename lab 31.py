import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("day31_seaborn.csv")

sns.histplot(df, x="age", hue="segment", bins=25, element="step", stat="density", common_norm=False)
plt.title("Age Distribution by Segment")

sns.kdeplot(data=df, x="income", hue="segment", fill=True, common_norm=False, alpha=0.4)
plt.title("Income Density by Segment")

sns.boxplot(data=df, x="segment", y="income")
plt.title("Income by Segment — Boxplot")

sns.boxplot(data=df, x="segment", y="income")
plt.title("Income by Segment — Boxplot")
