import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot([1, 2, 3], [1, 2, 3])

ax_twin = ax.twinx()
ax_twin.plot([1, 1], [2, 2])

ax.set_ylim([1, 3])

ax.invert_yaxis()
plt.show()
