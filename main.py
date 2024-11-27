#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('C:\\Users\\Malpertui\\PycharmProjects\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Input\\Names\\invited_names.txt') as file:
    raw_names = file.readlines()

with open('C:\\Users\\Malpertui\\PycharmProjects\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt') as file:
    letter = file.read()

for name in raw_names:
    name = name.strip()
    ready_letter = letter.replace('[name]', name)
    with open(f'C:\\Users\\Malpertui\\PycharmProjects\\Mail+Merge+Project+Start\\Mail Merge Project Start\\Output\\ReadyToSend\\letter_for_{name}.txt', 'w') as file:
        file.write(ready_letter)
