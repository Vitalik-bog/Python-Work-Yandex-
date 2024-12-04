def encode(word):
   out = ''
   for symbol in word:
      if symbol.lower() in MorseCode: out += MorseCode[symbol.lower()]+' '
      else: out += symbol
   return out
MorseCode = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--.." }
line = input().split()
print('\n'.join(map(lambda x: encode(x).rstrip(), line)))
