import os
import sys
import subprocess
import csv

def ask_yes_no(question):
    while True:
        answer = input(question + " (y/n): ").lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        else:
            print("Please enter y or n.")

def main(platform):
    # カレントディレクトリをスクリプトのディレクトリに変更
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    required_list = []
    cmd_list = []
    with open(f"packages-{platform}.csv", 'r') as f:
        reader = list(csv.reader(f))
        for row in reader[1:]:
            if ask_yes_no(f"you need {row[0]}?"):
                required_list.append(row[0])
                cmd_list.append(row[1])
    if len(cmd_list) > 0:
        print("The chosen packages are:")
        print("\n".join([f"  {name}" for name in required_list]))
        if ask_yes_no("Are you sure want to install these packages?"):
            process = subprocess.Popen("bash", stdin=subprocess.PIPE)
            process.communicate(input="\n".join(cmd_list).encode())

if __name__ == "__main__":
    supported_platform_list = [
        "ubuntu"
    ]
    if len(sys.argv) != 2:
        sys.stderr.write(f"usage: {sys.argv[0]} [platform]")
        sys.stderr.write(f"Supported platforms:")
        sys.stderr.write("\n".join([f"  {platform}" for platform in supported_platform_list]))
        exit(1)
    elif sys.argv[0] in supported_platform_list:
        main(sys.argv[0])