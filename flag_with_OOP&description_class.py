class CheckN:
    class ArgumentError(Exception):
        pass

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if type(value) != int:
            raise self.ArgumentError("type must be int")
        if value % 2:
            raise self.ArgumentError('digit must be even')
        instance.__dict__[self.name] = value


class BuildFlag:
    N = CheckN()

    def __init__(self, N):
        self.N = N
        self.half_rows = self.N
        self.half_columns = 3 * self.N // 2
        self.start_row_draw_circle = N // 2
        self.end_row_draw_circle = N

    def build_quarter_field(self):
        self.quarter_field = []
        for row in range(self.half_rows):
            self.quarter_field.append([" " for i in range(self.half_columns)])

    def draw_border_quarter_circle(self):
        rows_for_draw = range(
            self.start_row_draw_circle,
            self.end_row_draw_circle)
        for index, row in enumerate(rows_for_draw, 1):
            self.quarter_field[row][self.half_columns - index] = '*'

    def pour_angle_in_quarter_circle(self):
        rows_for_pour = range(
            self.start_row_draw_circle + 1,
            self.end_row_draw_circle)
        for index, row in enumerate(rows_for_pour, 1):
            for column in range(self.half_columns - index, self.half_columns):
                self.quarter_field[row][column] = 'O'

    def add_quarter_border_field(self):
        for row in self.quarter_field:
            row.insert(0, '#')
        border = ['#' for i in range(self.half_columns + 1)]
        self.quarter_field.insert(0, border)

    def build_flag_by_quarter_field(self):
        for row in self.quarter_field:
            row.extend(row[::-1])
        self.quarter_field.extend(self.quarter_field[::-1])
        for index in range(self.half_rows * 2 + 2):
            self.quarter_field[index] = "".join(self.quarter_field[index])
        self.flag = "\n".join(self.quarter_field)
        self.quarter_field.clear()


def flag(N):
    factory = BuildFlag(N)
    factory.build_quarter_field()
    factory.draw_border_quarter_circle()
    factory.pour_angle_in_quarter_circle()
    factory.add_quarter_border_field()
    factory.build_flag_by_quarter_field()
    return factory.flag


if __name__ == '__main__':
    print(flag(2))
    print(flag(4))
    print(flag(6))
