"""Simulate a six-sided dice roll."""

import random

DICE_ART = {
    1: (
        "   /\ ",
        "  /  \ ",
        " /    \ ",
        "/   1  \ ",
        "--------- ",
    ),
    2: (
        "    /\ ",
        "   /  \ ",
        "  /    \ ",
        " /   2  \ ",
        "---------- ",
    ),
    3: (
        "    /\ ",
        "   /  \ ",
        "  /    \ ",
        " /   3  \ ",
        "---------- ",
    ),
    4: (
        "    /\ ",
        "   /  \ ",
        "  /    \ ",
        " /   4  \ ",
        "---------- ",
    ),
    5: (
        "    /\ ",
        "   /  \ ",
        "  /    \ ",
        " /   5  \ ",
        "---------- ",
    ),

}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = ""

#Initialize list to record the the results
roll_results = []  

def parse_input(input_string):
    """Return `input_string` as an integer between 0 and  4.

    Check if `input_string` is an integer number between 1 and 5.
    If so, return an integer with the same value. Otherwise, tell
    the user to enter a valid number and quit the program.
    """
    if input_string.strip() in {"1", "2", "3", "4","5"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 5.")
        raise SystemExit(1)

# continue playing until you surpass the 
# number of dice that meets the required constraints
#Initialize variable to help count the number of rolls made
num_rolls=0
while True:
    def roll_dice(num_dice):
        """Return a list of integers with length `num_dice`.

        Each integer in the returned list is a random number between
        1 and 4, inclusive.
        """
        roll_results_1roll = []        
        for _ in range(num_dice):
            roll = random.randint(1, 5)
            roll_results.append(roll)
            roll_results_1roll.append(roll)          
            print("---------------STEP----------------")
            print("Roll results for Last Roll:",roll_results_1roll)
            print("Roll results:",roll_results)
            
                   
        return roll_results_1roll
        # print(roll_re)

    def generate_dice_faces_diagram(dice_values):
        """Return an ASCII diagram of dice faces from `dice_values`.
        The string returned contains an ASCII representation of each die."""

        # Generate a list of dice faces from DICE_ART

        dice_faces = _get_dice_faces(dice_values)
        dice_faces_rows = _generate_dice_faces_rows(dice_faces)

        # Generate header with the word "RESULTS" centered
        width = len(dice_faces_rows[0])
        diagram_header = " RESULTS ".center(width, "~")

        dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
        return dice_faces_diagram


    def _get_dice_faces(dice_values):
        dice_faces = []
        for value in dice_values:
            dice_faces.append(DICE_ART[value])
        return dice_faces


    def _generate_dice_faces_rows(dice_faces):
        dice_faces_rows = []
        for row_idx in range(DIE_HEIGHT):
            row_components = []
            for die in dice_faces:
                row_components.append(die[row_idx])
            row_string = DIE_FACE_SEPARATOR.join(row_components)
            dice_faces_rows.append(row_string)
        return dice_faces_rows


    # 1. Get and validate user's input
    num_dice_input = input("How many dice do you want to roll? [1-5] ")
    num_dice = parse_input(num_dice_input)
    # 2. Roll the dice
    roll_results_1roll = roll_dice(num_dice)
   
    # 3. Generate the ASCII diagram of dice faces
    dice_face_diagram = generate_dice_faces_diagram(roll_results_1roll)
    # 4. Display the diagram
    print(f"\n{dice_face_diagram}")
    
    print("Dice Returns to initial position ",roll_results.count(roll_results[0])-1, "Time(s)")
    # Count the number of Rolls
    num_rolls+=1    
    print("The Dice has been rolled ",num_rolls, " Time(s)" )  
