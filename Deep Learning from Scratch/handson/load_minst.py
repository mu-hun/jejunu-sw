# 3.6.1
import sys
sys.path.append('../deep-learning-from-scratch/dataset')
from mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape, t_train.shape, x_test.shape, t_test.shape)
