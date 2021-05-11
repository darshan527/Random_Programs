l = []
with open('fil.txt', 'r') as fl:
    sl = fl.readlines()
    # while fl.:
    #     n = fl.readline()
    #     s = fl.readline()
    #     l.append((n, s))
# for i in range(0, len(sl), step=2):
#     print(i, sl[i])
for i in range(len(sl)):
    print(i, sl[i])