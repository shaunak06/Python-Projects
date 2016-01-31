import re
var=raw_input("Enter phonenumber ")

phonepat = '^(\d{3})-(\d{3})-(\d{4,6})'|'(/d{7})'|'((/d{3})-(/d{7}))'
prog= re.compile(phonepat)
result=prog.match(var)
print result

if result:
    print result.string
    
#patern matches
pat= "[abc]" #patern matches to a,b or c and returns true or false
pat= "([abc])" #patern matches makes groups
pat= "([^abc])" #matches with anything that is not s,b or c
pat= "(abc|xyz)" #matches with the specific strings abc and/or xyz
pat= "(abc.*abc)" #matches with any string that is surrounded by abc string ex. abc-any amount of characters-abc
#\w: word characters, numbers and letters
pat= "([a-zA-Z])" #matches a-z for upper and lower case
pat= '(?P<first>[a-zA-Z]+),*(?P<first>)' #makes the second match the same as the first one
#when searching through text re.findall can be used but the data is given back in a list instead of groups