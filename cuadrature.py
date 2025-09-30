import numpy as np

def Integrando(x):
    return x**6 - (x**2 * np.sin(2*x))

def Gaussxw(N):
    x,w = np.polynomial.legendre.leggauss(N)
    return x,w 

def Gaussxw_ab (a,b,x,w):
    return 0.5 * (b-a) * x + 0.5 * (b+a), 0.5 * (b-a) * w

x_2, w_2 = Gaussxw(2)
x_3, w_3 = Gaussxw(3)
x_4, w_4 = Gaussxw(4)
x_5, w_5 = Gaussxw(5)
x_6, w_6 = Gaussxw(6)
x_7, w_7 = Gaussxw(7)
x_8, w_8 = Gaussxw(8)
x_9, w_9 = Gaussxw(9)

exc_x2, exc_w2 = Gaussxw_ab(1,3,x_2, w_2)
exc_x3, exc_w3 = Gaussxw_ab(1,3,x_3, w_3)
exc_x4, exc_w4 = Gaussxw_ab(1,3,x_4, w_4)
exc_x5, exc_w5 = Gaussxw_ab(1,3,x_5, w_5)
exc_x6, exc_w6 = Gaussxw_ab(1,3,x_6, w_6)
exc_x7, exc_w7 = Gaussxw_ab(1,3,x_7, w_7)
exc_x8, exc_w8 = Gaussxw_ab(1,3,x_8, w_8)
exc_x9, exc_w9 = Gaussxw_ab(1,3,x_9, w_9)

integ_2 = np.sum(exc_w2 * Integrando(exc_x2))
integ_3 = np.sum(exc_w3 * Integrando(exc_x3))
integ_4 = np.sum(exc_w4 * Integrando(exc_x4))
integ_5 = np.sum(exc_w5 * Integrando(exc_x5))
integ_6 = np.sum(exc_w6 * Integrando(exc_x6))
integ_7 = np.sum(exc_w7 * Integrando(exc_x7))
integ_8 = np.sum(exc_w8 * Integrando(exc_x8))
integ_9 = np.sum(exc_w9 * Integrando(exc_x9))


print(f"N=2: Integral ≈ {integ_2}")
print(f"N=3: Integral ≈ {integ_3}")
print(f"N=4: Integral ≈ {integ_4}")
print(f"N=5: Integral ≈ {integ_5}")
print(f"N=6: Integral ≈ {integ_6}")
print(f"N=7: Integral ≈ {integ_7}")
print(f"N=8: Integral ≈ {integ_8}")
print(f"N=9: Integral ≈ {integ_9}")


print("El valor exacto se alcanza en N=9")