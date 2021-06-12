import re, pyperclip

# paste text
txt = pyperclip.paste()

# creates regex for phone number
phoneNumberRegex = re.compile('''
( 
((\d{3})|(\(\d{3}\)))?       #area code
(\s|-)          #first seperator
(\d){3}         #next three digits
-  #second seperator
(\d){4} #last four digits
)
''', re.VERBOSE)

# creates regex for email
emailRegex = re.compile('''
[a-zA-Z0-9_+.-]+ #name part
@ # the @ symbol
[a-zA-Z0-9_+.-]+ #domain
''', re.VERBOSE)

# extracts email
extractedEmail = emailRegex.findall(txt)

# extracts phone number
extractedPhoneNumber = phoneNumberRegex.findall(txt)
PhoneNumberFull= []
for phoneNumber in extractedPhoneNumber:
    PhoneNumberFull.append(phoneNumber[0])
    # goes through list of tuples and adds the first index to the list (the actual #)

# copies extracted to emails to clipboard and format it ~nicely~ and print them!!!!
totalResult = '\n'.join(PhoneNumberFull) + '\n' + '\n'.join(extractedEmail)
print(totalResult)
pyperclip.copy(totalResult)
