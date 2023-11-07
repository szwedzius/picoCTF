#This encryption takes two characters out of flag and puts them like this xxxxxxxxyyyyyyyy where x are bits of the
#first char and y are bits of the second char so we need to reverse that process
#def encryption():
#    ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

def decryption(enc_text: str) -> str:
    decrypted_text = ""
    for char in enc_text:
        value_of_current = ord(char)
        first_char = value_of_current >> 8
        second_char = value_of_current - (first_char << 8)
        decrypted_text += chr(first_char) + chr(second_char)

    return decrypted_text



encrypted_text = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽"
print(decryption(encrypted_text))

