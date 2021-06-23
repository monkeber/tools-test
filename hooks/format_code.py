import sys
from subprocess import call

if len(sys.argv) <= 1:
    sys.exit(0)

file_list = sys.argv[1:]

for file in file_list:
    command = ["clang-format", "-style=chromium", "-i", file]
    return_code = call(command)
    if return_code != 0:
        raise Exception("There is some issue with clang-format")
    command = ["git", "add", file]
    call(command)
