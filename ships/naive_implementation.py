# naive implementation

def get_list_of_ships() -> list:
    with open('examples_of_maps/new_map.txt', 'r') as f:
        fields = f.read()
    return list(map(list, fields.splitlines()))


def file_check() -> list:
    list_of_ships = get_list_of_ships()
    map_size = len(list_of_ships)
    for i in range(1, map_size):
        for j in range(1, map_size):
            if ((list_of_ships[i][j] == list_of_ships[i - 1][j - 1] and list_of_ships[i][
                j] == '#') and (
                        list_of_ships[i - 1][j] == '#' or list_of_ships[i][j - 1] == '#')) or (
                    (list_of_ships[i][j - 1] == list_of_ships[i - 1][j] and list_of_ships[i][
                        j - 1] == '#') and (
                            list_of_ships[i][j] == '#' or list_of_ships[i - 1][j - 1] == '#')):
                raise RuntimeError
    return list_of_ships


def ships_counter(list_of_ships, final_array):
    map_size = len(list_of_ships)
    single_doubles = False
    if final_array:
        single_doubles = True
    ship_size = 0

    def append_non_single_ship(ship_size_):
        if ship_size_:
            if single_doubles:
                if ship_size_ != 1:
                    final_array.append(ship_size_)
                    ship_size_ = 0
                else:
                    ship_size_ = 0
            else:
                final_array.append(ship_size_)
                ship_size_ = 0
        return ship_size_

    # top border
    for column in range(map_size):
        if list_of_ships[0][column] == '#' and list_of_ships[1][column] == '#':
            pass
        elif list_of_ships[0][column] == '#':
            ship_size += 1
        else:
            if ship_size:
                if single_doubles:
                    if ship_size == 1:
                        ship_size = 0
                    else:
                        final_array.append(ship_size)
                        ship_size = 0
                else:
                    final_array.append(ship_size)
                    ship_size = 0
            ship_size = append_non_single_ship(ship_size)
    ship_size = append_non_single_ship(ship_size)

    # center
    for row in range(1, map_size - 1):
        if ship_size:
            if single_doubles:
                if ship_size == 1:
                    ship_size = 0
                else:
                    final_array.append(ship_size)
                    ship_size = 0
            else:
                final_array.append(ship_size)
                ship_size = 0
        for column in range(map_size):
            if list_of_ships[row][column] == '#' and \
                    list_of_ships[row + 1][column] == '#' and \
                    list_of_ships[row - 1][column] == '#':
                pass
            elif list_of_ships[row][column] == '#' and \
                    list_of_ships[row + 1][column] == '#' and \
                    list_of_ships[row - 1][column] != '#':
                pass
            elif list_of_ships[row][column] == '#' and \
                    list_of_ships[row + 1][column] != '#' and \
                    list_of_ships[row - 1][column] == '#':
                pass
            elif list_of_ships[row][column] == '#':
                ship_size += 1
            else:
                ship_size = append_non_single_ship(ship_size)
    ship_size = append_non_single_ship(ship_size)

    # bottom border
    for column in range(map_size):
        if list_of_ships[map_size - 1][column] == '#' and list_of_ships[map_size - 2][column] == '#':
            pass
        elif list_of_ships[map_size - 1][column] == '#':
            ship_size += 1
        else:
            ship_size = append_non_single_ship(ship_size)
    append_non_single_ship(ship_size)


if __name__ == '__main__':
    primary_list_of_ships = file_check()
    transpose_list_of_ships = list(zip(*primary_list_of_ships))
    length_of_all_ships = []

    ships_counter(primary_list_of_ships, length_of_all_ships)
    ships_counter(transpose_list_of_ships, length_of_all_ships)

    print(length_of_all_ships)
    print(len(length_of_all_ships))
