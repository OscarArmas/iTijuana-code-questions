import argparse
import sys
from functions import *

def load_parseargs():
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

    # Create a fq_sumcsv subcommand
    parser_listapps = subparsers.add_parser(
        "fq_sumcsv",
        help="""Give a Comma Separated File (csv) and a column number (zero being the left most column) return the sum of all the entries in that column
    Assume that all the entries in the CSV are numbers.
    Assume also that there are no column headers.""",
    )
    parser_listapps.set_defaults(func=fq_sumcsv)
    parser_listapps.add_argument(
        "--file-path", type=str, help="path to read csv", dest="file_path"
    )
    parser_listapps.add_argument("--col", type=int, help="num column", dest="col")


    if len(sys.argv) <= 1:
        sys.argv.append("--help")
    options = parser.parse_args()
    # Run the appropriate function
    options.func(options)

if __name__ == '__main__':
    load_parseargs()