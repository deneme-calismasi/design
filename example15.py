import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
data = [[1, 2, 3],
        [5, 6, 7],
        [8, 9, 10]]
column_labels = ["Column 1", "Column 2", "Column 3"]
df = pd.DataFrame(data, columns=column_labels)
ax.axis('tight')
ax.axis('off')
ax.table(cellText=df.values,
         colLabels=df.columns,
         rowLabels=["A", "B", "C"],
         rowColours=["yellow"] * 3,
         colColours=["yellow"] * 3,
         loc="center")
plt.show()
