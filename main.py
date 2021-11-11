import re

with open('input.txt', 'r') as pre:
    content = pre.read()
    content_new = re.sub('(cyn-nick|Cyn-nick|cyn-Nick)', "Cyn-Nick", content, flags=re.M)
pre.close()

with open('out.txt', 'w') as post:
    post.write(content_new)