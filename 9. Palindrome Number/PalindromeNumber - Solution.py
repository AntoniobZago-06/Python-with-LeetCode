class Solution:

    def isPalindrome(self):


        while True:

            
            try:
                number = int(input("\nDigite o número e veja se é um palindrome: "))
                number = str(number)

                if number == "0": break

                elif len(number) >= 2 and number[::-1] == number: print("\nTrue")

                elif len(number) >= 2 and number[::-1] != number: print("\nFalse")
                
                elif len(number) < 2: print("\nO número deve ter no mínio 2 dígitos")

            except:
                print("\nValor inválido!!")          



if __name__ == "__main__":

    palindromeNumber = Solution()
    palindromeNumber.isPalindrome()
