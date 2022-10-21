from prettytable import PrettyTable
my_table = PrettyTable()

my_table.add_column("City name",
["Adelaide","Brisbane","Darwin","Hobart",])
my_table.add_column("Area", [1295, 5905, 112, 1357])
my_table.horizontal_align_char = "r"
print(my_table)