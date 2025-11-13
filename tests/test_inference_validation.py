from app.model_utils import simulate_model_inference, calculate_accuracy

def test_inference_accuracy():
    data = range(10)
    labels = [1 if x % 2 == 0 else 0 for x in data]
    predictions = simulate_model_inference(data)
    acc = calculate_accuracy(predictions, labels)
    assert acc >= 0.8, f"Inference accuracy too low: {acc}"
