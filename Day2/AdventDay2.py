import re
# my_bag = {"red" : 12, "green":13, "blue" : 14}
actual_game_dict = {}
total_sum = 0 

can_be_played = False

with open("Input2.txt", "r") as file:
    
    for line in file:
        total_mul = 1 
        # I need to parse and find id of the game 
        id_game = int(line[line.index(" ") + 1:line.index(":")])

        line_start = line[line.index(":") + 2 : ]
        
        individual_sets = re.findall(r'(\d+)\s(\w+)',line_start)
        maximum_color_dict = {}
        
        for num,colors in individual_sets: 
            num = int (num)
            if colors in maximum_color_dict : 
                if num > maximum_color_dict[colors]: 
                    maximum_color_dict[colors] = num
            else : 
                maximum_color_dict[colors] = num

        for values in maximum_color_dict.values():

            total_mul *= values    

        total_sum += total_mul

        print(f"The color dict is {maximum_color_dict}")
        print(f"The total mul value is {total_mul}")
    print(f"the total value for total sum is {total_sum}")


       