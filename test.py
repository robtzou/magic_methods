from note import Note

note = Note(1, "b")
print(note)

bar1 = Note(8)
bar2 = Note(3)
print (bar1 << bar2)

bar = Note(4, 'b')

sub = bar - 1
print(sub.pitch, sub.perspective)

add = bar + 1
print(add.pitch, note.perspective)

foo = ~bar
print(foo.pitch,foo.perspective)
