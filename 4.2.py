import xmltodict
import yaml

fileout=open("Лабораторная №4.2.yaml","w")
with open("Laboratornaya №4.1.xml", encoding="utf-8") as f:
    doc = xmltodict.parse(f.read())
print(doc)
fileout.write(yaml.dump(doc, allow_unicode=True))
fileout.close()
