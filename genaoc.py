import sys

def generate_files(day_number):
    py_file_name = f"day_{day_number}.py"
    txt_file_name = f"day_{day_number}_input.txt"

    py_content = f"f = open('day_{day_number}_input.txt','r')\nlines = f.readlines()\n\n\n"
    with open(py_file_name, 'w') as py_file:
        py_file.write(py_content)
        py_file.write("#-----------part 1--------------------------------------\n\n\n\n")
        py_file.write("#-----------part 2--------------------------------------")

    with open(txt_file_name, 'w') as txt_file:
        txt_file.write('')

    print(f"Files '{py_file_name}' and '{txt_file_name}' have been generated.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <day_number>")
        sys.exit(1)

    day_number = sys.argv[1]
    generate_files(day_number)