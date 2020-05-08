#32

file_path = "tset.txt"

def File_Check(filename):
    try:
        input_file = open(filename, 'r')
    except:
        raise Exception("Error: file is not found")
    input_string = input_file.read()
    number_of_ints = 0
    if (len(input_string) == 0):
        raise Exception('Error: empty file')
    temp_character = ''
    prev = ''
    for index in range(len(input_string)):
        if (input_string[index] != ' ') and (input_string[index] != '\n'):
            temp_character += input_string[index]
        if (input_string[index] == ' ') or (input_string[index] == '\n') or (index == (len(input_string) - 1)):
            try:
                temp_character = int(temp_character)
                number_of_ints += 1
            except ValueError:
                if (prev != ' ') and (prev != '\n') and (index != 0):
                    raise Exception("Error: non-integer character in sequence")
                else:
                    pass
            temp_character = ''
        prev = input_string[index]

    input_file.close()
    if (number_of_ints == 0):
        raise Exception("Error: there are no integers in sequence")
    return number_of_ints

def Sequence(filename):
    try:
        input_file = open(filename, "r")
    except:
        raise Exception("Error: file is not found")
    string = input_file.read()
    satisfying_elements = 0
    seq_len = File_Check(filename)
    if (seq_len == 1) or (seq_len == 2):
        return 0
    index = 0
    temp_1, temp_2, prev = '', '', ''
    while True:
        if (string[index] != ' ') and (string[index] != '\n'):
            temp_1 += string[index]
        if (string[index] == ' ') or (string[index] == '\n'):
            if (prev != ' ') and (prev != '\n') and (index != 0):
                temp_1 = int(temp_1)
                prev = string[index]
                index += 1
                break
        prev = string[index]
        index += 1

    while True:
        if (string[index] != ' ') and (string[index] != '\n'):
            temp_2 += string[index]
        if (string[index] == ' ') or (string[index] == '\n') or (index == (len(string) - 1)):
            if (prev != ' ') and (prev != '\n'):
                temp_2 = int(temp_2)
                prev = string[index]
                index += 1
                break
        prev = string[index]
        index += 1
    current_char = ''
    for index_ in range(index, len(string)):
        if (string[index_] != ' ') and (string[index_] != '\n'):
            current_char += string[index_]
        if (string[index_] == ' ') or (string[index_] == '\n') or (index_ == (len(string) - 1)):
            if ((prev != ' ') and (prev != '\n')) or (index_ == (len(string) - 1)):
                if (temp_2 == (temp_1 + current_char)/2):
                    satisfying_elements += 1
                temp_1 = temp_2
                temp_2 = current_char
                current_char = ''
        prev = string[index_]
    return satisfying_elements

def Autotest():
    test_file = "test.txt"
    ans = Sequence(test_file)
    if (ans == 3):
        print("Autotest passed successfully")
    else:
        raise Exception("Error: autotest not passed")
Autotest()
result = Sequence(file_path)
print("result is ",result)

