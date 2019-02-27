import re
import json
import sys

if __name__ == "__main__":
    query = "SELECT * FROM customers;"
    f2 = "output-complexity.json"
    if(len(sys.argv) > 2):
        f1 = sys.argv[1]
        f2 = sys.argv[2]

        f = open(f1, 'r')
        query = f.read()
        f.close()

    parser = re.compile(r"""
        ([0-9]+\.?[0-9]*|'.*')                  # 1. literals
        |(<-|->|[{}()[\],:;-])                  # 2. seperators
        |([A-Z]?[a-z]+\.?[a-z_]*|(?<=:)[A-Z_]+) # 3. identifiers
        |(=|>=|>|<=|<|!=|\*)                    # 4. operators
        |([A-Z]+)                               # 5. keywords
        |(\s+)                                  # 6. whitespace
        """, re.VERBOSE)

    groups = [
        "literals",
        "seperators",
        "identifiers",
        "operators",
        "keywords",
        "whitespace"
    ]

    result = {group: {} for group in groups}

    # bind a scanner to the target string
    scan = parser.scanner(query)

    # print all tokens
    while 1:
        m = scan.match()
        if not m:
            break
        group = result[groups[m.lastindex - 1]]
        token = m.group(m.lastindex)
        group[token] = group.get(token, 0) + 1

    # remove whitespace group from result dict
    del result["whitespace"]

    with open(f2, 'w') as f_out:
        json.dump(result, f_out)
