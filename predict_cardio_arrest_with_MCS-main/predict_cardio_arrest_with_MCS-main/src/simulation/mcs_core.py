 # Core Monte Carlo simulation logic
import numpy as np
from typing import Dict

class CardiacArrestSimulator:
    def __init__(self, parameters: Dict[str, np.ndarray]):
        self.parameters = parameters
        self.num_samples = len(next(iter(parameters.values())))
        
    def _calculate_critical_window(self, age: np.ndarray, health_status: np.ndarray) -> np.ndarray:
        """Calculate time window for potential intervention"""
        base_window = np.random.normal(15, 5, self.num_samples)
        return np.clip(base_window - (age/5) - (health_status*2), 2, 30)
    
    def _evaluate_accident_risk(self, reaction_time: np.ndarray, speed: np.ndarray) -> np.ndarray:
        """Safety envelope model for accident probability"""
        speed_factor = np.interp(speed, [30, 120], [0.2, 1.0])
        time_factor = 1 / (1 + np.exp(-(reaction_time - 5)))
        return speed_factor * time_factor
    
    def run(self) -> Dict[str, np.ndarray]:
        sca_events = np.random.rand(self.num_samples) < self.parameters['sca_probability']
        reaction_times = self._calculate_critical_window(
            self.parameters['age'],
            self.parameters['health_status']
        )
        
        accident_probs = self._evaluate_accident_risk(reaction_times, self.parameters['speed'])
        accidents = accident_probs > np.random.rand(self.num_samples)
        
        return {
            'sca_events': sca_events,
            'reaction_times': reaction_times,
            'accident_probs': accident_probs,
            'accidents_occurred': accidents
        }