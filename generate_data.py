"""
generate_data.py
Creates a synthetic network-traffic CSV for demo IDS.
Columns: duration, src_bytes, dst_bytes, wrong_fragment, urgent, hot, num_failed_logins, count, srv_count, serror_rate, srv_serror_rate, dst_host_srv_count, dst_host_diff_srv_rate, label
label: 0 = normal, 1 = attack
"""
import argparse
import numpy as np
import pandas as pd

def make_row(is_attack):
    if not is_attack:
        duration = np.random.exponential(1.0)
        src_bytes = np.random.normal(300, 100)
        dst_bytes = np.random.normal(200, 80)
        wrong_fragment = 0
        urgent = 0
        hot = np.random.poisson(1)
        num_failed_logins = np.random.binomial(1, 0.01)
        count = np.random.poisson(10)
        srv_count = np.random.poisson(8)
        serror_rate = np.random.beta(1,20)
        srv_serror_rate = np.random.beta(1,20)
        dst_host_srv_count = np.random.poisson(5)
        dst_host_diff_srv_rate = np.random.beta(2,10)
    else:
        duration = np.random.exponential(5.0)
        src_bytes = np.random.normal(2000, 800)
        dst_bytes = np.random.normal(1500, 700)
        wrong_fragment = np.random.binomial(1, 0.05)
        urgent = np.random.binomial(1, 0.02)
        hot = np.random.poisson(5)
        num_failed_logins = np.random.binomial(3, 0.2)
        count = np.random.poisson(100)
        srv_count = np.random.poisson(90)
        serror_rate = np.random.beta(5,5)
        srv_serror_rate = np.random.beta(4,6)
        dst_host_srv_count = np.random.poisson(80)
        dst_host_diff_srv_rate = np.random.beta(5,2)
    return [duration, src_bytes, dst_bytes, wrong_fragment, urgent, hot, num_failed_logins, count, srv_count, serror_rate, srv_serror_rate, dst_host_srv_count, dst_host_diff_srv_rate]

def generate(n=1000, attack_ratio=0.2, seed=42):
    np.random.seed(seed)
    rows = []
    labels = []
    for i in range(n):
        is_attack = np.random.rand() < attack_ratio
        rows.append(make_row(is_attack))
        labels.append(1 if is_attack else 0)
    cols = ['duration','src_bytes','dst_bytes','wrong_fragment','urgent','hot','num_failed_logins','count','srv_count','serror_rate','srv_serror_rate','dst_host_srv_count','dst_host_diff_srv_rate']
    df = pd.DataFrame(rows, columns=cols)
    df['label'] = labels
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='demo_data.csv')
    parser.add_argument('--n', type=int, default=2000)
    parser.add_argument('--attack_ratio', type=float, default=0.2)
    args = parser.parse_args()
    df = generate(n=args.n, attack_ratio=args.attack_ratio)
    df.to_csv(args.output, index=False)
    print(f"Wrote {args.output} with {len(df)} rows")
