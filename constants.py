#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 7, 2025
# This module contains constants.

# Create a 3-dimensional list to store all the corresponding
# questions and answers for each of the six stages.
STAGE_ENTRIES = [
    [
        ["3 + 4 = ", 7],
        ["Are truths and lies the same? (yes/no/both)", "both"],
        ["13 - 8 = ", 5],
    ],
    [
        ["Is it okay to forget often...? (yes/no)", "no"],
        ["(2 x 3) + 3 = ", 9],
        ["1 + (12 / 12) * 12 = ", 24],
        ["In this void, does time still exist? (yes/no)", "yes"],
    ],
    [
        ["Is life supposed to be fun? (yes/no)", "yes"],
        ["2^4 = ", 16],
        ["5 + (3 x 4)^2 + ((10 - 2) / 2) = ", 153],
        ["What is my name? (null/nothing/nobody)", "null"][
            "(2 + 1) x (3 - 2) x 16 = ", 48
        ],
    ],
    [
        ["Do morals always mean good...? (yes/no)", "no"],
        ["10 % 2 + 9^(3/6) = ", 3],
        ["Could this all be an illusion? (yes/no/maybe)", "maybe"],
        ["2 x (4^9^0.5) = ", 128],
    ],
    [
        ["(-3 x (3 - 4)) + 31 = ", 34],
        ["What is good to one person can be bad to another. (yes/no)", "yes"],
        ["(6 + 3 x 2) x 2^3 + 4 + (12-2) = ", 110],
    ],
    [
        ["1 + (1 % 1) - 1 + 1 + (1^0.88) / 1 - (1^1) - 1 + 1 - (1^0.5) + 1", 1][
            "Morality is complex and everyone sees it differently. (yes/no)", "yes"
        ],
    ],
]

# Create a 3-dimensional list to store all the
# corresponding dialogue lines and delay times
# for each of the six story parts.
STAGE_DIALOGUES = [
    [
        [
            "\nYou are in a void of space, yet you still can breathe. You are confused. What is all this?",
            1,
        ],
        ["Null: ...", 0.5],
        ["User: Who... are you?", 1.5],
        ["Null: I am null.", 1.5],
        ["User: Null as in nothing?", 1],
        [
            "Null: Well, sort of. "
            "I forgot my name and pretty much everything else, "
            "so that is what I go by.",
            1.5,
        ],
        ["User: Wow... may I ask why I'm here?", 2],
        [
            "Null: I do not know. "
            "People just spawn here like this is "
            "some sort of dimension.",
            3,
        ],
        ["User: So I'm stuck here forever???", 1],
        [
            "Null: No. Others managed to leave, some shorter than the others. "
            "I would tell my story, and most of them would just disappear.",
            2,
        ]["User: Ah... wait, story? You have a backstory?", 2],
        [
            "Null: Yes. I would happy to share it.",
            1.5,
        ],
        [
            "User: Well, I have nothing to do, so sure, tell me what happened to you, how you got here.",
            1,
        ],
        ["Null: Alright.", 0.5],
        [".", 0.5],
        [".", 0.5],
        [".", 0.5],
        [
            "It was a sunny day outside. The birds were chirping, "
            "flowers were blooming, and the scattered breezes made it all "
            "the more pleasant.",
            3,
        ],
        ["I felt like I could stay in this happy state forever."],
    ]
]
