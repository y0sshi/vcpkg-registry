# ==================================================
# Import
# ==================================================
import os
import argparse
import subprocess
import re


# ==================================================
# Function
# ==================================================
def main():
    ## 引数処理
    parser = argparse.ArgumentParser(description='update git-tree for vcpkg')
    parser.add_argument('--ports', '-p', type=str, nargs="*", default=[
        'vcpkg-lib-example',
        ])
    args = parser.parse_args()
    list_port_name = args.ports

    ## 各portに対してgit-tree更新
    for port_name in list_port_name:
        git_tree_update(port_name)


def git_tree_update(port_name: str):
    dir_version_file  :str = f'versions/{port_name[0]}-'
    path_version_file :str = f'{dir_version_file}/{port_name}.json'

    if not os.path.isdir(dir_version_file):
        os.makedirs(dir_version_file)

    subprocess.run(f'git add ports/{port_name}', text=True)
    tree_hash :str = subprocess.run(f'git write-tree --prefix=ports/{port_name}', text=True, capture_output=True).stdout.rstrip()

    print(f'tree_hash:"{tree_hash}" => {path_version_file}')
    if os.path.isfile(path_version_file):
        with open(path_version_file, mode="r") as f:
            lines = f.readlines()
    else:
        lines = [
                '{\n',
                '   "versions" : [\n',
                '       {\n',
                '           "version"  : "0.1.0",\n',
                '           "git-tree" : "treehash0000"\n',
                '       }\n',
                '   ]\n',
                '}\n',
                '\n',
                ]

    with open(path_version_file, mode="w", encoding="utf-8") as f:
        for line in lines:
            line_replaced : str = line
            if "git-tree" in line:
                line_replaced = re.sub(r'"git-tree"\s+:\s+"[a-z|A-Z|0-9]+"', f'"git-tree" : "{tree_hash}"', line)
            f.write(line_replaced)


# ==================================================
# Script
# ==================================================
if __name__ == '__main__':
    main()

