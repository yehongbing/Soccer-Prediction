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

        result_temp = 0
        row_num = 0

        for row in reader:

            if row_num == 0:
                header = row
                for i in range(0, 7):
                    desired_col.append(header[i])
                desired_col.append(header[26])
                desired_col.append(header[27])
                desired_col.append("Final_Result")
                writer.writerow(desired_col)

            elif row_num == 1:
                previous = row
                previous_matchID = previous[0]

            else:
                if row[0] != previous_matchID:
                    for i in range(0, 7):
                        desired_col.append(previous[i])
                    desired_col.append(previous[26])
                    desired_col.append(previous[27])
                    # append the final result according to score difference
                    if int(previous[11]) > 0:
                        result_temp = 1
                    elif int(previous[11]) == 0:
                        result_temp = 0
                    else:
                        result_temp = -1

                    # write the result to file
                    desired_col.append(result_temp)
                    writer.writerow(desired_col)
                # record current row to previous to next iteration
                previous = row
                previous_matchID = previous[0]
            # Since our algorithm is kind of dumb, here we need to append the last line manually

            if row_num == 100998:
                for i in range(0, 7):
                    desired_col.append(previous[i])
                desired_col.append(previous[26])
                desired_col.append(previous[27])
                # append the final result according to score difference
                if int(row[11]) > 0:
                    result_temp = 1
                elif int(row[11]) == 0:
                    result_temp = 0
                else:
                    result_temp = -1

                # write the result to file
                desired_col.append(result_temp)
                writer.writerow(desired_col)

            row_num += 1
            desired_col.clear()




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
