import math
import numpy as np
from numpy.polynomial.legendre import leggauss
import mpmath as mp

def gauss_legendre_nodos_pesos(N):
    """
    Devuelve nodos y pesos de Gauss-Legendre en [-1,1].
    """
    nodos, pesos = leggauss(N)
    return nodos, pesos

def escala(nodos, a, b):
    """
    Escala nodos en [-1,1] al intervalo [a,b].
    """
    return 0.5 * (b - a) * nodos + 0.5 * (b + a)

def gauss_integral(f, a, b, N):
    """
    Integra f en [a,b] usando N puntos de Gauss-Legendre.
    """
    nodos, pesos = gauss_legendre_nodos_pesos(N)
    x_escala = escala(nodos, a, b)
    w_escala = 0.5 * (b - a) * pesos
    vals = np.array([f(xi) for xi in x_escala])
    return float(np.sum(w_escala * vals))

def integrando(x):
    """La función: x^6 - x^2 * sin(2x)."""
    return x**6 - x**2 * math.sin(2*x)


def referencia_integral():
    """Calcula el valor de referencia con alta precisión."""
    mp.mp.dps = 50  # 50 dígitos de precisión
    f_mp = lambda x: x**6 - x**2 * mp.sin(2*x)
    I_ref = mp.quad(f_mp, [1, 3])
    return float(I_ref)


if __name__ == "__main__":
    a, b = 1.0, 3.0
    I_ref = referencia_integral()
    print(f"Referencia (alta precisión): {I_ref:.15f}")

    tol = 1e-12
    found = None

    for N in range(1, 21):
        I_N = gauss_integral(integrando, a, b, N)
        err = abs(I_N - I_ref)
        print(f"N={N:2d}  I_N={I_N:.15f}  err={err:.3e}")
        if err < tol:
            found = N
            break

    if found is not None:
        print(f"\nSe alcanza tol={tol:e} con N = {found}")
    else:
        print("\nNo se alcanzó la tolerancia para N<=20")
