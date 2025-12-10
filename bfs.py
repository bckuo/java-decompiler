import os
import re
from typing import List, Callable
from collections import deque
from tqdm import tqdm


def getChildrenPaths(path: str, exclude: List[str]) -> List[str]:
    return [
        os.path.join(path, child) for child in os.listdir(path) if child not in exclude
    ]


def bfs(root: str, exclude: List[str], file_extension: str, execute: Callable):
    q = deque([root])
    while q:
        for _ in tqdm(range(len(q))):
            cur_path = q.popleft()

            if os.path.isdir(cur_path):
                # print(cur_path)
                q.extend(getChildrenPaths(cur_path, exclude))
                continue

            if not re.match(file_extension, os.path.splitext(cur_path)[1]):
                continue

            execute(cur_path)
