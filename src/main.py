import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

basepath = ""
if sys.argv[0]:
    basepath = sys.argv[0]
else:
    basepath = "/"
dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = dir_path_static + "/content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(basepath, dir_path_content, template_path, dir_path_public)


main()
