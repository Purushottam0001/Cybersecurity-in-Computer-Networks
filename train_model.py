"""
train_model.py
Trains a RandomForest classifier on the generated CSV and saves using joblib.
"""
import argparse
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def main(input_csv, out_model):
    df = pd.read_csv(input_csv)
    X = df.drop(columns=['label'])
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    joblib.dump({'model': clf, 'X_test': X_test, 'y_test': y_test}, out_model)
    print(f"Model trained and saved to {out_model}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='demo_data.csv')
    parser.add_argument('--model', default='model.joblib')
    args = parser.parse_args()
    main(args.input, args.model)
