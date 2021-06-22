import sys
from subprocess import call

if len(sys.argv) <= 1:
    sys.exit(0)

file_list = sys.argv[1:]

for file in file_list:
    command = ["clang-format", "-style=chromium", "-i", file]
    call(command)
    command = ["git", "add", file]
    call(command)
