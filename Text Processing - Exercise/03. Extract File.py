fail_path = input().split("\\")
fail_name_extension = fail_path[-1].split(".")

print(f"File name: {fail_name_extension[0]}")
print(f"File extension: {fail_name_extension[1]}")