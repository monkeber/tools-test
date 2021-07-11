import argparse
import os
import shutil
import subprocess
import time
import json
from termcolor import colored

#
# Few helper function for printing messages.
#


def PrintError(text: str):
    print(colored(text, "red"))


def PrintInfo(text: str):
    print(colored(text, "green"))


def PrintWarning(text: str):
    print(colored(text, "yellow"))

#
# Script body.
#


parser = argparse.ArgumentParser()

# Optional parameters.
parser.add_argument("-G", "--generator", type=str,
                    help="specifies which generator to use with CMake, i.e. 'Visual Studio 16 2019'",
                    default="Visual Studio 16 2019")
parser.add_argument("-T", "--toolset", type=str,
                    help="specifies toolset name if supported by generator",
                    default="v142")
parser.add_argument("--delete-build-dir",
                    help="deletes build directory before starting build process",
                    action="store_true")
parser.add_argument("--build",
                    help="builds the application after generating",
                    action="store_true")
parser.add_argument("--build-type", type=str,
                    help="specifies the build type",
                    choices=["Debug", "Release"],
                    default="Debug")

args = parser.parse_args()

# Show current configuration to the user.
print("Building current configuration:")
print("\tgenerator={}".format(args.generator))
print("\ttoolset={}".format(args.toolset))
print("\tdelete-build-dir={}".format(args.delete_build_dir))
print("\tbuild={}".format(args.build))
print("\tbuild-type={}".format(args.build_type))

build_dir = "../build/{}".format(args.build_type)
if args.delete_build_dir:
    PrintInfo("Deleting {} directory...".format(build_dir))
    try:
        shutil.rmtree(build_dir)
    except FileNotFoundError:
        PrintInfo("Nothing to delete, proceeding to the next step...")

try:
    os.mkdir(build_dir)
except FileExistsError:
    PrintInfo("Build directory already exists...")
except OSError:
    PrintError("Cannot create build directory, exiting...")
    quit()

PrintInfo("Generating CMake files...")
os.chdir(build_dir)

generate_start = time.time()

cmake_command = ("cmake ../.. -G\"{}\" -T \"{}\" -A x64 "
                 "-DCMAKE_BUILD_TYPE={}")
cmake_command = cmake_command.format(
    args.generator, args.toolset, args.build_type)
process = subprocess.run(cmake_command)

generate_end = time.time()
if process.returncode != 0:
    PrintError("Generating finished with errors!")
    quit()
else:
    PrintInfo("Generating finished!")

build_start = 0
build_end = 0

if args.build:
    build_start = time.time()
    PrintInfo("Building application...")
    process = subprocess.run("cmake --build . --config {}".format(args.build_type))

    build_end = time.time()
    if process.returncode != 0:
        PrintError("Build finished with errors!")
    else:
        PrintInfo("Build finished!")

PrintInfo("Generating time: {}s".format(generate_end - generate_start))
if args.build:
    PrintInfo("Build time: {}s".format(build_end - build_start))
    PrintInfo("Total time: {}s".format(build_end - generate_start))
