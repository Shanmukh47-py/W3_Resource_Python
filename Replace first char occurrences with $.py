input_string = "success" #input("Enter input string")
first_char = input_string[0]
result = first_char + input_string[1:].replace(first_char,"$")
print(result)