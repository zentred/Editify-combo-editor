import re
import colorama
from colorama import init, Fore, Back, Style
init()

def suffix(combo):
    output = []
    print(green + '\n[SUFFIX]' + red + '\nEnter a suffix')
    suffix = input('')
    for c in combo:
        try:
            username, password = str(c).split(':', 2)
            password = f'{password}{suffix}'
            output.append(f'{username}:{password}\n')
        except: pass
    print(cyan + 'Completed.')
    with open('output.txt','w') as e:
        e.writelines(output)

def prefix(combo):
    output = []
    print(green + '\n[PREFIX]' + red + '\nEnter a prefix')
    prefix = input('')
    for c in combo:
        try:
            username, password = str(c).split(':', 2)
            password = f'{prefix}{password}'
            output.append(f'{username}:{password}\n')
        except: pass
    print(cyan + 'Completed.')
    with open('output.txt','w') as e:
        e.writelines(output)

def strip(combo):
    output = []
    print(green + '\n[STRIP]' + red + '\nEnter a character(s) to strip')
    strip = input('')
    if not strip in '1234567890':
        strip = f'{strip}{strip.upper()}'
    for c in combo:
        try:
            username, password = str(c).split(':', 2)
            for s in strip:
                password = password.replace(s, '')
            output.append(f'{username}:{password}\n')
        except: pass
    print(cyan + 'Completed.')
    with open('output.txt','w') as e:
        e.writelines(output)

def ep_to_up(combo):
    output = []
    print(green + '\n[EP -> UP]' + red + '\nDo you want to strip symbols from outputted users?')
    choice = input('')
    yes = ['y', 'yes', 'YES', 'Y']
    no = ['n', 'no', 'NO', 'N']
    strip = '-._'
    for c in combo:
        try:
            username, password = str(c).split(':', 2)
            username = username.split('@')[0]
            if choice in str(yes):
                for a in strip:
                    username = username.replace(a, '')
                output.append(f'{username}:{password}\n')
            elif choice in str(no):
                output.append(f'{username}:{password}\n')
        except: pass
    print(cyan + 'Completed.')
    with open('output.txt','w') as e:
        e.writelines(output)

def up_to_ep(combo):
    output = []
    print(green + '\n[UP -> EP]' + red + '\nEnter email domain')
    choice = input('')
    for c in combo:
        try:
            c = c.replace(':', f'@{choice}:')
            output.append(c+'\n')
        except: pass
    print(cyan + 'Completed.')
    with open('output.txt','w') as e:
        e.writelines(output)

def domain_switch(combo):
    output = []
    print(green + '\n[DOMAIN SWITCH]' + red + '\nEnter a domain to switch to')
    choice = input('Switch all domains to: ')
    for c in combo:
        try:
            match = re.findall('@(.*?):', c)
            c = c.replace(match[0], choice)
            output.append(c+'\n')
        except: pass
    print(cyan + 'Completed.')
    with open('output.txt','w') as e:
        e.writelines(output)

def case_swap(combo):
    output = []
    print(green + '\n[PREFIX]' + red + '\nPassword casing is being swapped')
    a = 'abcdefghijklmnopqrstuvwxyz'
    for c in combo:
        d = 0
        try:
            username, password = str(c).split(':', 2)
            for letters in password:
                if letters in a:
                    d += 1
            if d >= 1:
                if str(password[0]).islower() == True:
                    password = password.replace(password[0], password[0].upper())
                elif str(password[0]).isupper() == True:
                    password = password.replace(password[0], password[0].lower())
                output.append(f'{username}:{password}\n')
        except: pass
    print(cyan + 'Completed.')
    with open('output.txt','w') as e:
        e.writelines(output)

def choice():
    print(green + '[MODES]' + red + '\n1 - Suffix\n2 - Prefix\n3 - Strip\n4 - Email:Pass to User:Pass\n5 - User:Pass to Email:Pass\n6 - Domain Switcher\n7 - Case Swap\ninfo - Tells you about what each mode does\n')
    print(green + '\nEnter Mode:')
    mode = input('')
    if mode == '1':
        suffix(combo)
        choice()
    elif mode == '2':
        prefix(combo)
        choice()
    elif mode == '3':
        strip(combo)
        choice()
    elif mode == '4':
        ep_to_up(combo)
        choice()
    elif mode == '5':
        up_to_ep(combo)
        choice()
    elif mode == '6':
        domain_switch(combo)
        choice()
    elif mode == '7':
        case_swap(combo)
        choice()
    elif mode == 'info':
        print(cyan + '\nSuffix - (combo = test:hello123 / input = ! / output = test:hello123!)\nPrefix - (combo = test:hello123 / input = ! / output = test:!hello123)\nStrip - (combo = test:hello123 / input = l / output = test:heo123)\nEmail:Pass to User:Pass - (combo = test@gmail.com:hello123 / output = test:hello123)\nUser:Pass to Email:Pass - (combo = test:hello123 / output = test@gmail.com:hello123)\nDomain Switch - (combo = test@gmail.com:hello123 / input = aol.com / output = test@aol.com:hello123)\nCase Swap - (combo = test:hello123 / output = test:Hello123)\n')
        choice()

green = Fore.GREEN
red = Fore.RED
cyan = Fore.CYAN
combo = open('combo.txt','r').read().splitlines()

choice()
