## Explicación del Método - Cuadratura Gaussiana con Polinomios de Legendre

###Polinomios de Legendre:
Un polinomio de Legendre es una solución polinómica a una ecuación diferencial lineal de segundo orden (Ecuación de Legendre). Los polinomios de Legendre $P_N(x)$ forman un sistema de polinomios ortogonales en el intervalo $[-1, 1]$. 

Estos polinomios se definen recursivamente como: 
\begin{align}
P_0(x) = 1 \\
P_1(x) = x
\end{align}

\begin{align}
(N+1)P_{N+1}(x) = (2N+1)xP_N(x) - NP_{N-1}(x)
\end{align}

O bien, de una forma altenativa, se puede utilizar la Fórmula de Rodrigues para definir esto polinomios como: 

\begin{align}
P_N(x) = \frac{1}{2^N N!}\frac{d^N}{dx^N}\left[(x^2-1)^N\right]
\end{align}


### Cuadratura Gaussiana 
Las raíces de lo polinomios de Legendre brindan los puntos óptimos para evaluar la función, lo cual es fundamental para la implementación del método de la Cuadratura Gaussiana. 

La Cuadratura Gaussiana aproxima integrales mediante la forma: 

\begin{align}
\int_a^b {\rm{d}}x  f(x) \approx \sum_{k=1}^{N} w_k f(x_k)
\end{align}

Donde $w_k$ son los pesos (que es como decir de forma coloquial cual relevante es un punto en la suma) y $x_k$ son los puntos de muestreo (es decir las $N$ raíces del polinomio de Legendre)

Los pesos se calculan de la forma: 
\begin{align}
w_k = \frac{2}{(1-x_k^2)\left[P_N'(x_k)\right]^2}
\end{align}

Mientras que las raíces del Polinomio de Legendre se calculan de la siguiente manera:
\begin{align}
P_N(x_k) = 0 \quad \text{para } k = 1, 2, \ldots, N
\end{align}

Este método funciona de una forma muy precisa debido a que cada peso compensa la distribución no uniforme de los puntos hallados; además de que con $N$ puntos se logran integrar de forma exacta polinomios de grado $2N-1$. 

