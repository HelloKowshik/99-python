def get_word(sentence, n):
    if n > 0:
        words = sentence.split()
        if n <= len(words):
            return words[n - 1]
    return ""


# print(get_word("This is a lesson about lists", 4)) # Should print: lesson
# print(get_word("This is a lesson about lists", -4)) # Nothing
# print(get_word("Now we are cooking!", 1)) # Should print: Now
# print(get_word("Now we are cooking!", 5)) # Nothing

def full_email(people):
    user_list = []
    for email, name in people:
        user_list.append("{}<{}>".format(name, email))
    return user_list


# print(full_email([("user1@bd.com", "User-1"), ("user2@bd.com", "User-2"), ("user3@bd.com", "User-3")]))

x = [x * 2 for x in range(1, 11) if x % 2 == 0]
languages = ['javascript', 'python', 'java', 'C++', 'SQL']
lengths = [len(lang) for lang in languages]
# print(lengths)

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
new_file_names = [file_name.replace('.hpp', '.h') for file_name in filenames]
print(new_file_names)
