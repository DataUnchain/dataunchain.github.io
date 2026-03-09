import os
import re

directory = r"c:\Users\hp\Documents\GitHub\dataunchain.github.io"

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the frontmatter block
    if not content.startswith('---'):
        return
        
    end_idx = content.find('\n---\n', 3)
    if end_idx == -1:
        end_idx = content.find('\n---', 3)
        if end_idx == -1:
            return

    frontmatter = content[:end_idx]
    rest = content[end_idx:]

    # In frontmatter, find description: "..."
    def replace_newlines(match):
        s = match.group(1)
        s = s.replace('\n', ' ').replace('\r', '')
        s = re.sub(' +', ' ', s)
        return 'description: "' + s + '"'

    new_frontmatter = re.sub(r'description:\s*"([^"]*)"', replace_newlines, frontmatter, flags=re.DOTALL)

    if new_frontmatter != frontmatter:
        new_content = new_frontmatter + rest
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed: {filepath}")

for root, dirs, files in os.walk(directory):
    if '.git' in root or '_site' in root or '.github' in root or 'assets' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.md')):
            path = os.path.join(root, file)
            try:
                fix_file(path)
            except Exception as e:
                print(f"Error on {path}: {e}")
