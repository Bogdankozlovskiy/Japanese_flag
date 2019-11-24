def check_N(N):
    class ArgumentError(Exception):
        pass
    if type(N) != int:
        raise ArgumentError("type must be int")
    if N % 2:
        raise ArgumentError('digit must be even')


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
    for index, row in enumerate(range(start_row, end_row), 1):
        quarter_field[row][columns - index] = '*'


def pour_angle_in_quarter_circle(quarter_field):
    N = len(quarter_field)
    end_row = N
    start_row = N // 2
    columns = 3 * N // 2
    for index, row in enumerate(range(start_row + 1, end_row), 1):
        for column in range(columns - index, columns):
            quarter_field[row][column] = 'O'


def add_quarter_border_field(quarter_field):
    for row in quarter_field:
        row.insert(0, '#')
    quarter_field.insert(0, ['#' for i in range(len(quarter_field[0]))])


def builf_flag_by_quarter_field(quarter):
    for row in quarter:
        row.extend(row[::-1])
    quarter.extend(quarter[::-1])
    for index in range(len(quarter)):
        quarter[index] = "".join(quarter[index])
    final_flag = "\n".join(quarter)
    quarter.clear()
    quarter.append(final_flag)


def flag(N):
    check_N(N)
    quarter_field = build_quarter_field(N)
    draw_border_quarter_circle(quarter_field)
    pour_angle_in_quarter_circle(quarter_field)
    add_quarter_border_field(quarter_field)
    builf_flag_by_quarter_field(quarter_field)
    return quarter_field[0]


if __name__ == '__main__':
    print(flag(2))
    print(flag(4))
    print(flag(6))
