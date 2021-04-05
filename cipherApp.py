
# Python program to implement Atbash Cipher
'''
--Upper Case Chiper Char
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ZYXWVUTSRQPONMLKJIHGFEDCBA

--Lower Case Chiper Char
abcdefghijklmnopqrstuvwxyz
zyxwvutsrqonmlkjihgfedcba

'''

chiperDict={'A':'Z','B':'Y','C':'X','D':'W','E':'V','F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N',
            'N':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A',
            'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
            'k': 'p', 'l': 'o', 'm': 'n',
            'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd',
            'x': 'c', 'y': 'b', 'z': 'a',' ':' ',
            }

def getChiper(words):
    chiper=''
    for char in words:
           chiper+=chiperDict[char]

    return chiper

if __name__=='__main__':

    str= input("Enter the String for Chiper:")
    chiperString=getChiper(str)
    print(f"Chiper String is:{chiperString}")


'''
input:
Enter the String for Chiper:Dablu Prasad

output:
Chiper String is:Wzyof Kizhzw
'''