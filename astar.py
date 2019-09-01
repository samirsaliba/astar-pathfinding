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
			print 'error adding edge: missing ' + frm + ' vertex'
		elif to not in self.vertices:
			print 'error adding edge: missing ' + to + ' vertex'
		else:
			self.vertices[frm].add_neighbor(self.vertices[to], distance)
			self.vertices[to].add_neighbor(self.vertices[frm], distance)

	def add_sld(self, frm, to, sld=0):
		if frm not in self.vertices:
			print 'error adding straight line distance: missing ' + frm + ' vertex'
		elif to not in self.vertices:
			print 'error adding straight line distance: missing ' + to + ' vertex'
		else:
			self.vertices[frm].add_sld(self.vertices[to], sld)
			self.vertices[to].add_sld(self.vertices[frm], sld)

	def get_vertices(self):
		return self.vertices.keys()

def aStar(grafo, str_start, str_end):
	bound = []
	closed = []

	start = grafo.get_vertex(str_start)
	end = grafo.get_vertex(str_end)

	print 'A* (astar) pathfinding algorithm'
	print 'from ' + start.id + ' to ' + end.id

	
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

	grafo.add_vertex('oradea')
	grafo.add_vertex('zerind')
	grafo.add_vertex('arad')
	grafo.add_vertex('timisoara')
	grafo.add_vertex('lugoj')
	grafo.add_vertex('mehadia')
	grafo.add_vertex('dobreta')
	grafo.add_vertex('craiova')
	grafo.add_vertex('rimnicu')
	grafo.add_vertex('sibiu')
	grafo.add_vertex('fagaras')
	grafo.add_vertex('pitesti')
	grafo.add_vertex('bucharest')
	grafo.add_vertex('giurgiu')
	grafo.add_vertex('neamt')
	grafo.add_vertex('iasi')
	grafo.add_vertex('vaslui')
	grafo.add_vertex('urziceni')
	grafo.add_vertex('hirsova')
	grafo.add_vertex('eforie')

	grafo.add_edge('oradea', 'zerind', 71)
	grafo.add_edge('zerind', 'arad', 75)
	grafo.add_edge('arad', 'timisoara', 118)
	grafo.add_edge('timisoara', 'lugoj', 111)
	grafo.add_edge('lugoj', 'mehadia', 70)
	grafo.add_edge('oradea', 'sibiu', 151)
	grafo.add_edge('mehadia', 'dobreta', 75)
	grafo.add_edge('dobreta', 'craiova', 120)
	grafo.add_edge('craiova', 'rimnicu', 146)
	grafo.add_edge('craiova', 'pitesti', 138)
	grafo.add_edge('rimnicu', 'sibiu', 80)
	grafo.add_edge('arad', 'sibiu', 140)
	grafo.add_edge('sibiu', 'fagaras', 99)
	grafo.add_edge('fagaras', 'bucharest', 211)
	grafo.add_edge('rimnicu', 'pitesti', 97)
	grafo.add_edge('pitesti', 'bucharest', 101)
	grafo.add_edge('giurgiu', 'bucharest', 90)
	grafo.add_edge('bucharest', 'urziceni', 85)
	grafo.add_edge('urziceni', 'hirsova', 98)
	grafo.add_edge('hirsova', 'eforie', 86)
	grafo.add_edge('urziceni', 'vaslui', 142)
	grafo.add_edge('vaslui', 'iasi', 92)
	grafo.add_edge('iasi', 'neamt', 87)


	grafo.add_sld('arad', 'bucharest', 366)
	grafo.add_sld('bucharest', 'bucharest', 0)
	grafo.add_sld('craiova', 'bucharest', 160)
	grafo.add_sld('dobreta', 'bucharest', 242)
	grafo.add_sld('eforie', 'bucharest', 161)
	grafo.add_sld('fagaras', 'bucharest', 176)
	grafo.add_sld('giurgiu', 'bucharest', 77)
	grafo.add_sld('hirsova', 'bucharest', 151)
	grafo.add_sld('iasi', 'bucharest', 226)
	grafo.add_sld('lugoj', 'bucharest', 244)
	grafo.add_sld('mehadia', 'bucharest', 241)
	grafo.add_sld('neamt', 'bucharest', 234)
	grafo.add_sld('oradea', 'bucharest', 380)
	grafo.add_sld('pitesti', 'bucharest', 10)
	grafo.add_sld('rimnicu', 'bucharest', 193)
	grafo.add_sld('sibiu', 'bucharest', 253)
	grafo.add_sld('timisoara', 'bucharest', 329)
	grafo.add_sld('urziceni', 'bucharest', 80)
	grafo.add_sld('vaslui', 'bucharest', 199)
	grafo.add_sld('zerind', 'bucharest', 374)

	path = aStar(grafo, 'lugoj', 'bucharest')


	for x in path:
		print '-> ', x,