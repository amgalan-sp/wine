def get_read_file(filename):
    with open(filename, "r", encoding='utf-8-sig') as rose_file:
        return rose_file.read()