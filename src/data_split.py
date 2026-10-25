import pandas as pd
import numpy as np
import os

RAW_DATA_PATH = "data/raw/test.csv"
INCOMING_DIR = "data/incoming"
NUM_BATCHES = 4

def split_and_save_batches():
    try:
        df = pd.read_csv(RAW_DATA_PATH)
    except FileNotFoundError:
        print(f"Ошибка чтения файла {RAW_DATA_PATH}")
        return

    df['cookie_created_at'] = pd.to_datetime(df['cookie_created_at'])
    df_sorted = df.sort_values(by='cookie_created_at').reset_index(drop=True)
    batches = np.array_split(df_sorted, NUM_BATCHES)

    for i, batch in enumerate(batches, 1):
        filename = f"batch_{i:02d}.csv"
        filepath = os.path.join(INCOMING_DIR, filename)
        batch_df = pd.DataFrame(batch, columns=df_sorted.columns)
        batch_df.to_csv(filepath, index=False)

if __name__ == '__main__':
    split_and_save_batches()