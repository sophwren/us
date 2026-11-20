"""Memory of love.py over a year: before and after the fix."""

import plotext as plt

LIMIT = 64  # MiB, then MemoryError and a restart

days = list(range(1, 366))
before = [4 + d % (LIMIT - 4) for d in days]
after = [4] * len(days)

plt.theme("clear")
plt.plotsize(64, 16)
plt.title("love.py · memory, MiB")
plt.plot(days, before, label="before", color="red")
plt.plot(days, after, label="after", color="green")
plt.xlabel("day")
plt.ylim(0, LIMIT + 8)
plt.show()
