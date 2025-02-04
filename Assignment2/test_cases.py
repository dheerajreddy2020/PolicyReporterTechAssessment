from fsm import mod_three_fsm

input_strings = ['1101',
                 '1110',
                 '1111']
for input_string in input_strings:
    remainder = mod_three_fsm(input_string)
    print(f"The remainder when {input_string} is divided by 3 is: {remainder}")