import pytest
from ships.naive_implementation import ships_counter
from pathlib import Path

path_to_examples = '../examples_of_maps/'
path_to_wrong_examples = '../wrong_examples_of_maps/'


def get_list_of_files(path):
    list_of_path_to_examples = list(Path(path).glob('*.txt'))
    return list(dict(filename=x.parent / x.name, ship_count=int(x.stem)) for x in list_of_path_to_examples)


LIST_OF_SHIPS = get_list_of_files(path_to_examples)
WRONG_LIST_OF_SHIPS = get_list_of_files(path_to_wrong_examples)


@pytest.mark.parametrize('list_of_ships', LIST_OF_SHIPS, ids=[x['ship_count'] for x in LIST_OF_SHIPS])
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


@pytest.mark.parametrize('list_of_ships', WRONG_LIST_OF_SHIPS, ids=[x['ship_count'] for x in WRONG_LIST_OF_SHIPS])
def test_negative_ship_counter(list_of_ships):
    with open(list_of_ships['filename'], 'r') as f:
        fields = f.read()
    primary_list_of_ships = list(map(list, fields.splitlines()))
    transpose_list_of_ships = list(zip(*primary_list_of_ships))
    len_of_ships = []

    try:
        ships_counter(primary_list_of_ships, len_of_ships)
        ships_counter(transpose_list_of_ships, len_of_ships)
    except RuntimeError:
        print('Test passed!')
