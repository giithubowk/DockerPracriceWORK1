import matplotlib.pyplot as plt
import random
import os
import sys

os.makedirs("output", exist_ok=True)

count = int(sys.argv[1]) if len(sys.argv) > 1 else 10

x = list(range(count))
y = [random.randint(10, 100) for _ in x]

plt.plot(x, y, marker="o")
plt.title(f"Graph with {count} points")

plt.savefig("output/graph.png")
print("Saved to output/graph.png")

------------
FROM python:3.11-slim

WORKDIR /app
RUN pip install --no-cache-dir matplotlib

COPY generate.py .

ENTRYPOINT ["python", "generate.py"]