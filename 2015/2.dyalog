l w h←↓⍉a←↑⍎¨¨'\d+'⎕S'&'¨⊃⎕NGET'2.txt'1
p1←(+/(2×l×w)+(2×w×h)+(2×h×l)) + +/×/↑s←2↑¨{⍵[⍋⍵]}¨↓a
p2←+/2×+/↑s + +/(l×w×h)
p1 p2
