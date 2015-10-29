__author__ = 'HB_Y'

import csv
import sys

source = open('sample.csv', 'rt')
dest = open('aggregation_first_30mins.csv', 'wt')
row_num = 0
count = 0
score_home = 0
score_away = 0
redcard_home = 0
redcard_away = 0
try:
    reader = csv.reader(source)
    writer = csv.writer(dest)
    # before write to the row, we need to take the desired value from each row
    desired_col = []
    mins = 0
    for row in reader:
        if row_num == 0:
            for value in row:
                desired_col.append(value)
            desired_col.append('ScoreH')
            desired_col.append('ScoreA')
            desired_col.append('RedCardH')
            desired_col.append('RedCardA')
            writer.writerow(desired_col)
        else:
            if int(row[9]) == 30:
                for value in row:
                    desired_col.append(value)
                score_home = (int(row[10]) + int(row[11])) / 2
                score_away = (int(row[10]) - int(row[11])) / 2
                redcard_home = (int(row[12]) + int(row[13])) / 2
                redcard_away = (int(row[12]) - int(row[13])) / 2
                desired_col.append(score_home)
                desired_col.append(score_away)
                desired_col.append(redcard_home)
                desired_col.append(redcard_away)
                writer.writerow(desired_col)

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
    source.close()
    dest.close()
