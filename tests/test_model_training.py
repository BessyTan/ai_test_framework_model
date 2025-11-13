from app.pipeline import run_pipeline_step, validate_results

def test_model_training_pipeline():
    steps = ["load_data", "preprocess", "train", "evaluate"]
    results = {step: run_pipeline_step(step) for step in steps}
    assert validate_results(results), "Model training pipeline failed"
    # Ensure accuracy is >= 0.8
    assert results["evaluate"] >= 0.8, f"Accuracy too low: {results['evaluate']}"