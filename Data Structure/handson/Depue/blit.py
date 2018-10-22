from collections import deque

dq = deque('data')

print(dq)
for i, v in enumerate(dq):
	if i < len(dq) - 1:
		print(v.upper(), end='')
	else:
		print(v.upper())
dq.append('r')
dq.appendleft('l')
dq.extend('hello')
print(dq)
