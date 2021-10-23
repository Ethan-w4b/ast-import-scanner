import ast
from collections import namedtuple

# issues to look for:
# reading/writing/interacting with files, accessing the network, importing non-approved libs
#print(astunparse.unparse(head))


def scanForTarget(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.With):
            print(node.items)



def scanForFunctions(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            print(node.name)


def scanForImports(file):
    with open(f'{file}','r') as r_file:
        file = r_file.read()
    
    tree = ast.parse(file)
    Import = namedtuple("Import", ["module", "name", "alias"])
    FLAG = False
    good_imports = [['docx'], ['tkinter']]
    found_imports = []

    for node in ast.walk(tree):
        if isinstance(node,ast.Import):
            module = []
        elif isinstance(node, ast.ImportFrom):
            module = node.module.split('.')
        else:
            continue

        for n in node.names:
            r = Import(module, n.name.split('.'), n.asname)
            found_imports.append(r[1])
            #print(r[1])
            if r[1] not in good_imports:
                FLAG = True
            else:
                pass
    return FLAG
