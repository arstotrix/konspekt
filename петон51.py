def divide(filename):
    with open (filename, encoding="utf-8") as f:
        lineraw=f.readlines()
    lines=[]
    for line in lineraw:
        clear_line=line.strip()
        if clear_line:
            lines.append(clear_line)
        return lines

lines = divide('text.txt')
print(lines)
    
    
