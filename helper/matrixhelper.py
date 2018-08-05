def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


f = open("matrix.txt", "r")
w = open("matrixr.txt", "w")
j = 0

for line in f:
    matrix = line.split(",")
    line_matrix = ""

    for element in matrix:

        j = 0;

        for i in element:

            if j == len(element) - 1:

                line_matrix = line_matrix + i + "\\\\"


            else:
                if j < len(element) - 1:
                    if i == "-":
                        line_matrix = line_matrix + i
                    else:
                        line_matrix = line_matrix + i + "&"

            # print(j,len(element))
            j = j + 1
    w.write("\( \\begin{pmatrix}\n" + rreplace(line_matrix, "&\n\\\\", "\\\\", 1) + "\n\end{pmatrix}\)\n")
    #print(rreplace(line_matrix, "&\n\\\\", "\\\\", 1))

    #nb = line_matrix[::-1].index("&")


   # print(line_matrix)

w.close()
f.close()
