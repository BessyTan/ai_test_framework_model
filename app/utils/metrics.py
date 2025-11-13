from sklearn.metrics import accuracy_score

def evaluate_accuracy(y_pred, y_true):
    return accuracy_score(y_true, y_pred)
