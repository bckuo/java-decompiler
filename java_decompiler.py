import subprocess
import os
import re
from typing import List, Callable, Any
from collections import deque
from tqdm import tqdm
from functools import partial
from dotenv import dotenv_values

from bfs import bfs
from str_helper import parsePath, setLibraryPath, wrapExtension


CONFIG = dotenv_values(".env")

# Root of the library to decompile
ROOT_PATH = CONFIG["ROOT_PATH"]
OUTPUT_PATH = "output"

# Path to Java 17
JAVA = CONFIG["JAVA"]
SUBPROCESS_KARGS = {"shell": True, "capture_output": True, "text": True}


def unzip(root_path: str, jar_path: str, output_path: str):
    group_id, artifact_id, _, _ = parsePath(root_path, jar_path)
    library_path = setLibraryPath(output_path, group_id, artifact_id)

    result = subprocess.run(
        f"cd {library_path} && jar -xf {jar_path}", **SUBPROCESS_KARGS
    )
    # print(result)


def decomplie(class_path: str):
    dirname = os.path.dirname(class_path)
    result = subprocess.run(
        f"{JAVA} -jar fernflower.jar -dgs=1 {class_path} {dirname}", **SUBPROCESS_KARGS
    )
    # print(result)


def unzipRoot(root_path: str, output_path: str):
    print(f"Unzip jar under {root_path} to {output_path}:")
    root = root_path
    exclude = []
    file_extension = wrapExtension("jar")
    execute = partial(unzip, root_path, output_path=output_path)
    bfs(root, exclude, file_extension, execute)


def decomplieOutput(output_path: str):
    print(f"Decompile class file under {output_path}:")
    root = os.path.join(os.getcwd(), output_path)
    exclude = []
    file_extension = wrapExtension("class")
    execute = decomplie
    bfs(root, exclude, file_extension, execute)


def main():
    unzipRoot(ROOT_PATH, OUTPUT_PATH)
    decomplieOutput(OUTPUT_PATH)
    pass


if __name__ == "__main__":
    main()
