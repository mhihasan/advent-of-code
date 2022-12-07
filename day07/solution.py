from day07.file_parser import parse_file, ROOT_DIR

TOTAL_DISK_SPACE = 70000000
REQUIRED_UNUSED_SPACE = 30000000
DIRECTORY_SIZE_THRESHOLD = 100000


def _calculate_folder_sizes(fs, folder_path, folder_sizes=None):
    if folder_sizes is None:
        folder_sizes = {}

    folder_items = fs[folder_path]
    if folder_items.get("file_size", 0) > 0:
        return folder_items["file_size"]

    total_size = sum([_calculate_folder_sizes(fs, child, folder_sizes) for child in folder_items["children"]])
    folder_sizes[folder_path] = int(total_size)
    return total_size


def calculate_sum_of_directory_size(folder_sizes, directory_size_threshold):
    return sum([file_size for folder_path, file_size in folder_sizes.items() if file_size <= directory_size_threshold])


def find_folder_to_free_up_required_space(folder_sizes, total_disk_space, required_unused_space):
    current_unused_space = total_disk_space - folder_sizes[ROOT_DIR]
    sizes_to_delete = [
        size for path, size in folder_sizes.items() if size > (required_unused_space - current_unused_space)
    ]
    return min(sizes_to_delete)


def solve(file_name: str, part: int = 1):
    file_system = parse_file(file_name)
    folder_sizes: dict[str, int] = {}
    _calculate_folder_sizes(fs=file_system, folder_path=ROOT_DIR, folder_sizes=folder_sizes)

    if part == 1:
        return calculate_sum_of_directory_size(folder_sizes, directory_size_threshold=DIRECTORY_SIZE_THRESHOLD)

    return find_folder_to_free_up_required_space(
        folder_sizes, total_disk_space=TOTAL_DISK_SPACE, required_unused_space=REQUIRED_UNUSED_SPACE
    )
