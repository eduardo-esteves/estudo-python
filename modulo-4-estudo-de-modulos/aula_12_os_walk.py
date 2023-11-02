import os


# CPBA 284

base_dir = "/home/esteves"
downloads = os.path.join(base_dir, 'Downloads')
_counter = 0

if os.path.exists(downloads):
    for root_dir, dirs, files in os.walk(downloads):
        _counter += 1
        print(_counter, 'Pasta atual', root_dir)

        for _dir in dirs:
            print(' ', _counter, 'Dir:', _dir)

        for file in files:
            path_completo = os.path.join(root_dir, file)
            print(' ', _counter, 'FILE:', path_completo)
