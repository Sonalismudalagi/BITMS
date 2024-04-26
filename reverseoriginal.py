input_string = input("Enter the string")
special_char= [char for char in input_string if not char.isalnum()]
alpha_char = [char for char in input_string if char.isalnum()]

    # Reverse alpha characters
reversed_alpha = ''.join(alpha_char[::-1])

    # Inserting slecial character
reversed_string = ''
for char in input_string:
    if char.isalnum():
            reversed_string += reversed_alpha[0]
            reversed_alpha = reversed_alpha[1:]
    else:
            reversed_string += char

print(reversed_string)