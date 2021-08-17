def get_sum_str(file):
    lines = 0
    with open(file, 'r', encoding='utf8') as files:
        for line in files:
            lines += 1
    return lines

def sort_files():
    f_lng_dict = {'1.txt':get_sum_str('1.txt'), '2.txt':get_sum_str('2.txt'),'3.txt':get_sum_str('3.txt'),}
    sorted_values = sorted(f_lng_dict.values())
    sorted_dict = {}
    for i in sorted_values:
        for k in f_lng_dict.keys():
            if f_lng_dict[k] == i:
                sorted_dict[k] = f_lng_dict[k]
                break
    return sorted_dict

len_sorted_files = len(sort_files())
with open('dz7_task3_result.txt', 'w', encoding='utf8') as f:
    for key in sort_files().keys():
        # print(key)
        with open(key, 'r', encoding='utf8') as file:
            p = key + '\n' + str(get_sum_str(key)) + '\n' + file.read() + '\n'
        f.write(p)



