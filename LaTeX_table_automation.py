__name__ = "LaTeX table generator from CSV"
__author__ = "Marcin Lisiecki"
__license__ = "Open-source"
__version__ = "1.0"
__status__ = "production"


import csv

# Function for getting information and data from CSV
def get_table_info(datafilename):

    data_list = []
    dlm = "\t"
    # datafilename = input("Path to CSV: \n")

    # Open file
    file = open(datafilename, "r")
    reader = csv.reader(file, delimiter=dlm)
    # Get heading of table and number of columns
    heading = file.readline()
    number_of_columns = heading.count(";") + 1
    # Get data
    for row in reader:
        data_list.append(row)
    return number_of_columns, data_list, heading


def generate_table(number_of_columns, data_list, heading):

    columns_string = "{|"
    hline_string = "\\hline"
    data_string = ""
    end_string = "\t\\end{tabular}\n\\end{center}"
    final_table = ""
    # Put info about number of culumns
    for i in range(0, number_of_columns):
        columns_string += " c |"
    columns_string = columns_string + "}\n"

    begin_string = (
        "\\begin{center}\n\t\\begin{tabular}"
        + columns_string
        + "\t\t"
        + hline_string
        + "\n"
    )

    # Add heading on the top
    data_string += (
        "\t\t" + heading.replace("\n", "") + "\\" + "\\" + "\n"
        "\t\t" + hline_string + hline_string + "\n"
    )
    # Extract data and put in table
    for row in data_list:
        data_string += (
            "\t\t" + (row[0]) + "\\" + "\\" + "\n" + "\t\t" + hline_string + "\n"
        )
    data_string = data_string.replace(";", " & ")

    # Create final syntax for table
    final_table += begin_string + data_string + end_string
    return final_table


def print_syntax(final_table):
    print(final_table)


# Call functions
def combine_functions(datafilename):
    number_of_columns, data_list, heading = get_table_info(datafilename)
    final_table = generate_table(number_of_columns, data_list, heading)
    return final_table