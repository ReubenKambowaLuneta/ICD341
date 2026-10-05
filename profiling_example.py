import numpy as np

@profile
def calculate_statistics(x):
    total = np.sum(x)
    mean = np.mean(x)
    variance = np.var(x)
    result = np.sqrt(variance)
    return total, mean, result

if __name__ == "__main__":
    x = np.random.normal(size=1_000_000)
    calculate_statistics(x)