import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from .base import OptionsPricingModel

class MonteCarloModel(OptionsPricingModel):
    
    def __init__(self, underlying_spot_price, strike_price, days_to_maturity, risk_free_rate, sigma, number_of_simulations):
        
        self.S_0 = underlying_spot_price
        self.K = strike_price
        self.T = days_to_maturity / 365
        self.r = risk_free_rate
        self.sigma = sigma
        self.N = number_of_simulations
        self.num_of_steps = days_to_maturity
        self.dt = self.T / self.num_of_steps 
    
    def simulate_prices(self):
        np.random.seed(20)
        self.simulation_results = None
        
        S = np.zeros((self.num_of_steps, self.N))
        S[0] = self.S_0
        
        for t in range(1, self.num_of_steps):
            Z = np.random.standard_normal(self.N)
            S[t] = S[t - 1] * np.exp((self.r - 0.5 * self.sigma ** 2) * self.dt + (self.sigma * np.sqrt(self.dt) * Z))
            
        self.simulation_results_S = S
        
        
    def calculate_option_call_price(self):
        
        if self.simulation_results_S is None:
            return -1

        return np.exp(-self.r * self.T) * 1 / self.N * np.sum(np.maximum(self.simulation_results_S[-1] - self.K, 0))
    
    def calculate_option_put_price(self):
        
        if self.simulation_results_S is None:
            return -1

        return np.exp(-self.r * self.T) * 1 / self.N * np.sum(self.K - np.maximum(self.simulation_results_S[-1], 0))\
            
    def plot_simulation_results(self, num_of_movements):
        
        plt.figure(figsize=(12,8))
        plt.plot(self.simulation_results_S[:,0:num_of_movements])
        plt.axhline(self.K, c='k', xmin=0, xmax=self.num_of_steps, label='Strike Price')
        plt.xlim([0, self.num_of_steps])
        plt.ylabel('Simulated price movements')
        plt.xlabel('Days in future')
        plt.title(f'First {num_of_movements}/{self.N} Random Price Movements')
        plt.legend(loc='best')
        plt.show()
        