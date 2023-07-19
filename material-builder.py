import os
import json
import shutil

if not os.path.exists("./lapce_out/"):
    os.makedirs("./lapce_out/")

with open("./lapce_out/volt.toml", "w") as voltFile:
    voltFile.writelines("""name = "lapce-material-icon-theme"
display-name = "Material Icon Theme"
icon = "icon.png"
version = "1.0.0"
author = "Reokodoku"
description = "A fork of vscode-material-icon-theme that can be used for Lapce"
icon-themes = ["material.toml"]
repository = "https://github.com/Reokodoku/lapce-material-icon-theme"
""")

shutil.copytree("./icons", "./lapce_out/icons/")
shutil.copy("./logo.png", "./lapce_out/logo.png")
shutil.copy("./LICENSE.md", "./lapce_out/LICENSE.md")

iconsFile = open("./lapce_out/material.toml", "w")

iconsFile.writelines("""[icon-theme]
name = "Material Icon Theme"
[icon-theme.ui]
"settings" = "icons/settings.svg"
"file" = "icons/logo.svg"
#"directory_opened" = "icons/folder.svg"
""")

with open("./dist/material-icons.json") as jsonFile:
    data = json.load(jsonFile)
    
    iconsFile.writelines("[icon-theme.filename]\n")
    for key, value in data["fileNames"].items():
        iconsFile.writelines(f"\"{key}\" = \"icons/{value}.svg\"\n")
    # Additions
    iconsFile.writelines(f"\".vscodeignore\" = \"icons/vscode.svg\"\n")
    iconsFile.writelines(f"\"LICENSE\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENSE.rst\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENSE.md\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENSE.txt\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENSE-AGPL\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENSE-APACHE\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENSE-BSD\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENSE-MIT\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENSE-GPL\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENSE-LGPL\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENCE\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENCE.rst\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENCE.md\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENCE.txt\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENCE-AGPL\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENCE-APACHE\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENCE-BSD\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENCE-MIT\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENCE-GPL\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"LICENCE-LGPL\" = \"icons/certificate.svg\"\n")
    iconsFile.writelines(f"\"README\" = \"icons/readme.svg\"\n")
    iconsFile.writelines(f"\"README.rst\" = \"icons/readme.svg\"\n")
    iconsFile.writelines(f"\"README.md\" = \"icons/readme.svg\"\n")
    iconsFile.writelines(f"\"README.txt\" = \"icons/readme.svg\"\n")
    iconsFile.writelines(f"\"CHANGELOG\" = \"icons/changelog.svg\"\n")
    iconsFile.writelines(f"\"CHANGELOG.rst\" = \"icons/changelog.svg\"\n")
    iconsFile.writelines(f"\"CHANGELOG.md\" = \"icons/changelog.svg\"\n")
    iconsFile.writelines(f"\"CHANGELOG.txt\" = \"icons/changelog.svg\"\n")
    iconsFile.writelines(f"\"CHANGES\" = \"icons/changelog.svg\"\n")
    iconsFile.writelines(f"\"CHANGES.rst\" = \"icons/changelog.svg\"\n")
    iconsFile.writelines(f"\"CHANGES.md\" = \"icons/changelog.svg\"\n")
    iconsFile.writelines(f"\"CHANGES.txt\" = \"icons/changelog.svg\"\n")
    iconsFile.writelines(f"\"CONTRIBUTING\" = \"icons/contributing.svg\"\n")
    iconsFile.writelines(f"\"CONTRIBUTING.rst\" = \"icons/contributing.svg\"\n")
    iconsFile.writelines(f"\"CONTRIBUTING.md\" = \"icons/contributing.svg\"\n")
    iconsFile.writelines(f"\"CONTRIBUTING.txt\" = \"icons/contributing.svg\"\n")
    iconsFile.writelines(f"\"CONTRIBUTORS\" = \"icons/authors.svg\"\n")
    iconsFile.writelines(f"\"CONTRIBUTORS.rst\" = \"icons/authors.svg\"\n")
    iconsFile.writelines(f"\"CONTRIBUTORS.md\" = \"icons/authors.svg\"\n")
    iconsFile.writelines(f"\"CONTRIBUTORS.txt\" = \"icons/authors.svg\"\n")
    iconsFile.writelines(f"\"CREDITS\" = \"icons/credits.svg\"\n")
    iconsFile.writelines(f"\"CREDITS.rst\" = \"icons/credits.svg\"\n")
    iconsFile.writelines(f"\"CREDITS.md\" = \"icons/credits.svg\"\n")
    iconsFile.writelines(f"\"CREDITS.txt\" = \"icons/credits.svg\"\n")
    iconsFile.writelines(f"\"AUTHORS\" = \"icons/authors.svg\"\n")
    iconsFile.writelines(f"\"AUTHORS.rst\" = \"icons/authors.svg\"\n")
    iconsFile.writelines(f"\"AUTHORS.md\" = \"icons/authors.svg\"\n")
    iconsFile.writelines(f"\"AUTHORS.txt\" = \"icons/authors.svg\"\n")
    iconsFile.writelines(f"\"ARCHITECTURE\" = \"icons/architecture.svg\"\n")
    iconsFile.writelines(f"\"ARCHITECTURE.rst\" = \"icons/architecture.svg\"\n")
    iconsFile.writelines(f"\"ARCHITECTURE.md\" = \"icons/architecture.svg\"\n")
    iconsFile.writelines(f"\"ARCHITECTURE.txt\" = \"icons/architecture.svg\"\n")
    
    iconsFile.writelines("[icon-theme.foldername]\n")
    for key, value in data["folderNames"].items():
        iconsFile.writelines(f"\"{key}\" = \"icons/{value}.svg\"\n")
        
    iconsFile.writelines("[icon-theme.extension]\n")
    for key, value in data["fileExtensions"].items():
        iconsFile.writelines(f"\"{key}\" = \"./icons/{value}.svg\"\n")

iconsFile.close()
