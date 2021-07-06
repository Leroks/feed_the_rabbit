map_input = list(input("Please enter feeding map as a list:\n"))
directions = list(input("Please enter direction of movements as a list:\n"))

direction_list, elements, map_list = [], [], []
row_number, letter_count, column_number, element_number, score, rabbit = -1, 0, 0, 0, 0, 0
board, board_last = """""""", """"""""
poison = False

for x in map_input:  # sorting out board elements and adding them to an empty list
    if x == "W" or x == "X" or x == "C" or x == "M" or x == "A" or x == "P" or x == "*":
        map_list += x
        element_number += 1

for x in map_input:  # counting row number
    if x == "]":
        row_number += 1

column_number = element_number / row_number  # calculating column number

for x in map_list:  # creating the first state of the board
    board = board + x + " "
    letter_count += 1
    if letter_count % column_number == 0 and letter_count != element_number:
        board += "\n"
        continue

print(f"Your board is:\n{board}")

for i in board:  # creating a list from the board's elements
    if i != "\n" and i != " ":
        elements += i

for i in elements:  # finding the rabbit's position
    if i == '*':
        break
    rabbit += 1


def score_table(location_check):  # function for tracking the score and poison
    global score
    global poison
    if elements[location_check] == 'C':
        score += 10
    elif elements[location_check] == 'A':
        score += 5
    elif elements[location_check] == 'M':
        score -= 5
    elif elements[location_check] == 'P':
        poison = True


def move_rabbit(direction):  # function for the movement of the rabbit
    global rabbit

    if direction == 'U':
        location_check = rabbit - int(column_number)
        if (location_check + 1) >= 0:
            if elements[location_check] != 'W':
                score_table(location_check)
                elements[rabbit] = 'X'
                rabbit = location_check
                elements[rabbit] = '*'

    elif direction == 'D':
        location_check = rabbit + int(column_number)
        if (location_check + 1) <= element_number:
            if elements[location_check] != 'W':
                score_table(location_check)
                elements[rabbit] = 'X'
                rabbit = location_check
                elements[rabbit] = '*'

    elif direction == 'L':
        location_check = rabbit - 1
        if (location_check + 1) % int(column_number) > 0:
            if elements[location_check] != 'W':
                score_table(location_check)
                elements[rabbit] = 'X'
                rabbit = location_check
                elements[rabbit] = '*'

    elif direction == 'R':
        location_check = rabbit + 1
        if (location_check + 1) % int(column_number) != 0:
            if elements[location_check] != 'W':
                score_table(location_check)
                elements[rabbit] = 'X'
                rabbit = location_check
                elements[rabbit] = '*'

    return rabbit


for x in directions:  # sorting out directions from input string and adding them to a list
    if x == 'U' or x == 'D' or x == 'L' or x == 'R':
        direction_list += x

for i in direction_list:  # moving the rabbit at the board with direction inputs
    if not poison:
        move_rabbit(i)

letter_count = 0

for i in elements:  # creating the board's last state
    board_last = board_last + i + " "
    letter_count += 1
    if letter_count % column_number == 0 and letter_count != element_number:
        board_last += "\n"
        continue

print(f"Your output should be like this:\n{board_last}")
print(f"Your score is: {score}")
