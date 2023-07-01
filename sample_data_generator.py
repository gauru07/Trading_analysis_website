import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Function to generate random datetime within a specific range
def random_datetime(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_seconds = np.random.randint(int_delta)
    return start + timedelta(seconds=random_seconds)

# Generate 1000 rows of random data
np.random.seed(42)
rows = []
for i in range(1000):
    dt = random_datetime(datetime(2023, 6, 1), datetime(2023, 6, 30))
    stock = np.random.choice(['ABC', 'XYZ', 'DEF'])
    ordertype = np.random.choice(['Buy', 'Sell'])
    price = round(np.random.uniform(50, 150), 2)
    exchange = 'NSE'
    rows.append([dt, stock, ordertype, price, exchange])
    print(i)

# Create a DataFrame and save to CSV
df = pd.DataFrame(rows, columns=['datetime', 'stock', 'ordertype', 'price', 'Exchange'])
df.to_csv('sample_data.csv', index=False)
