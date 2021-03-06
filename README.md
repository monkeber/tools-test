# Tools-Test

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

This project was created in order to test different tools such as git hooks, build systems, package managers, etc. for managing and developing software.

# Setting Up

## Python Scripts

Python scripts for building require such packages to be installed with pip:
- termcolor

## Git Hooks

For pre commit git hooks I use a tool written in Python called [pre-commit](https://pre-commit.com/). Git hooks are being configured once per cloned repo by a developer and then could be updated automatically without involving every dev on a team.

0. Install Python 3 if you don't have it already on your machine and make sure that `python3` alias is accessible from your environment (symlink may need to be created).
1. Install [clang-format](https://llvm.org/builds/) and make sure it is accessible from your environment.
1. Run `pip3 install pre-commit`.
    - Check that installation is successful:
        ```bash
        $ pre-commit --version
        pre-commit 2.13.0
        ```
    - You may need to install it globally if after installation from pip it doesn't get recognized by your shell.
1. Run `pre-commit install` && `pre-commit install -t commit-msg` and you are done with the hooks! They will run automatically before each commit.

# Commit Style

I incorporated [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) with imperative English as the style for commits.

# Build

For complete build you can use python scripts from `scripts` directory.

For generating files for Visual Studio you can run this command from the build directory:
```
cmake .. -G"Visual Studio 16 2019" -T "v142" -A x64
```
