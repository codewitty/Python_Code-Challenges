import sys
import math

# Prints to standard output.
def reflowLines(line_length, lines):
      # IMPLEMENTATION GOES HERE
  word_list = []
  for i in lines:
      word_list.append(i.split())
  word_list = [y for x in word_list for y in x]
  total_length = 0
  small_list = []



  for index, elem in enumerate(word_list):
      total_length += (len(elem))
      small_list.append(elem)
      if index < len(word_list) - 1 and total_length + len(word_list[index + 1]) + (len(small_list)) <= line_length:
          continue
      elif total_length > 0 and total_length <= line_length:
        if len(small_list) > 2:
            dashes = math.ceil((line_length - total_length) / len(small_list))
            str = ""
            for index, word in enumerate(small_list):
                if index < len(small_list) - 1:
                    str += word + ('-' * dashes)
                else:
                    str += word
                    print(str)
                    str = ""
        elif len(small_list) == 2:
            dashes = (int(math.ceil(line_length - total_length)))
            str = ""
            for index, word in enumerate(small_list):
                if index < len(small_list) - 1:
                    str += word + ('-' * dashes)
                else:
                    str += word
                    print(str)
                    str = ""
        else:
            nstr = ""
            for word in small_list:
                nstr += word
            print(nstr)

        small_list = []
        total_length = 0

  return (word_list)

inputs = ["It was the best", "of times it was", "the worst of times"]
print(reflowLines(20, inputs))
