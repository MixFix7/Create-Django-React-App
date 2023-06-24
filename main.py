import os
import shutil
import subprocess
from colorama import Fore, Style
from tqdm import tqdm


def open_project_in_pycharm(django_project):
    subprocess.Popen(['explorer', django_project])


def create_new_website(new_project_folder: str):
    try:
        files = []
        for foldername, subprocess, filenames in os.walk("Website"):
            for filename in filenames:
                source_file = os.path.join(foldername, filename)
                files.append(source_file)

        progress_bar = tqdm(total=len(files), unit='file', ncols=80)

        for file in files:
            relative_path = os.path.relpath(file, "Website")
            new_project_file = os.path.join(new_project_folder, relative_path)

            os.makedirs(os.path.dirname(new_project_file), exist_ok=True)
            shutil.copy2(file, new_project_folder)
            progress_bar.update(1)

        progress_bar.close()

        print(Fore.GREEN + Style.BRIGHT + 'Creating a new website was successful')
        # open_project_in_pycharm(f"{new_project_folder}/backend")
    except shutil.Error as e:
        progress_bar.close()
        print(Fore.RED + Style.BRIGHT + f"Error: {e}")
    except OSError as e:
        progress_bar.close()
        print(Fore.RED + Style.BRIGHT + f"System Error: {e}")
    except KeyboardInterrupt:
        progress_bar.close()
        print(Fore.YELLOW + Style.BRIGHT + "Stopping...")
        shutil.rmtree(new_project_folder)
        print(Fore.YELLOW + Style.BRIGHT + "Creation has stopped")


if __name__ == "__main__":
    create_new_website(input("> "))

