import os
import math

bus = 149
Pl = 300.0
PF = 0.98
folder_path = r"D:\studies\organon\vale\vitoria\sensib_300"

def format_number(number):
    if number >= 10000:
        formatted = f"{number:.0f}"
    elif number >= 1000:
        formatted = f"{number:.1f}"
    elif number >= 100:
        formatted = f"{number:.2f}"
    elif number >= 10:
        formatted = f"{number:.3f}"
    else:
        formatted = f"{number:.4f}"
    
    return formatted[:5]

for subdir, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.PWF'):
            file_path = os.path.join(subdir, file_name)

            with open(file_path, 'r', encoding='latin-1') as file:
                content = file.readlines()

            section_started = False
            for i, line in enumerate(content):
                if line.strip() == 'DBAR':
                    section_started = True
                    continue
                if line.strip()[0] == '(':
                    continue
                if section_started:
                    if line.strip() == '99999':
                        break
                    line_parts = line.split()
                    if int(line_parts[0]) == bus:
                        existing_Pl = float(line[58:63].strip()) if line[58:63].strip() else 0.0
                        existing_Ql = float(line[63:68].strip()) if line[63:68].strip() else 0.0

                        updated_Pl = existing_Pl + Pl
                        updated_Ql = existing_Ql + Ql

                        new_line = (line[:58] + f"{format_number(updated_Pl):>5}" + f"{format_number(updated_Ql):>5}" + line[68:])
                        content[i] = new_line

            with open(file_path, 'w', encoding='latin-1') as file:
                file.writelines(content)

            print(f"The file {file_path} has been successfully updated.")