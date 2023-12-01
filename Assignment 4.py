'''
Name: Aakib Kibria Khan
Email: akkhan9@myseneca.ca
ID:157802224
PRG600_Assignment-4

'''
#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import csv
import os
import sys

# In[ ]:

def read_csv(file_name):
    """
    Reads a CSV file and returns a list of dictionaries.
    
    Parameters
    ----------
    file_name: str
    
    Returns
    -------
    temp_list: list
    """
    # Initialize empty list to receive data
    temp_list = []

    # Open the CSV file for reading
    with open(file_name, "r") as f:
        # Initialize a csv reader
        r = csv.DictReader(f)
        # Read each line
        for i in r:
            # Append in the empty list
            temp_list.append(i)

    return temp_list

# In[ ]:

def create_general_frame(table_data):
    """
    Create an extended data frame from raw csv data, to store "totalsales_sale" and "lostsales_sale".
    Make it easy for multiple tables to access these data.
    
    Parameters
    ----------
    table_data: list[dict]
        From read_csv().
    
    Returns
    -------
    frame: list[dict]
    """
    frame = table_data
    for i in frame:
        i['Current Stock'] = int(i['Current Stock'])  # Convert current stock to integer. For future calculating.
        i['Price per Item'] = float(i['Price per Item'])  # Convert price per item to float.
        i["totalsales_sale"] = 0  # Initialize total sales count
        i["lostsales_sale"] = 0  # Initialize lost sales count
    return frame

# In[ ]:

def make_sales(input_frame):
    """
    
    Parameters
    ----------
    input_frame
    
    Returns
    -------
    
    """
    item_number = len(input_frame)
    while True:
        user_choice = input(f"Select a number (1-{item_number}) to indicate a sale, or 'e' to indicate end of day: ")

        if user_choice == "e":
            break
        else:
            try:
                num_choice = int(user_choice)
            except ValueError:
                print(f"Invalid input. Please enter a number from 1 to {item_number}. Or 'e'.")
                continue

            if 1 <= num_choice <= item_number:

                actual_index = int(user_choice) - 1
                if input_frame[actual_index]["Current Stock"] > 0:
                    input_frame[actual_index]["Current Stock"] -= 1
                    input_frame[actual_index]["totalsales_sale"] += 1
                else:
                    input_frame[actual_index]["lostsales_sale"] += 1
            else:
                print(f"Please enter a number from 1 to {item_number}.")
    return input_frame

# In[ ]:

def create_totalsales(input_frame):
    """
    
    Parameters
    ----------
    input_frame
    
    Returns
    -------
    
    """
    ts_frame = [{
        'Item': i['Item'],
        'Sales': i['totalsales_sale'],
        'Price per Item': i['Price per Item'],
        'Total': int(i['totalsales_sale']) * float(i['Price per Item'])
    } for i in input_frame]

    return ts_frame

# In[ ]:

def create_lostsales(input_frame):
    """
    
    Parameters
    ----------
    input_frame
    
    Returns
    -------
    
    """
    ls_frame = [{
        'Item': i['Item'],
        'Sales': i['lostsales_sale'],
        'Price per Item': i['Price per Item'],
        'Total': int(i['lostsales_sale']) * float(i['Price per Item'])
    } for i in input_frame if int(i['lostsales_sale']) > 0]

    return ls_frame

# In[ ]:

def create_restockreport(input_frame):
    """
    
    Parameters
    ----------
    input_frame
    
    Returns
    -------
    
    """
    rr_frame = []

    for i in input_frame:
        item = i["Item"]
        demand = int(i['lostsales_sale']) + int(i['totalsales_sale'])
        add_demand = round(demand * 0.2 + 0.00000000000000000001)
        totaldemand = demand + add_demand
        currentstock = int(i['Current Stock'])
        fromwarehouse = max(totaldemand - currentstock, 0)

        result_dict = {
            'Item': item,
            'Demand': demand,
            '20%': add_demand,
            'Total Demand': totaldemand,
            'Current Stock': currentstock,
            'From Warehouse': fromwarehouse
        }
        rr_frame.append(result_dict)

    return rr_frame

# In[ ]:

def calculate_total_sum(temp_list, total_field):
    """
    Calculate the sum of the values in the “Total” column for each dictionary in the list.
    
    Parameters
    ----------
    temp_list : list[dict]
        List of dictionaries.
    total_field : str
        The name of the total field. Normally it is "Total".
    
    Returns
    -------
    float
        The sum of the values in the “Total” column. For further printing.
    """
    return sum(float(i.get(total_field, 0)) for i in temp_list)  # Default value set to 0.

# In[ ]:

def print_table_ver3(temp_list, selected_fields=None):
    """
    Prints the data in a table with a leading serial number column, and the first data column left-aligned.
    
    Parameters
    ----------
    temp_list: list<dict>
    selected_fields: list<str>
    
    Returns
    -------
    None
    """
    if not temp_list:
        print("No data to display.")
        return

    if selected_fields is None:
        selected_fields = list(temp_list[0].keys())

    headers = ['#'] + selected_fields

    # 3 items in temp_list, len(temp_list) == 3
    # str(3) == "3"
    # len("3") == 1
    # But if we have 13 items, len("13") == 2
    # plus 1 for the "."
    index_colunm_widths = len(str(len(temp_list))) + 1

    column_widths = {header: max(len(header), max(len(str(row.get(header, '')))
                                                  for row in temp_list)) for header in selected_fields}

    column_widths['#'] = index_colunm_widths

    formatted_headers = [f"{{:<{column_widths[header]}}}" if i <= 1 else
                         f"{{:>{column_widths[headers[-1]]}}}" if i == len(headers) - 1 else
                         f"{{:^{column_widths[header]}}}"
                         for i, header in enumerate(headers)]

    row_format = "    ".join(formatted_headers)

    print(row_format.format(*headers))

    print("=" * (sum(column_widths.values()) + (len(headers) - 1) * 4))  # 4 spaces in row_format's "   "

    row_len = len("=" * (sum(column_widths.values()) + (len(headers) - 1) * 4))

    # v2
    for idx, row in enumerate(temp_list, 1):
        row_data = [f"{idx}."] + [f"$ {row[header]}"
                                  if header == 'Price per Item' or header == 'Total' else
                                  row.get(header, '')
                                  for header in selected_fields]
        print(row_format.format(*row_data))

    # v3
    if 'Total' in selected_fields:
        total_sum = str(calculate_total_sum(temp_list, 'Total'))
        print_sum = '$ ' + total_sum
        print('Total:' + " " * (row_len - 6 - len(print_sum)) + print_sum)

# In[ ]:

def write_multiple_csvs(datasets, output_file):
    """
    Writes multiple datasets to a single CSV file, each with their own headers.
    
    Parameters
    ----------
    datasets : list
        A list of datasets, where each dataset is a list of dictionaries.
    output_file : str
        The file path where the CSV will be written.
    
    Returns
    -------
    None
    """
    with open(output_file, 'w', newline='', encoding='utf-8') as f:

        name_writer = csv.writer(f)

        for name, data in datasets.items():
            if data:

                name_writer.writerow([name])

                # Use the keys of the first dictionary in each dataset as fieldnames
                fieldnames = data[0].keys()

                # Initialize a csv writer
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                # Write the header
                writer.writeheader()

                # Write the rows
                for row in data:
                    writer.writerow(row)

                # Optionally, write a blank row between datasets
                f.write('\n')
            else:
                print("One of the datasets is empty. Skipping.")

# In[ ]:

if __name__ == '__main__':

    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print(r"Please provide argument 1 as 'path\input.csv', 2 as 'path\export.csv' ")
        quit()
    else:
        try:
            file_name = sys.argv[1]
            store = read_csv(file_name)
        except FileNotFoundError:
            print("Please provide a valid input csv Path")
            quit()

        output_path = sys.argv[2]
        if not output_path.endswith(".csv"):
            output_path = output_path + ".csv"

        print("Store")
        print_table_ver3(store)

        general_frame = create_general_frame(store)
        final_frame = make_sales(general_frame)

        total_sales = create_totalsales(final_frame)
        lost_sales = create_lostsales(final_frame)
        restock_report = create_restockreport(final_frame)

        print()
        print("Total Sales")

        print_table_ver3(total_sales)
        print()
        print("Lost Sales")

        print_table_ver3(lost_sales)
        print()
        print("Restock Report")

        print_table_ver3(restock_report)

        datasets = {
            "Store": store,
            "Total Sales": total_sales,
            "Lost Sales": lost_sales,
            "Restock Report": restock_report
        }
        try:
            write_multiple_csvs(datasets, output_path)
        except FileNotFoundError:
            print("Please provide a valid export csv Path")
