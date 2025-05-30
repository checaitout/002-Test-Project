import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [5, 4, 3, 2, 1]})

df2 = pd.DataFrame({"C": [6, 7, 8, 9, 10], "D": [10, 9, 8, 7, 6]})

df3 = pd.DataFrame({"E": [11, 12, 13, 14, 15], "F": [15, 14, 13, 12, 11]})

print("DataFrames created successfully.")

plt.plot(df["A"], df["B"], label="A vs B")
plt.plot(df2["C"], df2["D"], label="C vs D")
plt.plot(df3["E"], df3["F"], label="E vs F")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Multiple DataFrames Plot")
plt.legend()
plt.show()
