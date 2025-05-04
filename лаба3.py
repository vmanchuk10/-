# Задание 1 вариант 1
import pandas as pd
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
data = pd.read_csv(url, header=None, names=column_names)
classes = data["class"].unique()
colors = ["red", "green", "blue"]
plt.figure(figsize=(8, 6))
for i, cls in enumerate(classes):
    subset = data[data["class"] == cls]
    plt.scatter(
        subset["sepal_length"], subset["sepal_width"], label=cls, color=colors[i]
    )
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Iris Sepal Dimensions")
plt.legend()
plt.grid(True)
plt.show()

# Задание 2 вариант 1
import statsmodels.api as sm

data = sm.datasets.co2.load_pandas()
co2_data = data.data
plt.figure(figsize=(12, 6))
plt.plot(co2_data.index, co2_data["co2"])
plt.xlabel("Date")
plt.ylabel("CO2 concentration (ppm)")
plt.title("Atmospheric CO2 Concentration (1958-1980)")
plt.grid(True)
plt.show()
