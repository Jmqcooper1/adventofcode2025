def get_input_lines(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return file.read()

def split_string_by_delimiter(string: str, delimiter: str) -> list[str]:
    return string.split(delimiter)