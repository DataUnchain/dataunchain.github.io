import os
import re

directory = r"c:\Users\hp\Documents\GitHub\dataunchain.github.io"

for root, dirs, files in os.walk(directory):
    if '.git' in root or '_site' in root or '.github' in root or 'assets' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.md')):
            path = os.path.join(root, file)
            try:
                with open(path, 'rb') as f:
                    content = f.read().decode('utf-8')
                
                def replacer(match):
                    inner = match.group(1)
                    inner = inner.replace('\r\n', ' ').replace('\n', ' ').replace('\r', ' ')
                    while '  ' in inner:
                        inner = inner.replace('  ', ' ')
                    return 'description: "' + inner + '"'
                    
                new_content = re.sub(r'description:\s*"([^"]*)"', replacer, content)
                if new_content != content:
                    with open(path, 'wb') as f:
                        f.write(new_content.encode('utf-8'))
                    print(f"Fixed: {path}")
            except Exception as e:
                print(f"Error on {path}: {e}")
