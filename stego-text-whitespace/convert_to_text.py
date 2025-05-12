def convert_to_text_from_steg(steg_file):
    with open(steg_file, 'r') as file:
        text = ''
        for line in file:
            line = line.split(':')[-1].strip()  
            ascii_codes = line.split()

            text += ''.join(chr(int(code)) for code in ascii_codes)

    return text

hidden_text = convert_to_text_from_steg('Steg.txt')

with open('hidden_text_complete.txt', 'w') as output_file:
    output_file.write(hidden_text)

print("Da giau tin thanh cong va luu van ban vao 'hidden_text_complete.txt'.")

