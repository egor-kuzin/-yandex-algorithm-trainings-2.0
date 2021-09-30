def check_input(line):
    try:
        output = int(line)
    except:
        output = line
    return output


def recurs(list, element):
    if element[1] == 0:
        return element[2]
    else:
        b1 = element[1]
        b2 = list[b1 - 1]
        return recurs(list, b2)


lines_list = []
messages_nums = []


with open('input.txt', 'r', encoding='utf-8') as fin:
    for _ in fin:
        lines_list.append(_.strip())
fin.close()
del fin


j = 0
for _ in range(1, len(lines_list)):
    inputs = check_input(lines_list[_])
    if isinstance(inputs, int) and inputs == 0:
        j += 1
        messages_nums.append([j, inputs, _+3])   # номер сообщения, id сообщения, номер строки в файле
    if isinstance(inputs, int) and inputs != 0:
        j += 1
        messages_nums.append([j, inputs, _+2])   # номер сообщения, id сообщения, номер строки в файле
del _
del j
del inputs


ans_dict = {}

for _ in range(len(messages_nums)-1, -1, -1):
    topic_num = recurs(messages_nums, messages_nums[_])
    topic_name = lines_list[topic_num-2]
    if topic_name in ans_dict:
        ans_dict[topic_name][0] += 1
    else:
        ans_dict[topic_name] = [1, topic_num]
del _
del topic_name
del topic_num
del lines_list
del messages_nums

m = max([ans_dict[_][0] for _ in ans_dict])
ans_dict = dict({_: ans_dict[_] for _ in ans_dict if ans_dict[_][0] == m})

print(min(ans_dict, key=lambda k: ans_dict[k][1]))
