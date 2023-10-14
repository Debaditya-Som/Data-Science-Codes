from bardapi import Bard
import os
import time

os.environ['_BARD_API_KEY']="Insert-Key-Here"

input_text = "Tell me about Hacktoberfest 2023"
print(Bard().get_answer(input_text)['content'])