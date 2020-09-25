# -*- coding: utf-8 -*-
# author:Gary

# cross_validation等模块弃用,所有的包和方法都在model_selection中,包和方法名没有发生变化
#参考链接 https://blog.csdn.net/qi_1221/article/details/76071555
#
from sklearn import datasets, svm
from sklearn.model_selection import cross_val_score

iris = datasets.load_iris()
X = iris.data
y = iris.target

# 习题中的kemel应该是拼写错误
'''
C：C-SVC的惩罚参数C?默认值是1.0
C越大，相当于惩罚松弛变量，希望松弛变量接近0，即对误分类的惩罚增大，趋向于对训练集全分对的情况，这样对训练集测试时准确率很高，但泛化能力弱。
C值小，对误分类的惩罚减小，允许容错，将他们当成噪声点，泛化能力较强。

kernel ：核函数，默认是rbf，可以是"linear", "poly", "rbf", "sigmoid", "precomputed"
"linear":– 线性核函数：u’v
"poly":– 多项式核函数：(gamma*u’v + coef0)^degree
"rbf":– RBF函数(径像核函数/高斯核)：exp(-gamma|u-v|^2)
"sigmoid":–sigmoid核函数：tanh(gammau’*v + coef0)
"precomputed":核矩阵

gamma ： ‘rbf’,‘poly’ 和‘sigmoid’的核函数参数。默认是’auto’，则会选择1/n_features
'''
svc = svm.SVC(C=1, kernel="rbf", gamma=0.001)

'''
参考链接 https://blog.csdn.net/qq_41937076/article/details/101313985
sklearn.model_selection.cross_val_score(estimator, X, y=None, groups=None, scoring=None, cv=None,
 n_jobs=1, verbose=0, fit_params=None, pre_dispatch=‘2*n_jobs’)
 
estimator:估计方法对象(分类器)
X：数据特征(Features)
y：数据标签(Labels)
soring：调用方法(包括accuracy和mean_squared_error等等)
cv：几折交叉验证，cv=几就表示几折。
n_jobs：同时工作的cpu个数（-1代表全部）

'''
scores = cross_val_score(svc, X, y, cv=5)
print(scores)
print("平均得分：", scores.mean())
