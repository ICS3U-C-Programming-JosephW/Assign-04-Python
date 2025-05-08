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
    print("Let us see...")

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
    # Determine the chance of the effect taking place.
    effect_chance = (0.5 * (stage_num**2)) + (0.5 * stage_num) + 39

    # Check if lives are less than or equal to 0.
    if lives <= 0:
        # Return the lives early in the function.
        return lives

    # Check if a random integer from 1 to 100 is less than
    # or equal to the effect chance.


# Define the main function.
def main():
    pass


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
