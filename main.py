"""
Given a string as input, print the following pattern. Note that you need to
maintain two strings
String1 : where the characters from the input string are being added
String2: Where the output string is being created
Input: "123"
Output: 1#12#123#
"""

st = "123"
ln = len(st)
pt = "#"
st1 = ""
st2 = ""
for i in range(0,ln):
  ch = st[i]
  st1 = st1 + ch
  st2 = st1 + pt
  print(st2,end="")