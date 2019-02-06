# CSV build script command
# > py build_csv.py [INPUT_FILE] [OUTPUT_DIR]

import json
import sys

if __name__ == "__main__":
    f1 = "output.json"
    f2 = "."
    if(len(sys.argv) > 2):
        [f1, f2] = sys.argv[1:3]

    f = open(f1)
    data = json.loads(f.read())
    f.close()

    for key in data:
        queries, label = [], data[key]
        keys = list(label[0].keys())
        queries.append('~'.join(keys))
        for entry in label:
            queries.append('~'.join(str(v) for v in entry.values()).replace('\n', ', '))

        with open('{}/{}.csv'.format(f2, key), 'w') as f_out:
            f_out.write('\n'.join(queries))
