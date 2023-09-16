# 标量-只有一个元素的张量表示
import torch
import numpy as np

x = torch.tensor(3.0)
y = torch.tensor(2.0)

x + y, x * y, x / y, x**y

#向量，标量值组成的列表
z = torch.arange(4)
z

#使用下标引用向量的任一元素，通过xi来引用第i个元素。
# 元素是一个标量，所以我们在引用它时不会加粗。 
# 认为列向量是向量的默认方向，
z[3]

#长度、维度和形状
# 我们可以通过调用Python的内置len()函数来访问张量的长度。
len(z)

#对于只有一个轴的张量，形状只有一个元素。
z.shape

#矩阵
A = torch.arange(20).reshape(5, 4)
A.T

B = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
B
B == B.T

#张量
C = np.arange(24).reshape(2, 3, 4)
C

#张量算法的基本性质
D = np.arange(20).reshape(5, 4)
E = D.copy()  # 通过分配新内存，将A的一个副本分配给B
D, D + E
D * E
