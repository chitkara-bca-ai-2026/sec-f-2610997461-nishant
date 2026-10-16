Sentence = input("Enter a sentence: ")

Position = int(input("Enter position for indexing: "))

Character = Sentence[Position]

Start_Index = int(input("Enter start index for slicing: "))
End_Index = int(input("Enter end index for slicing: "))

Sliced_String = Sentence[Start_Index:End_Index]

Uppercase = Sentence.upper()
Lowercase = Sentence.lower()

Word_To_Replace = input("Enter word to replace: ")
Replacement_Word = input("Enter replacement word: ")

After_Replace = Sentence.replace(Word_To_Replace, Replacement_Word)

Length = len(Sentence)


print("--- Processing Results ---")

print(f"Character at position {Position} : '{Character}' ")
print(f"Sliced string [{Start_Index}:{End_Index}] : '{Sliced_String}'")
print(f"Uppercase                    : {Uppercase}")
print(f"Lowercase                    : {Lowercase}")
print(f"After replace                : {After_Replace}")
print(f"Length of sentence           : {Length}")

print(f"==========================================")
print(f"Analysis Complete!")
print(f"==========================================")
