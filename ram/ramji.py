import sys
import re

keywords = {
    'False': 'ASATYA',           
    'True': 'SATYA',       
    'and': 'SITARAMA',
    'as': 'BHARAT', 
    'assert': 'YAMRAJ',     
    'break': 'RAVAN',      
    'class': 'KAKSHA',        
    'continue': 'LAKSHMANA',
    'def': 'HANUMAN',       
    'del': 'SITATYAG',
    'elif': 'SUGRIVA',
    'else': 'VIBHISHANA', 
    'except': 'RAMRAJYA',
    'for': 'ANUSHTHAN',
    'from': 'VANVAS',
    'global': 'VISHVAMITRA',
    'if': 'YADI',         
    'import': 'SARASWATI', 
    'in': 'ANTARGATHA',     
    'is': 'HOTA',       
    'lambda': 'MANTRA',  
    'nonlocal': 'PRAJA',    
    'not': 'ADRISHYA',      
    'or': 'RAMRAM',        
    'pass': 'KUMBHAKARNA',  
    'raise': 'UTKRISHTA', 
    'return': 'RAMSETU',   
    'try': 'PRAYAS',    
    'while': 'SADHANA',     
    'with': 'SAATH',        
    'yield': 'PHALA',    
    '==': 'SAMAAN',
    '!=': 'ASAMAAN',
    'print': 'VALMIKI_JI_LIKHO',

    'int': 'SANKHYA',
    'type': 'PRAKAR',
    'str': 'SHABD',
    'float': 'ANSH',
    'bool': 'SATYA-ASATYA',
    'None': 'SHUNYA',  
}
# Lexer
def lexer(input_string):
    # Define the keywords and their corresponding Python equivalents
    
    lines = input_string.strip().split('\n')
    if lines[0] != 'JAI_SHRI_RAM':
        raise ValueError('code likhne se pehle "JAI_SHRI_RAM"')
    if lines[-1] != 'SHRI_RAM_JAI_RAM_JAI_JAI_RAM':
        raise ValueError('code likhne ke baad "SHRI_RAM_JAI_RAM_JAI_JAI_RAM"')
    
    lines = lines[1:-1]
    input_string = '\n'.join(lines)

    # Replace the keywords with their Python equivalents
    for python_equivalent, keyword in keywords.items():
        input_string = input_string.replace(keyword, python_equivalent)

    return input_string

# Get the filename from the command-line arguments
filename = sys.argv[1]

# Read input from the file
with open(filename, 'r') as file:
    input_string = file.read()

# Process the input
try:
    code = lexer(input_string)
    print('Jai Shree Ram! Your code is being executed...\n')
    exec(code)
except SyntaxError as se:
    error_message = str(se)
    for python_keyword, ramji_keyword in keywords.items():
        error_message = error_message.replace('\''+python_keyword+'\'', ramji_keyword)
    print("Shishya use Ram Naam in your code:")
    print(se.args)
except NameError as ne:
    error_message = str(ne)
    for python_keyword, ramji_keyword in keywords.items():
        error_message = error_message.replace('\''+python_keyword+'\'', ramji_keyword)
    print("Shishya Ram Naam me hul hai:")
    print(ne)
except Exception as e:
    print("Apka code RAM bharose:")
    error_message = str(e)
    for python_keyword, ramji_keyword in keywords.items():
        error_message = error_message.replace('\''+python_keyword+'\'', ramji_keyword)
    # raise type(e)(error_message)
    print(error_message)