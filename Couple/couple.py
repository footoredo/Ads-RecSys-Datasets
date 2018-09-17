#!/usr/bin/python3
#
#   generate special data that has strong feature combinations.
#

import random


num_fc = 100
size_data = 10000
lens_fc = [ 3, 3, 3, 3, 3, 4, 4, 4, 5,]
fields = [4] * 20 + [5] * 5 + [6] * 5 + [10, 20, 30]

all_fc = []
all_data = []
all_targets = []
all_tags = []
fid = []


#
#   generate feature combinations
#
def gen_fc() :
    id_clock = 0
    for l in fields :
        cur = [0]
        for j in range(l) :
            id_clock = id_clock + 1
            cur.append(id_clock)
        fid.append(cur)
    for i in range(num_fc) :
        length = random.choice(lens_fc)
        sub_fields = random.sample(range(len(fields)), length)
        sorted(sub_fields)
        fc = dict()
        for f in sub_fields :
            fc[f] = random.randint(1, fields[f])
        all_fc.append(fc)
    return all_fc

def gen_data() :
    while len(all_data) < size_data :
        fc_id = random.randint(0, len(all_fc) - 1)
        fc = all_fc[fc_id]

        data = dict()
        for i in range(len(fields)) :
            if i in fc :
                data[i] = fc[i]
            else :
                data[i] = random.randint(1, fields[i])
        all_data.append(data)
        all_tags.append((fc_id, -1))

        for (p,v) in fc.items() :
            data = dict()
            for i in range(len(fields)) :
                if i in fc and i != p :
                    data[i] = fc[i]
                else :
                    data[i] = random.randint(1, fields[i])
                    if i in fc and i == p :
                        while data[i] == fc[i] :
                            data[i] = random.randint(1, fields[i])
            all_data.append(data)
            all_tags.append((fc_id, fid[p][v]))


def eval_targets() :
    for data in all_data :
        ok = False
        for fc in all_fc :
            subok = True
            for (p,v) in fc.items() :
                if data[p] != v :
                    subok = False
                    break
            if subok :
                ok = True
                break
        all_targets.append(ok)

def output() :
#    print("Categoris:")
#    for i in range(len(fields)) :
 #       for j in range(1,fields[i]+1) :
#            print("%2d " % fid[i][j], end="")
 #   print()
#    for i in range(len(fields)) :
 #       for j in range(fields[i]) :
 #           print("%2d " % (i + 1), end="")
 #   print()
#    print("Key Features:")
#    for fc in all_fc :
#        for (p,v) in sorted(fc.items()) :
#            print("%d " % fid[p][v], end="")
#        print()
    for i in range(len(all_data)) :
        print(1 if all_targets[i] else 0, end=" ")
        data = all_data[i]
        s = 0
        for j in range(len(fields)) :
            print("%s" % (str(s + data[j] - 1) + ":1 "), end="")
            s = s + fields[j]
#        print("%d %d" % (all_tags[i][0], all_tags[i][1]), end="")
        print()

def main() :
    gen_fc()
    gen_data()
    eval_targets()
    output()

if __name__ == "__main__" : 
    main()
