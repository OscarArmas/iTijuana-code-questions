import argparse
import sys
from util import *


def fq_sumcsv(args):
    path_file = args.file_path
    col_index = args.col
    sum_col = 0
    for row in  read_csv(path_file):
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


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# Create a mq_divisible subcommand
parser_showtop20 = subparsers.add_parser(
    "mq_divisible",
    help="Math Question: Takes two integers (x and y) and returns a list of numbers between x and y that are divisible by 5 but not by 7",
)
parser_showtop20.set_defaults(func=mq_divisible)
parser_showtop20.add_argument("--x", type=int, help="x integer", dest="x")
parser_showtop20.add_argument("--y", type=int, help="y integer", dest="y")

# Create a fq_find_in_doc subcommand
parser_listapps = subparsers.add_parser(
    "fq_finder",
    help="Takes a phrase and a text file as inputs. The function returns True if the phrase is found in the document and returns False otherwise. Note: Newline characters will not be included in the phrase.",
)
parser_listapps.set_defaults(func=fq_finder)
parser_listapps.add_argument("--text", type=str, help="some text", dest="text")
parser_listapps.add_argument(
    "--file-path", type=str, help="path to read file", dest="file_path"
)

# Create a vector_chess subcommand
parser_listapps = subparsers.add_parser(
    "ga_chessboard",
    help=""" You have a chessboard with only the Rook on it. The Rook can move up, down, left or right from your perspective. Write a function (or a class) that takes a series of movements and at the
end of the sequence of movements prints two numbers:
a. The distance traveled by the Rook
b. How far away the Rook is from its starting point
Assume that the chessboard has no edges (the rook can travel any distance in any direction)
For example, if the Rook is moved in the following sequence (up 1, left 3, down 2), then the Rook as traveled a distance of 6 spaces, and is 4 spaces away from its starting point.""",
)
parser_listapps.set_defaults(func=ga_chessboard)
parser_listapps.add_argument(
    "--mv_sequence",
    type=str,
    help='movement sequence. Example: "1-left 2-right 3-up 5-down"',
    dest="mv_sequence",
)

# Create a fq_find_in_doc subcommand
parser_listapps = subparsers.add_parser(
    "fq_sumcsv",
    help="""Give a Comma Separated File (csv) and a column number (zero being the left most column) return the sum of all the entries in that column
Assume that all the entries in the CSV are numbers.
Assume also that there are no column headers.""",
)
parser_listapps.set_defaults(func=fq_sumcsv)
parser_listapps.add_argument("--file-path", type=str, help="path to read csv", dest="file_path")
parser_listapps.add_argument(
    "--col", type=int, help="num column", dest="col"
)


if len(sys.argv) <= 1:
    sys.argv.append("--help")
options = parser.parse_args()

# Run the appropriate function
options.func(options)

