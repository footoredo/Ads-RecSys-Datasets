import sys
#from datasets import ml100k
from datasets.Couple import Couple

#data = ml100k(initialized=False)
#data.summary()

data = Couple(initialized=False)
data.summary()
