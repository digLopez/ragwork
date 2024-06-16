import os

from docx import Document as word_loader

import config


def get_file_list(filepath: str = config.KNOWLEDGE_FILE_BASE_PATH):
    file_list = []
    for dirpath, _, filenames in os.walk(filepath):
        for filename in filenames:
            file_list.append(os.path.join(dirpath, filename))
    return file_list


def read_file_para(filepath: str):
    file = word_loader(filepath)
    return [para.text for para in file.paragraphs]


def read_file(filepath: str):
    para_list = read_file_para(filepath)
    return "".join(para_list)


if __name__ == "__main__":
    fl = get_file_list("../knowledge_files/")
    for fn in fl:
        f = read_file_para(fn)
        print(f)
