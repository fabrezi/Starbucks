#python doesn't have a graph model package
#work to build a dijsktra. graph model and then SSP implementation
class Graph(object):

    """"constructor"""
    def __init__(self, graph_dic):

        if graph_dic == None:
            graph_dic = {}
        self.__graph_dic = graph_dic

    #vertices
    def vertices(self):
        return list(self.__graph_dic.keys())

    #edges
    def edges(self):
        return self.__generate_edges()

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dic:
            for neighbour in self.__graph_dic[vertex]:
                if{neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
            return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dic:
            res += str(k) + " "
        res += "\n edges:"
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

if __name__ == "__main__":

    g = {"a" : ["b", "c" , "d"],
          "b" : ["c", "e"],
         "c" : ["d"],
          "d" : [],
          "e" : []
         }

    graph = Graph(g)

    print("vertices of graph:")
    print(graph.vertices())

    print("edges:")
    print(graph.edges())






