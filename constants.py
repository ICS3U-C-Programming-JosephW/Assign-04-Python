#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 7, 2025
# This module contains constants.

# Create a 3-dimensional list to store all the corresponding
# questions and answers for each of the six stages.
STAGE_ENTRIES = [
    [
        ["3 + 4 = ", 7],
        ["Are truths and lies the same? (yes/no): ", "no"],
        ["13 - 8 = ", 5],
    ],
    [
        ["Is it okay to forget often...? (yes/no): ", "no"],
        ["(2 x 3) + 3 = ", 9],
        ["1 + (12 / 12) * 12 = ", 13],
        ["In this void, does time still exist? (yes/no): ", "yes"],
    ],
    [
        ["Is life supposed to be fun? (yes/no): ", "yes"],
        ["2^4 = ", 16],
        ["5 + (3 x 4)^2 + ((10 - 2) / 2) = ", 153],
        ["What is my name? (null/nothing/nobody): ", "null"],
        ["(2 + 1) x (3 - 2) x 16 = ", 48],
    ],
    [
        ["Do morals always mean good...? (yes/no): ", "no"],
        ["10 % 2 + 9^(3/6) = ", 3],
        ["Could this all be an illusion? (yes/no/maybe): ", "maybe"],
        ["2 x (4^9^0.5) = ", 128],
    ],
    [
        ["(-3 x (3 - 4)) + 31 = ", 34],
        ["What is good to one person can be bad to another. (yes/no): ", "yes"],
        ["(6 + 3 x 2) x 2^3 + 4 + (12-2) = ", 110],
    ],
    [
        ["1 + (1 % 1) - 1 + 1 + (1^0.88) / 1 - (1^1) - 1 + 1 - (1^0.5) + 1 = ", 1],
        ["Morality is complex and everyone sees it differently. (yes/no): ", "yes"],
    ],
]

# Create a 3-dimensional list to store all
# the corresponding dialogue lines and delay
# times for each of the six story parts.
STAGE_DIALOGUES = [
    [
        [
            "\nYou are in a void of space, yet you still can breathe. You are confused. What is all this?",
            2,
        ],
        ["Null: ...", 2],
        ["User: Who... are you?", 2.5],
        ["Null: I am null.", 2.5],
        ["User: Null? As in nothing?", 2.5],
        [
            "Null: Well, sort of. "
            "I forgot my name and practically everything else, "
            "so that is what I go by.",
            2.5,
        ],
        ["User: Wow... may I ask why I'm here?", 2.5],
        [
            "Null: I do not know. "
            "People just spawn here like this is "
            "some sort of dimension.",
            3,
        ],
        ["User: So I'm stuck here forever???", 2.5],
        [
            "Null: No. Others managed to leave, some shorter than the others. "
            "I would tell my story, and most of them would just "
            "disappear before I even finish it.",
            3,
        ],
        ["User: Ah... wait, story? You have a backstory?", 2],
        [
            "Null: Yes. I would be happy to share it.",
            2.5,
        ],
        [
            "User: Sure! It's not like I have anything else to do... "
            "Tell me what happened to you and how you got here.",
            3,
        ],
        ["Null: Alright.", 1.5],
        [".", 0.75],
        [".", 1],
        [".", 1.5],
        [
            "It was a sunny day outside. The birds were chirping, "
            "flowers were blooming, and the scattered breezes made\nit all "
            "the more pleasant.",
            3.5,
        ],
        [
            "I felt like I could stay in this happy state forever. "
            "As I lay on the seemingly endless field of grass and flowers, "
            "it felt like I was one with nature.",
            3.5,
        ],
        ["I would attend to school, do my work, and look forward to the next day.", 3],
        [
            "I repeated this routine daily, quickly eating my breakfast "
            "so I could go outside early and run to the large field, just to experience "
            "that feeling over and over again.",
            3.5,
        ],
        ["However, as days passed, everything got weirder and less exciting.", 3],
        [
            "I still went to the field, but I could not make the same connections, ever.",
            3,
        ],
        [
            "I thought it was normal and the weather changes had to do with it, but even doing "
            "work and attending classes got harder.",
            3.5,
        ],
        ["It was...", 2.5],
    ],
    [
        ["...ME. It was me.", 2.5],
        [
            "I was losing touch. My memory started receding, and I silently panicked in my\n"
            "head, fighting endless battles against my diminishing neurons.",
            3.5,
        ],
        ["Things were blurry, and my grades were hitting an all-time low.", 3.5],
        [
            "I tried to make up for them by working extra time, but it did not do\n"
            "anything but add on to my confusion and distress.",
            3.5,
        ],
        [
            "Asking my parents for help because I forgot how to do simple tasks "
            "made them very concerned.",
            3.5,
        ],
        [
            "The final nail in the coffin was genuinely asking my parents\nhow to make a "
            "grilled cheese sandwich, which is what I always prepare for lunch.",
            3.5,
        ],
        [
            "They looked at me fearfully, and that was when I got sent to the hospital.",
            3.5,
        ],
    ],
    [
        [
            "Most other people outside of the hospital held the same feelings. Not "
            "even the neurologists could find anything wrong,\nand they looked at each other, "
            "baffled. This was not some typical condition.",
            3.5,
        ],
        ["It was like a nightmare, especially for my parents.", 2.5],
        [
            "It is excruciatingly painful when your own child suddenly does not remember "
            "anything about you anymore.\nI saw those feelings etched on my parents faces as "
            "tears freely flowed from their faces.",
            3.5,
        ],
        [
            "My parents urged the other doctors to do something, but it was to no avail.",
            3,
        ],
        [
            "Family, friends, work, the flower field, and routine, all forgotten. That was "
            "when I completely faded and ceased to live.",
            3,
        ],
    ],
    [
        [
            "I escaped out of my own body for a short period of time, being able to see "
            "the reaction of my parents and other friends.\nIt was heartbreaking, but I "
            "did not have a heart anymore.",
            3.5,
        ],
        [
            "After that short period of time, I could only see black and some distant dots.",
            3,
        ],
        [
            "I came to realize I was in what looked like outer space with stars, "
            "but I did not know why.",
            3,
        ],
        [
            "I could feel my own body and breathe, unaffected by being present in "
            "this empty space.",
            3,
        ],
        [
            "Maybe this was a reflection of my diminishing memories, or not. I "
            "never felt like connecting all the pieces.",
            4,
        ],
        [
            "Being able to tell this story multiple times was surprising. It's "
            "like some instance of\nmyself that somewhat wasn't affected "
            "by forgetfulness was reloaded.",
            3.5,
        ],
    ],
    [
        [
            "I could not count time, do work, play, or go to the fields anymore. "
            "All I could do was\nreflect and contemplate in this VOID.",
            3.5,
        ],
        ["There were no feelings, but that would change.", 3],
        [
            "Once I saw someone appear in my 'realm,' I got scared "
            "for some reason, thinking how it was possible.",
            3,
        ],
        [
            "People were able to fade out of my realm as well "
            "since they were still connected\nto their living selves, "
            "unlike me.",
            3.5,
        ],
        [
            "However, every person that managed to crawl into my space "
            "seemed to have the same feelings of loss and forgetfulness.",
            3,
        ],
        [
            "I could immediately connect myself to them, just like how I "
            "felt when I embraced nature on what seemed like the perfect day.",
            3.5,
        ],
        [
            "Knowing that, I wished them the best as they faded, and decided to "
            "keep contemplating until someone else appeared.",
            3.5,
        ],
        [
            "Those gaps in time seemed long, although it felt like I was being "
            "impatient. I was grateful, anyway.\nEven if they faded sooner than "
            "I expected, I still sighed in relief, every time.",
            4,
        ],
        ["And I will sigh in relief again once you manage to fade, user.", 3.5],
    ],
    [
        [
            "Every day, hour, minute, second, millisecond, without any doubt, "
            "I will have to embrace the\neverlasting confusion and void feelings "
            "that wander about in my head.",
            3.5,
        ],
        ["...ha.", 3.5],
    ],
]

# Create a one-dimensional array to store the void effects
# that have a possible chance of affecting the user.
VOID_EFFECTS = [
    "The distant stars glare at the unfamiliar "
    "figure that is you, setting you ablaze internally",
    "You feel a deep pang of loneliness that eats you inside, "
    "even though null is by your side",
    "The temperature of this silent and empty void "
    "sends powerful chills down your spine",
    "The lack of entropy present in this void scares you",
    "Some meteoroids seem to have their own mind and fly "
    "towards you without your notice, surprising both "
    "you and null",
    "Lingering in this void makes you feel unwell, "
    "and you somewhat feel like leaving",
]

# For text escape codes.
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
DARK_GRAY = "\033[1;30m"
BOLD = "\033[1m"
WHITE = "\033[0m"
