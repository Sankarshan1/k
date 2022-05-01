import random
import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv('medium_data.csv')
data=df['reading_time'].tolist()
def random_set_of_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    setofmean=random_set_of_mean(100)
    mean_list.append(setofmean)
    
mean=statistics.mean(mean_list)
print('samplemean',mean)

standardDevation=statistics.stdev(mean_list)
print('standardDeviation',standardDevation)

first_standard_Deviation_start,first_standard_Deviation_end=mean-standardDevation,mean+standardDevation
second_standard_Deviation_start,second_standard_Deviation_end=mean-(2*standardDevation),mean+(2*standardDevation)
third_standard_Deviation_start,third_standard_Deviation_end=mean-(3*standardDevation),mean+(3*standardDevation)

df=pd.read_csv('medium_data.csv')
data=df['reading_time'].tolist()

meansample1=statistics.mean(data)
print('samplemean',meansample1)
fig=ff.create_distplot([mean_list],['reading_time'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='mean'))
fig.add_trace(go.Scatter(x=[meansample1,meansample1],y=[0,0.17],mode='lines',name='reading_time'))
fig.add_trace(go.Scatter(x=[first_standard_Deviation_end,first_standard_Deviation_end],y=[0,0.17],mode='lines',name='standardDeviation1'))
fig.add_trace(go.Scatter(x=[second_standard_Deviation_end,second_standard_Deviation_end],y=[0,0.17],mode='lines',name='standardDeviation2'))
fig.add_trace(go.Scatter(x=[third_standard_Deviation_end,third_standard_Deviation_end],y=[0,0.17],mode='lines',name='standardDeviation3'))
fig.show()




zscore=(mean-meansample1)/standardDevation
print(zscore)