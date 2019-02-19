from faker import Faker
import random
import json
import sys


def minimize(f1="output.json", f2="output-minimized.json"):
    f = open(f1, 'r')
    data = json.loads(f.read())
    f.close()

    output = {x: data[x][:10000] for x in data}

    with open(f2, 'w') as f_out:
        json.dump(output, f_out)


if __name__ == "__main__":
    if(len(sys.argv) > 2):
        minimize(sys.argv[1], sys.argv[2])
    else:
        minimize()
