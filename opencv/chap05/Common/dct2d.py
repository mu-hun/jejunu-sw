import numpy as np, cv2, math
import scipy.fftpack as sf

def cos(n,k,N):
    return math.cos((n + 1/2) * math.pi * k / N)

def ck(k, N):
    return math.sqrt(1/N) if k==0 else math.sqrt(2/N)

def dct(g):
    N = len(g)
    f = [ck(k, N) * sum(g[n] * cos(n, k, N ) for n in range(N)) for k in range(N)]
    return np.array(f, np.float32)

def idct(f):
    N = len(f)
    g = [sum(ck(k, N) * f[k] * cos(n, k, N) for k in range(N)) for n in range(N)]
    return np.array(g)

def dct2(image):
    tmp = [dct(row) for row in image]
    dst = [dct(row) for row in np.transpose(tmp)]
    return np.transpose(dst)                   # 전치 환원 후 반환

def idct2(image):
    tmp = [idct(row) for row in image]
    dst = [idct(row) for row in np.transpose(tmp)]
    return np.transpose(dst)                   # 전치 환원 후 반환

def scipy_dct2(a):
    tmp = sf.dct(a, axis=0, norm='ortho' )
    return sf.dct(tmp, axis=1, norm='ortho' )

def scipy_idct2(a):
    tmp = sf.idct(a, axis=0, norm='ortho')
    return sf.idct(tmp, axis=1 , norm='ortho')


def dct2_mode(block, mode):
    if mode==1: return dct2(block)
    elif mode==2: return  scipy_dct2(block)
    elif mode==3: return  cv2.dct(block.astype('float32'))

def idct2_mode(block, mode):
    if mode==1: return idct2(block)
    elif mode==2: return scipy_idct2(block)
    elif mode==3: return cv2.dct(block, flags=cv2.DCT_INVERSE)
