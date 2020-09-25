# -*- coding: utf-8 -*-
# author:Gary
from sklearn.metrics import confusion_matrix
import matplotlib.pylab as plt

guess = ["cat", "cat", "bird", "ant", "cat", "cat", "ant", "bird", "ant", "cat", "cat", "ant", "bird", "bird", "ant"]
fact = ["ant", "ant", "ant", "ant", "cat", "cat", "ant", "cat", "ant", "cat", "bird", "ant", "bird", "bird", "bird"]
C3 = confusion_matrix(fact, guess, labels=["ant", "cat", "bird"])
print(C3)
classes = list(set(fact))
classes.sort()
confusion = confusion_matrix(guess, fact)
plt.imshow(confusion, cmap=plt.cm.Blues)
indices = range(len(confusion))
plt.xticks(indices, classes)
plt.yticks(indices, classes)
plt.colorbar()
plt.xlabel("guess")
plt.ylabel('fact')
for m in range(len(confusion)):
    for n in range(len(confusion)):
        plt.text(m, n, confusion[m])

plt.show()
