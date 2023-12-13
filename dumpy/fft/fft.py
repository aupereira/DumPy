# To-Do
# Add checks to pad out the FFT to size n^2.
# Multithreading.

import cmath, math

type Vec_Complex = list[complex or float or int]

def fft(x: Vec_Complex) -> Vec_Complex:
    """Radix-2 DIT FFT using list comprehension.

    Args:
        x (Vec_Complex): The input vector of real or complex numbers.

    Returns:
        Vec_Complex: The output vector after performing the FFT.
    """

    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [cmath.exp(-2j * math.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

def fft_for(x: Vec_Complex) -> Vec_Complex:
    """Radix-2 DIT FFT using for loops.

    Args:
        x (Vec_Complex): The input vector of real or complex numbers.

    Returns:
        Vec_Complex: The output vector after performing the FFT.
    """
    
    N = len(x)
    if N <= 1:
        return x
    even = fft_for(x[0::2])
    odd = fft_for(x[1::2])
    T = []
    for k in range(N // 2):
        T.append(cmath.exp(-2j * math.pi * k / N) * odd[k])
    R1 = []
    R2 = []
    for k in range(N // 2):
        R1.append(even[k] + T[k])
        R2.append(even[k] - T[k])
    return R1 + R2