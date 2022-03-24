import csv
import plotly.express as px
import numpy as np


def plotfig(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="MarksInPercentage",y="Days Present")
        fig.show()

def get_data_source(data_path):
    marks = []
    days = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
    
        for rows in csv_reader:
            marks.append(float(rows["MarksInPercentage"]))
            days.append(float(rows["Days Present"]))
    return{"x":marks,"y":days}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between marks in percent and days present is  ",correlation[0,1])

def setup():
    data_path="marksvsdays.csv"
    data_source=get_data_source(data_path)
    find_correlation(data_source)
    plotfig(data_path)
setup()





    
     




