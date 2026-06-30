with open('c:/frontend_quad/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if '<div class="app-nav"' in line:
        skip = True
    
    if skip and '</div>' in line:
        skip = False
        continue
    
    if not skip:
        new_lines.append(line)

with open('c:/frontend_quad/index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
