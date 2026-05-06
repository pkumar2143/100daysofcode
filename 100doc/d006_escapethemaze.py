# Day 6: Escape the (Reeborg.ca) Maze
# The underlying code is Python, but we work with the given functions
# https://reeborg.ca/reeborg.html (Select "Maze" in the first drop-down menu at the top.)

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def face_north():
    if not is_facing_north():
        turn_left()


face_north() # Standardize robot's starting position no matter where in the maze.
right_turn_move_count = 0
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        right_turn_move_count += 1
        # Starting along one section of the maze gives an infinite loop.
        # If the robot goes in a cycle, we "reset" by turning left. Will justify later...
        if right_turn_move_count == 4:
            turn_left()
            right_turn_move_count = 0
    elif not wall_in_front():
        move()
    else:
        turn_left()