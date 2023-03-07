import os


dirs = [
    os.path.join('data','raw'),
    os.path.join('data','processed'),
    'notebooks',
    'saved_models',
    'src'
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok = True)
    with open(os.path.join(dir_,'.gitkeep')) as f:
        pass

files = [
    'dvc.yaml',
    'paramal.yaml',
    '.gitignore',
    os.path.join('src','__init__.py')
]

for file_ in files:
    os.makedirs(file_, exist_ok = True)
    with open(os.path.join(file_,'.gitkeep')) as f:
        pass

