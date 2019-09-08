
import sys
sys.path.append("mymodules")
import mymodules
from mymodules.mathy import *
print(responses[0])
while True:
    text=input("Enter some text\n")
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract_number_from_text(text)
                r=operations[word.upper()](l[0],l[1])
                print(r)
            except:
                print("something is wrong, please retry")
            finally:
                break

        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()
        
