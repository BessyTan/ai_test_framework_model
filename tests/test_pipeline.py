import pytest
from app.pipeline import run_pipeline_step, validate_results

def test_pipeline_steps():
    steps = ["load_data", "preprocess", "train", "evaluate"]
    results = {step: run_pipeline_step(step) for step in steps}
    assert validate_results(results), "Pipeline failed validation"
