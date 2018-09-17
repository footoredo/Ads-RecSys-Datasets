import sys
from datasets import ml100k

data = ml100k(initialized=False)
data.summary()
