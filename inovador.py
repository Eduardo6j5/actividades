# ACTIVIDAD 2: RUTA CON EL ALGORITMO DE DIJKSTRA
import heapq # Permite extraer primero el nodo con menor costo.
 
def dijkstra(grafo, inicio, objetivo):
    """
    Encuentra la ruta de menor costo.
    grafo: diccionario de nodos y vecinos (vecino, costo).
    inicio: localidad de salida.
    objetivo: localidad de llegada.
    Devuelve la ruta y su costo total.
    """
    cola = [(0, inicio)]       # Cola: (costo acumulado, nodo).
    distancias = {inicio: 0}   # Menor costo conocido desde el inicio.
    anteriores = {}            # Permite reconstruir la ruta final.
    visitados = set()          # Nodos ya procesados.
 
    while cola:                # Repetir mientras haya nodos pendientes.
        costo_actual, nodo = heapq.heappop(cola)
 
        if nodo in visitados:   # Ignorar entradas repetidas.
            continue
        visitados.add(nodo)     # Marcar el nodo como procesado.
 
        if nodo == objetivo:    # Si llegamos al destino, terminar.
            break
 
        # Revisar cada conexión que sale del nodo actual.
        for vecino, costo_tramo in grafo.get(nodo, []):
            if costo_tramo < 0:
                raise ValueError("Dijkstra no admite costos negativos")
 
            nuevo_costo = costo_actual + costo_tramo
 
            # Actualizar solo si encontramos una ruta más barata.
            if nuevo_costo < distancias.get(vecino, float("inf")):
                distancias[vecino] = nuevo_costo
                anteriores[vecino] = nodo
                heapq.heappush(cola, (nuevo_costo, vecino))
 
    # Si el destino no tiene distancia registrada, no hay ruta.
    if objetivo not in distancias:
        return None, float("inf")
 
    # Reconstruir la ruta desde el destino hasta el inicio.
    ruta = []
    actual = objetivo
    while actual != inicio:
        ruta.append(actual)
        actual = anteriores[actual]
    ruta.append(inicio)
    ruta.reverse()             # Poner los nodos en orden de viaje.
 
    return ruta, distancias[objetivo]
 
 
# Grafo de ejemplo: solo se requiere llegar hasta Amecameca.
# El costo 8 es ficticio y se usa para demostrar el algoritmo.
grafo_transporte = {
    "Atlautla": [("Amecameca", 8)],
    "Amecameca": [("Atlautla", 8)]
}
 
inicio = "Atlautla"            # Punto donde comienza el recorrido.
objetivo = "Amecameca"         # Punto donde termina el recorrido.
ruta, costo_total = dijkstra(grafo_transporte, inicio, objetivo)
 
# Mostrar el resultado en la terminal.
print("Ruta de transporte")
print("Inicio:", inicio)
print("Destino:", objetivo)
if ruta is None:
    print("No se encontro una ruta.")
else:
    print("Camino encontrado:", " -> ".join(ruta))
    print("Costo total de ejemplo:", costo_total)
