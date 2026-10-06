import heapq

grafo = {
    'S': {'A': 5, 'C': 2},
    'A': {'S': 5, 'B': 4, 'G': 9},
    'C': {'S': 2, 'N': 1, 'F': 8, 'E': 10, 'P': 21},
    'N': {'C': 1, 'B': 4, 'Q': 1},
    'B': {'A': 4, 'N': 4, 'I': 3, 'D': 5},
    'Q': {'N': 1, 'D': 7},
    'F': {'C': 8, 'E': 12},
    'E': {'C': 10, 'F': 12, 'D': 2, 'T': 2, 'P': 12, 'L': 7, 'K': 2},
    'D': {'B': 5, 'Q': 7, 'O': 13, 'E': 2, 'T': 6},
    'T': {'D': 6, 'E': 2, 'J': 9},
    'I': {'B': 3, 'O': 7},
    'O': {'I': 7, 'D': 13},
    'G': {'A': 9},
    'P': {'C': 21, 'E': 12},
    'L': {'E': 7},
    'K': {'E': 2},
    'J': {'T': 9}
}

def dijkstra(grafo, inicio):
    """
    Calcula los caminos mínimos desde un vértice de origen a todos los demás en O(|E| log |V|).
    """
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    predecesores = {nodo: None for nodo in grafo}
    
    cola = [(0, inicio)]
    
    while cola:
        dist_actual, u = heapq.heappop(cola)
        
        if dist_actual > distancias[u]:
            continue
            
        for v, peso in grafo[u].items():
            nueva_dist = dist_actual + peso
            
            if nueva_dist < distancias[v]:
                distancias[v] = nueva_dist
                predecesores[v] = u
                heapq.heappush(cola, (nueva_dist, v))
                
    return distancias, predecesores

def reconstruir_camino(predecesores, inicio, destino):
    """
    Reconstruye la ruta óptima retrocediendo por el árbol de caminos mínimos.
    """
    camino = []
    actual = destino
    while actual is not None:
        camino.insert(0, actual)
        if actual == inicio:
            break
        actual = predecesores[actual]
    return camino

origen = 'S'
farmacias = ['B', 'C', 'F', 'T']
entregas = {
    'D': 'Antipsicóticos y aspirinas', 
    'E': 'Supositorios y vendas', 
    'T': 'Antitusivo y chicles'
}

distancias_minimas, arbol_predecesores = dijkstra(grafo, origen)

print(f"--- RUTAS ÓPTIMAS DESDE ORIGEN ({origen}) ---")

nodos_interes = set(farmacias + list(entregas.keys()))

for nodo in sorted(nodos_interes, key=lambda x: distancias_minimas[x]):
    camino = reconstruir_camino(arbol_predecesores, origen, nodo)
    
    etiquetas = []
    if nodo in farmacias: etiquetas.append("Farmacia")
    if nodo in entregas: etiquetas.append(f"Entrega de {entregas[nodo]}")
    
    print(f"[{' | '.join(etiquetas)}] Nodo {nodo}: {distancias_minimas[nodo]} min")
    print(f"   Camino: {' -> '.join(camino)}\n")