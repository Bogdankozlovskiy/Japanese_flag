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
        self._half_rows = self.N
        self._half_columns = 3 * self.N // 2
        self._start_row_draw_circle = N // 2
        self._end_row_draw_circle = N

    def _build_quarter_field(self):
        simple_row = [" " for i in range(self._half_columns)]
        self._quarter_field = [simple_row[::] for i in range(self._half_rows)]

    def _rows_for_draw(self):
        rows = range(
            self._start_row_draw_circle,
            self._end_row_draw_circle)
        return rows

    def _column_for_draw(self, index):
        return self._half_columns - index

    def _draw_border_quarter_circle(self):
        for index, row in enumerate(self._rows_for_draw(), 1):
            self._quarter_field[row][self._column_for_draw(index)] = '*'

    def _rows_for_pour(self):
        rows = range(
            self._start_row_draw_circle + 1,
            self._end_row_draw_circle)
        return rows

    def _columns_for_pour(self, index):
        columns = range(
            self._half_columns - index,
            self._half_columns)
        return columns

    def _pour_angle_in_quarter_circle(self):
        for index, row in enumerate(self._rows_for_pour(), 1):
            for column in self._columns_for_pour(index):
                self._quarter_field[row][column] = 'O'

    def _add_quarter_border_field(self):
        for row in self._quarter_field:
            row.insert(0, '#')
        border = ['#' for i in range(self._half_columns + 1)]
        self._quarter_field.insert(0, border)

    def _build_flag_by_quarter_field(self):
        for row in self._quarter_field:
            row.extend(row[::-1])
        self._quarter_field.extend(self._quarter_field[::-1])
        for index in range(self._half_rows * 2 + 2):
            self._quarter_field[index] = "".join(self._quarter_field[index])
        self.flag = "\n".join(self._quarter_field)
        self._quarter_field.clear()

    def run(self):
        self._build_quarter_field()
        self._draw_border_quarter_circle()
        self._pour_angle_in_quarter_circle()
        self._add_quarter_border_field()
        self._build_flag_by_quarter_field()


def flag(N):
    factory = BuildFlag(N)
    factory.run()
    return factory.flag


if __name__ == '__main__':
    print(flag(2))
    print(flag(4))
    print(flag(6))
