import sys

def optimize2(lines):
    d = dict()
    lno = 0

    def unset_dict(d, line):
        for k in d.keys():
            for member in line.split():
                if member == k and type(d[k]) == list:
                    if( len(d[k]) > 1):
                        d[k] = d[k][:-1]
                    else:
                        d[k] = -1


    #print(lines)
    for line in lines:
        temp_list = line.split('=', 1)
        #print(d)
        #print(temp_list)

        if len(temp_list) > 1:
            if('[' in temp_list[0]):
                print(temp_list[0])
                #print(x[list(x).index('[') + 1: list(x).index(']')])
                x = temp_list[0]
                unset_dict(d, x[((list(x)).index('[')) + 1: ((list(x)).index(']'))])
            else:
                try:
                    d[temp_list[0].strip()].append(lno)
                except:
                    d[temp_list[0].strip()] = [lno]

            unset_dict(d, temp_list[1])

        else:
            unset_dict(d,line)

        lno += 1

    to_remove = []
    #print(d)
    for k in d.keys():
        if type(d[k]) == list:
            to_remove.append(d[k])

    to_remove = [item for sub in to_remove for item in sub]

    #print(to_remove)
    final_lines = []
    for i in range(len(lines)):
        #print(line)
        if i not in to_remove:
            final_lines.append(lines[i])
            #print(lines[i])

    return final_lines


with open(sys.argv[1], 'r') as f:
    lines2 = f.readlines()

lines = []
for i in range(len(lines2)):
    x = lines2[i].strip()
    if(x):
        lines.append(x)

new_lines = []
i = 1
while(1):
    print("Deadcode elimination : ", i)
    new_lines = optimize2(lines)
    #print(new_lines)
    if(len(lines) == len(new_lines)):
        break
    lines = new_lines[:]
    i += 1

print("\n\nAFTER DEADCODE ELIMINATTION\n\n")
for i in new_lines:
    print(i)
print("\n")
