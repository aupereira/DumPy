# To-Do
# Add checks to pad out the FFT to size n^2.
# Multithreading.
# Add my own cmath implementation.

import cmath, math

def radix2_fft_lc(x):
    N = len(x)
    if N <= 1:
        return x
    even = radix2_fft_lc(x[0::2])
    odd = radix2_fft_lc(x[1::2])
    T = [cmath.exp(-2j * math.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

def radix2_fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = radix2_fft(x[0::2])
    odd = radix2_fft(x[1::2])
    T = []
    for k in range(N // 2):
        T.append(cmath.exp(-2j * math.pi * k / N) * odd[k])
    R1 = []
    R2 = []
    for k in range(N // 2):
        R1.append(even[k] + T[k])
        R2.append(even[k] - T[k])
    return R1 + R2