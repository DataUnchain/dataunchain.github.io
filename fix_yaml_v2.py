import os
import re

directory = r"c:\Users\hp\Documents\GitHub\dataunchain.github.io"

def replace_newlines(match):
    s = match.group(1)
    if '\n' in s or '\r' in s:
        s = s.replace('\n', ' ').replace('\r', '')
        s = re.sub(' +', ' ', s)
        return 'description: "' + s + '"'
    return match.group(0)

for root, dirs, files in os.walk(directory):
    if '.git' in root or '_site' in root or '.github' in root or 'assets' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.md')):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = re.sub(r'description:\s*"([^"]*)"', replace_newlines, content, count=1, flags=re.DOTALL)
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Fixed: {path}")
            except Exception as e:
                print(f"Error on {path}: {e}")
