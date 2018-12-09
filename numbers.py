dot = [
'00000000000',
'00000000000',
'00000000000',
'00000000000',
'00000000000',
'00000000000',
'00000000000',
'00000000000',
'00001110000',
'00001110000',
'00000010000'
]

num1 = [
'00000000000',
'00001100000',
'00011100000',
'00001100000',
'00001100000',
'00001100000',
'00001100000',
'00001100000',
'00001100000',
'00111111000',
'00000000000'
]

num2 = [
'00000000000',
'00001110000',
'00111011100',
'01110001110',
'00000011100',
'00000111000',
'00001110000',
'00011100000',
'00111000000',
'01111111100',
'00000000000'
]

num3 = [
'00000000000',
'00001110000',
'00111011100',
'01110001110',
'00000011100',
'00001111000',
'00000011100',
'01110001110',
'00111011100',
'00001110000',
'00000000000'
]

num4 = [

'00000000000',
'00000011000',
'00000111000',
'00001111000',
'00011011000',
'00110011000',
'01100011000',
'01111111110',

'00000011000',
'00000011000',
'00000000000'
]

num5 = [
'00000000000',
'01111111110',
'01100000000',
'01100000000',
'01101111000',
'01110001100',
'01100000110',
'00000000110',
'01100001100',
'00011111000',
'00000000000'
]

num6 = [
'00000000000',
'00111111100',
'01100000110',
'01100000000',
'01111111000',
'01110001100',
'01100000110',
'01100000110',
'00110001110',
'00011111000',
'00000000000'
]

num7 = [
'00000000000',
'01111111110',
'01100000110',
'00000001100',
'00000011000',
'00000110000',
'00001100000',
'00001100000',
'00001100000',
'00001100000',
'00000000000'
]

num8 = [
'00000000000',
'00011111000',
'00110001100',
'01100000110',
'00110001100',
'00011111000',
'00110001100',
'01100000110',
'00110001100',
'00011111000',
'00000000000'
]

num9 = [
'00000000000',
'00011111000',
'00110001110',
'01100000110',
'01100000110',
'00110001110',
'00001110110',
'00000000110',
'01100000110',
'00111111100',
'00000000000'
]

num0 = [
'00000000000',
'00111111000',
'01110011100',
'01100001100',
'01100001100',
'01100001100',
'01100001100',
'01100001100',
'01110011100',
'00111111000',
'00000000000'
]

num0 = [
'00000000000',
'00111111000',
'01110011100',
'01100001100',
'01100001100',
'01100001100',
'01100001100',
'01100001100',
'01110011100',
'00111111000',
'00000000000'
]

grau = [
'0000000',
'0000000',
'0000000',
'0000000',
'0011100',
'0111110',
'0110110',
'0110110',
'0110110',
'0011100',
'0000000'
]

celc = [
'0000000000',
'0001111100',
'0011000110',
'0110000000',
'0110000000',
'0110000000',
'0110000000',
'0110000000',
'0011000110',
'0001111100',
'0000000000'
]

def swith_number(number):
  switcher = {
    '1': num1,
    '2': num2,
    '3': num3,
    '4': num4,
    '5': num5,
    '6': num6,
    '7': num7,
    '8': num8,
    '9': num9,
    '0': num0,
    'º': grau,
    'C': celc,
    '.': dot
  }
  return switcher.get(number, 'invalid')

def get_number(text_number):
  split_number = list(text_number)
  ret = []
  for num in split_number:
    ret.append(swith_number(num))
  return ret









