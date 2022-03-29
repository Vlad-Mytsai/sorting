import os
import os.path


def sorting():
    for root, dirs, parts in os.walk(".", topdown=False):
        for name in parts:
            part = os.path.join(root, name)
            file = os.path.join(name)
            extension = file.rsplit(".", 1)
            if file == "sorting.py" or file == "sorting.exe":
                part = os.getcwd() + "\\" + part
                new_path = part
                os.rename(part, new_path)

            elif len(extension) > 1 and (
                    extension[1].lower() == "jpg" or extension[1].lower() == "png" or extension[1].lower() == "svg" or
                    extension[1].lower() == "gif" or extension[1].lower() == "psd" or extension[1].lower() == "ai"):
                part = os.getcwd() + "\\" + part
                new_path = image + file
                os.rename(part, new_path)

            elif len(extension) > 1 and (
                    extension[1].lower() == "mp4" or extension[1].lower() == "avi" or extension[1].lower() == "mkv"):
                part = os.getcwd() + "\\" + part
                new_path = video + file
                os.rename(part, new_path)

            elif len(extension) > 1 and (
                    extension[1].lower() == "exe" or extension[1].lower() == "msi"):
                part = os.getcwd() + "\\" + part
                new_path = prog + file
                os.rename(part, new_path)

            elif len(extension) > 1 and (
                    extension[1].lower() == "doc" or extension[1].lower() == "docx" or extension[1].lower() == "pdf" or
                    extension[1].lower() == "xls" or extension[1].lower() == "xlsx" or extension[1].lower() == "txt"):
                part = os.getcwd() + "\\" + part
                new_path = doc + file
                os.rename(part, new_path)

            elif len(extension) > 1 and (
                    extension[1].lower() == "zip" or extension[1].lower() == "rar" or extension[1].lower() == "7z"):
                part = os.getcwd() + "\\" + part
                new_path = arch + file
                os.rename(part, new_path)

            elif len(extension) > 1 and extension[1].lower() != "":
                part = os.getcwd() + "\\" + part
                new_path = oth + file
                #if os.path.exists(oth + file):
                #     new_path = oth + file.rsplit(".", 1)[0] + " - Копия." + file.rsplit(".", 1)[1]
                #    os.rename(part, new_path)
                #else:
                os.rename(part, new_path)


sort = os.getcwd() + "\\Sorted"
image = os.getcwd() + "\\Sorted\Images\\"
video = os.getcwd() + "\\Sorted\Videos\\"
prog = os.getcwd() + "\\Sorted\Programs\\"
doc = os.getcwd() + "\\Sorted\Documents\\"
arch = os.getcwd() + "\\Sorted\Archives\\"
oth = os.getcwd() + "\\Sorted\Other\\"

fold = [image, video, prog, doc, arch, oth]

if os.path.isdir(sort):
    for i in range(len(fold)):
        if os.path.isdir(fold[i]):
            continue
        else:
            os.mkdir(fold[i])
    sorting()
else:
    os.mkdir(sort)
    os.mkdir(image)
    os.mkdir(video)
    os.mkdir(prog)
    os.mkdir(doc)
    os.mkdir(arch)
    os.mkdir(oth)
    sorting()
