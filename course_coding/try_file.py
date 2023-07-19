from set import *
# def caesar_encrypt(text, shift):
#     encrypted_text = ""
#     for char in text:
#         if char.isalpha():
#             if char.isupper():
#                 encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
#             else:
#                 encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
#         else:
#             encrypted_text += char
#     return encrypted_text
#
#
# def caesar_decrypt(text, shift):
#     decrypted_text = ""
#     for char in text:
#         if char.isalpha():
#             if char.isupper():
#                 decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
#             else:
#                 decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
#         else:
#             decrypted_text += char
#     return decrypted_text
#
#
# # 示例用法
# message = "Hello, World!114"
# shift_amount = 3
#
# encrypted_message = caesar_encrypt(message, shift_amount)
# print("加密后的消息:", encrypted_message)
#
# decrypted_message = caesar_decrypt(encrypted_message, shift_amount)
# print("解密后的消息:", decrypted_message)


d = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",
     9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",
     17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
def code_1_next():
    r = random.randint(1,7)
    text = ""
    for i in range(r):
        a = d[random.randint(1,26)]
        text += a
    return text


def code_1(txt):
    ls = []
    length = len(txt)
    res = ""
    num = length
    a = 0
    cnt = 0
    while num != 0:
        if a == 0:
            ls.append(res)
            res = ""
            if length <= 6:
                a = randint(1, length)
                if a >= num:
                    a = num
                ls.append(code_1_next())
                ls.append(a)

            else:
                a = randint(1, 6)
                ls.append(code_1_next())
                ls.append(a)


        if cnt != length:
            if txt[cnt] != " ":
                res = res + txt[cnt]
                cnt += 1
                a -= 1
                num -= 1
            else:
                cnt += 1
        else:
            break
    ls.append(res)

    res = ""
    for i in range(len(ls)):
        res = res + str(ls[i])
    return res

print(code_1("im a famous"))
