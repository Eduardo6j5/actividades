from collections import deque
 
grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": ["G"],
    "G": []
}
 
def reconstruir_camino(padres, inicio, objetivo):
    if objetivo not in padres and objetivo != inicio:
        return None
    camino = []
    actual = objetivo
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    return list(reversed(camino))
 
def bfs(grafo, inicio, objetivo):
    cola = deque([inicio])
    visitados = {inicio}
    padres = {inicio: None}
    orden = []
 
    while cola:
        nodo = cola.popleft()
        orden.append(nodo)
 
        if nodo == objetivo:
            break
 
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = nodo
                cola.append(vecino)
 
    return orden, reconstruir_camino(padres, inicio, objetivo)
 
def dfs(grafo, inicio, objetivo):
    pila = [inicio]
    visitados = set()
    padres = {inicio: None}
    orden = []
 
    while pila:
        nodo = pila.pop()
        if nodo in visitados:
            continue
 
        visitados.add(nodo)
        orden.append(nodo)
 
        if nodo == objetivo:
            break
 
        # Se invierte para respetar el orden definido en el grafo
        for vecino in reversed(grafo.get(nodo, [])):
            if vecino not in visitados:
                if vecino not in padres:
                    padres[vecino] = nodo
                pila.append(vecino)
 
    return orden, reconstruir_camino(padres, inicio, objetivo)
 
for nombre, algoritmo in [("BFS", bfs), ("DFS", dfs)]:
    orden, camino = algoritmo(grafo, "A", "G")
    print(nombre)
    print("Orden de exploración:", orden)
    print("Camino encontrado:", camino)
5. Resultados esperados
Con el grafo y el orden de vecinos definidos en el código, BFS explora por niveles y encuentra el camino A → B → E → G. DFS profundiza por la primera rama según el orden definido y encuentra una ruta válida; el orden exacto puede cambiar si se modifica la lista de vecinos.
BFS
Orden de exploración: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
Camino encontrado: ['A', 'B', 'E', 'G']
 
DFS
Orden de exploración: ['A', 'B', 'D', 'E', 'G']
Camino encontrado: ['A', 'B', 'E', 'G']
