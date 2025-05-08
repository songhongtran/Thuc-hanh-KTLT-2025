def count_lines_in_file(fname):
    with open(fname, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return len(lines)

filename = 'abc.txt'
number_of_lines = count_lines_in_file(filename)
print(f"The number of lines in the file {filename} is {number_of_lines}")
