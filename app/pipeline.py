import random
import time

from app.utils.data_loader import load_data
from app.utils.metrics import evaluate_accuracy
from app.model_utils import simulate_model_training, simulate_model_inference
# app/pipeline.py

def run_pipeline_step(step_name):
    if step_name == "load_data":
        return load_data("data/sample.csv")
    elif step_name == "preprocess":
        df = load_data()
        # Example preprocessing: normalize x
        df["x_norm"] = df["x"] / df["x"].max()
        return df
    elif step_name == "train":
        return simulate_model_training()
    elif step_name == "evaluate":
        df = load_data()
        predictions = simulate_model_inference(df["x"])
        labels = df["y"]
        return evaluate_accuracy(predictions, labels)
    else:
        raise ValueError(f"Unknown step {step_name}")


def validate_results(results):
    return all(result is not None for result in results.values())
