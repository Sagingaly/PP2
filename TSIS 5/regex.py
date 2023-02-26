"""
1)import re


pattern = r'a[b]*'

strings = ['ab', 'abb', 'a', 'ac', 'abcd', 'bab']
for s in strings:
    if re.match(pattern, s):
        print(f"{s} matches the pattern.")
    else:
        print(f"{s} does not match the pattern.")

2)import re


pattern = r'a[b]{2,3}'


strings = ['ab', 'abb', 'a', 'ac', 'abbb', 'abbbb', 'bab']
for s in strings:
    if re.match(pattern, s):
        print(f"{s} matches the pattern.")
    else:
        print(f"{s} does not match the pattern.")

3)import re


pattern = r'[a-z]+_[a-z]+'

strings = ['hello_world', 'foo_bar', 'this_is_a_test', 'not_a_match', 'Mixed_Case']
for s in strings:
    if re.search(pattern, s):
        print(f"{s} contains a lowercase letter sequence joined with an underscore.")
    else:
        print(f"{s} does not contain a lowercase letter sequence joined with an underscore.")

4)import re


pattern = r'[A-Z][a-z]+'


strings = ['Hello', 'JohnDoe', 'ThisIsASequence', 'NotAMatch', 'Mixed_Case']
for s in strings:
    if re.search(pattern, s):
        print(f"{s} contains a sequence of one uppercase letter followed by lowercase letters.")
    else:
        print(f"{s} does not contain a sequence of one uppercase letter followed by lowercase letters.")

5)import re


pattern = r'a.*b$'


strings = ['abc', 'adcb', 'acbc', 'ab', 'not_a_match_b']
for s in strings:
    if re.search(pattern, s):
        print(f"{s} matches the pattern 'a.*b'.")
    else:
        print(f"{s} does not match the pattern 'a.*b'.")

6)import re


input_string ='This is a, test. With some spaces and dots.'


output_string = re.sub(r'[ ,.]', ':', input_string)


print(output_string)



7)def snake_to_camel(s):
    words = s.split('_')


    capitalized_words = [words[0]] + [word.capitalize() for word in words[1:]]

    camel_case_string = ''.join(capitalized_words)

    return camel_case_string



snake_case_string = 'hello_world_how_are_you'
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)


8)import re


input_string ='SplitThisStringAtUpperCaseLetters'


split_string = re.findall('[A-Z][^A-Z]*', input_string)


print(split_string)

9)import re

input_string = 'InsertSpacesBetweenWordsStartingWithCapitalLetters'


output_string = re.sub(r'(?<!^)(?=[A-Z])', ' ', input_string)

print(output_string)


10)import re

input_string = 'ConvertGivenCamelCaseStringToSnakeCase'

output_string = re.sub(r'(?<!^)(?=[A-Z])', '_', input_string).lower()

print(output_string)
"""
