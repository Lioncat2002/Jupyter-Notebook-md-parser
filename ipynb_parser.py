from pprint import pprint
import re
import sys
import os
OUTPUT_DIR='generated'
def help_command():
        print('Usage:')
        print('python ipynb_parser.py ipynb_exported_file.md')
        print('Example usage:')
        print('python ipynb_parser.py testing.md')
        print('\n\n')
        print('output directory is optional')
if len(sys.argv)!=2:
    print('Error! Incorrect usage\n\n')
    help_command()
    exit(1)
if sys.argv[1]=='help':
    help_command()
    exit(0)


file=open(sys.argv[1])
r=file.read().split('\n')
file.close()
stack=[]
output=''
is_in_code_block=False
counter=0
for i in r:
    if re.match("^```python$",i):
        is_in_code_block=True
    elif re.match("^```$",i):
        
        is_in_code_block=False
        output='\n'.join(stack)
        print(f'Generating...{counter}_program.py')
        if not os.path.isdir(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        file=open(f'{OUTPUT_DIR}/{counter}_program.py','w')
        file.write(output)
        file.close()
        counter+=1
        
        stack=[]
        
        
    else:
        if is_in_code_block:
            stack.append(i)
