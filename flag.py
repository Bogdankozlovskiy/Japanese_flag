def check_N(N):
    if type(N) != int:
        raise AttributeError("type must be int")
    if N % 2:
        raise AttributeError('digit must be even')
    if N == 0:
        raise AttributeError('N have to more then zero')


def build_quarter_field(N):
    rows = N
    columns = 3 * N // 2
    quarter_field = [[" " for i in range(columns)] for j in range(rows)]
    return quarter_field


def draw_border_quarter_circle(quarter_field):
    N = len(quarter_field)
    end_row = N
    start_row = N // 2
    columns = 3 * N // 2
    out_field = quarter_field.copy()
    for index, row in enumerate(range(start_row, end_row), 1):
        out_field[row][columns - index] = '*'
    return out_field


def pour_angle_in_quarter_circle(quarter_field):
    N = len(quarter_field)
    end_row = N
    start_row = N // 2
    columns = 3 * N // 2
    out_field = quarter_field.copy()
    for index, row in enumerate(range(start_row + 1, end_row), 1):
        for column in range(columns - index, columns):
            out_field[row][column] = 'O'
    return out_field


def add_quarter_border_field(quarter_field):
    out_field = quarter_field.copy()
    for row in out_field:
        row.insert(0, '#')
    out_field.insert(0, ['#' for i in range(len(out_field[0]))])
    return out_field


def build_flag_by_quarter_field(quarter_field):
    out_field = quarter_field.copy()
    for row in out_field:
        row.extend(row[::-1])
    out_field.extend(out_field[::-1])
    for index in range(len(out_field)):
        out_field[index] = "".join(out_field[index])
    final_flag = "\n".join(out_field)
    return final_flag


def flag(N):
    check_N(N)
    quarter_field = build_quarter_field(N)
    quarter_field = draw_border_quarter_circle(quarter_field)
    quarter_field = pour_angle_in_quarter_circle(quarter_field)
    quarter_field = add_quarter_border_field(quarter_field)
    quarter_field = build_flag_by_quarter_field(quarter_field)
    return quarter_field


if __name__ == '__main__':
    print(flag(2))
    print(flag(4))
    print(flag(6))
