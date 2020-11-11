inputRange = range(248345,746315)

def check_for_doubles(inputlist):
  numbersWithPairs = []
  for number in inputlist:
    number = str(number)
    passFlag = False
    if number[0] == number[1]:
      if number[1] != number[2]:
        passFlag = True
    if number[1] == number[2]:
      if number[0] != number[1] and number[2] != number[3]:
        passFlag = True
    if number[2] == number[3]:
      if number[1] != number[2] and number[3] != number[4]:
        passFlag = True
    if number[3] == number[4]:
      if number[2] != number[3] and number[4] != number[5]:
        passFlag = True
    if number[4] == number[5]:
      if number[3] != number[4]:
        passFlag = True
    if passFlag == True:
      numbersWithPairs.append(int(number))
  return(numbersWithPairs)

def check_for_increase(inputlist):
    numbersWhichIncrease = []
    for number in inputlist:
      number = str(number)
      if float(number[0]) <= float(number[1]):
        if float(number[1]) <= float(number[2]):
          if float(number[2]) <= float(number[3]):
            if float(number[3]) <= float(number[4]):
              if float(number[4]) <= float(number[5]):
                numbersWhichIncrease.append(int(number))
    return(numbersWhichIncrease)

def main():
  increasers = check_for_increase(inputRange)
  doubles = check_for_doubles(increasers)
  print(len(doubles))

if __name__ == "__main__":
  main()