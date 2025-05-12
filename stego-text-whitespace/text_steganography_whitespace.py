
with open('binary_message.txt', 'r') as file:
    binary_message = file.read().strip() 

with open('ascii_message.txt', 'r') as file1:
    count = 0  
    hidden_chunks = [] 

    while True:
        data = file1.readline()  
        if not data:  
            break

        data = data.strip()
        chunk_list = data.split()

        if count < len(binary_message): 
            if binary_message[count] == '1':
                for i in range(len(chunk_list)):
                    if chunk_list[i] == '32':
                        chunk_list.insert(i + 1, '32')
                        break
            elif binary_message[count] == '0':
                count_32 = 0
                for i in range(len(chunk_list)):
                    if chunk_list[i] == '32':
                        count_32 += 1
                        if count_32 == 2:  
                            chunk_list.insert(i + 1, '32')
                            break
            count += 1  

        hidden_chunks.append(' '.join(chunk_list))

with open('Steg.txt', 'w') as file2:
    file2.write('\n'.join(hidden_chunks) + '\n')

print("Da hoan thanh giau tin va luu vao 'Steg.txt'.")

