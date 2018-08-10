import re
file = open("latextry.txt", "r")
FileF= open ("latexresult.txt","w+")

for line in file:
     prog= re.compile("(^|\b|\(|\t|<|>|=|,|:|)(t|p|M|T|P)(( )[0-9kji]|[0-9])( |\b|,|<|>|=|\.|$|)")
     result=prog.findall(line)
   #  print(line)
     if str(result) != str(None):
        # FileF.write(result.group(0))
         for element in result:
            line =line.replace(element[1]+element[2]+element[3],"$" + element[1]+"_{"+ element[2]+"}$")
            line=line.replace("~σ","$\overrightarrow{\sigma}$")

            print (str(element))
     FileF.write(line)
import re
f1= open("matrix.txt","r")
f2=open("latexr.txt","w+")


for line in f1:
    prog = re.compile("(\\\includegraphics(|<.*>)[.*]{.*})")
    result = prog.match(line)

    if str(result) != str(None):
        print (line)






FileF.close()
file.close()