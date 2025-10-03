# src/data/scale_data.py
import argparse
import pandas as pd
from sklearn.preprocessing import StandardScaler

def main(in_dir, out_dir):
    X_tr = pd.read_csv(f"{in_dir}/X_train.csv")
    X_te = pd.read_csv(f"{in_dir}/X_test.csv")

    # Garder seulement les colonnes numériques
    num_cols = X_tr.select_dtypes(include="number").columns

    scaler = StandardScaler()
    X_tr_s = pd.DataFrame(scaler.fit_transform(X_tr[num_cols]), columns=num_cols)
    X_te_s = pd.DataFrame(scaler.transform(X_te[num_cols]),  columns=num_cols)

    X_tr_s.to_csv(f"{out_dir}/X_train_scaled.csv", index=False)
    X_te_s.to_csv(f"{out_dir}/X_test_scaled.csv", index=False)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--in_dir",  default="data/processed_data")
    p.add_argument("--out_dir", default="data/processed_data")
    args = p.parse_args()
    main(**vars(args))
