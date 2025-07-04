# utils.py
def extract_messages(file_path):
    messages = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if '-' in line and ':' in line:
                try:
                    msg = line.split('-', 1)[1].split(':', 1)[1].strip()
                    messages.append(msg)
                except IndexError:
                    continue
    return messages
