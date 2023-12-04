import os
import glob
import shutil
import argparse

# parses command line arguments
argParser = argparse.ArgumentParser(description='Organizes files in a directory into folders by extension',
                                    usage='%(prog)s [h] [-d DIR]')
argParser.add_argument('-d', '--dir', help='directory to organize', default='.')
argParser.add_argument('-v', '--verbose', help='toggle verbose output', action='store_true')
args = argParser.parse_args()

# file extensions to organize
extensions = {
    'jpg': 'images',
    'png': 'images',
    'gif': 'images',
    'svg': 'images',
    'exe': 'installers',
    'msi': 'installers',
    'pdf': 'pdfs',
    'xlsx': 'excel',
    'csv': 'excel',
    'rar': 'archives',
    'zip': 'archives',
    'gz': 'archives',
    'tar': 'archives',
    'docx': 'word',
    'doc': 'word',
    'torrent': 'torrents',
    'txt': 'text',
    'py': 'python',
    'pptx': 'powerpoint',
    'ppt': 'powerpoint',
    'mp3': 'audio',
    'wav': 'audio',
    'mp4': 'video',
    'm3u8': 'video',
    'json': 'json',
    'css': 'webdev',
    'html': 'webdev',
    'js': 'webdev',
    'sqlite3': 'sqlite3',
    'xls': 'excel',
    'jpeg': 'images',
    'webp': 'images',
    '7z': 'archives',
    'iso': 'installer images',
    'log': 'logs'
}

# calls back the directory supplied earlier
path = args.dir
# Set verbose to 1 to show all file moves
# Set verbose to 0 to show only basic info

for extension, folder_name in extensions.items():
    # get all the files matching the extension in the dir
    files = glob.glob(os.path.join(path, f"*.{extension}"))
    print(f"[*] Found {len(files)} files with {extension} extension")
    if not os.path.isdir(os.path.join(path, folder_name)) and files:
        # if the folder doesn't exist, create it
        print(f"[+] Making {folder_name} folder")
        os.mkdir(os.path.join(path, folder_name))
    for file in files:
        # for each file with that extension move it to the folder
        basename = os.path.basename(file)
        dst = os.path.join(path, folder_name, basename)
        if args.verbose:
            print(f"[*] Moving {file} to {dst}")
        shutil.move(file, dst)
