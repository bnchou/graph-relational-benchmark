from subprocess import call
import json

def insert(adapter):
    filename = "backend/api/db/out/output.txt"
    call('run_{}.sh'.format(adapter), cwd='backend/api/db', shell=True)

    f = open(filename)
    data = json.loads(f.read())
    f.close()
    return data
