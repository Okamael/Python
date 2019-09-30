#! python 3
# pw.py - um programa para repositorio de senha que não é seguro.

PASSWORDS = {'email':
'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage':'12345'}
import sys, pyperclip
if len(sys.argv)<2:
    print('Usage: python.py [account] - copy account password')
    sys.exit()

account = sys.argv[0] # o primeiro argumento da linha de comando é o nome 

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named '+ account)