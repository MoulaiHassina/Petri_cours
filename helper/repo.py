import re

f1 = open("../latex","r")
f2=open("../latexr.txt","w+")


for line in f1:
    prog = re.compile("(.*\\\includegraphics(.*?){(.*)?}(.*|.+))")
    result = prog.match(line)

    if str(result) != str(None):
        if result.group(3).__contains__("page") :
         f2.write("{\\includegraphics"+str(result.group(2)+"{images/"+str(result.group(3))+"}\\\\"))
        else :
            f2.write("\\includegraphics" + str(result.group(2) + "{images/" + str(result.group(3)) + "}\\\\"))
        print(line)
    else: f2.write(line)