# CEFET-MG BH, Eng. de Computacao
# algoritmo A* (a estrela / astar) para busca de caminhos
# para a disciplina Laboratorio de Inteligencia Artificial
# professor Rogerio Martins
# aluno: Samir Saliba Jr

# algoritmo pode ser encontrado em https://github.com/samirsaliba/astar-pathfinding
# foi baseado no pseudocodigo e na explicacao: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

import csv

class Vertex:
	def __init__(self, node):
		self.id = node
		self.adjacent = {}
		self.sld = {}
		self.parent=None
		self.f=0
		self.h=0
		self.g=0
		self.depth=0

	def __str__(self):
		return self.id

	def add_neighbor(self, neighbor, weight=0):
		self.adjacent[neighbor] = weight
		self.sld[neighbor] = 0

	def add_sld(self, to, sld=0):
		self.sld[to] = sld

	def get_connections(self):
		return self.adjacent.keys()

	def get_id(self):
		return self.id

	def get_weight(self, neighbor):
		return self.adjacent[neighbor]

	def get_sld(self, destination):
		return self.sld.setdefault(destination, 0)

class Graph:
	def __init__(self):
		self.vertices = {}
		self.num_vertices = 0

	def __iter__(self):
		return iter(self.vertices.values())

	def add_vertex(self, node):
		self.num_vertices = self.num_vertices + 1
		new_vertex = Vertex(node)
		self.vertices[node] = new_vertex
		return new_vertex

	def get_vertex(self, n):
		if n in self.vertices:
			return self.vertices[n]
		else:
			return None

	def add_edge(self, frm, to, distance=0):
		if frm not in self.vertices:
			self.add_vertex(frm)
		if to not in self.vertices:
			self.add_vertex(to)

		if distance!=0:
			self.vertices[frm].add_neighbor(self.vertices[to], int(distance, 10))
			self.vertices[to].add_neighbor(self.vertices[frm], int(distance, 10))				
			
	def add_sld(self, frm, to, sld=0):
		if frm not in self.vertices:
			self.add_vertex(frm)
		if to not in self.vertices:
			self.add_vertex(to)

		if sld!=0:
			self.vertices[frm].add_sld(self.vertices[to], int(sld, 10))
			self.vertices[to].add_sld(self.vertices[frm], int(sld, 10))

	def get_vertices(self):
		return self.vertices.keys()

def aStar(grafo, str_start, str_end):
	bound = []
	closed = []

	start = grafo.get_vertex(str_start)
	end = grafo.get_vertex(str_end)
	
	bound.append(start)

	while bound:
		node = bound[0]
		current_index = 0
		for index, item in enumerate(bound):
			if item.f < node.f:
				node = item
				current_index = index

		bound.pop(current_index)
		closed.append(node)

		print 'no analisado: ' + node.id + ' f: ' + str(node.f) + ' g: ' + str(node.g) + ' h: ' + str(node.h)
		if node == end:
			path = []
			aux = node
			while aux is not None:
				path.append(aux)
				aux = aux.parent
			return path[::-1] # Return reversed path

		for neighbor in node.adjacent:
			if neighbor in closed:
				continue

			neighbor.parent = node
			neighbor.depth = node.depth+1
			neighbor.g = node.g + node.get_weight(neighbor)
			neighbor.h = neighbor.get_sld(end)
			neighbor.f = neighbor.g + neighbor.h

			if neighbor in bound:
				continue

			bound.append(neighbor)

if __name__ == '__main__':

	grafo = Graph()

	with open('cidades.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			print(row)

			if row == []:
				continue

			elif row[0]=='e':
				grafo.add_edge(row[1], row[2], row[3])
		
			elif row[0]=='h':
				grafo.add_sld(row[1], row[2], row[3])

			elif row[0]=='a*':
				print 'astar: from ' + row[1] + ' to ' +  row[2]
				start = row[1]
				end = row[2]


	path = aStar(grafo, start, end)
	for x in path:
		print '-> ', x,