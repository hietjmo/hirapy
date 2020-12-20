
# Usage: python hirapy.py example-1.txt

from romkan import to_hiragana,to_katakana
import sys
import re

repl_hira = [
  (r"(?<=\W)wa(?=\W)","ha"),
  (r"(?<=\W)o(?=\W)", "wo"),
]

repl_rom = [
  (r"\*", ""),
]

def hira_and_kata (jp):
  result = ""
  for a,b in repl_hira:
    jp = re.sub (a,b,jp)
  for i,p in enumerate (jp.split ("*")):
    f = [to_hiragana,to_katakana][i%2]
    result += f (p)
  return result

def wordlist (jpen):
  jp,en = jpen
  return hira_and_kata (jp) + "\t" + en

def romaji (jp):
  for a,b in repl_rom:
    jp = re.sub (a,b,jp)
  return jp

part1,part2,part3 = "","",""

filename = sys.argv [1]
with open (filename) as f:
  s1 = f.readlines()
for s in s1:
  jpen = s.split ("\t")
  if len (jpen) == 1:
    part1 += hira_and_kata (jpen[0])
    part2 += romaji (jpen[0])
  if len (jpen) > 1: 
    part3 += wordlist (jpen)

print (part1 + part2 + part3)

