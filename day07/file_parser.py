import os
from collections import defaultdict

COMMAND_SIGN = "$"
CHANGE_DIR_COMMAND = "cd"
LIST_DIR_COMMAND = "ls"
ROOT_DIR = "/"


def read_file(file_name: str) -> list[str]:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as f:
        return f.read().splitlines()


def process_cd(command, dir_stacks=None, file_system=None):
    arg = command.split(" ")[1]
    if arg == ROOT_DIR:
        current_dir = ROOT_DIR
        dir_stacks = [ROOT_DIR]
        file_system = defaultdict(dict)
    elif arg == ".." and dir_stacks:
        dir_stacks.pop()
        current_dir = dir_stacks[-1]
    else:
        dir_stacks.append(arg)
        current_dir = arg
    return current_dir, dir_stacks, file_system


def process_ls(ls_results, current_dir=None, dir_stacks=None, file_system=None):
    for item in ls_results:
        file_marker, file_name = item.split(" ")

        path = _prepare_path(dir_stacks, file_name)
        current_dir_path = _prepare_path(dir_stacks)
        file_data = {"name": file_name, "parent": current_dir, "children": set()}
        if file_marker == "dir":
            file_data["file_size"] = -1
        else:
            file_data["file_size"] = int(file_marker)

        file_system[path].update(file_data)

        try:
            file_system[current_dir_path]["children"].add(path)
        except KeyError:
            file_system[current_dir_path].update({"children": {path}})

    return file_system


def _read_ls_results(inputs):
    ls_res = []
    for line in inputs:
        if line.startswith(COMMAND_SIGN):
            break

        ls_res.append(line)

    return ls_res


def _prepare_path(dir_stacks, file_name=None):
    if file_name == ROOT_DIR:
        return file_name

    dirs_except_root = dir_stacks[1:]
    if not dirs_except_root and file_name:
        return ROOT_DIR + file_name

    return "".join([ROOT_DIR, "/".join(dirs_except_root), (file_name and f"/{file_name}" or "")])


def prepare_file_system(inputs):
    file_system = defaultdict(dict)

    current_dir = (ROOT_DIR,)
    dir_stacks = [ROOT_DIR]

    i = 0

    while i < len(inputs):
        line = inputs[i]

        if not line.startswith(COMMAND_SIGN):
            i += 1
            continue

        command = line.split(" ", 1)[1]
        if command.startswith(CHANGE_DIR_COMMAND):
            current_dir, dir_stacks, file_system = process_cd(command, dir_stacks=dir_stacks, file_system=file_system)
            i += 1
        elif command.startswith(LIST_DIR_COMMAND):
            ls_results = _read_ls_results(inputs[i + 1 :])
            file_system = process_ls(
                ls_results, current_dir=current_dir, dir_stacks=dir_stacks, file_system=file_system
            )
            i += len(ls_results) + 1

    return file_system


def parse_file(file_name: str) -> dict[str, dict]:
    return prepare_file_system(read_file(file_name))
