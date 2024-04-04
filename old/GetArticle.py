import random
from JOC import *


# List of journals
journals = [
    "The Journal of Organic Chemistry",
    "The Journal of the American Chemical Society",
    "Organic Letters"
]

# Randomly select a journal from the list
#selected_journal = random.choice(journals)
selected_journal = "The Journal of Organic Chemistry"

#call correct journal module based on the randomly selected result
if selected_journal == "The Journal of Organic Chemistry":
    JOC()






