from bfs import BFS
from graph import Graph


def main():
    # TODO clear example after finish the final code of the game.
    graph = Graph(74)

    v0 = graph.add_vertex(0)
    v1 = graph.add_vertex(1)
    v2 = graph.add_vertex(2)
    v3 = graph.add_vertex(3)
    v4 = graph.add_vertex(4)
    v5 = graph.add_vertex(5)
    v6 = graph.add_vertex(6)
    v7 = graph.add_vertex(7)
    v8 = graph.add_vertex(8)
    v9 = graph.add_vertex(9)
    v10 = graph.add_vertex(10)
    v11 = graph.add_vertex(11)
    v12 = graph.add_vertex(12)
    v13 = graph.add_vertex(13)
    v14 = graph.add_vertex(14)
    v15 = graph.add_vertex(15)
    v16 = graph.add_vertex(16)
    v17 = graph.add_vertex(17)
    v18 = graph.add_vertex(18)
    v19 = graph.add_vertex(19)
    v20 = graph.add_vertex(20)
    v21 = graph.add_vertex(21)
    v22 = graph.add_vertex(22)
    v23 = graph.add_vertex(23)
    v24 = graph.add_vertex(24)
    v25 = graph.add_vertex(25)
    v26 = graph.add_vertex(26)
    v27 = graph.add_vertex(27)
    v28 = graph.add_vertex(28)
    v29 = graph.add_vertex(29)
    v30 = graph.add_vertex(30)
    v31 = graph.add_vertex(31)
    v32 = graph.add_vertex(32)
    v33 = graph.add_vertex(33)
    v34 = graph.add_vertex(34)
    v35 = graph.add_vertex(35)
    v36 = graph.add_vertex(36)
    v37 = graph.add_vertex(37)
    v38 = graph.add_vertex(38)
    v39 = graph.add_vertex(39)
    v40 = graph.add_vertex(40)
    v41 = graph.add_vertex(41)
    v42 = graph.add_vertex(42)
    v43 = graph.add_vertex(43)
    v44 = graph.add_vertex(44)
    v45 = graph.add_vertex(45)
    v46 = graph.add_vertex(46)
    v47 = graph.add_vertex(47)
    v48 = graph.add_vertex(48)
    v49 = graph.add_vertex(49)
    v50 = graph.add_vertex(50)
    v51 = graph.add_vertex(51)
    v52 = graph.add_vertex(52)
    v53 = graph.add_vertex(53)
    v54 = graph.add_vertex(54)
    v55 = graph.add_vertex(55)
    v56 = graph.add_vertex(56)
    v57 = graph.add_vertex(57)
    v58 = graph.add_vertex(58)
    v59 = graph.add_vertex(59)
    v60 = graph.add_vertex(60)
    v61 = graph.add_vertex(61)
    v62 = graph.add_vertex(62)
    v63 = graph.add_vertex(63)
    v64 = graph.add_vertex(64)
    v65 = graph.add_vertex(65)
    v66 = graph.add_vertex(66)
    v67 = graph.add_vertex(67)
    v68 = graph.add_vertex(68)
    v69 = graph.add_vertex(69)
    v70 = graph.add_vertex(70)
    v71 = graph.add_vertex(71)
    v72 = graph.add_vertex(72)
    v73 = graph.add_vertex(73)

    L = "LEFT"
    R = "RIGHT"
    U = "UP"
    D = "DOWN"

    graph.add_edge(v0, v1, R)
    graph.add_edge(v0, v2, L)
    graph.add_edge(v0, v3, U)
    graph.add_edge(v1, v0, L)
    graph.add_edge(v1, v4, R)
    graph.add_edge(v1, v23, D)
    graph.add_edge(v2, v0, R)
    graph.add_edge(v2, v5, L)
    graph.add_edge(v2, v28, U)
    graph.add_edge(v3, v0, D)
    graph.add_edge(v3, v6, R)
    graph.add_edge(v4, v1, L)
    graph.add_edge(v4, v9, U)
    graph.add_edge(v4, v7, D)
    graph.add_edge(v5, v2, R)
    graph.add_edge(v5, v8, L)
    graph.add_edge(v5, v29, D)
    graph.add_edge(v6, v3, L)
    graph.add_edge(v6, v9, R)
    graph.add_edge(v6, v62, U)
    graph.add_edge(v7, v4, U)
    graph.add_edge(v7, v10, R)
    graph.add_edge(v8, v5, R)
    graph.add_edge(v8, v11, D)
    graph.add_edge(v8, v24, U)
    graph.add_edge(v9, v4, D)
    graph.add_edge(v9, v6, L)
    graph.add_edge(v9, v12, R)
    graph.add_edge(v9, v31, U)
    graph.add_edge(v10, v7, L)
    graph.add_edge(v10, v13, R)
    graph.add_edge(v10, v18, U)
    graph.add_edge(v11, v8, U)
    graph.add_edge(v11, v14, L)
    graph.add_edge(v12, v9, L)
    graph.add_edge(v12, v15, D)
    graph.add_edge(v13, v10, L)
    graph.add_edge(v13, v16, D)
    graph.add_edge(v14, v11, R)
    graph.add_edge(v14, v17, U)
    graph.add_edge(v14, v32, L)
    graph.add_edge(v15, v12, U)
    graph.add_edge(v15, v18, R)
    graph.add_edge(v16, v13, U)
    graph.add_edge(v16, v19, L)
    graph.add_edge(v17, v14, D)
    graph.add_edge(v17, v20, L)
    graph.add_edge(v18, v10, D)
    graph.add_edge(v18, v15, R)
    graph.add_edge(v19, v16, R)
    graph.add_edge(v19, v21, U)
    graph.add_edge(v19, v25, L)
    graph.add_edge(v20, v17, R)
    graph.add_edge(v20, v22, U)
    graph.add_edge(v21, v19, D)
    graph.add_edge(v21, v23, R)
    graph.add_edge(v21, v20, D)
    graph.add_edge(v22, v20, D)
    graph.add_edge(v22, v24, R)
    graph.add_edge(v23, v1, U)
    graph.add_edge(v23, v21, L)
    graph.add_edge(v24, v8, D)
    graph.add_edge(v24, v22, L)
    graph.add_edge(v24, v26, R)
    graph.add_edge(v24, v34, U)
    graph.add_edge(v25, v19, R)
    graph.add_edge(v25, v27, U)
    graph.add_edge(v25, v30, L)
    graph.add_edge(v26, v24, L)
    graph.add_edge(v26, v28, R)
    graph.add_edge(v26, v63, U)
    graph.add_edge(v27, v25, D)
    graph.add_edge(v27, v29, L)
    graph.add_edge(v28, v2, D)
    graph.add_edge(v28, v26, L)
    graph.add_edge(v29, v5, U)
    graph.add_edge(v29, v27, R)
    graph.add_edge(v30, v25, R)
    graph.add_edge(v30, v32, U)
    graph.add_edge(v31, v9, D)
    graph.add_edge(v31, v33, U)
    graph.add_edge(v31, v60, L)
    graph.add_edge(v31, v64, R)
    graph.add_edge(v32, v14, R)
    graph.add_edge(v32, v30, D)
    graph.add_edge(v33, v31, D)
    graph.add_edge(v33, v39, U)
    graph.add_edge(v33, v35, R)
    graph.add_edge(v34, v24, D)
    graph.add_edge(v34, v36, U)
    graph.add_edge(v34, v61, R)
    graph.add_edge(v34, v65, L)
    graph.add_edge(v35, v33, L)
    graph.add_edge(v35, v37, U)
    graph.add_edge(v36, v34, D)
    graph.add_edge(v36, v38, L)
    graph.add_edge(v36, v42, U)
    graph.add_edge(v37, v35, D)
    graph.add_edge(v37, v39, L)
    graph.add_edge(v37, v43, U)
    graph.add_edge(v38, v36, R)
    graph.add_edge(v38, v40, U)
    graph.add_edge(v39, v33, D)
    graph.add_edge(v39, v37, R)
    graph.add_edge(v39, v41, U)
    graph.add_edge(v39, v50, L)
    graph.add_edge(v40, v38, D)
    graph.add_edge(v40, v42, R)
    graph.add_edge(v40, v46, U)
    graph.add_edge(v41, v39, D)
    graph.add_edge(v41, v43, R)
    graph.add_edge(v41, v45, L)
    graph.add_edge(v42, v36, D)
    graph.add_edge(v42, v40, L)
    graph.add_edge(v42, v44, U)
    graph.add_edge(v42, v51, R)
    graph.add_edge(v43, v37, D)
    graph.add_edge(v43, v41, L)
    graph.add_edge(v44, v42, D)
    graph.add_edge(v44, v46, L)
    graph.add_edge(v44, v48, R)
    graph.add_edge(v45, v41, R)
    graph.add_edge(v45, v47, D)
    graph.add_edge(v46, v40, D)
    graph.add_edge(v46, v44, R)
    graph.add_edge(v47, v45, U)
    graph.add_edge(v47, v49, L)
    graph.add_edge(v47, v50, R)
    graph.add_edge(v48, v44, L)
    graph.add_edge(v48, v49, D)
    graph.add_edge(v49, v47, R)
    graph.add_edge(v49, v48, U)
    graph.add_edge(v49, v51, R)
    graph.add_edge(v50, v39, R)
    graph.add_edge(v50, v47, L)
    graph.add_edge(v50, v52, D)
    graph.add_edge(v51, v42, L)
    graph.add_edge(v51, v49, R)
    graph.add_edge(v51, v53, D)
    graph.add_edge(v52, v50, U)
    graph.add_edge(v52, v54, L)
    graph.add_edge(v53, v51, U)
    graph.add_edge(v53, v55, R)
    graph.add_edge(v54, v52, R)
    graph.add_edge(v54, v56, D)
    graph.add_edge(v55, v53, L)
    graph.add_edge(v55, v57, D)
    graph.add_edge(v56, v54, U)
    graph.add_edge(v56, v58, R)
    graph.add_edge(v56, v66, L)
    graph.add_edge(v57, v55, U)
    graph.add_edge(v57, v59, R)
    graph.add_edge(v57, v66, L)
    graph.add_edge(v58, v56, L)
    graph.add_edge(v58, v60, D)
    graph.add_edge(v59, v57, R)
    graph.add_edge(v59, v61, D)
    graph.add_edge(v60, v31, R)
    graph.add_edge(v60, v62, D)
    graph.add_edge(v61, v34, L)
    graph.add_edge(v61, v63, D)
    graph.add_edge(v62, v6, D)
    graph.add_edge(v62, v60, U)
    graph.add_edge(v62, v63, L)
    graph.add_edge(v63, v26, D)
    graph.add_edge(v63, v61, U)
    graph.add_edge(v63, v62, R)
    graph.add_edge(v64, v31, L)
    graph.add_edge(v64, v65, L)
    graph.add_edge(v65, v34, R)
    graph.add_edge(v65, v64, L)
    graph.add_edge(v66, v56, R)
    graph.add_edge(v66, v57, L)
    graph.add_edge(v66, v67, D)
    graph.add_edge(v67, v66, U)
    graph.add_edge(v67, v70, R)
    graph.add_edge(v67, v71, L)
    graph.add_edge(v68, v70, D)
    graph.add_edge(v69, v71, D)
    graph.add_edge(v70, v67, L)
    graph.add_edge(v70, v68, U)
    graph.add_edge(v70, v72, D)
    graph.add_edge(v71, v67, R)
    graph.add_edge(v71, v69, U)
    graph.add_edge(v71, v73, D)
    graph.add_edge(v72, v70, U)
    graph.add_edge(v73, v71, U)

    graph.print_vertices()

    def find_path(graph, start, end, path=[], directions = []):
        path = path + [start]
        if start == end:
            path = directions
            return path
        if not graph.has_key(start):
            return None
        for node in graph.get_vertex(start):
            if node[0].ID not in path:
                directions.append(node[1])
                newpath = find_path(graph, node[0].ID, end, path, directions)
                if newpath:
                    return newpath
        return None

    route = BFS(graph, v0)
    vertex_list = []
    for vertex in route:
        vertex_list.append(vertex.ID)
        print(f"{vertex.ID}")

    def bfs_path(vertex_list):
        final_directions = []
        for i in range(len(vertex_list)):
            if i == len(vertex_list) - 1:
                return final_directions
            else:
                try:
                    directions = find_path(graph, vertex_list[i], vertex_list[i+1])
                    print(vertex_list[i])
                    print(vertex_list[i+1])
                    print(directions)
                    final_directions.append(directions)
                except EOFError as error:
                    return error

    print(vertex_list)
    print(vertex_list[0])
    print(vertex_list[-1])
    print(find_path(graph, vertex_list[0], vertex_list[-1]))

main()