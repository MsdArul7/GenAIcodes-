#Create a program that counts how many lines, words, and characters exist in a text file.Write a script to copy the contents of one text file into another, but exclude all lines that start with a “#” symbol
line_count = 0
word_count = 0  
char_count = 0

with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
    for line in infile:
        line_count += 1
        words = line.split()
        word_count += len(words)
        char_count += len(line)
        if not line.lstrip().startswith("#"):
            outfile.write(line)
print(f"Total lines: {line_count}")
print(f"Total words: {word_count}")
print(f"Total characters: {char_count}")
