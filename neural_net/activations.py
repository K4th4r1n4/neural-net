"""Activation functions."""

from math import exp


def sigmoid(x: float) -> float:
    """ToDo"""
    return 1.0 / (1.0 + exp(-x))
