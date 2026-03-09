import os
import codecs

def remove_bom(filepath):
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
        if data.startswith(codecs.BOM_UTF8):
            print(f"Removing BOM from: {filepath}")
            with open(filepath, 'wb') as f:
                f.write(data[3:])
    except Exception as e:
        print(f"Failed on {filepath}: {e}")

repo_dir = r"c:\Users\hp\Documents\GitHub\dataunchain.github.io"
print("Starting BOM scan...")
for root, dirs, files in os.walk(repo_dir):
    if '.git' in root or '_site' in root or '.github' in root or 'assets' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.md', '.yml', '.xml', '.txt', '.py', '.json')):
            filepath = os.path.join(root, file)
            remove_bom(filepath)
print("BOM scan complete.")
