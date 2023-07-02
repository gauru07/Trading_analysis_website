import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_cumulative_returns(df):
    df['returns'] = df['price'].pct_change()
    df['cumulative_returns'] = (1 + df['returns']).cumprod()
    return df

def calculate_max_drawdown(df):
    df['cumulative_returns'] = df['cumulative_returns'].ffill()
    df['daily_drawdown'] = df['cumulative_returns'] / df['cumulative_returns'].cummax() - 1
    df['max_drawdown'] = df['daily_drawdown'].cummin()
    return df

def calculate_win_loss_ratio(df):
    df['gain'] = df['returns'].apply(lambda x: x if x > 0 else 0)
    df['loss'] = df['returns'].apply(lambda x: -x if x < 0 else 0)
    df['win_loss_ratio'] = df['gain'].cumsum() / abs(df['loss'].cumsum())
    return df

def calculation(df):

    # Convert the 'datetime' column to datetime type for further calculations
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Calculate cumulative returns
    df = calculate_cumulative_returns(df)

    # Calculate max drawdown
    df = calculate_max_drawdown(df)

    # Calculate win/loss ratio
    df = calculate_win_loss_ratio(df)

    # Calculate overall Cumulative Returns
    overall_cumulative_returns = (1 + df['returns']).prod() - 1

    # Calculate overall Max Drawdown
    overall_max_drawdown = df['max_drawdown'].min()

    # Calculate overall Win/Loss Ratio
    overall_win_loss_ratio = df['gain'].sum() / abs(df['loss'].sum())

    print("Overall Cumulative Returns:")
    print(overall_cumulative_returns)

    print("\nOverall Max Drawdown:")
    print(overall_max_drawdown)

    print("\nOverall Win/Loss Ratio:")
    print(overall_win_loss_ratio)

    return df
