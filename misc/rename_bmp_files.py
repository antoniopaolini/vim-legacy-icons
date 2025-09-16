import os

# Rinomina i file BMP secondo la mappatura
mapping = {
    "00": "New",
    "01": "Open",
    "02": "Save",
    "03": "Undo",
    "04": "Redo",
    "05": "Cut",
    "06": "Copy",
    "07": "Paste",
    "08": "Print",
    "09": "Help",
    "10": "Find",
    "11": "SaveAll",
    "12": "SaveSesn",
    "13": "NewSesn",
    "14": "LoadSesn",
    "15": "RunScript",
    "16": "Replace",
    "17": "WinClose",
    "18": "WinMax",
    "19": "WinMin",
    "20": "WinSplit",
    "21": "Shell",
    "22": "FindPrev",
    "23": "FindNext",
    "24": "FindHelp",
    "25": "Make",
    "26": "TagJump",
    "27": "RunCtags",
    "28": "WinVSplit",
    "29": "WinMaxWidth",
    "30": "WinMinWidth",
}

for key, new_name in mapping.items():
    old_filename = f"BuiltIn{key}.bmp"
    new_filename = f"{new_name}.bmp"
    if os.path.exists(old_filename):
        os.rename(old_filename, new_filename)
        print(f"Rinominato: {old_filename} → {new_filename}")
    else:
        print(f"File non trovato: {old_filename}")
