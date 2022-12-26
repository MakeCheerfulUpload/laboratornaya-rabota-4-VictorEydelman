import re
filein=open('Laboratornaya №4.1.xml',"r",encoding="utf-8")
fileout=open("Лабораторная №4.3.yaml","w")
t=0
filein.readline()
for line in filein:
    if line.count("<")==1:
        if line.count("/")==0:
            s=re.findall(r'[<][^>]*[>]',line)
            fileout.write(" "*t+s[0][1:-1]+'\n')
            t+=1
        else:
            t-=1
    else:
        s = re.findall(r'[<][^>]*[>]', line)
        n = re.findall(r'[>][\s][^<]*[<]',line)
        fileout.write(' '*t+s[0][1:-1]+":"+' "'+n[0][2:-1]+'"'+'\n')
fileout.close()