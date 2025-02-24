#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
controllers.py

This module contains various controllers that can be integrated into the DME framework
to adjust or guide the behavior of the dynamic morphology process.
"""

from typing import Any

class BaseController:
    """
    Base controller class. Other controllers should inherit from this.
    """

    def __init__(self, name: str = "BaseController"):
        self.name = name

    def control(self, current_state: Any, target_state: Any) -> Any:
        """
        Applies the control logic to move from the current state
        toward the target state.

        Args:
            current_state (Any): The current system or material state.
            target_state (Any): The desired state of the system.

        Returns:
            Any: The new control inputs or actions.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")


class PIDController(BaseController):
    """
    A simple PID controller example for demonstration.
    """

    def __init__(self, kp: float, ki: float, kd: float, name: str = "PIDController"):
        super().__init__(name)
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self._integral = 0.0
        self._previous_error = 0.0

    def control(self, current_state: float, target_state: float) -> float:
        """
        A simple 1D PID control strategy.

        Args:
            current_state (float): Current scalar state.
            target_state (float): Desired scalar state.

        Returns:
            float: Control output (e.g., an adjustment or action).
        """
        error = target_state - current_state
        self._integral += error
        derivative = error - self._previous_error
        self._previous_error = error

        output = (
            self.kp * error
            + self.ki * self._integral
            + self.kd * derivative
        )
        return output
