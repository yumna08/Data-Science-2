Project Overview
This project implements a pure Python statistical engine built from scratch without using external libraries such as NumPy or pandas. The engine processes raw numerical datasets and computes key statistical measures including central tendency, dispersion, and outlier detection.
In addition, the project includes a Monte Carlo simulation to model a real-world scenario of server failures and demonstrates the Law of Large Numbers (LLN).
The goal of this project is to combine mathematical understanding, software engineering, and probability simulation to analyze and interpret data effectively.
⚙️ Features
🔹 Central Tendency
Mean – Average value of the dataset
Median – Middle value (handles both even and odd datasets)
Mode – Supports multimodal datasets (returns all modes or a message if none exist)
🔹 Dispersion
Variance
Population variance (divide by N)
Sample variance (divide by N - 1, using Bessel’s correction)
Standard Deviation
Square root of variance
🔹 Outlier Detection
Identifies data points that are more than a specified threshold (default = 2) standard deviations away from the mean
🔹 Error Handling
Handles empty datasets safely (avoids division errors)
Detects and handles mixed or invalid data types
Provides descriptive error messages
🧮 Mathematical Logic
Mean
Mean is calculated as:

mean = sum(data) / len(data)
Median
Sort the dataset
If odd → return middle value
If even → return average of two middle values
Variance
Population Variance:

variance = sum((x - mean)^2) / N
Sample Variance:

variance = sum((x - mean)^2) / (N - 1)
Standard Deviation

std_dev = sqrt(variance)
Why Bessel’s Correction?
When working with a sample instead of the full population, dividing by N - 1 reduces bias and provides a more accurate estimate.
🚨 Outlier Detection Logic
A value is considered an outlier if:

|x - mean| > threshold × standard_deviation
🎲 Monte Carlo Simulation
Scenario
A startup server has a 4.5% probability (0.045) of crashing on any given day.
Simulation
The function simulate_crashes(days):
Simulates server behavior over a given number of days
Counts total crashes
Computes simulated probability:

simulated_probability = crashes / days
Purpose
To demonstrate how probability behaves under repeated trials and validate the Law of Large Numbers.
📈 Law of Large Numbers (LLN)
The Law of Large Numbers states that:
As the number of trials increases, the experimental probability approaches the theoretical probability.
Observation:
Small sample (e.g., 30 days) → highly variable results
Large sample (e.g., 10,000 days) → stable and accurate results
⚠️ Real-World Insight
Using small datasets (like 30 days) to predict long-term outcomes is dangerous because:
Results are heavily influenced by randomness
Can lead to incorrect business decisions
Larger datasets provide more reliable insights
🗂️ Project Structure

statistical_engine/
│
├── data/
│   └── sample_salaries.json
│
├── src/
│   ├── init.py
│   ├── stat_engine.py
│   └── monte_carlo.py
│
├── tests/
│   ├── init.py
│   └── test_stat_engine.py
│
├── README.md
└── main.py
🚀 Setup Instructions
1. Clone the repository
Bash
git clone https://github.com/your-username/statistical_engine.git
cd statistical_engine
2. Run the program
Bash
python main.py
🧪 Testing
Run the unit tests using:
Bash
python -m unittest discover tests
Tests include:
Mean and median correctness (odd and even datasets)
Standard deviation validation
Handling empty datasets
Error handling for invalid inputs
