def rot13(l):
    result=''
    for i in l:
        if i.islower():
            if i.isalpha():
                new_code=ord(i)
                if new_code<=109:
                    new_code+=13
                else:
                    new_code-=13
                result+=chr(new_code)
        elif i.isupper():
            if i.isalpha():
                new_code=ord(i)
                if new_code<=109:
                    new_code+=13
                else:
                    new_code-=13
                result+=chr(new_code)
        else:
            result+=i
    return result

if __name__=='__main__':
    print(rot13('test'))
    print(rot13('TeSt'))
    print(rot13('fgsagfjsdfijgosirg4534%@#$% 5jky5n 5g'))
