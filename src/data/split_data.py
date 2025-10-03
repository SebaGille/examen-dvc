# src/data/split_data.py
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

def main(raw_path, out_dir, test_size, random_state):
    df = pd.read_csv(raw_path)                     # charge le CSV
    y = df.iloc[:, -1]                             # cible = dernière colonne (silica_concentrate)
    X = df.iloc[:, :-1]                            # features = toutes sauf dernière
    X_tr, X_te, y_tr, y_te = train_test_split(     # split simple
        X, y, test_size=test_size, random_state=random_state
    )
    X_tr.to_csv(f"{out_dir}/X_train.csv", index=False)
    X_te.to_csv(f"{out_dir}/X_test.csv", index=False)
    y_tr.to_csv(f"{out_dir}/y_train.csv", index=False)
    y_te.to_csv(f"{out_dir}/y_test.csv", index=False)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--raw_path", default="data/raw_data/raw.csv")
    p.add_argument("--out_dir",  default="data/processed_data")
    p.add_argument("--test_size", type=float, default=0.2)
    p.add_argument("--random_state", type=int, default=42)
    args = p.parse_args()
    main(**vars(args))