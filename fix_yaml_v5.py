import os
import re

directory = r"c:\Users\hp\Documents\GitHub\dataunchain.github.io"

for root, dirs, files in os.walk(directory):
    dirs[:] = [d for d in dirs if d not in ['.git', '_site', '.github', 'assets']]
    for file in files:
        if file.endswith(('.html', '.md')):
            path = os.path.join(root, file)
            try:
                with open(path, 'rb') as f:
                    content = f.read().decode('utf-8')
                
                # We want to replace multi-line descriptions
                # like description: "text \n text"
                # to single-line
                def replacer(match):
                    inner = match.group(1)
                    if '\n' in inner or '\r' in inner:
                        inner = inner.replace('\r\n', ' ').replace('\n', ' ').replace('\r', ' ')
                        while '  ' in inner:
                            inner = inner.replace('  ', ' ')
                        return 'description: "' + inner + '"'
                    return match.group(0)
                    
                new_content = re.sub(r'description:\s*"([^"]*)"', replacer, content)
                if new_content != content:
                    with open(path, 'wb') as f:
                        f.write(new_content.encode('utf-8'))
                    print(f"Fixed Description: {path}")
            except Exception as e:
                pass
