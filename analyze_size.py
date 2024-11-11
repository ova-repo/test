import os

def get_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return sum(get_size(os.path.join(path, f)) for f in os.listdir(path))
    return 0

def analyze_directory(directory='.'):
    items = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        item_size = get_size(item_path)
        items.append((item, item_size))

    items.sort(key=lambda x: x[1], reverse=True)

    for item, size in items:
        print(f"{item}: {size} байт")

analyze_directory()
