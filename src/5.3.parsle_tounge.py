import re

def parsle_tounge(file_path, chunk_size=4096):
    pattern = re.compile(r'([a-z]{5,}!)')
    buffer = '' 
    messages = set() 

    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk: 
                break
            decoded_chunk = chunk.decode('latin-1')
            combined = buffer + decoded_chunk
            
            matches = []
            last_end = 0
            for match in pattern.finditer(combined):
                msg = match.group()
                messages.add(msg)
                last_end = match.end()
            
            remaining = combined[last_end:] if last_end > 0 else combined
            
            buffer_match = re.match(r'^[a-z]*', remaining)
            buffer = buffer_match.group() if buffer_match else ''

    return sorted(messages)

if __name__ == '__main__':
    secret_messages = parsle_tounge("resources/logo.jpg")
    for msg in secret_messages:
        print(msg)