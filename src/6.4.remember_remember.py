from PIL import Image
import os

def remember_remember(image_path):
    try:
        img = Image.open(image_path).convert('RGB')
        pixels = img.load()
        width, height = img.size
        
        message = []
        
        for x in range(width):
            for y in reversed(range(height)):
                r, g, b = pixels[x, y]
                if r <= 15 and g <= 15 and b <= 15:
                    message.append(chr(y))
                    break
            else:
                message.append('�')
        
        return ''.join(message)
    
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return None

if __name__ == '__main__':
    image_path = os.path.abspath('resources/code.png')
    secret = remember_remember(image_path)
    print("\nDecrypted message:", secret if secret else "DECRYPTION FAILED")