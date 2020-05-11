import argparse
import PyPDF2 as pdf
from util.py import *

def main():


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    main(args.sts_train_file, args.sts_dev_file, args.w2v_file)