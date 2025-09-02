import numpy as np
import matplotlib.pyplot as plt
from option_pricing_models import black_scholes


# Parameters
S = 100 #
r = 0.05 #
sigma = 0.2 #
option_type = "call"

K_values = np.linspace(50, 150, 50) # Tickers 
T_values = np.linspace(0.01, 2, 50) # Years
K_grid, T_grid = np.meshgrid(K_values, T_values)


if __name__ == "__main__":
    prices = np.array([
    [black_scholes(S, K, T, r, sigma, option_type) for K in K_values]
    for T in T_values
    ])

    plt.figure(figsize = (8, 6))
    contour = plt.contourf(K_grid, T_grid, prices, 20, cmap = "viridis")
    plt.colorbar(contour, label = "Call Option Price")
    plt.xlabel("Strike Price (K)")
    plt.ylabel("Time in Maturity (Years)")
    plt.title("Black-Scholes Call Option Price Heatmap")
    plt.show()