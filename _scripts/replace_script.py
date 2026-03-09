import os

directory = r"c:\Users\hp\Documents\GitHub\dataunchain.github.io"

replacements = [
    ("LocalLayer", "DataUnchain"),
    ("locallayer.github.io", "dataunchain.com"),
    ("https://github.com/locallayer/locallayer", "https://github.com/dataunchain/dataunchain"),
    ("/locallayer/", "/dataunchain/"),
    ("locallayer", "dataunchain") # Catch-all for remaining URLs and IDs
]

for root, dirs, files in os.walk(directory):
    if '.git' in root or '_site' in root or '.github' in root or 'assets' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.md', '.yml', '.txt', '.xml', '.scss', '.py')):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original = content
                
                # Careful replacements to avoid double-replacing
                # Actually, if we just do locallayer.github.io -> dataunchain.com first, then locallayer -> dataunchain, it's fine.
                content = content.replace("LocalLayer", "DataUnchain")
                content = content.replace("locallayer.github.io", "dataunchain.com")
                content = content.replace("github.com/locallayer/locallayer", "github.com/dataunchain/dataunchain")
                content = content.replace("locallayer", "dataunchain")
                
                if content != original:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated: {path}")
            except Exception as e:
                print(f"Failed {path}: {e}")
