import pytest
from ships.naive_implementation import ships_counter
from pathlib import Path

path_to_examples = '../examples_of_maps/'
list_of_path_to_examples = list(Path(path_to_examples).glob('*.txt'))

LIST_OF_SHIPS = list(dict(filename=x.parent/x.name, ship_count=int(x.stem)) for x in list_of_path_to_examples)


@pytest.mark.parametrize('list_of_ships', LIST_OF_SHIPS)
def test_ship_counter(list_of_ships):

    with open(list_of_ships['filename'], 'r') as f:
        fields = f.read()
    primary_list_of_ships = list(map(list, fields.splitlines()))
    transpose_list_of_ships = list(zip(*primary_list_of_ships))
    len_of_ships = []
    ships_counter(primary_list_of_ships, len_of_ships)
    ships_counter(transpose_list_of_ships, len_of_ships)

    assert len(len_of_ships) == list_of_ships['ship_count'], 'Wrong count of ships!'
    print('Right count of ships!')
