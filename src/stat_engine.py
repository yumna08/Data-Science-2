import math

class StatEngine:
    def __init__(self, data):
        self.data = self._clean_data(data)
        if len(self.data) == 0:
            raise ValueError("Dataset is empty after cleaning.")

    def _clean_data(self, data):
        if not isinstance(data, (list, tuple)):
            raise TypeError("Input must be a list or tuple.")

        cleaned = []
        for x in data:
            if isinstance(x, (int, float)):
                cleaned.append(float(x))
            else:
                raise TypeError(f"Invalid data type: {type(x)}")

        return cleaned

    # ✅ Mean
    def get_mean(self):
        return sum(self.data) / len(self.data)

    # ✅ Median
    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    # ✅ Mode (multimodal support)
    def get_mode(self):
        freq = {}
        for x in self.data:
            freq[x] = freq.get(x, 0) + 1

        max_freq = max(freq.values())

        if max_freq == 1:
            return "No mode (all values are unique)"

        modes = [k for k, v in freq.items() if v == max_freq]
        return modes

    # ✅ Variance
    def get_variance(self, is_sample=True):
        n = len(self.data)
        mean = self.get_mean()

        if is_sample and n < 2:
            raise ValueError("Sample variance requires at least 2 data points.")

        squared_diff = [(x - mean) ** 2 for x in self.data]

        if is_sample:
            return sum(squared_diff) / (n - 1)  # Bessel correction
        else:
            return sum(squared_diff) / n

    # ✅ Standard Deviation
    def get_standard_deviation(self, is_sample=True):
        return math.sqrt(self.get_variance(is_sample))

    # ✅ Outliers
    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_standard_deviation()

        if std == 0:
            return []

        outliers = []
        for x in self.data:
            z = abs((x - mean) / std)
            if z > threshold:
                outliers.append(x)

        return outliers