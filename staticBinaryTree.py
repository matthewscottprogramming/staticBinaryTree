data = [-1]*10
left = [-1]*10
right = [-1]*10

def add_letter(letter):
    #adding node
    new_position = 0
    while data[new_position] != -1:
        new_position += 1
    data[new_position] = letter
    left[new_position] = -1
    right[new_position] = -1

    #traverse tree and update pointer
    if new_position != 0:
        current_position = 0
        while True:
            if data[new_position] > data[current_position] and right[current_position] == -1:
                right[current_position] = new_position
                break
            if data[new_position] > data[current_position] and right[current_position] != -1:
                current_position = right[current_position]
            if data[new_position] <= data[current_position] and left[current_position] == -1:
                left[current_position] = new_position
                break
            if data[new_position] <= data[current_position] and left[current_position] != -1:
                current_position = left[current_position]

def print_tree_in_order():
    pass

def print_tree_post_order():
    pass

def print_tree_pre_order():
    pass

if __name__ == '__main__':
    for letter in "mftjepz":
        add_letter(letter)

    for i in range(10):
        print(data[i], left[i], right[i])
