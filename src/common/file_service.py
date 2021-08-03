from os import write


def write_list(content: list, path: str):
    #writes the contents of a list to a file 
    with open(path,'w') as file:
        for tx in content:
            file.write(str(tx)+'\n')

def write_source_code(content: str, path: str):
    with open(path,'w') as file:
        file.write(content)