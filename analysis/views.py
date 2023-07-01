from django.shortcuts import render,redirect
from django.http import HttpResponse
from io import TextIOWrapper
import csv
# Create your views here.

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
        print(csv_contents)

        return redirect('data_analysis')

    # return HttpResponse("WTF ARE YOU DOINT..!!")
    return render(request,"file_upload.html")


def analysis_data(request):

    return render(request,"analysis.html")

