import re
text = '''elon musks phone number is 9910202030 call  him if you have any questions on dodgecoin teslas revenue is 40 billion american number is (123)-123-1234'''
pattern = '\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches = re.findall(pattern,text)
print(matches)