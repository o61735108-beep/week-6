import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("day32_relationships.csv")
sns.scatterplot(data=data, x="feature1", y="outcome", hue="segment", alpha=0.5)
plt.title("Outcome vs feature1 — Basic scatterplot")
plt.show()



sns.relplot(data=data, x="feature1", y="outcome", hue="outcome")
plt.show()
