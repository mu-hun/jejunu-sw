# 3.4.3
import numpy as np

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def identity(x): # 항등 함수
	return x

def forward(net, x):
	a1 = np.dot(x, net['W1']) + net['b1']
	z1 = sigmoid(a1)
	a2 = np.dot(z1, net['W2'])
	z2 = sigmoid(a2)
	a3 = np.dot(z2, net['W3']) + net['b3']
	y = identity(a3)
	return y

network = {
	'W1': np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]),
	'b1': np.array([0.1, 0.2, 0.3]),
	'W2': np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]),
	'b2': np.array([0.1, 0.2]),
	'W3':np.array([[0.1, 0.3], [0.2, 0.4]]),
	'b3': np.array([0.1, 0.2])
}

x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)
