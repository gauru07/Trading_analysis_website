from django.shortcuts import render,redirect
from django.http import HttpResponse
from io import TextIOWrapper
import csv
import pandas as pd
from .final_analysis import *
from sample_data_generator import *


def csv_upload(request):
    if request.method == 'POST':


        csv_file = request.FILES.get('csv_file')

        if csv_file is None:
            return HttpResponse("No file uploaded.")

        with TextIOWrapper(csv_file, encoding=request.encoding) as text_file:
            reader = csv.reader(text_file)
            csv_contents = [row for row in reader]


        df = pd.DataFrame(csv_contents[1:], columns=csv_contents[0])
        df['datetime'] = pd.to_datetime(df['datetime'])


        df['price'] = df['price'].astype(float)
        df['quantity'] = df['quantity'].astype(int)
        


        df = calculation(df)

        df.dropna(inplace=True)
        print(df)
        context = {
            'datetime': df['datetime'].dt.strftime('%m-%d ').tolist(),
            'max_drawdown': df['max_drawdown'].tolist(),
            'win_loss': df['win_loss_ratio'].tolist(),
            'quantity': df['quantity'].tolist(),
            'cumulative_returns':df['cumulative_returns'].tolist(),

        }

        return render(request, 'analysis_final.html', context)

    return render(request, "file_upload.html")

def analysis_data(request):
    generate()

    df=pd.read_csv('./sample_data.csv')
    df['datetime'] = pd.to_datetime(df['datetime'])


    df['price'] = df['price'].astype(float)
    df['quantity'] = df['quantity'].astype(int)
    


    df = calculation(df)

    df.dropna(inplace=True)
    print(df)
    context = {
        'datetime': df['datetime'].dt.strftime('%m-%d ').tolist(),
        'max_drawdown': df['max_drawdown'].tolist(),
        'win_loss': df['win_loss_ratio'].tolist(),
        'sortino_ratio': df['sortino_ratio'].tolist(),
        'sharpe_ratio': df['sharpe_ratio'].tolist(),
        'cumulative_returns':df['cumulative_returns'].tolist(),
        'standard_deviation':df['standard_deviation'].tolist(),
        'excess_returns':df['excess_returns'].tolist(),
        'information_ratio':df['information_ratio'].tolist(),
        'calmar_ratio':df['calmar_ratio'].tolist(),
    }

    return render(request, 'analysis_final.html', context)

