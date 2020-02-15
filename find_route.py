import sys
dist = []
h_dist = []
fringe = []
result = 0
nc = 0
ds = 0
dsp = 0
visited_node = []

class node:
    def __init__(self,name,dist,parent):
        self.name = name
        self.dist = dist

        if parent:
            self.total = int(dist) + int(parent.total)
            # print("cumulative cost if not empty : ", self.cumulative_cost)
        else:
            self.total = int(dist) # removing zero from here
            # print("cumulative cost if empty : ", self.cumulative_cost)

        if len(sys.argv) == 5:
            for lists in h_dist:
                if self.name == lists[0]:
                    self.total_cost = self.total + int(lists[1])
                    break
        self.parent = parent

def usc(src, destini,node_object):
    global ds
    global dsp
    global nc
    global visited_node
    fringe.append(node_object)
    nc += 1
#
#
    while(len(fringe) != 0 ):
        ds = ds + 1
        def end(destini):
            neighbour = fringe[0]
            if neighbour.name == destini:
                return neighbour
            else:
                return None

        end_city = end(destini)

        def fringe_fun(end_city):
            print("Nodes expanded : ", ds)
            print("Nodes generated : ", dsp)
            print("Max node in memory : ", nc)

                #todo : if there is no path to the goal node
            if end_city == "ZERO":
                print("distance : infinity")
                print("route: None")

            else:
                final = []
                distance_travelled = 0
                present = end_city

                while present.parent is not None:
                    parent = present.parent
                    final.append([parent.name, present.name, present.dist])
                    distance_travelled = distance_travelled + int(present.dist)
                    present = parent
                    final.reverse()
                    print("distance: ",distance_travelled,"KM")
                    print("route: ")
                    for i in final:
                        print(i[0] + " to " + i[1] + "," + i[2]+"KM")
        if end_city:
            fringe_fun(end_city)
            break
        else:
            neighbour = fringe.pop(0)
            if neighbour.name not in visited_node:
                for i in dist:
                    if i[0] == neighbour.name:
                        child = node(i[1] ,i[2],neighbour)
                        fringe.append(child)
                        dsp += 1

                    elif i[1] == neighbour.name:
                        child = node(i[0] ,i[2],neighbour)
                        fringe.append(child)
                        dsp += 1
                visited_node.append(neighbour.name)

            if len(fringe) > nc:
                nc = len(fringe)

            if (len(sys.argv) == 5):
                fringe.sort(key=lambda l: l.total_cost)
            else:
                fringe.sort(key=lambda l: l.total)
    if(len(fringe) == 0):
        fringe_fun("ZERO")


leng = len(sys.argv)
def read(inp):
    global dist
    file = open(inp, "r")
    for i in file:
        route = i.split()
        if route[0] != "END":
            dist.append(route)
        else:
            break

def hread(h_inp, heuristic):
    global h_dist
    h_file = open(heuristic, "r")
    for i in h_file:
        heu_lists = i.split(" ")
        if heu_lists[0] != "END":
            h_dist.append(heu_lists)
        else:
            break

if leng == 4:
    heuristic = None
    inp = sys.argv[1]
    src = sys.argv[2]
    destni = sys.argv[3]
    r = read(inp)
    node_object = node(src,0, None)
    usc(src, destni, node_object)

elif leng == 5:
    h_inp = sys.argv[1]
    h_src = sys.argv[2]
    h_destni = sys.argv[3]
    heuristic = sys.argv[4]
    hread(h_inp,heuristic)
    hr = read(h_inp)
    node_object = node(h_src,0, None)
    usc(h_src, h_destni, node_object)
