def get_data(user_input):
    problem = user_input.replace('+', ' + ') \
        .replace('-', ' - ') \
        .replace('*', ' * ') \
        .replace('/', ' / ') \
        .replace('(', '( ') \
        .replace(')', ' )') \
        .replace('i', 'j') \
        .split()
    problem_list = list()
    for el in problem:
        if 'j' in el:
            problem_list.append(complex(el))
        elif el.isdigit():
            problem_list.append(int(el))
        else:
            problem_list.append(el)
    return problem_list