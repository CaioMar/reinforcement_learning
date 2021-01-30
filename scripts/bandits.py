"""
Script designed to test different Multi-ArmedBandit Algorithms.
"""

from abc import ABC, abstractclassmethod
import random

class AbstractBandit(ABC):
    """
    Interface for all bandits.
    """
    @abstractclassmethod
    def update(self, x) -> float:
        pass

    @abstractclassmethod
    def pull(self) -> bool:
        pass

class Bandit(AbstractBandit):
    """
    Implements a simple Bandit.
    """
    def __init__(self, p: float) -> None:
        self.p_real = p
        self.n_trials = 0 #number of trials
        self.x_mean = 0 #mean the random variable (bernoulli dist), estimate of probability

    def pull(self) -> bool:
        return random.random() < self.p_real

    def update(self, x: bool) -> float:
        self.n_trials += 1
        self.x_mean = self.x_mean + (x - self.x_mean)/self.n_trials
        return self.x_mean
