import re  # We need Regex
import shutil  # Copy tool
import difflib  # Diff tool
import os
import glob


# Create the "datafiles" folder if it does not exist
def create_folder():
    if not os.path.exists('datafiles'):
        os.makedirs('datafiles')
    else:
        print('folder already exists')


# Remove Old Files
def remove_old():
    files = glob.glob('datafiles/*.*', recursive=True)
    for file in files:
        try:
            os.remove(file)
            print(str(file) + " Removed")
        except OSError:
            print("File: " + str(file) + " does not exist, skipping.")


# Replace the contents of the file
def replace_words(pattern, replace_with):
    print("Replacing: " + pattern + " with: " + replace_with)
    with open("../input.txt", 'r') as pre:
        content = pre.read()
        content = re.sub(pattern, replace_with, content, flags=re.M)
    with open("datafiles/output.txt", 'w') as post:
        post.write(content)
    pre.close()
    post.close()


# Make the diff
def create_diff():
    print("Creating Diff View")
    with open("datafiles/copyfile.txt") as f1, open("datafiles/output.txt") as f2:  # Open two files
        content1 = f1.read().splitlines(keepends=True)  # Read the file
        content2 = f2.read().splitlines(keepends=True)
        diff = difflib.HtmlDiff(wrapcolumn=100)  # Create a tool object, set it to wrap then at 80 chars
        result = diff.make_file(content1, content2, context=True, numlines=2)  # Get file comparison results,
        # show the context rather then full file, and shows 2 lines of context
        diff_file = open("diffoutput.html", "w")
        diff_file.write(result)  # Output results, you can see the source code written in html)
        diff_file.close()


# Do Shit Here
create_folder()
remove_old()
shutil.copy("../input.txt", "datafiles/copyfile.txt")
replace_words("(cyn-nick|Cyn-nick|cyn-Nick)", "Cyn-Nick")
create_diff()
print("Done")
