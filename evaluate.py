"""
evaluate.py
Loads model.joblib and prints classification report on test set.
"""
import joblib
from sklearn.metrics import classification_report, accuracy_score

def main(model_file):
    data = joblib.load(model_file)
    clf = data['model']
    X_test = data['X_test']
    y_test = data['y_test']
    preds = clf.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, preds))
    print("Classification report:\\n", classification_report(y_test, preds))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', default='model.joblib')
    args = parser.parse_args()
    main(args.model)
