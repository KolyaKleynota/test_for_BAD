text1 = """The Tao gave birth to machine language.  Machine language gave birth
to the assembler.
The assembler gave birth to the compiler.  Now there are ten thousand
languages.
Each language has its purpose, however humble.  Each language
expresses the Yin and Yang of software.  Each language has its place within
the Tao.
But do not program in COBOL if you can avoid it.
        -- Geoffrey James, "The Tao of Programming"
"""

text2 = """C makes it easy for you to shoot yourself in the foot. C++ makes that harder, 
but when you do, it blows away your whole leg. (с) Bjarne Stroustrup"""


def my_foo(first_letters):
    flag = False
    for i in range(len(first_letters)):
        flag = False
        for j in range(i + 1, len(first_letters)):
            if first_letters[i] == first_letters[j]:
                flag = True
        if not flag:
            return first_letters[i]


def unique_letter(text_par):
    text = text_par

    words = text.split()
    first_letters = []

    for word in words:
        first_letters.append(my_foo(word))
    print("here a first letters", first_letters)

    result = my_foo(first_letters)
    print("here is result ", result)


if __name__ == "__main__":
    unique_letter(text2)