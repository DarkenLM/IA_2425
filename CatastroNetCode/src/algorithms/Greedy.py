##########################################
#   Greedy
##########################################

def greedy(self, start, end):

    open_list = set([start])
    closed_list = set([])
    paths = {}

    # parents é um dicionário que mantém o antecessor de um nodo
    # começa com start
    parents = {}
    parents[start] = start

    while len(open_list) > 0:
        n = None
        if not end:
            return paths

        # encontra nodo com a menor heuristica
        for v in open_list:
            if n == None or min(self.getHeuristica(v, d) for d in end) < min(self.getHeuristica(n, d) for d in end):
                n = v

        if n == None:
            print('Path does not exist!')
            return None

        # se o nodo corrente é o destino
        # reconstruir o caminho a partir desse nodo até ao start
        # seguindo o antecessor
        if n in end:
            backN = n
            reconst_path = []
            end.remove(n)

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start)

            reconst_path.reverse()

            # return (reconst_path, self.calcula_custo(reconst_path))
            paths[backN] = reconst_path

        # para todos os vizinhos  do nodo corrente
        for m in self.getNeighbors(n):
            # Se o nodo corrente nao esta na open nem na closed list
            # adiciona-lo à open_list e marcar o antecessor
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n

        # remover n da open_list e adiciona-lo à closed_list
        # porque todos os seus vizinhos foram inspecionados
        if n in open_list:
            open_list.remove(n)
            closed_list.add(n)

    print('Path does not exist!')
    return None



# def greedy(self, start, end):

#     open_list = set([start])
#     closed_list = set([])

#     # parents é um dicionário que mantém o antecessor de um nodo
#     # começa com start
#     parents = {}
#     parents[start] = start

#     while len(open_list) > 0:
#         n = None
#         # encontra nodo com a menor heuristica
#         for v in open_list:
#             if n == None or self.getHeuristica(v, end[0]) < self.getHeuristica(n, end[0]):
#                 n = v

#         if n == None:
#             print('Path does not exist!')
#             return None

#         # se o nodo corrente é o destino
#         # reconstruir o caminho a partir desse nodo até ao start
#         # seguindo o antecessor
#         if n == end[0]:
#             reconst_path = []

#             while parents[n] != n:
#                 reconst_path.append(n)
#                 n = parents[n]

#             reconst_path.append(start)

#             reconst_path.reverse()

#             # return (reconst_path, self.calcula_custo(reconst_path))
#             return reconst_path
#         # para todos os vizinhos  do nodo corrente

#         for m in self.getNeighbors(n):
#             # Se o nodo corrente nao esta na open nem na closed list
#             # adiciona-lo à open_list e marcar o antecessor
#             if m not in open_list and m not in closed_list:
#                 open_list.add(m)
#                 parents[m] = n

#         # remover n da open_list e adiciona-lo à closed_list
#         # porque todos os seus vizinhos foram inspecionados
#         open_list.remove(n)
#         closed_list.add(n)

#     print('Path does not exist!')
#     return None