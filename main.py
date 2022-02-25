import string
from uc3mCare import vaccineManager
#from uc3mCare import vaccineRequest


#GLOBAL VARIABLES
letters = string.ascii_letters + string.punctuation + string.digits
shift = 3


def Encode(word):
    ENCODED = ""
    for LETTER in word:
        if LETTER == ' ':
            ENCODED = ENCODED + ' '
        else:
            X__ = (letters.index(LETTER) + shift) % len(letters)
            ENCODED = ENCODED + letters[X__]
    return ENCODED

def Decode(word):
    ENCODED = ""
    for LETTER in word:
        if LETTER == ' ':
            ENCODED = ENCODED + ' '
        else:
            X__ = (letters.index(LETTER) - shift) % len(letters)
            ENCODED = ENCODED + letters[X__]
    return ENCODED

def Main():
    MNG = vaccineManager()
    RES = MNG.ReadAccessRequestFromJSON("test.json")
    STRRES = RES.__str__()
    print(STRRES)
    ENCODERES= Encode(STRRES)
    print("Encoded Res "+ ENCODERES)
    DECODERES = Decode(ENCODERES)
    print("Decoded Res: " + DECODERES)


if __name__ == "__main__":
    Main()
