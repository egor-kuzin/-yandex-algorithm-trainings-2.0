def check_input(line):
    try:
        output = set(list(map(int, line.split())))
    except:
        output = line
    return output


def find_answer(file, number):
    beatrice = set()
    august = ''
    main_set = set([_ for _ in range(1, number)])
    for line in file:
        output = check_input(line.strip())
        if output == 'HELP':
            break
        if isinstance(output, set):
            beatrice = output
        if isinstance(output, str):
            august = output
        if august:
            if august == 'YES':
                main_set = main_set.intersection(beatrice)
                august = ''
            elif august == 'NO':
                for _ in beatrice:
                    main_set.discard(_)
                august = ''
    return main_set


with open('input.txt', 'r') as fin:
    nums = int(fin.readline().strip())
    ans = find_answer(fin, nums)
    print(*sorted(ans))
