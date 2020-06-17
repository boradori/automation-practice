import csv


def get_csv_data(file_name):
    rows = []
    f = open(file_name, 'r', encoding='utf-8')

    reader = csv.reader(f)

    next(reader)

    for row in reader:
        rows.append(row)

    f.close()

    return rows
