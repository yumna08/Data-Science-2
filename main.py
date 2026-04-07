from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes

# Sample dataset
data = [10, 20, 20, 30, 40, 100]

engine = StatEngine(data)

print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())
print("Variance:", engine.get_variance())
print("Std Dev:", engine.get_standard_deviation())
print("Outliers:", engine.get_outliers())

print("\nMonte Carlo Simulation:")
for days in [100, 1000, 10000]:
    prob = simulate_crashes(days)
    print(f"{days} days → {prob}")