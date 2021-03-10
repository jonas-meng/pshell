#!/usr/bin/env python
# coding: utf-8

import json
import sys

with open("./config.json", "r") as config_file:
    global_config = json.load(config_file)

PROMPT_STRING = global_config['prompt_string']


def read_entire_cmd():
    cmd = input(PROMPT_STRING)

    while cmd.endswith("\\"):
        cmd = cmd[:-1] + input(" ")

    return cmd


def main():
    while True:
        try:
            cmd = read_entire_cmd()
            print(cmd)
        except KeyboardInterrupt:
            print("\nexit...")
            sys.exit()


if __name__ == "__main__":
    main()
