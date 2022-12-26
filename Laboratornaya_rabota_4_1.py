filein = open('Laboratornaya №4.1.xml', "r", encoding="utf-8")
fileout = open("Лабораторная №4.1.yaml", "w")
t = 0
filein.readline()
for line in filein:
    if line.count("<") == 1:
        if line.count("/") == 0:
            type = ''
            for i in range(len(line)):
                if line[i] == "<":
                    type = line[i]
                elif type != '':
                    if line[i] == ">":
                        i = len(line)
                        type += ":"
                    else:
                        type += line[i]
            fileout.write(" " * t + type[1:])
            t += 1
        else:
            t -= 1
    else:
        type = ''
        word = ''
        for i in range(0, len(line) - 1):
            if type == '' and line[i] == '<':
                type = line[i]
            elif type != '' and word == '' and line[i] != ">":
                type += line[i]
                if line[i + 1] == ">":
                    type += ":"
            elif line[i + 1] != "<" and type != '':
                word += line[i + 1]
            elif type != '':
                break
        fileout.write(' ' * t + type[1:] + ' "' + word[1:] + '"' + '\n')
fileout.close()
