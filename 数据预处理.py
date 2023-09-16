#数据预处理
import os
import pandas as pd
import numpy as np

#创建人工数据集，数据集放到csv
os.makedirs(os.path.join('..','data'),exist_ok=True)
#print(os.path.join('..','data'),exist_ok=True)
# os.makedirs() 递归创建目录
# 语法格式：os.makedirs(path, mode=0o777)
# path: path -- 需要递归创建的目录，可以是相对或者绝对路径。。
# mode -- 权限模式。

# os.path.join()函数：连接两个或更多的路径名组件

# os.makedirs() 方法用于递归创建多层目录。
# os.makedirs(path, mode=511, exist_ok=False)
# path -- 需要递归创建的目录，可以是相对或者绝对路径。
# exist_ok：是否在目录存在时触发异常。如果 exist_ok 为 False（默认值），则在目标目录已存在的情况下触发 FileExistsError 异常；如果 exist_ok 为 True，则在目标目录已存在的情况下不会触发 FileExistsError 异常。


data_file = os.path.join('..','data','house_tiny.csv')
with open(data_file,'w') as f:
    f.write('NumRooms,Alley,Price\n') # 列名
    f.write('NA,Pave,127500\n') # 每行表示一个数据样本
    f.write('2,NA,106000\n') #列名
    f.write('4,NA,178100\n') #列名
    f.write('NA,NA,140000\n') #列名

data = pd.read_csv(data_file)
print(data)

# 处理缺失数值
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2] #iloc位置索引 用同一列均值替换"NAN"
inputs = inputs.fillna(inputs.mean())#.fillna()填充空值，插入其它值的平均数作为空值
print(inputs)

inputs = pd.get_dummies(inputs, dummy_na=True)
#http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html
#pandas.get_dummies(data, prefix=None, prefix_sep='_', 
#			dummy_na=False, columns=None, 
#			sparse=False, drop_first=False, dtype=None)

#data : array-like, Series, or DataFrame
#prefix : 给输出的列添加前缀，如prefix="A",输出的列会显示类似
#prefix_sep : 设置前缀跟分类的分隔符sepration，默认是下划线"_"
#dummy_nabool, default False
#Add a column to indicate NaNs, if False NaNs are ignored.
print(inputs)

#数据类型转换成张量类型
import torch

X, y = torch.tensor(inputs.values), torch.tensor(outputs.values)
X, y

#pandas可以与张量兼容
#创建包含更多行和列的原始数据集。
#删除缺失值最多的列。
#将预处理后的数据集转换为张量格式。

