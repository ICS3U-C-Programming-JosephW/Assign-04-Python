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
        if (user_str_input != target_str):
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
                f"Correct. You currently have {lives} {'life' if lives == 1 else 'lives'}."
            )

        # Check if the user input was the correct answer or
        # if their lives are less than or equal to zero.
        if (user_str_input == target_str) or (lives <= 0):
            # Break the loop.
            break


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
            if (user_int_input != target_int):
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
                    f"Correct. You currently have {lives} {'life' if lives == 1 else 'lives'}."
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



# Define the main function.
def main():
    pass


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
