from random import randint

def caesar_decrypt(text, shift):

    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text

def reverse_code_1(txt):
    length = len(txt)
    res = ""
    i = 0
    while i < length:
        if txt[i].isdigit():
            num = int(txt[i])
            res += txt[i+1:i+1+num]
            i += num + 1
        else:
            i += 1

    return res

def sm(strs):
    smlist = 'bpmfdtnlgkhjqxrzcsyw'
    nosm = ['eR','aN','eN','iN','uN','vN','nG','NG']
    rep = {'ZH':'Zh','CH':'Ch','SH':'Sh'}

    for s in smlist:
        strs = strs.replace(s,s.upper())

    for s in nosm:
        strs = strs.replace(s,s.lower())

    for s in rep.keys():
        strs = strs.replace(s,rep[s])

    for s in nosm:
        tmp_num = 0
        isOk = False
        while (tmp_num < len(strs)) and (isOk==False):
            try:
                tmp_num = strs.index(s.lower(),tmp_num)
            except:
                isOk = True
            else:
                tmp_num = tmp_num + len(s)
                if strs[tmp_num:tmp_num+1].lower() not in smlist:
                    strs = strs[:tmp_num-1]+strs[tmp_num-1:tmp_num].upper()+strs[tmp_num:]

    return strs

def onep(strs):
    restr = ''
    strs = sm(strs)
    for s in strs:
        if 'A' <= s and s <= 'Z':
            restr = restr + ' ' + s
        else:
            restr = restr + s

    restr = restr[1:]
    restr = restr.lower()
    return restr.split(' ')



def struct(ls):
    str = ""
    for i in ls:
        str += i
        str += " "

    return str

def decoding(text):
    txt = text.txt
    txt = reverse_code_1(txt)
    txt = caesar_decrypt(txt, 4)
    txt = struct(onep(sm(txt)))

    return txt




