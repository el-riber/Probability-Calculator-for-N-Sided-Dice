import random
from collections import Counter
import matplotlib.pyplot as plt


def roll_dice_once(n_sides: int, m_dice: int) -> int:
    return sum(random.randint(1, n_sides) for _ in range(m_dice))


def simulate_rolls(n_sides: int, m_dice: int, k_trials: int) -> list:
    return [roll_dice_once(n_sides, m_dice) for _ in range(k_trials)]


def calculate_distribution(results: list, k_trials: int) -> dict:
    counts = Counter(results)
    return {total: count / k_trials for total, count in sorted(counts.items())}


def display_distribution(distribution: dict):
    print("\nProbability Distribution:")
    for total, prob in distribution.items():
        print(f"Sum = {total}: Probability = {prob:.4f}")

    # Optional: plot histogram
    plt.bar(distribution.keys(), distribution.values())
    plt.xlabel("Sum")
    plt.ylabel("Probability")
    plt.title("Probability Distribution of Dice Rolls")
    plt.show()


def main():
    print("🎲 N-sided Dice Probability Calculator 🎲")
    try:
        n = int(input("Enter number of sides on each die (N): "))
        m = int(input("Enter number of dice rolled (M): "))
        k = int(input("Enter number of simulations to run (K): "))

        if n < 2 or m < 1 or k < 1:
            raise ValueError("Invalid input: N must be ≥ 2, M and K must be ≥ 1.")

        results = simulate_rolls(n, m, k)
        distribution = calculate_distribution(results, k)
        display_distribution(distribution)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
