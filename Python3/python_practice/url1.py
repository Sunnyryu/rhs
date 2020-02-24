import re
url = input()
print(re.match('http[s]*:\/\/[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\/*[a-zA-Z0-9-_.?=/]*', url) != None)
