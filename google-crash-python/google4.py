def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


x = replace_domain('helloanik@ymail.com', 'ymail.com', 'dev.com')


def change_user_name(email, old_user_name, new_user_name):
    user_name = email.split('@')[0]
    if old_user_name in user_name:
        current_user_name = new_user_name
        return current_user_name
    return old_user_name


x = change_user_name('helloanik@bd.com', 'helloanik', 'anik_2021')


def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()


# print(initials("Universal Serial Bus"))
# print(initials("local area network"))
# print(initials("Operating system"))


def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""
    for word in input_string.strip():
        word = word.lower()
        if word != "":
            new_string = new_string + word
            reverse_string = word + reverse_string
    if new_string == reverse_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))
print(is_palindrome("abc"))
print(is_palindrome("kayak"))


def replace_ending(sentence, old, new):
    if sentence.endswith(old):
        i = len(old)
        new_sentence = sentence[:-i] + new
        return new_sentence
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
print(replace_ending("The weather is nice in May", "may", "april"))
print(replace_ending("The weather is nice in May", "May", "April"))
