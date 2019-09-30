#! python 3
# bulletPointAdder.py - Add mark's  on start Wikipedia
# each lines
import pyperclip
text = pyperclip.paste()

#TODO: Separates to lines and adds asterisks.

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* '+ lines[i] # cycles through all indexes in list "lines"  in loop

text = '\n'.join(lines)

pyperclip.copy(text)

print('Mudança concluida')