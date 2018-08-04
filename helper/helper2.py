import re
file = open("latextry.txt", "r")
FileF= open ("latexresult.txt","w+")

i=0

for line in file:
     prog= re.compile("(^|\b|\(|\t|<|>|=|,|:|)(t|p|M)( )([0-9kji])( |\b|,|<|>|=|\.|$|)")
     result=prog.findall(line)
   #  print(line)
     if str(result) != str(None):
        # FileF.write(result.group(0))
         for element in result:
            line =line.replace(element[1]+element[2]+element[3],"$" + element[1]+"_{"+ element[3]+"}$")
            print (str(element))
     FileF.write(line)







FileF.close()
file.close()