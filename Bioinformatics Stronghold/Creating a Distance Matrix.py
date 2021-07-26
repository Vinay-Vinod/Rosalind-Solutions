def cap(data):
    # Create DNA Strings
    s = []
    ros_loc = []
    data = data.split()
    
    i = 0
    while i < len(data) - 1:
        if ">" in data[i]:
            ros_loc.append(i)
        i += 1

    i = 0
    while i < len(ros_loc) - 1:
        temp_list = data[ros_loc[i] + 1 : ros_loc[i + 1]]
        temp_string = ""
        for letter in temp_list:
            temp_string += letter
        s.append(temp_string)
        i += 1

    temp_list = data[ros_loc[i] + 1:]
    temp_string = ""
    for letter in temp_list:
        temp_string += letter
    s.append(temp_string)
    
    return s

data = '''
>Rosalind_9499
TTTCCATTTA
>Rosalind_0942
GATTCATTTC
>Rosalind_6568
TTTCCATTTT
>Rosalind_1833
GTTCCATTTA
'''

data = cap(data)

length = len(data[0])
for i in data:
    dis = []
    for j in data:
        ham = 0
        for x, y in zip(i, j):
            if x !=y:
                ham += 1
        dis.append(str.format('{0:.5f}', ham / length))

    print(*dis, sep= ' ')
