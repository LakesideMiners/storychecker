import re  # We need Regex
import shutil  # Copy tool
from difflib import Differ

# Make a copy of the file, the way this works will never change, so its not a function
shutil.copy("input.txt", "copyfile.txt")


# Replace the contents of the file
def replace_words(pattern, replace_with):
    with open("input.txt", 'r') as pre:
        content = pre.read()
        content = re.sub(pattern, replace_with, content, flags=re.M)
    with open("output.txt", 'w') as post:
        post.write(content)
    pre.close()
    post.close()


def create_diff():
    file1 = open("input.txt")
    file2 = open("copyfile.txt")
    with open("file1.txt") as f:
        file1_lines = f.readlines()
    with open("file2.txt") as f:
        file2_lines = f.readlines()
    d = Differ()
    difference = list(d.compare(file1_lines, file2_lines))
    difference = '\n'.join(difference)
    print(difference)
    diff = difflib.ndiff(f1_content, f2_content)
    output = difflib.SequenceMatcher(None, file1.read(), file2.read())
    print(output)


replace_words(str("(cyn-nick|Cyn-nick|cyn-Nick)"), str("Cyn-Nick"))
create_diff()
