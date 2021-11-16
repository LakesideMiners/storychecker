import re  # We need Regex
import shutil  # Copy tool
import difflib  # Diff tool
import os

# Make a copy of the file, the way this works will never change, so its
# not a function
shutil.copy("input.txt", "copyfile.txt")


# TODO make this delate the files if they exist

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
    with open("copyfile.txt") as f1, open("output.txt") as f2:  # Open two files
        content1 = f1.read().splitlines(keepends=True)  # Read the file
        content2 = f2.read().splitlines(keepends=True)
        # Create a tool object, set it to wrap then at 80 chars
        diff = difflib.HtmlDiff(wrapcolumn=80)
        result = diff.make_file(
            content1,
            content2,
            context=True,
            numlines=5)  # Get file comparison results,
        # show the context rather then full file, and shows 5 lines of context
        diff_file = open("diffoutput.html", "w")
        # Output results, you can see the source code written in html)
        diff_file.write(result)
        diff_file.close()


# format is
replace_words(str("(cyn-nick|Cyn-nick|cyn-Nick)"), str("Cyn-Nick"))
replace_words(str("why"), str("APPLE"))  # This is just a test,
create_diff()
print("Done")
