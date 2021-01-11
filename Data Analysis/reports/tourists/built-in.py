import csv

from variable import input_file, output_file

Row = list[str]
Table = list[Row]


def parse_columns(table: Table, pick_range=(3, 8)):
    return list(map(lambda row: row[pick_range[0]:pick_range[1]], table))


def row_filter(table: Table, targets=((1, '스포츠레져용품'), (2, '여'), (3, '20대'))):
    def isValid(row: Row):
        for target in targets:
            if row[target[0]] != target[1]:
                return False
        return True

    return (table[0], *filter(isValid, table[1:]))


with open(input_file, 'r') as csv_in_file:
    reader = csv.reader(csv_in_file)
    parsed_by_columns = parse_columns(list(reader))

    filtered_77 = row_filter(parsed_by_columns)

    with open(output_file, 'w') as csv_out_file:
        writer = csv.writer(csv_out_file)
        writer.writerows(filtered_77)
