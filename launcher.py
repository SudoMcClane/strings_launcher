#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Launch strings with all encoding in one command.

Author: Clément Gatefait
Date: 11/07/2019
"""

import argparse
import subprocess


def main():
    """Main function
    """

    parser = argparse.ArgumentParser(prog="strings_launcher.py",
                                     description="Launch strings with all \
                                     encoding in one command.")
    parser.add_argument("--output", metavar="FILE", default=None,
                        help="File to save results.")
    parser.add_argument("additional", nargs=argparse.REMAINDER,
                        help="strings arguments")

    args = parser.parse_args()

    encodings = ["s", "S", "l", "L", "b", "B"]

    for encoding in encodings:
        command = ["/usr/bin/strings", "-e", encoding] + args.additional

        if args.output is None:
            subprocess.call(command)
        else:
            with open(args.output, "a") as f:
                subprocess.call(command, stdout=f)

    exit(0)


main()
