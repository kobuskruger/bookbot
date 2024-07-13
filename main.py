def count_words(string):
  words = string.split()
  return len(words)

def read_file(file_path):
  with open(file_path) as f:
    text = f.read()
    return text
  
def count_characters(string):
  chars = {}
  for char in string:
    lower_char = char.lower()
    if lower_char in chars:
      chars[lower_char] += 1
    else:
      chars[lower_char] = 1
  return chars

def main():
  text = read_file('./books/frankenstein.txt')
  words = count_words(text)
  chars = count_characters(text)
  print('--- Begin report of books/frankenstein.txt ---')

  print(f'{words} words found in the document')

  for char, count in chars.items():
    if not char.isalpha():
      continue
    print(f'The {char} character was found {count} times')

  print('--- End report ---')
main()