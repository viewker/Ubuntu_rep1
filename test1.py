import itertools

num = int(raw_input())

for i in range(num):
    ra = raw_input().split()
    sta = int(ra[0])
    ending = int(ra[1])
    alp2 = []
    alp = raw_input().split()
    for j in range(26):
        alp[j] = int(alp[j])
        if alp[j] == 1:
            temp = (65 + j)
            alp2.append(temp)
    num_alp = len(alp2)
    max_alp = alp2[num_alp-1]
    min_alp = alp2[0]
    if sta % max_alp == 0 :
        min_num = sta/max_alp
    else:
        min_num = int(sta/max_alp) + 1
        max_num = ending/min_alp
    count = 0
    for j in range(num_alp):
        for k in combinations_with_replacement(alp2,j):
            if sta <= sum(k) <= ending:
                count += 1
        print "Case #"+str(i+1)+":"+str(count)
