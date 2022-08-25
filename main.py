import csv
import yaml


# We want to be able to scan a csv file, with all the missions
# and generate a complete missions.yml out of it. So we can add missions via
# a spreadsheet and not manually change 2 files

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def file_csv_as_dict(file):
    return csv.DictReader(file)


def open_file(file_name):
    return file_csv_as_dict(open(file_name, "r"))


# Press the green button in the gutter to run the script.
column_name = "Name"
column_display_name = "DisplayName"
column_req = "Requirements"
column_crystals = "Crystals"
column_money = "Money"
column_xp = "XP"
column_item = "Item"
column_daily = "Daily"

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
