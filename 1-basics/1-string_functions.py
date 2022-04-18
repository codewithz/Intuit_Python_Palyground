name="Zartab"
print(name)
print(type(name))

# String can be enclosed in "Some String's" | 'Some String'

# Multi Line String

paragraph="""
India is my country
All Indians are my brothers and sisters
I love my country
"""

print(paragraph)

# Strings are iterable in Python

word="Kitkat"

print(word[1])

print(word[1:3])

print(word[-4])


# print(word[9])
# IndexError: string index out of range

print(word[0:20])

print(word[1:])

print(word[:5])

# Length

print("Length",len(word))

# Trimming -- strip()

word_with_spaces="   hello world   "
print("Length before trimming",len(word_with_spaces));
print(word_with_spaces)
word_with_spaces=word_with_spaces.strip();
print("Length after trimming",len(word_with_spaces))
print(word_with_spaces)

# Casing

company="intuit"
print("Company:",company)

company=company.upper()
print("Company:",company)

sentence="I AM HAPPY TO BE HERE"
print("Sen:",sentence)

sentence=sentence.lower()
print("Sen:",sentence)

sentence=sentence.capitalize()
print("Sen Capitalize:",sentence)

sentence=sentence.title()
print("Sen Title:",sentence)

#  Replacement
language="Jxvx"
print(language)
language=language.replace("x","a");
print(language)

# Split a String

line="1,Tom,IT,Dev,20000"
print("O:",line)

data=line.split(",");
print("S:",data)
print(type(data))

# Format Functions

line="My name is Zartab, I am {} years old"
age=31

fline=line.format(age)
print("O:",line)
print("F:",fline)

line="My name is {}, I am {} years old"
name="Micheal"
age=35

fline=line.format(name,age)
print("O:",line)
print("F:",fline)

# Numbered Formating

line="Hey I am a {0}, I train my {1},{1} asks doubt to {0}"
trainer="Trainer"
trainee="Trainee"

fline=line.format(trainer,trainee)
print("O:",line)
print("F:",fline)

# Named Formating
line="Hey I am a {trainer}, I train my {trainee},{trainer} asks doubt to {trainee}"


fline=line.format(trainer="TRAINER",trainee="TRAINEE")
print("O:",line)
print("F:",fline)

#  Count

name="Zartab"
a_count=name.count("a");
print("Count of a in ",name," is ",a_count)

#  Escape Characters

#  \n - New Line
#  \t Tab
#  \\ Backslash
#  \" Double Quotes

text='this is a backslash \\'
print(text)
text='this are two backslash \\\\'
print(text)
#  I work at "Intuit"

text="I work at \"Intuit\""
print(text)


