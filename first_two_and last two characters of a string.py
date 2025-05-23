input_string = "s" #input("Enter input string")
if len(input_string)<2:
    print("")
else:
    first_2 = input_string[0:2]
    last_2 = input_string[-2:]
    combined = first_2+last_2
    print(combined)