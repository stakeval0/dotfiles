import os
import subprocess
import csv

def ask_yes_no(question):
    while True:
        answer = input(question + " (y/n): ").lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        else:
            print("Please enter y or n.")

# カレントディレクトリをスクリプトのディレクトリに変更
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

required_list = []
cmd_list = []
with open('packages.csv', 'r') as f:
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
