##Tutorial de uso

A continuación se presenta el código para calcular la integral ∫(x⁶ - x²sen(2x)) dx desde 1 hasta 3 usando cuadratura Gaussiana.

Primeramente se importa la biblioteca NumPy para realizar cálculos y accesar a los polinomios de Legendre 

```python
import numpy as np
```
Luego, se define la función a Integrar:
```python
def Integrando(x):
    return x**6 - (x**2 * np.sin(2*x))
```
###Ahora se obtienen los puntos y los pesos con: 
```python
def Gaussxw(N):
    x,w = np.polynomial.legendre.leggauss(N)
    return x,w 
```
donde leggauss(N) devuelve los puntos y los pesos para la cuadratura 

###Luego se construye la función para escalar al intervalo [a,b]
```python
def Gaussxw_ab (a,b,x,w):
    return 0.5 * (b-a) * x + 0.5 * (b+a), 0.5 * (b-a) * w
```
#Seguidamente se calculan los puntos y pesos con diferentes vLORES DE n
Esto se logra siguiendo la sintaxis 
```python
x_2, w_2 = Gaussxw(2)
x_3, w_3 = Gaussxw(3)
```
Hasta que se crea haber encontrado un valor de convergencia exacto.

###Ahora se escalan los puntos y pesos en el intervalo correspondiente 
```python
exc_x2, exc_w2 = Gaussxw_ab(1,3,x_2, w_2)
exc_x3, exc_w3 = Gaussxw_ab(1,3,x_3, w_3)
```
###Finalmente se calculan las integrales aproximadas:
```python
integ_2 = np.sum(exc_w2 * Intengrando(exc_x2))
integ_3 = np.sum(exc_w3 * Intengrando(exc_x3))
```
Para visualizarlas se invoca el print:
```python
print(f"N=2: Integral ≈ {integ_2}")
```

En este caso, se encontró que en N=9 se obtiene el valor exacto de esa integral el cual es: 317.34424667382643
Por lo que todo lo anteriormente definido se repitió 9 veces para mostar el resultado correcto y los resultados anteriores. 

##Importante:

Es posible reutilizar la estructura de este código solamente cambiando la función a integrar y los intervalos en donde será evaluada. 
