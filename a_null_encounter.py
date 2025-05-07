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

# Define the function to help get the correct
# string from the user input.
def get_correct_string(prompt, target_str, lives):

    # Replicate a do..while loop by constructing an infinite loop.
    while True:
        # Display the prompt to the user and get their answer.
        user_str_input = input(prompt)

        # Check if the input was the correct answer and the user lives.
        if (user_str_input == target_str) and (lives <= 0):
            # Break the loop.
            break

        

# Define the main function.
def main():
    pass


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
