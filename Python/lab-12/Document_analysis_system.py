
a=input("Enter a sentance: ")

print("================================")
print("DOCUMENT ANALYSIS REPORT")
print("================================")
vowel=0
consonent=0
digit=0
space=0
spc=0
words=0
for ch in a:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowel+=1
        else:
            consonent+=1
    elif ch.isdigit():
        digit+=1
    elif ch.isspace():
            space+=1
    words=len(a.split())
else:
    spc+=1

print(f"Sentence : {a}")

total_ch=len(a)

print("Total Characters: " , total_ch)


print("==================CHARACTER BREAKDOWN==================")


print(f"vowel:      {vowel}\nconsonent:  {consonent}\ndigit:      {digit}\nspace:      {space}\nspc:        {spc} \nwords:      {words}")




print("=============SUMMARY===============")

total=vowel+consonent
print("Total letters:" , total)


if total > 0:
    print("Vowel percentage:", round(vowel/total*100, 2), "%")

print("=======================================")
print("Analysis Complete!")
print("=======================================")