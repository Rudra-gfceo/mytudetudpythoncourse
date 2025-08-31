user_input = input("Enter some data to write to the file: ")

with open("my.txt", "w") as file:
    file.write(f"{user_input}\n")

with open("my.txt", "a") as file:
    file.write("This line was appended to the file.\n")

print("\nFinal content of 'my.txt':")
with open("my.txt", "r") as file:
    for line in file:
        print(line.strip())
#i added 12 in my.txt file