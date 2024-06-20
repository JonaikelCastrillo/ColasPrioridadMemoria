import heapq

class ColaPrioridad:
    def __init__(self):
        self._cola = []
        self._indice = 0
        
    def agregar_tarea(self, dato, prioridad):
        heapq.heappush(self._cola, (-prioridad, self._indice, dato))
        self._indice += 1
        
    def realizar_tarea(self):
        return heapq.heappop(self._cola)[-1] 