import re

def main():
    ip='((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))'

    mail = '^[a-zA-Z0-9_.-]+@([a-zA-Z0-9]+\.)+(com|cn|me|net|edu|org|club|xyz|mail|pro|gov|info|name|us)$'
    print("Please input a mail address:")
    maddr = input()
    
    if re.search(mail,maddr) !=None:
        print("Success")
    else:
        print("Not match")

    print("Please input a ipv4 address:")
    ipaddr = input()
    
    if re.search(ip,ipaddr) !=None:
        print("Success")
    else:
        print("Not match")

    
main()
