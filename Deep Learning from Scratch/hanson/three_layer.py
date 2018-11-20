# 3.4.3
import numpy as np

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def identity(x): # 항등 함수
	return x

def forward(net, x):
	a1 = np.dot(x, net['W1']) + net['b1'] #1층
	z1 = sigmoid(a1)
	a2 = np.dot(z1, net['W2']) + net['b2'] #2층
	z2 = sigmoid(a2)
	a3 = np.dot(z2, net['W3']) + net['b2'] #3층
	return identity(a3)

network = {
	'W1': np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]),
	'b1': np.array([0.1, 0.2, 0.3]),
	'W2': np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]),
	'b2': np.array([0.1, 0.2]),
	'W3':np.array([[0.1, 0.3], [0.2, 0.4]])
}

x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)
