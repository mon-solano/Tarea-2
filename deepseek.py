"""
Módulo para integración numérica usando cuadratura Gaussiana.

Este módulo implementa el método de cuadratura Gaussiana basado en los polinomios
de Legendre para aproximar integrales definidas.
"""

import numpy as np

def gauss_legendre_points_weights(n):
    """
    Calcula los puntos y pesos de Gauss-Legendre para el intervalo [-1, 1].
    
    Args:
        n (int): Número de puntos de cuadratura.
        
    Returns:
        tuple: (puntos, pesos) donde:
            - puntos: array de puntos de Gauss en [-1, 1]
            - pesos: array de pesos correspondientes
            
    Examples:
        >>> puntos, pesos = gauss_legendre_points_weights(2)
        >>> print(f"Puntos: {puntos}")
        >>> print(f"Pesos: {pesos}")
    """
    # Para n=1 caso especial
    if n == 1:
        return np.array([0.0]), np.array([2.0])
    
    # Calcula los puntos de Legendre (raíces del polinomio de Legendre de grado n)
    beta = 0.5 / np.sqrt(1 - (2 * np.arange(1, n)) ** (-2))
    T = np.diag(beta, 1) + np.diag(beta, -1)
    puntos, V = np.linalg.eigh(T)
    
    # Calcula los pesos
    pesos = 2 * (V[0, :] ** 2)
    
    return puntos, pesos

def scale_interval(puntos, pesos, a, b):
    """
    Escala los puntos y pesos de Gauss del intervalo [-1, 1] a [a, b].
    
    Args:
        puntos (array): Puntos de Gauss en [-1, 1]
        pesos (array): Pesos de Gauss correspondientes
        a (float): Límite inferior del intervalo de integración
        b (float): Límite superior del intervalo de integración
        
    Returns:
        tuple: (puntos_escalados, pesos_escalados)
        
    Examples:
        >>> puntos = np.array([-0.57735, 0.57735])
        >>> pesos = np.array([1.0, 1.0])
        >>> p_esc, w_esc = scale_interval(puntos, pesos, 0, 2)
        >>> print(f"Puntos escalados: {p_esc}")
        >>> print(f"Pesos escalados: {w_esc}")
    """
    # Escala los puntos
    puntos_escalados = 0.5 * (b - a) * puntos + 0.5 * (a + b)
    
    # Escala los pesos
    pesos_escalados = 0.5 * (b - a) * pesos
    
    return puntos_escalados, pesos_escalados

def gaussian_quadrature(f, a, b, n):
    """
    Calcula la integral de f(x) en [a, b] usando cuadratura Gaussiana de n puntos.
    
    Args:
        f (function): Función a integrar
        a (float): Límite inferior de integración
        b (float): Límite superior de integración
        n (int): Número de puntos de Gauss
        
    Returns:
        float: Aproximación de la integral
        
    Examples:
        >>> # Integrar x^2 en [0, 2]
        >>> f = lambda x: x**2
        >>> resultado = gaussian_quadrature(f, 0, 2, 3)
        >>> print(f"Resultado: {resultado:.6f}")
        >>> # Valor exacto: 8/3 ≈ 2.666667
    """
    # Obtener puntos y pesos base en [-1, 1]
    puntos_base, pesos_base = gauss_legendre_points_weights(n)
    
    # Escalar al intervalo [a, b]
    puntos_esc, pesos_esc = scale_interval(puntos_base, pesos_base, a, b)
    
    # Evaluar la función en los puntos escalados
    valores_f = f(puntos_esc)
    
    # Calcular la integral aproximada
    integral = np.sum(pesos_esc * valores_f)
    
    return integral

def calcular_integral_exacta():
    """
    Calcula el valor exacto de la integral ∫(x⁶ + x²sen(2x)) dx desde -1 hasta 1.
    
    Returns:
        float: Valor exacto de la integral
    """
    # Para x⁶: ∫x⁶ dx = x⁷/7, evaluado de -1 a 1 = (1/7) - (-1/7) = 2/7
    parte_polinomio = 2/7
    
    # Para x²sen(2x): se resuelve por integración por partes
    # ∫x²sen(2x)dx = -x²cos(2x)/2 + ∫xcos(2x)dx
    # ∫xcos(2x)dx = xsen(2x)/2 - ∫sen(2x)/2 dx = xsen(2x)/2 + cos(2x)/4
    
    # Evaluando de -1 a 1:
    # En x=1: -1²cos(2)/2 + 1*sen(2)/2 + cos(2)/4 = -cos(2)/2 + sen(2)/2 + cos(2)/4
    # En x=-1: -1²cos(-2)/2 + (-1)*sen(-2)/2 + cos(-2)/4 = -cos(2)/2 - sen(2)/2 + cos(2)/4
    
    # Diferencia: [-cos(2)/2 + sen(2)/2 + cos(2)/4] - [-cos(2)/2 - sen(2)/2 + cos(2)/4]
    # = sen(2)/2 + sen(2)/2 = sen(2)
    
    from math import sin
    parte_trigonometrica = sin(2)
    
    return parte_polinomio + parte_trigonometrica

def main():
    """
    Función principal que resuelve la integral específica de la tarea.
    
    La integral a resolver es: ∫(x⁶ + x²sen(2x)) dx desde -1 hasta 1
    """
    # Definir la función a integrar: f(x) = x⁶ + x²sen(2x)
    def f(x):
        return x**6 + x**2 * np.sin(2*x)
    
    a, b = -1, 1  # Límites de integración
    
    # Calcular valor exacto
    valor_exacto = calcular_integral_exacta()
    
    print("Cuadratura Gaussiana para ∫(x⁶ + x²sen(2x))dx desde -1 hasta 1")
    print(f"Valor exacto: {valor_exacto:.10f}")
    print("-" * 70)
    
    # Probar con diferentes valores de N
    for n in range(1, 10):
        resultado = gaussian_quadrature(f, a, b, n)
        error = abs(resultado - valor_exacto)
        
        print(f"N = {n}: Resultado = {resultado:.10f}, Error = {error:.10f}")
        
        # Verificar si hemos alcanzado una precisión aceptable
        if error < 1e-10:
            print(f"¡Resultado exacto alcanzado con N = {n}!")
            break
    else:
        print("No se alcanzó la precisión deseada con N ≤ 9")

if __name__ == "__main__":
    main()