import json
import sys

if __name__ == "__main__":
    filename = "output.json"
    if(len(sys.argv) > 1):
        filename = sys.argv[1]

    f = open(filename)
    data = json.loads(f.read())
    f.close()
    
    print(data)