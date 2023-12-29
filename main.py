from os import path, listdir, mkdir
from time import sleep
from shutil import move

# pip install rich
from rich.console import Console
from rich.prompt import Prompt


def main():
    console = Console()
    prompt = Prompt()

    console.print("[red]Title:[/] AutoFileSorter")
    console.print("[red]Author: [cyan]ᴋ ᴀ ɪ ᴢ ᴇ ɴ")
    console.print("[red]Version:[/] '1.0.0'")
    console.print("-------------------")

    console.print(
        "[yellow]\[INFO] Before Starting, Specify the folder path for automated file sorting")

    while True:
        folder = prompt.ask("[blue]Enter a Folder Path")
        if path.isdir(folder):
            break

        console.print("[bright_red]\[ERR] Enter a valid Path to a Folder")

    console.print("[red]\[AutoFileSorter][/] is now [spring_green3]active")
    auto_sort_files(folder)


def auto_sort_files(folder: str):
    while True:
        found_files = []
        for f in listdir(folder):
            f_path = path.join(folder, f)

            if path.isfile(f_path):
                found_files.append(f_path)

        if found_files:
            list(map(sort_file, found_files))
        sleep(0.1)


def sort_file(file_path: str):
    # You can further expand the file types
    # by adding them in the dictionary below
    sort_map = {
        'Documents': ['pdf', 'docx'],
        'Music': ['mp3'],
        'Photos': ['png', 'jpeg', 'jpg'],
        'Videos': ['mp4', 'mkv'],
    }

    file_type = file_path.split('.')[-1]
    result = [key for key, values in sort_map.items() if file_type in values]

    if not result:
        result = 'Others'
    else:
        result = result[0]

    file_name = path.basename(file_path)
    folder_path = path.dirname(file_path)
    target_folder = path.join(folder_path, result)

    if not path.exists(target_folder):
        mkdir(target_folder)

    move(file_path, path.join(target_folder, file_name))

    console = Console()
    console.print(f'Moved [cyan]{file_name}[/] to [yellow]{result}')


if __name__ == '__main__':
    main()
