import re

file = open("sommaire.txt", "r")
FileF= open ("sommaire2.Txt","w+")
frame="	\\begin{frame}\n\\frametitle{}\n\end{frame}\n"

for line in file:
     prog= re.compile("^([0-9].([A-Z].+))")
     result=prog.match(line)
     if str(result) != str(None):
        FileF.write("\section{"+str(result.group(2).replace(".",""))+"}\n"+frame)



     prog = re.compile('^([0-9].[0-9].[0-9])(.*)')

     result = prog.match(line)
     if str(result) != str(None):
         FileF.write("\subsubsection{"+str(result.group(2).replace(".",""))+"}\n"+frame)
     prog2 =re.compile("(^[0-9].[0-9])(.[A-Z].*)")
     result2=prog2.match(line)
     if str(result2) != str(None):
         FileF.write("\subsection{"+str(result2.group(2).replace(".",""))+"}\n"+frame)





FileF.close()
file.close()