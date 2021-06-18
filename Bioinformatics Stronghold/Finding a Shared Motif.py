#Search can be slow for big DNA strings
def strip(data):
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

    return s


def find_sub(data):
    # Common alogrithm for searching
    substrs = lambda x: {
        x[i : i + j] for i in range(len(x)) for j in range(len(x) - i + 1)
    }
    s = substrs(data[0])
    for val in data[1:]:
        s.intersection_update(substrs(val))
    return max(s, key=len)


s = """
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""

print(find_sub(strip(s)))
