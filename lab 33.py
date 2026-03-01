import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("day33_corr.csv")



plt.figure(figsize=(6, 5))
sns.heatmap(data, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()


corr_matrix = (data.corr())
print(corr_matrix)
