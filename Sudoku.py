import sys


class Sudoku:
    matrix = []
    wonder_map = {}
    wonder_num = [i for i in range(0, 10)]
    zero_count = 0
    attempt_error = False

    def collect_input(self):
        for i in range(9):
            print("Input line #%d:" % (i+1))
            input_str = sys.stdin.readline().strip()
            self.matrix.append(list(map(int, input_str.split(","))))

    def test(self):
        self.matrix = [
            [0, 0, 0, 0, 0, 0, 0, 0, 6],
            [0, 0, 7, 0, 9, 0, 5, 0, 3],
            [0, 3, 0, 4, 0, 0, 0, 0, 9],
            [4, 8, 3, 0, 0, 6, 0, 2, 0],
            [0, 0, 1, 0, 4, 0, 6, 0, 0],
            [0, 6, 0, 3, 0, 0, 9, 4, 8],
            [8, 0, 0, 0, 0, 5, 0, 6, 0],
            [3, 0, 2, 0, 8, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def process(self):
        self.zero_count = 0
        for px, line in enumerate(self.matrix):
            for py, value in enumerate(line):
                if value > 0:
                    continue
                self.zero_count += 1
                rx = self.__get_area_index(px)
                ry = self.__get_area_index(py)
                list_o = [self.matrix[x][y] for x in rx for y in ry]
                list_x = [lx for lx in self.matrix[px]]
                list_y = [ly[py] for ly in self.matrix]
                pv = list(set(self.wonder_num).difference(set(list_o).union(set(list_x)).union(set(list_y))))
                if len(pv) == 1:
                    key = str(px)+","+str(py)
                    if key in self.wonder_map:
                        del self.wonder_map[key]
                    self.matrix[px][py] = pv.pop()
                    return True
                elif len(pv) == 2:
                    self.wonder_map[str(px)+","+str(py)] = pv
                elif len(pv) == 0:
                    self.attempt_error = True
        self.is_game_over()
        return False

    def attempt(self):
        (key, value) = self.wonder_map.popitem()
        px = int(key[:1])
        py = int(key[2:])
        for item in value:
            self.matrix[px][py] = item
            while self.process():
                pass
            if self.attempt_error:
                self.attempt_error = False
                continue

            if len(self.wonder_map) > 0:
                self.attempt()

    def __get_area_index(self, v):
        if v < 3:
            return [0, 1, 2]
        elif v > 5:
            return [6, 7, 8]
        else:
            return [3, 4, 5]

    def show(self):
        print("")
        for item in self.matrix:
            print(item)

    def is_game_over(self):
        if self.zero_count == 0:
            self.show()
            sys.exit(0)

    def run(self):
        self.collect_input()
        # self.test()
        while self.process():
            pass
        print("Attempting...")
        self.attempt()


if __name__ == "__main__":
    sd = Sudoku()
    sd.run()





