import csv

def read_csv(filename, **fmtparams):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file, **fmtparams)
        for row in reader:
            yield row

def fq_sumcsv(args):
    path_file = args.file_path
    col_index = args.col
    sum_col = 0
    for row in read_csv(path_file):
        sum_col += int(row[col_index])
    print(sum_col)
    return sum_col


def fq_finder(args):
    text = args.text
    file_path = args.file_path
    with open(file_path) as f:
        if text in f.read():
            print("True")
            return
    print("False")


def mq_divisible(args):
    x = args.x
    y = args.y
    num_list = []
    for number in range(x, y):
        if number % 5 == 0 and number % 7 != 0:
            num_list.append(number)
    print(num_list)
    return


def ga_chessboard(args):
    sequence = args.mv_sequence
    up_count = 0
    left_count = 0
    right_count = 0
    down_count = 0

    for movement in sequence.split():
        mv_info = movement.split("-")

        if mv_info[-1] == "up":
            up_count += int(mv_info[0])
        elif mv_info[-1] == "left":
            left_count += int(mv_info[0])
        elif mv_info[-1] == "right":
            right_count += int(mv_info[0])
        elif mv_info[-1] == "down":
            down_count += int(mv_info[0])
    total_distance = up_count + left_count + right_count + down_count
    far_away_from_initp = abs(up_count - down_count) + abs(left_count - right_count)
    print(total_distance, far_away_from_initp)
    return