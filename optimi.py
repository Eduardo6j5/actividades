import math
import random
 
random.seed(7)
 
def costo(x):
    return (x - 3) ** 2 + 2
 
def hill_climbing(inicio, paso=0.1, max_iter=5000):
    x = inicio
    for _ in range(max_iter):
        candidatos = [x]
        if x - paso >= -10:
            candidatos.append(x - paso)
        if x + paso <= 10:
            candidatos.append(x + paso)
 
        mejor = min(candidatos, key=costo)
        if costo(mejor) >= costo(x):
            break
        x = mejor
    return x, costo(x)
 
def simulated_annealing(inicio, paso=0.1,
                        temperatura=10.0,
                        enfriamiento=0.995,
                        max_iter=5000):
    x = inicio
    mejor_x = x
    t = temperatura
 
    for _ in range(max_iter):
        direccion = random.choice([-1, 1])
        candidato = x + direccion * paso
 
        if candidato < -10 or candidato > 10:
            t *= enfriamiento
            continue
 
        diferencia = costo(candidato) - costo(x)
 
        if diferencia < 0 or random.random() < math.exp(-diferencia / max(t, 1e-12)):
            x = candidato
 
        if costo(x) < costo(mejor_x):
            mejor_x = x
 
        t *= enfriamiento
        if t < 0.001:
            break
 
    return mejor_x, costo(mejor_x)
 
inicio = -8.0
x_hc, f_hc = hill_climbing(inicio)
x_sa, f_sa = simulated_annealing(inicio)
 
print("Hill Climbing: x =", round(x_hc, 2),
      "costo =", round(f_hc, 4))
print("Simulated Annealing: x =", round(x_sa, 2),
      "costo =", round(f_sa, 4))
print("Óptimo teórico: x = 3, costo = 2")
