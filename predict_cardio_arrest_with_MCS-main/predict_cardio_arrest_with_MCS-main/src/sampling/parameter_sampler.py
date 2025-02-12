import yaml
import numpy as np
from typing import Dict, Any
from .distributions import NormalDistribution, LogNormalDistribution, CategoricalDistribution

class ParameterSampler:
    def __init__(self, config_path: str, mode: str = 'nominal'):
        self.config = self._load_config(config_path)
        self.mode = mode
        self.distributions = self._initialize_distributions()
        
    def _load_config(self, path: str) -> Dict[str, Any]:
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    
    def _initialize_distributions(self):
        dist_constructors = {
            'normal': lambda p: NormalDistribution(p['mean'], p['std']),
            'lognormal': lambda p: LogNormalDistribution(p['mu'], p['sigma']),
            'categorical': lambda p: CategoricalDistribution(p['categories'], p['probabilities'])
        }
        
        return {
            param: dist_constructors[spec['type']](spec['parameters'])
            for param, spec in self.config.items()
        }
    
    def generate_samples(self, num_samples: int) -> Dict[str, np.ndarray]:
        samples = {}
        for param, dist in self.distributions.items():
            samples[param] = dist.sample(num_samples)
            
            if self.mode == 'importance' and 'sca_risk' in param:
                # Apply importance sampling boost
                samples[param] *= self.config['importance_factors'].get(param, 1.5)
                
        return samples