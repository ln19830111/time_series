import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from pylab import mpl

# 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
mpl.rcParams['axes.unicode_minus'] = False 
np.set_printoptions(threshold=np.inf,suppress=True)


#定義基金14分類
# Label_columns=['新興市場', '美國', '大中華',
#     '亞太', '歐洲', '全球', '科技', '生技醫療', '天然資源礦業金屬',
#     '公債,投資級債,貨幣型', '新興市場債', '高收益債', '股債平衡&多重資產', '不動產'
#     ]

Label_columns ='區域	產業	投資標的'.split('	')

# data=pd.read_csv('test1819.csv',engine='c',parse_dates=['有效日期'],usecols=['有效日期']+Label_columns)
# pre_data=pd.read_csv('pre_test.csv',engine='c',parse_dates=['有效日期'],usecols=['CST_ID','有效日期']+Label_columns)

data=pd.read_csv('存戶_購買基金_瀏覽過金融_理財_19_07以後.csv',engine='c',parse_dates=['有效日期'],usecols=['CST_ID','有效日期']+Label_columns)
pre_data=pd.read_csv('pre_test.csv',engine='c',parse_dates=['有效日期'],usecols=['CST_ID','有效日期']+Label_columns)



data.drop_duplicates(inplace=True)
pre_data.drop_duplicates(inplace=True)


def buy_time_trend(data,name):
    data['year'] = data['有效日期'].dt.strftime('%Y').astype(int)
    data['month'] = data['有效日期'].dt.strftime('%m').astype(int)


    year=data['year'].unique()
    month=data['month'].unique()

    year.sort() ; month.sort() 

    time_list=[f'{str(x)}-{str(y)}' for x in year for y in month]
    
    array_2018=[]
    array_2019=[]

    for x in year:
        if x== 2018:
            tmp_list=array_2018
        else:
            tmp_list=array_2019

        for y in month:
            tmp_list.append(data[(data['year']==x) &( data['month']==y)][Label_columns].sum().values)

    if len(year) >1 :
        array_201819=np.vstack([array_2018,array_2019])
    else:
        array_201819=np.array(array_2019)
    plt.plot(array_201819.sum(axis=1),label=name)
    plt.xticks(list(range(len(time_list))),labels=time_list)


def class_buy_time_trend(data):
    data['year'] = data['有效日期'].dt.strftime('%Y').astype(int)
    data['month'] = data['有效日期'].dt.strftime('%m').astype(int)


    year=data['year'].unique()
    month=data['month'].unique()

    year.sort() ; month.sort() 

    time_list=[f'{str(x)}-{str(y)}' for x in year for y in month]
    
    array_2018=[]
    array_2019=[]
    
    for x in year:
        if x== 2018:
            tmp_list=array_2018
        else:
            tmp_list=array_2019

        for y in month:
            tmp_list.append(data[(data['year']==x) &( data['month']==y)][Label_columns].sum().values)

    if len(year) >1 :
        array_201819=np.vstack([array_2018,array_2019])
    else:
        array_201819=np.array(array_2019)

    for x in range(len(Label_columns)):
        plt.plot(array_201819[:,x])
    plt.xticks(list(range(len(time_list))),labels=time_list)
    plt.legend(Label_columns)
    plt.show()


buy_time_trend(pre_data,'預測')
buy_time_trend(data,'實際')
plt.legend()
plt.grid(True)
plt.show()
class_buy_time_trend(data)
class_buy_time_trend(pre_data)
