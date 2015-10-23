__author__ = 'HB_Y'
import csv
import sys


def combine_by_id(source_file, dest_file):
    row_num = 0
    count = 0
    try:
        reader = csv.reader(source_file)
        writer = csv.writer(dest_file)
        desired_col = []

        # before write to the row, we need to take the desired value from each row
        for row in reader:
            if row_num == 0:
                header = row
                for i in range(0,7):
                    desired_col.append(header[i])

                desired_col.append(header[26])
                desired_col.append(header[27])
                writer.writerow(desired_col)
            elif row_num == 1:
                previous = row[0]
                for i in range(0,7):
                    desired_col.append(row[i])
                desired_col.append(row[26])
                desired_col.append(row[27])
                writer.writerow(desired_col)
                count += 1
            else:
                if row[0] != previous:

                    previous = row[0]
                    for i in range(0,7):
                        desired_col.append(row[i])
                    desired_col.append(row[26])
                    desired_col.append(row[27])
                    writer.writerow(desired_col)
                    count += 1
            desired_col.clear()
            row_num += 1

    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    finally:
        source_file.close()
        dest_file.close()

source = open('sample.csv', 'rt')
dest_id = open('combine_by_id.csv', 'wt')

combine_by_id(source, dest_id)
