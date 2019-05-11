"""DFT / IDFT as matrix operation.

Digital Signal Processing (DSP) M.Eng. Course #24505
Prof. Sascha Spors, Frank Schultz
Institute of Communications Engineering
University of Rostock

revision:
0.0  init version for winter term 2019/20

MIT License
Copyright (c) <2019> <Frank Schultz, Sascha Spors>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
import numpy as np
from numpy.linalg import inv

# DFT size:
N = 2**3

k = np.arange(0, N)  # sample/time index
mu = np.arange(0, N)  # DFT frequency index
A = np.outer(mu, k)  # get entries k*mu for the W^k^mu matrix

# signal as DFT input:
x = np.cos(2*np.pi/N*2*k+np.pi/4)

# DFT preps:
Fa = np.exp(-1j * 2*np.pi/N * A) / np.sqrt(N)  # analysis matrix
Fs = np.exp(+1j * 2*np.pi/N * A) / np.sqrt(N)  # synthesis matrix
# please realize that the inverse of Fa has just reversed sign in exp():
Fs_check = inv(Fa)  # so Fs == Fs_check holds
Ieye = np.matmul(Fs, Fa)  # we might check that this gives the identity matrix
# (besides numerical precision errors)
np.vdot(Fa[:,0],Fa[:,1])  # this checks two individual cols against orthonormality
np.vdot(Fa[0,:],Fa[1,:])  # this checks two individual rows against orthonormality

# DFT / IDFT:
X = np.matmul(Fa, x)  # DFT
xr = np.matmul(Fs, X)  # inverse DFT
print('\n### 1/sqrt(N) normalization ###')
print('DFT X = ', X)
print('check reconstruction: max |x-xr| = ', np.max(np.abs(x-xr)))

# the normalization is often performed in other way, such as
Fa = np.exp(-1j * 2*np.pi/N * A) / 1  # analysis matrix
Fs = np.exp(+1j * 2*np.pi/N * A) / N  # synthesis matrix
# this is a commonly used convention in Matlab and numpy
# please double check in other software!

Xnp = np.fft.fft(x)  # numpy DFT
xrnp = np.fft.ifft(Xnp)  # numpy IDFT
X = np.matmul(Fa, x)  # DFT
xr = np.matmul(Fs, X)  # inverse DFT
print('\n### Python numpy / Matlab convention ###')
print('DFT X = ', X)
print('check reconstruction: max |x-xr| = ', np.max(np.abs(x-xr)))
print('check numpy DFT X = ', Xnp)

print('max |real(X-Xnp)| = ', np.max(np.abs(np.real(X-Xnp))))
print('max |imag(X-Xnp)| = ', np.max(np.abs(np.imag(X-Xnp))))
