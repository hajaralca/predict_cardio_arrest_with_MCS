import argparse
from pathlib import Path
from .sampling.parameter_sampler import ParameterSampler
from .simulation.mcs_core import CardiacArrestSimulator
from .analysis import RiskAggregator, ResultVisualizer
from .utils.file_io import save_results

def main():
    parser = argparse.ArgumentParser(
        description="Monte Carlo Simulation for Cardiac Arrest Impact on Traffic Safety",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-n', '--num_samples', type=int, default=10000,
                       help='Number of Monte Carlo iterations')
    parser.add_argument('-o', '--output_dir', type=Path, default=Path('data/simulation_results'),
                       help='Output directory for results')
    parser.add_argument('-c', '--config', type=Path, default=Path('config/parameters.yml'),
                       help='Path to parameter configuration file')
    parser.add_argument('-m', '--mode', choices=['nominal', 'importance'], default='nominal',
                       help='Sampling strategy mode')
    
    args = parser.parse_args()
    
    # Initialize components
    sampler = ParameterSampler(args.config, args.mode)
    simulator = CardiacArrestSimulator(sampler.generate_samples(args.num_samples))
    
    # Execute simulation
    results = simulator.run()
    
    # Post-processing
    aggregator = RiskAggregator()
    aggregated_risk = aggregator.analyze(results)
    
    visualizer = ResultVisualizer()
    visualizer.generate_plots(results, args.output_dir / 'visualizations')
    
    # Save results
    save_results(
        results=results,
        aggregated_risk=aggregated_risk,
        output_path=args.output_dir / 'simulation_output.pkl'
    )

if __name__ == '__main__':
    main()