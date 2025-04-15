from note import Note

# note = Note(1)
# print(note)

bar1 = Note(7, None)
bar2 = Note(11, None)
print (bar2 << bar1)

bar1 = Note(11, None)
bar2 = Note(7, None)
print (bar2 << bar1)

# bar = Note(4, 'b')

# sub = bar - 1
# print(sub.position, sub.perspective)

# add = bar + 1
# print(add.position, note.perspective)

# foo = ~bar
# print(foo.position,foo.perspective)
