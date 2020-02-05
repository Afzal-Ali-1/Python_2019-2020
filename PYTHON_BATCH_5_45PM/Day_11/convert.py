import excel2json
import json
file=open("gec.json","w")
data=excel2json.convert_from_file("gec modasa")
json.dump(data,file)
file.close()
