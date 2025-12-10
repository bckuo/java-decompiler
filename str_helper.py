import os


def parsePath(root_path: str, jar_path: str):
    relative_path = jar_path.removeprefix(root_path + os.sep)
    folders = relative_path.split(os.sep)
    group_id = ".".join(folders[:-3])
    artifact_id = folders[-3]
    version = folders[-2]
    jar = folders[-1]
    return group_id, artifact_id, version, jar


def setLibraryPath(output_path: str, group_id: str, artifact_id: str):
    folders = [output_path, group_id, artifact_id]

    cur = "."
    for folder in folders:
        cur = os.path.join(cur, folder)
        if not os.path.exists(cur):
            os.mkdir(cur)
    # os.makedirs(os.sep.join(folders))

    library_path = os.path.join(*folders)

    return library_path


def wrapExtension(ext: str) -> str:
    return f"^\\.{ext}$"
