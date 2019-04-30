from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from index.fusioncharts import FusionCharts
import os
import csv

# Create your views here.



def home(request):

  # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
  dataSource = OrderedDict()

  # The `mapConfig` dict contains key-value pairs data for chart attribute
  mapConfig = OrderedDict()
  mapConfig["chartLeftMargin"] = "100"
  mapConfig["caption"] = "Water Quality Parameter(Flouride) Across India"
  # mapConfig["subcaption"] = "1955-2015"
  mapConfig["numbersuffix"] = "%"
  # mapConfig["includevalueinlabels"] = "1"
  # mapConfig["labelsepchar"] = "Flouride:"

  mapConfig["theme"] = "fusion"

  # Map color range data
  colorDataObj = { "minvalue": "0", "code" : "#FFE0B2", "gradient": "1",
    "color" : [
        { "minValue" : "0", "maxValue" : "0.05", "code" : "#FFD74D" },
        { "minValue" : "0.05", "maxValue" : "0.20", "code" : "#FB8C00" },
        { "minValue" : "0.20", "maxValue" : "0.50", "code" : "#E65100" },
        { "minValue" : "0.50", "maxValue" : "1.0", "code" : "#FFD700" }
        # { "minValue" : "2001", "maxValue" : "3000", "code" : "#FFA500" },
        # { "minValue" : "3001", "maxValue" : "4000", "code" : "#FF8C00" },
        # { "minValue" : "4001", "maxValue" : "7000", "code" : "#FB8C00" }
    ]
  }

  dataSource["chart"] = mapConfig
  dataSource["colorrange"] = colorDataObj
  dataSource["data"] = []


  # Map data array
  mapDataArray = [
    ["001", "0","1.5"],
    ["002", "0.5", "1"],
    ["003", "0", "1"],
    ["004", "0.016", "1"],
    ["005", "0.26", "1"],
    ["006", "0", "1"],
    ["007", "0.0042", "1"],
    ["008", "0", "1"],
    ["009", "0", "1"],
    ["0010", "0", "1"],
    ["0011", "0", "1"],
    ["0012", "0.013", "1"],
    ["0013", "0.004", "1"],
    ["0014", "0", "1"],
    ["0015", "0.0", "1"],
    ["0016", "0.010", "1"],
    ["0017", "0.22", "1"],
    ["0018", "0.008", "1"],
    ["0019", "0", "1"],
    ["0020", "0.2", "1"],
    ["0021", "0.0685", "1"],
    ["0022", "0", "1"],
    ["0023", "0", "1"],
    ["0024", "0", "1"],
    ["0025", "0", "1"],
    ["0026", "0.036", "1"],
    ["0027", "0", "1"],
    ["0028", "0.0016", "1"],
    ["0029", "0.66", "1"],
    ["0031", "0", "1"],
    ["0033", "0.043", "1"],
    ["0034", "0", "1"],
    ["0035", "0.055", "1"]
  ]


  # Iterate through the data in `mapDataArray` and insert in to the `dataSource["data"]` list.
  # The data for the `data` should be in an array wherein each element of the array is a JSON object
  # having the `id`, `value` and `showlabel` as keys.
  print(len(mapDataArray))
  for i in range(len(mapDataArray)):
      dataSource["data"].append({"id": mapDataArray[i][0], "value": mapDataArray[i][1], "showLabel": mapDataArray[i][2] })

  # Create an object for the world map using the FusionCharts class constructor
  # The chart data is passed to the `dataSource` parameter.
  fusionMap = FusionCharts("maps/india", "ex1" , "800", "1000", "chart-1", "json", dataSource)

  # returning complete JavaScript and HTML code, which is used to generate map in the browsers.
  return  render(request, 'home.html', {'output' : fusionMap.render(), 'chartTitle': 'Simple Map Using Array'})



# def home(request):
#     return render(request, "home.html")

def plot(request):
    os.system("python water_quality.py")
    return HttpResponse("<h1>Successful</h1>")

def state_wise(request):
    return render(request, 'states.html')

def theory(request):
    return render(request, 'theory.html')





def state_chart(request, state_name = "state name"):
    name = state_name
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR, "database")

    filename = str(path) + '/' + name + '.csv'
    dataSource = OrderedDict()
    chartConfig = OrderedDict()
    temp_name = name.upper()
    chartConfig["caption"] = temp_name + " Water Quality Parameters "
    # chartConfig["subCaption"] = "In MMbbl = One Million barrels"
    chartConfig["xAxisName"] = "Quality Parameters"
    chartConfig["yAxisName"] = "Count"

    chartConfig["theme"] = "fusion"

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        chartData = OrderedDict()
        for row in csvreader:
            # print(row[0]
            chartData[row[0]] = row[1]

        dataSource["chart"] = chartConfig
        dataSource["data"] = []


        for key, value in chartData.items():
            data = {}
            data["label"] = key
            data["value"] = value
            dataSource["data"].append(data)

        chart_option = "pie3d"
        column2D = FusionCharts(chart_option, "ex1" , "1000", "600", "chart-1", "json", dataSource)

    return  render(request, 'plot.html', {'output' : column2D.render(), 'chartTitle': 'Simple Chart Using Array'})
