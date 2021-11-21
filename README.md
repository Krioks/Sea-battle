## Sea-battle

This program calculates the number of ships located on the field for playing sea battle.
The input is a file consisting of n lines, n characters each. 
Symbol "**-**" means that there is no ship in this cell, 
symbol "**#**" means that there is a ship or part of a ship in this cell. 
A ship is considered to be a continuous sequence of "**#**" characters vertically 
or horizontally. 
The ships are not touching sides, but they can touch the corners. 
The length and width of the playing field cannot be more than 1000. 

At the moment, a simple check option has been implemented, 
and a test has been written that covers possible options 
for files from the **examples_of_maps** folder.

To run the project file you need: 
* run **Powershell**/**cmd** or **terminal** in _ships_ folder
* type:
```bash
python3 .\naive_implementation.py -path path_to_map
```
default value – `examples_of_maps/5.txt`
* The output will be a list with the weights of all ships, and the number of ships(lengths of list). 


To run the project test, you need:
* install `pytest`:
  * `pip install pytest` or `pip install -r requirements.txt`
* run **Powershell**/**cmd** or **terminal** in _tests_ folder
* type:
```bash
pytest --tb=native 
```

To run the separate test , you need:
* run **Powershell**/**cmd** or **terminal** in _tests_ folder
* type:
```bash
pytest counter_test.py::test_ship_counter --tb=native 
```

