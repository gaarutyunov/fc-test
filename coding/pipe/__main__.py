import argparse
import sys

from .run import run


def main(args: argparse.Namespace):
    if args.output == "stdout":
        run(args.data, args.mappings, sys.stdout, args.num_processes)
    else:
        with open(args.output, "w") as f:
            run(args.data, args.mappings, f, args.num_processes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--data", type=str, required=True)
    parser.add_argument("--mappings", type=str, required=True)
    parser.add_argument("--num_processes", type=int, default=1)
    parser.add_argument("--output", type=str, default="stdout")

    args = parser.parse_args()
    main(args)
