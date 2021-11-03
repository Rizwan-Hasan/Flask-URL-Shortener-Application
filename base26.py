"""
For 7 letter hash,
Start from number 308915776
End at 8031810175
"""


class Base26Converter:
    def __init__(self):
        self.__BASE26: tuple = tuple("abcdefghijklmnopqrstuvwxyz")
        self.__BASE26INDEX: dict = dict()
        for i, char in enumerate(self.__BASE26):
            self.__BASE26INDEX[char] = i

    def __encodeToBase62(self, decimal: int):
        if decimal <= 0:
            return 0
        else:
            quotient, reminder = divmod(decimal, len(self.__BASE26))
            ans: str = self.__BASE26[reminder]
            while quotient != 0:
                quotient, reminder = divmod(quotient, len(self.__BASE26))
                ans = "{0}{1}".format(self.__BASE26[reminder], ans)
            return ans

    def encode(self, decimal: int):
        return self.__encodeToBase62(decimal)


if __name__ == "__main__":
    print("Hello World")
