import subprocess

# url = "https://github.com/socialdotbee/timmer"
# url = "https://github.com/naitik0608/digitalmarketingblog"
# subprocess.run(["powershell", f"git clone {url}"])

# print(url.split("/")[-1])

# # f = open("timmer/index.html", "r")
# # data = f.read()
# # f.close()

# # print(type(data))
# # subprocess.run(['powershell', 'ls'])
# # subprocess.run(['powershell', 'node script.js'])
# subprocess.run(["powershell", "cd timmer"])
# subprocess.run(["powershell", "tree"])

# import os

# def folder_size(folder_path):
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(folder_path):
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             total_size += os.path.getsize(fp)
#     return total_size
# fname = url.split("/")[-1]
# # Example usage:
# folder_path = f"D:\\College\\SEM-8\\final-project\\test\\{fname}"
# size_bytes = folder_size(folder_path)
# total_size_kb = size_bytes / 1024
# total_size_mb = total_size_kb / 1024
# total_size_gb = total_size_mb / 1024
# print(f"Size of {folder_path}: {size_bytes} bytes")
# print(f"Size of folder in {total_size_kb} kb")
# print(f"Size of folder in {total_size_mb} mb")
# print(f"Size of folder in {total_size_gb} gb")


import os


def folder_size_and_extensions(folder_path):
    total_size = 0
    extensions = set()

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
            _, ext = os.path.splitext(f)
            extensions.add(
                ext.lower()
            )  # Lowercasing to ensure case-insensitive comparison

    return total_size, extensions


# Example usage:
# folder_path = "D:\\College\\SEM-8\\final-project\\finalProject"
# folder_path = r"D:\Work\Professional\GRRAS\Batches\Regular batches\Alternative\Ongoing\TT\Ongoing\Angular400\day2\wishes"
folder_path = r"D:\Work\Professional\GRRAS\Batches\Regular batches\Alternative\Ongoing\MWF\local\c. 500FullStack\day61"
size_bytes, file_extensions = folder_size_and_extensions(folder_path)
# print(f"Size of {folder_path}: {size_bytes} bytes")
# print("File Extensions:", file_extensions)
final_file_extensions = []
for i in file_extensions:
    if i != "":
        # print(i)
        final_file_extensions.append(i.split(".")[-1])

print(final_file_extensions)
