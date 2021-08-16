import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics 
import random
import pandas as pd 
import csv 
df=pd.read_csv("mathScore.csv")
data= df["Math_score"].tolist()
#fig=ff.create_distplot([data],["average"],show_hist=False)
#fig.show()
def randomsetofmeans(c):
    dataSet=[]
    for i in range(0,c):
        index=random.randint(0,len(data)-1)
        value=data[index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean 

def showFig(meanList):
    mean=statistics.mean(meanList)
    stdev=statistics.stdev(meanList)
    stdev1start,stdev1end=mean-stdev,mean+stdev
    stdev2start,stdev2end=mean-2*stdev,mean+2*stdev
    stdev3start,stdev3end=mean-3*stdev,mean+3*stdev
    fig=ff.create_distplot([meanList],["average"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.5],mode="lines",name="mean"))
    fig.add_trace(go.Scatter(x=[stdev1start,stdev1start],y=[0,0.5],mode="lines",name="stdev1"))
    fig.add_trace(go.Scatter(x=[stdev1end,stdev1end],y=[0,0.5],mode="lines",name="stdev1"))
    fig.add_trace(go.Scatter(x=[stdev2start,stdev2start],y=[0,0.5],mode="lines",name="stdev2"))
    fig.add_trace(go.Scatter(x=[stdev2end,stdev2end],y=[0,0.5],mode="lines",name="stdev2"))
    fig.add_trace(go.Scatter(x=[stdev3start,stdev3start],y=[0,0.5],mode="lines",name="stdev3"))
    fig.add_trace(go.Scatter(x=[stdev3end,stdev3end],y=[0,0.5],mode="lines",name="stdev3"))


    fig.show()

def setUp():
    meanList=[]
    for i in range(0,1000):
        setofmeans=randomsetofmeans(100)
        meanList.append(setofmeans)
    showFig(meanList)
    samplingMean=statistics.mean(meanList)
    print("samplingmean ",samplingMean)
    samplingStd=statistics.stdev(meanList)
    print("sampling standard devition ",samplingStd)
    zScore=(populationmean-samplingMean)/samplingStd
    print ("zscore=",zScore)

populationmean=statistics.mean(data)
print(populationmean)
populationstd=statistics.stdev(data)
print("standard deviation ",populationstd)
stdev1start,stdev1end=populationmean-populationstd,populationmean+populationstd
stdev2start,stdev2end=populationmean-2*populationstd,populationmean+2*populationstd
stdev3start,stdev3end=populationmean-3*populationstd,populationmean+3*populationstd
setUp()

