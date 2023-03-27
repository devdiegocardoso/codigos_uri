document = []
formatted_doc = []
while 1:
    try:
        line = input()
        document.append(line)
        formatted_doc.append(line.strip(' '))
    except EOFError:
        break

start_index = formatted_doc.index('<body>')
end_index = formatted_doc.index('</body>')

for element in document[start_index+1:end_index]:
    print(element)