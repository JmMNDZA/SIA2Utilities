## External Tools Setup

Go to **Settings → Tools → External Tools**.

Click **+** and fill in the fields below. In every tool, set **Group** to `QT` so they're grouped. PyCharm creates the group the first time you type the name. Leave the other checkboxes at their defaults.

### 1. Convert UI to PY

- **Name:** Convert UI to PY
- **Program:** `$PyInterpreterDirectory$/pyside6-uic`
- **Arguments:** `$FilePath$ -o $FileDir$/ui_$FileNameWithoutExtension$.py`
- **Working directory:** `$FileDir$`

### 2. Open in Designer

Opens the selected `.ui` file.

- **Name:** Open in Designer
- **Program:** `$PyInterpreterDirectory$/pyside6-designer`
- **Arguments:** `$FilePath$`
- **Working directory:** `$FileDir$`

### 3. Convert RSC to PY

For `.qrc` resource files.

- **Name:** Convert RSC to PY
- **Program:** `$PyInterpreterDirectory$/pyside6-rcc`
- **Arguments:** `$FilePath$ -o $ProjectFileDir$/$FileNameWithoutExtension$_rc.py`
- **Working directory:** `$FileDir$`

### 4. Open Designer

Opens Designer blank.

- **Name:** Open Designer
- **Program:** `$PyInterpreterDirectory$/pyside6-designer`
- **Arguments:** *(leave empty)*
- **Working directory:** `$ProjectFileDir$`

> **Note:** After converting UI or RSC to PY, **DO NOT** edit the generated `.py` files. To make changes, open Designer, save the `.ui` or `.qrc` file, then convert it again.
