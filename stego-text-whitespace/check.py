def text_to_ascii(text):
    return [ord(char) for char in text]

def split_ascii_with_spaces(ascii_codes, k):
    ascii_chunks = []
    count = 0  
    chunk = []
    group_counter = 1  

    for code in ascii_codes:
        if code == 32:
            count += 1
        
        chunk.append(code)

        if count == k:
            ascii_chunks.append(f"A{group_counter}: " + ' '.join(map(str, chunk)))
            chunk = []  
            count = 0  
            group_counter += 1  

    if chunk:
        ascii_chunks.append(f"A{group_counter}: " + ' '.join(map(str, chunk)))
    
    return ascii_chunks

def text_to_binary_6bit(text):
    text_to_binary = {
        '0': '000000', '1': '000001', '2': '000010', '3': '000011', '4': '000100',
        '5': '000101', '6': '000110', '7': '000111', '8': '001000', '9': '001001',
        'A': '010001', 'B': '010010', 'C': '010011', 'D': '010100', 'E': '010101',
        'F': '101100', 'G': '010110', 'H': '010111', 'I': '011000', 'J': '100000',
        'K': '100001', 'L': '100010', 'M': '100011', 'N': '100100', 'O': '100101',
        'P': '100110', 'Q': '100111', 'R': '101000', 'S': '110001', 'T': '110010',
        'U': '110011', 'V': '110100', 'W': '110101', ' ': '010000',
    }
    return ''.join(text_to_binary.get(char, 'UNKNOWN') for char in text)

file_path = 'demo.txt' 
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read() 

    N = text.count(' ') 

    k = int(input("Nhap so khoang trang (k): "))
    
    if k < 3:
        print("Loi: so khoang trang phai lon hon 3.")
    else:
        num_chunks = N // k

        msg = input("Nhap IN HOA thong diep can giau: ") 
        
        binary_msg = text_to_binary_6bit(msg)

        length_msg = len(binary_msg) 

        if num_chunks >= length_msg:
            with open('binary_message.txt', 'w') as f:
                f.write(binary_msg)
            print("Ma nhi phan cua thong diep da duoc luu vao 'binary_message.txt'.")

            ascii_codes = text_to_ascii(text)

            ascii_chunks = split_ascii_with_spaces(ascii_codes, k)

            with open('ascii_message.txt', 'w') as f:
                f.write('\n'.join(ascii_chunks))
            print("Cac chuoi ASCII da duoc luu vao 'ascii_text.txt'.")

        else:
            print(f"Loi: so lupng chuoi con khong du de chua thong diep. Can {length_msg} chuoi con.")
  
except FileNotFoundError:
    print(f"File '{file_path}' khong tim thay.")

