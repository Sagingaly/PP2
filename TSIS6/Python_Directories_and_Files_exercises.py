# import os
# path = input("Enter path: ")
# directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
# print("Directories in path:")
# print(directories)
# files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
# print("Files in path:")
# print(files)
# all = os.listdir(path)
# print("All contents in path:")
# print(all)

# import os
# path = input("Enter path to checking: ")
# if os.path.exists(path):
#     print(f"{path} существует")
#     if os.access(path, os.R_OK):
#         print(f"{path} читаемый")
#     else:
#         print(f"{path} не читаемый")
#     if os.access(path, os.W_OK):
#         print(f"{path} доступный для записи")
#     else:
#         print(f"{path} не доступный для записи")
#     if os.access(path, os.X_OK):
#         print(f"{path} исполняемый")
#     else:
#         print(f"{path} не исполняемый")
# else:
#     print(f"{path} не существует")


# import os
# path = input("Введите путь: ")
# if os.path.exists(path):
#     print("Path to directory:", os.path.dirname(path))
#     print("Directory name:", os.path.basename(path))
# else:
#     print("Path does not exist")

# f = "example.txt"
# cnt = 0
# with open(f, "r") as file:
#     for line in file:
#         cnt += 1
# print("Number of lines in", f, ":", cnt)

# l = ["Real", "Kairat", "Chelsea"]
# with open("fruits.txt", "a") as file:
#     for i in l:
#         file.write(i + "\n")
#

# import string
# l = list(string.ascii_uppercase)
# for letter in l:
#     n = letter + ".txt"
#     with open(n, "w") as file:
#         file.write("This is file " + n)

#
# s_file = input("Введите путь к файлу: ")
# d_file = input("Введите путь ко второму файлу: ")
# with open(s_file, "r") as s, open(d_file, "w") as d:
#     contents = s.read()
#     d.write(contents)
# print("File copied successfully!")



# import os
# path = input("Введите путь к файлу: ")
# if os.path.exists(path):
#     if os.access(path, os.W_OK):
#         os.remove(path)
#         print("File deleted successfully")
#     else:
#         print("You don't have permission to delete the file")
# else:
#     print("File does not exist")