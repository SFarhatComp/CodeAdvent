
digits=("one", "two", "three", "four","five", "six", "seven", "eight", "nine")

digits_converter_reversed = {
    "1": "one", "2": "two", "3": "three", "4": "four",
    "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"
}

digits_converter = {
    "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

total_sum = 0
with open("Input.txt", "r") as file:
    for line in file:
        indexes_dyct = {} # index : Value
        # Remove leading and trailing whitespace characters
        line = line.strip()
        # print(line)
        size_of_text = len(line) - 1
        left_pointer = 0
        right_pointer = size_of_text
        
        for digit in digits: 
                if digit in line : 
                    # indexes_dyct[line.rindex(digit)] = digit
                    indexes_dyct[line.index(digit)] = digit


        while left_pointer < size_of_text and not line[left_pointer].isdigit():
            left_pointer += 1

        if line[left_pointer].isdigit():    
            indexes_dyct[left_pointer] = digits_converter_reversed[line[left_pointer]]
            
        
        while right_pointer > 0 and not line[right_pointer].isdigit():
            right_pointer -= 1
        
        if line[right_pointer].isdigit():    
            indexes_dyct[right_pointer] = digits_converter_reversed[line[right_pointer]]
        

        # sorted_dict = {k: indexes_dyct[k] for k in sorted(indexes_dyct.keys())}

        smallest_keys = min(indexes_dyct.keys())
        largest_keys =  max(indexes_dyct.keys())

        left_number = digits_converter[indexes_dyct[smallest_keys]]
        right_number = digits_converter[indexes_dyct[largest_keys]]


        result = f"{left_number}{right_number}"
        new_int = int(result)
        total_sum += new_int
        
print(total_sum)


