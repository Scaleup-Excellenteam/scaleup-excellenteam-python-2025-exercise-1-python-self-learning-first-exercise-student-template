import re
import os

def parsle_tongue(file_path=None, chunk_size=4096):
    if file_path is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, '../resources/logo.jpg')
    
    pattern = re.compile(r'([a-z]{5,})')
    buffer = ''
    messages = set()

    try:
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                
                try:
                    decoded_chunk = chunk.decode('latin-1', errors='ignore')
                except UnicodeDecodeError:
                    continue
                    
                combined = buffer + decoded_chunk
                
                last_end = 0
                for match in pattern.finditer(combined):
                    msg = match.group(1)
                    if len(msg) >= 5:
                        messages.add(msg)
                    last_end = match.end()
                
                buffer = combined[last_end:] if last_end > 0 else combined

        return sorted(messages)
    
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []

if __name__ == '__main__':
    secret_messages = parsle_tongue()
    print("Found messages:", secret_messages)