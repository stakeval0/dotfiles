#!/usr/bin/env python3
import os
import sys
import subprocess
import re
import glob
import csv

def ask_yes_no(question):
    while True:
        answer = input(question + " (y/n): ").lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        else:
            print("Please enter y or n.")

def main(platform):
    required_list = []
    cmd_list = []
    with open(f"packages-{platform}.csv", 'r') as f:
        reader = list(csv.reader(f))
        for row in reader[1:]:
            if ask_yes_no(f"you need {row[0]}?"):
                required_list.append(row[0])
                cmd_list.append(row[1] if row[1] != "./setup" else f"./{row[0]}/setup-{platform}.sh")
    if len(cmd_list) > 0:
        print("The chosen packages are:")
        print("\n".join([f"  {name}" for name in required_list]))
        if ask_yes_no("Are you sure want to install these packages?"):
            process = subprocess.Popen("bash", stdin=subprocess.PIPE)
            process.communicate(input="\n".join(cmd_list).encode())

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    # `packages-[platform name].csv`があれば[platform name]をサポート済みと認識
    supported_platform_list = [re.sub("packages-(.*).csv", "\\1", list_path) for list_path in glob.glob("packages-*.csv")]
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [platform]", file=sys.stderr)
        print(f"Supported platforms:", file=sys.stderr)
        print("\n".join([f"  {platform}" for platform in supported_platform_list]), file=sys.stderr)
        exit(1)
    elif sys.argv[1] in supported_platform_list:
        main(sys.argv[1])
