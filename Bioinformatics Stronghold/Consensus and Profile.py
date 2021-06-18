def consensus_and_profile(data):
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

    temp_list = data[ros_loc[i] + 1 :]
    temp_string = ""
    for letter in temp_list:
        temp_string += letter
    s.append(temp_string)

    # Create profile
    profile = {"A": [], "C": [], "G": [], "T": []}
    for col in range(len(s[0])):
        a_num, c_num, g_num, t_num = 0, 0, 0, 0
        for row in range(len(s)):
            if s[row][col] == "A":
                a_num += 1
            elif s[row][col] == "C":
                c_num += 1
            elif s[row][col] == "G":
                g_num += 1
            else:
                t_num += 1

        profile["A"].append(a_num)
        profile["C"].append(c_num)
        profile["G"].append(g_num)
        profile["T"].append(t_num)

    # Create consensus
    con = []
    for x in range(len(profile["A"])):
        big = 0
        big_key = ""
        for key in profile:
            if profile[key][x] > big:
                big = profile[key][x]
                big_key = key

        con.append(big_key)

    # Output
    print("".join(con))
    for key in profile:
        print("{}: {}".format(key, " ".join(map(str, profile[key]))))

data = """
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""
#Run function
consensus_and_profile(data)
