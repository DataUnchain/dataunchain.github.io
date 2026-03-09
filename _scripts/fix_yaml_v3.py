import os
import re

directory = r"c:\Users\hp\Documents\GitHub\dataunchain.github.io"

def fix_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        def replacer(match):
            inner = match.group(1)
            # Remove \r and \n from inner text
            inner_clean = inner.replace('\n', ' ').replace('\r', '')
            # Clean up double spaces
            while '  ' in inner_clean:
                inner_clean = inner_clean.replace('  ', ' ')
            return 'description: "' + inner_clean + '"'

        # Find description: "..."
        # We need to make sure we don't accidentally match across the whole file if there's a missing quote
        # So we match description: "[anything but quote]"
        new_content = re.sub(r'description:\s*"([^"]*)"', replacer, content)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed: {filepath}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")

for root, dirs, files in os.walk(directory):
    if '.git' in root or '_site' in root or '.github' in root or 'assets' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.md')):
            path = os.path.join(root, file)
            fix_file(path)
