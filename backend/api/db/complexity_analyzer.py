import json
import sys

if __name__ == "__main__":
    adapter = "sql"
    f1 = "complexity.json"
    f2 = "input.json"
    f3 = "output.json"
    if(len(sys.argv) > 4):
        adapter = sys.argv[1]
        f1 = sys.argv[2]
        f2 = sys.argv[3]
        f3 = sys.argv[4]

    with open(f1, 'r') as f:
        complexity = json.loads(f.read())
    with open(f2, 'r') as f:
        data = json.loads(f.read())

    result = {}
    missing = []

    for key in complexity[adapter].keys():
        cost = complexity[adapter][key]

        if isinstance(cost, dict):
            for k, v in data[key].items():
                if k in cost:
                    result[key] = result.get(key, 0) + cost[k] * v
                else:
                    missing.append(k)
        else:
            result[key] = cost * sum(data[key].values())

    result["total"] = sum(result.values())

    print(result)
    print("missing: " + str(missing))
    with open(f3, 'w') as f_out:
        json.dump(result, f_out)
