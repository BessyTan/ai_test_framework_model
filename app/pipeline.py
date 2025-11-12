import random
import time

# app/pipeline.py

def run_pipeline_step(step: str):
    """Simulate a pipeline step and return a numeric result."""
    print(f"Running step: {step}")
    if step == "load_data":
        return 0.55        # Simulated data load quality
    elif step == "preprocess":
        return 0.60        # Simulated preprocessing success
    elif step == "train":
        return 0.75        # Simulated training accuracy
    elif step == "evaluate":
        return 0.71        # Simulated evaluation score
    else:
        raise ValueError(f"Unknown pipeline step: {step}")


def validate_results(results: dict) -> bool:
    """Validate that each pipeline step meets a minimum threshold."""
    thresholds = {
        "load_data": 0.5,
        "preprocess": 0.5,
        "train": 0.7,
        "evaluate": 0.7
    }
    for step, value in results.items():
        if step not in thresholds:
            print(f"Warning: No threshold defined for step {step}")
            continue
        if value < thresholds[step]:
            print(f"Validation failed for {step}: {value} < {thresholds[step]}")
            return False
    return True
