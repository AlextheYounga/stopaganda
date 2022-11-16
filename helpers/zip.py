import zipfile

def zipfolder(path, filename, move=''):
    def zipdir(path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))

    def delete_old_export_files(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                os.remove(path + file)

    zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    zipdir(path, zipf)
    zipf.close()
    delete_old_export_files(path)
    if (move):
        os.rename(filename, f"{move+filename}.zip")
        return
    os.rename(filename, f"{path+filename}.zip")


def unzip_folder(directory, filepath):
    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(directory)