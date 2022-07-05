
# pop up window settings
#import tkinter as tk
#window = tk.Tk()


# types
topics = ["Software", "Hardware", "Spanish"]
sources = ["Caroline"]



# questions
# paramaters = (question, answer type, a, b, c, d, correct answer, topic, source)
Q1 = (
    "When is a good time to use a linked list?", 
    "0" # 0 = multiple choice, 1 = open-ended 
    "A. Never",
    "B. When you are searching for a data point",
    "C. When you are doing a lot of insertions or removals",
    "D. When you need to ramdonly access a data point",
    "C", # correct answer 
    "Software", # topic 
    "Caroline" # source
    )

print()
print()
print()
print()
answer = input(Q1[0])
print()


# pop up window continued 




# thoughts / features: 
    # allow users to select as many topics as they want (with buttons)
    # ask the user how many and what kind of questions do they want? 
    # maybe have sub topics? ex. software: python, java, OOP, git
    # user can pick answer type, topic, source
    # separate file for questions 