def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    if s.strip().isdigit():
      return int(s)
    stack = []
    currNum = 0
    i = 0
    
    while i < len(s):
        c = s[i]
        if c == ' ':
            i += 1
            continue
        elif c == '(':
            newNum = calculate(s[i+1:])
            if not stack:
              currNum += newNum[0]
            else:
              operand = stack.pop()
              oldNum = stack.pop()
              if operand == '+':
                  currNum = oldNum + newNum[0]
              else:
                  currNum = oldNum - newNum[0]
            i += newNum[1] + 1
        elif c == ')':
            return [currNum, i]
        elif c == '+':
            stack.append(currNum)
            stack.append(c)            
        elif c == '-':
            stack.append(currNum)
            stack.append(c)
        else:
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            num = s[start:i]
            if not stack:
                currNum = int(num)
            else:
                operand = stack.pop()
                oldNum = stack.pop()
                if operand == '+':
                    currNum = oldNum + int(num)
                else:
                    currNum = oldNum - int(num)
            i -= 1
        i += 1
    return currNum

calculate("(1+(4+35+2)-3)+(6+8)")