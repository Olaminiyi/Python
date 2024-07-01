# contents = ["gbemi soke", "Gbemi dide", "fami lowo soke"]

# filenames = ["doc.txt", "report.txt", "presentation.txt"]

# for content, filename in zip(contents, filenames):
#     file = open(f"../files/{filename}", 'w')
#     file.write(content)

# ==================================================================
# create a program that:

# 1. prompts the user to enter a new member.

# 2. adds that member to members.txt at the end of the existing members. For example, the user here has entered the member

# user_prompt = input("Add a new member: ") + "\n"
# file = open('../files/members.txt', 'r')
# newfile = file.readlines()
# file.close()
# newfile.append(user_prompt)

# file = open('../files/members.txt', 'w')
# file.writelines(newfile)
# file.close()

# solution

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# for file in (filenames):
#     file = open(f"../files/{file}", 'w')
#     file.write("Hello")
#     file.close()

# ===============================================================================

# Please download the three text files a.txt, b.txt, and c.txt from the resources and place them in your computer IDE.

# Then, create a program that:

# 1. reads each text file and

# 2. prints out the content of each file in the command line.

# The expected output would be like the following:



# solution

# filename = ['../files/members.txt', '../files/doc.txt', '../files/presentation.txt']

# for files in filename:
#     file = open(files, 'r')
#     content = file.read()
#     print(content)