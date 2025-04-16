import matplotlib.pyplot as plt
import random


def plot_walks(steps):
    vertices = [(0, 0), (2, 2), (4, 0)]
    x, y = random.choice(vertices)

    positions = [(x, y)]

    for _ in range(steps):
        vx, vy = random.choice(vertices)
        x = (x + vx) / 2
        y = (y + vy) / 2
        positions.append((x, y))

    xs, ys = zip(*positions)

    plt.figure(figsize=(6, 6))
    plt.title("Katniss's Walk")
    plt.xlim(0, 4)
    plt.ylim(0, 4)
    plt.grid(True)
    plt.scatter(xs, ys, color='purple', s=20)
    plt.plot(xs, ys, color='gray', linestyle='--', alpha=0.5)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


if __name__ == '__main__':
    plot_walks(100)
