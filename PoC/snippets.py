f = open(".\Poc\snippets.txt",'r',encoding = 'utf-8')

lines = []
lineStr = ""
for line in f:
    if line != '\n':
        if ('    ') in line:
            lines.append(line.replace('    ', '\t'))
            lineStr += line.replace('    ', '\t')
        else:
            lines.append(line)
            lineStr += line

print(lines)
f.close()
output = open(".\Poc\outputs.txt",'w',encoding = 'utf-8')
output.write(lineStr)
output.close()