from django.shortcuts import render,redirect
from django.http import HttpResponse
from io import TextIOWrapper
import csv
import pandas as pd
# Create your views here.
from .final_analysis import *

# def csv_upload(request):
#     if request.method == 'POST':

#         # Get the uploaded file from the form
#         csv_file = request.FILES.get('csv_file')
#         # Check if a file was uploaded
#         if csv_file is None:
#             return HttpResponse("No file uploaded.")

#         # Read the contents of the uploaded CSV file
#         with TextIOWrapper(csv_file, encoding=request.encoding) as text_file:
#             reader = csv.reader(text_file)
#             csv_contents = [row for row in reader]

#         # Print the contents of the CSV file (for demonstration purposes)
#         df = pd.DataFrame(csv_contents[1:], columns=csv_contents[0])
#         df['datetime'] = pd.to_datetime(df['datetime'])


#         # Convert numerical columns to appropriate data types
#         df['price'] = df['price'].astype(float)
#         df['quantity'] = df['quantity'].astype(int)
#         df=calculation(df)
#         print(df)


#         context = {
#         'datetime': df['datetime'].tolist(),
#         'max_drawdown':df['max_drawdown'].tolist(),
#         'win_loss':df['win_loss_ratio'].tolist(),
#         'quantity':df['quantity'].tolist()
#         }

#         return render(request, 'analysis_final.html',context)

#     return render(request,"file_upload.html")


def csv_upload(request):
    if request.method == 'POST':

        # Get the uploaded file from the form
        csv_file = request.FILES.get('csv_file')
        # Check if a file was uploaded
        if csv_file is None:
            return HttpResponse("No file uploaded.")

        # Read the contents of the uploaded CSV file
        with TextIOWrapper(csv_file, encoding=request.encoding) as text_file:
            reader = csv.reader(text_file)
            csv_contents = [row for row in reader]

        # Print the contents of the CSV file (for demonstration purposes)
        df = pd.DataFrame(csv_contents[1:], columns=csv_contents[0])
        df['datetime'] = pd.to_datetime(df['datetime'])

        # Convert numerical columns to appropriate data types
        df['price'] = df['price'].astype(float)
        df['quantity'] = df['quantity'].astype(int)
        
        # Perform calculations on the DataFrame

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

    df=pd.read_csv('./sample_data.csv')
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Convert numerical columns to appropriate data types
    df['price'] = df['price'].astype(float)
    df['quantity'] = df['quantity'].astype(int)
    
    # Perform calculations on the DataFrame

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

