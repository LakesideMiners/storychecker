import re

with open('input.txt', 'r') as f:
    content = f.read()
    content_new = re.sub('(cyn-nick|Cyn-nick|cyn-Nick)', "Cyn-Nick", content, flags=re.M)

print(content_new)
