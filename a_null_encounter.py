#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 7, 2025
# This program contains a story-based game
# where the user is trapped in a void and
# meets someone named null, an entity who
# later tells the user their story. The user
# must endure the harmful environment of
# the void and answer stages of questions
# to win.

# Import the constants module for useful constants.
import constants
# Import random module to use random functions.
import random
# Import the time module to delay the program.
import time


# Define a function to help get the correct
# string answer from the user input.
def get_correct_string(prompt, target_str, lives):
    # Replicate a do..while by constructing an infinite loop.
    while True:
        # Display the prompt to the user and get their
        # string answer, regardless of case.
        user_str_input = input(prompt).lower()

        # Check if the user entered an input that did not
        # match the answer, meaning it was incorrect.
        if user_str_input != target_str:
            # Take away one life from the user
            # and keep it from going below zero.
            lives = max(lives - 1, 0)
            # Display to the user that they were incorrect,
            # along with their resulting lives.
            print(f"Incorrect, you lost one life and have {lives} left.")
        # Otherwise, the user answered correctly.
        else:
            # Display to the user that they were correct,
            # along with their resulting lives.
            print(
                f"Correct. You currently have {lives} {'life' if (lives == 1) else 'lives'}."
            )

        # Check if the user input was the correct answer or
        # if their lives are less than or equal to zero.
        if (user_str_input == target_str) or (lives <= 0):
            # Break the loop.
            break
    # Return the amount of lives left.
    return lives


# Define a function to help get the correct
# integer answer from the user input.
def get_correct_integer(prompt, target_int, lives):
    # Replicate a do..while by constructing an infinite loop.
    while True:
        # Display the prompt to the user and get
        # their integer answer as a string.
        user_int_input_str = input(prompt)

        # Try to validate and proceed with the user input.
        try:
            # Attempt to convert the entered
            # string into an integer.
            user_int_input = int(user_int_input_str)
            # Check if the user entered an input that did not
            # match the answer, meaning it was incorrect.
            if user_int_input != target_int:
                # Take away one life from the user
                # and keep it from going below zero.
                lives = max(lives - 1, 0)
                # Display to the user that they were incorrect,
                # along with their resulting lives.
                print(f"Incorrect, you lost one life and have {lives} left.")
            # Otherwise, the user answered correctly.
            else:
                # Display to the user that they were correct,
                # along with their resulting lives.
                print(
                    f"Correct. You currently have {lives} {'life' if (lives == 1) else 'lives'}."
                )
        # Runs if int() could not convert the user's string input into an integer.
        except ValueError:
            # Display to the user that they did not enter a valid integer.
            print(f"{user_int_input_str} is not a valid integer. Try again.")

        # Check if the user input was the correct answer or
        # if their lives are less than or equal to zero.
        if (user_int_input == target_int) or (lives <= 0):
            # Break the loop.
            break
    # Return the amount of lives left.
    return lives


# Define a function to loop through stage questions.
def ask_questions(stage_entries, lives):
    # Copy the stage entries list to safely
    # modify it.
    stage_entries_copy = stage_entries.copy()

    # Shuffle the list copy for randomized questions.
    stage_entries_copy.shuffle()

    # Display the initial line for any stage.
    print(f"{constants.LIGHT_BLUE}Let us see...{constants.WHITE}")

    # Use a for loop to loop through every
    # question in the specific stage list.
    for question_num in range(len(stage_entries_copy)):
        # Check if the type of the answer is a string.
        if stage_entries_copy[question_num][1] == str:
            # Run the string question function.
            lives = get_correct_string(
                stage_entries_copy[question_num][0],
                stage_entries_copy[question_num][1],
                lives,
            )
        # Otherwise, the type of the answer has to be an integer.
        else:
            # Run the integer question function.
            lives = get_correct_string(
                stage_entries_copy[question_num][0],
                stage_entries_copy[question_num][1],
                lives,
            )
        # Check if the lives are less than or equal to zero.
        if lives <= 0:
            # Break the loop.
            break

    # Return the amount of lives left.
    return lives


# Define a function to generate a possible void
# effect which challenges the user.
def chance_void_effect(stage_num, lives):
    # Determine the chance of the effect taking place
    # based on the user's stage number.
    effect_chance = (0.5 * (stage_num**2)) + (0.5 * stage_num) + 39

    # Check if lives are less than or equal to 0.
    if lives <= 0:
        # Return the lives early in the function so
        # the user does not take any extra damage.
        return lives

    # Check if a random integer from 1 to 100 is less than
    # or equal to the effect chance.
    if random.randint(1, 100) <= effect_chance:
        # Determine a possible effect by randomly selecting 
        # one from the void effects array.
        possible_effect = random.choice(constants.VOID_EFFECTS)

        # Determine the damage of the effect
        # based on the user's stage number.
        effect_damage = (0.1 * (stage_num ** 2)) + (0.4 * stage_num) + 0.6

        # Take away the user's lives based on the effect damage.
        lives = max(lives - effect_chance, 0)

        # Display the resulting effect description.
        print(f"{constants.LIGHT_PURPLE}{possible_effect}. "
        f"You took {effect_damage} damage and have {lives} lives left.{constants.WHITE}")
    # Otherwise, the random number was greater than the effect chance.
    else:
        # Display the user that they are unaffected.
        print(f"{constants.LIGHT_PURPLE}You remain unaffected in "
        f"the seemingly soundless void.{constants.WHITE}")
    
    # Return the lives at the end if the function
    # was able to avoid the early return statement.
    return lives

# Define the main function.
def main():
    # Set the user's current lives to
    # 25, which can change overtime.
    user_current_lives = 25

    # Loop through all the stage entries.
    for base_stage_num in range(len(constants.STAGE_ENTRIES)):
        # Check if the user's lives are zero or less.
        if (user_current_lives <= 0):
            # Break the loop.
            break

        # Nest a for loop inside to loop through all 
        # the dialogue lines before the corresponding
        # stage entries.
        for line_num in range(len(constants.STAGE_DIALOGUES[base_stage_num])):
            # Display the line of dialogue based on the current line number.
            print(constants.STAGE_DIALOGUES[base_stage_num][line_num][0])
            # Delay the whole program based on the corresponding dialogue
            # line for dynamic pacing.
            time.sleep(constants.STAGE_DIALOGUES[base_stage_num][line_num][1])
        
        # Ask the user questions depending on their base stage number
        # and assign their remaining lives to their current lives. 
        user_current_lives = ask_questions(
            constants.STAGE_ENTRIES[base_stage_num], user_current_lives)





# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
