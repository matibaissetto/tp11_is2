
import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados en el TP11
dias = np.array([0, 1, 2, 3, 4, 5, 6])
defectos = np.array([9, 18, 5, 7, 23, 2, 8])

# Regresión lineal sobre el logaritmo de los defectos
defectos_log = np.log(defectos)
pendiente, intercepto = np.polyfit(dias, defectos_log, 1)

# Parámetros del modelo de Musa
lambda0 = np.exp(intercepto)
mu0 = -lambda0 / pendiente

# Funciones utilizadas en el taller
def mu_smooth(t, lambda0, mu0):
    return mu0 * (1 - np.exp(-(lambda0 * t) / mu0))


def lambda_smooth(t, lambda0, mu0):
    return lambda0 * np.exp(-(lambda0 / mu0) * t)


# Calcular defectos observados y estimados
defectos_observados = np.sum(defectos)
defectos_remanentes = mu0 - defectos_observados

# Evaluar la calidad del ajuste
prediccion_log = pendiente * dias + intercepto
r2 = 1 - (
    np.sum((defectos_log - prediccion_log) ** 2)
    / np.sum((defectos_log - np.mean(defectos_log)) ** 2)
)

# Mostrar resultados
print("=== PROYECCIÓN DE DEFECTOS - TP11 ===")
print(f"Defectos observados: {defectos_observados}")
print(f"Lambda inicial (λ0): {lambda0:.2f}")
print(f"Defectos totales estimados (μ0): {mu0:.2f}")
print(f"Defectos remanentes: {defectos_remanentes:.2f}")
print(f"Coeficiente R²: {r2:.4f}")

if r2 < 0.7:
    print("Advertencia: el ajuste tiene baja capacidad explicativa.")

# Graficar los resultados
tiempo = np.linspace(0, 25, 200)

plt.plot(
    tiempo,
    mu_smooth(tiempo, lambda0, mu0),
    label="Defectos acumulados estimados",
)

plt.plot(
    tiempo,
    lambda_smooth(tiempo, lambda0, mu0),
    label="Intensidad de defectos estimada",
)

plt.scatter(
    dias,
    defectos,
    label="Defectos diarios observados",
)

plt.axhline(
    mu0,
    linestyle="--",
    label=f"Total proyectado: {mu0:.2f}",
)

plt.xlabel("Días de prueba")
plt.ylabel("Cantidad de defectos")
plt.title("Regresión de defectos - Modelo de Musa")
plt.legend()
plt.grid(True)
plt.show()
