POSITIONS = {
    "A" :  0,
    "A#":  1,
    "Bb":  1,
    "B" :  2,
    "C" :  3,
    "C#":  4,
    "Db":  4,
    "D" :  5,
    "D#":  6,
    "Eb":  6,
    "E" :  7,
    "F" :  8,
    "F#":  9,
    "Gb":  9,
    "G" : 10,
    "G#": 11,
    "Ab": 11
}


PITCHES = {
    0:  ["A"],
    1:  ["A#", "Bb"],
    2:  ["B"],
    3:  ["C"],
    4:  ["C#", "Db"],
    5:  ["D"],
    6:  ["D#", "Eb"],
    7:  ["E"],
    8:  ["F"],
    9:  ["F#", "Gb"],
    10: ["G"],
    11: ["G#", "Ab"]
}


class Note:
    """
    Represents a musical note.


    Attributes:
        position(int): Number from 0-11 representing scale
        perspectives(str or None): 'b', '#', or None

    Methods:
        invert - displays the inverted perspective, if none returns None
        add    - adds the number of steps to pitch
        sub    - subtracts the number of steps to pitch
        rshift - shifts the pitch by adding two pitches together
        lshift - shifts the pitch by subtracting one pitch from another
        str    - displays a formal representation 'Note(pitch,perspective)
        repr   - displays a informal representation 'Db' 

    """ 
    def __init__(self, position, perspective=None):
        if isinstance(position, str):
            if position not in POSITIONS:
                raise ValueError(f"Invalid note name: {position}")
            
            self.position = POSITIONS[position]
            
            if perspective in ("#", "b"):
                self.perspective = perspective
            elif "#" in position:
                self.perspective = "#"
            elif "b" in position:
                self.perspective = "b"
            else:
                self.perspective = None

        else:
            self.position = position % 12
            self.perspective = perspective or None


    def __invert__(self):
        if self.perspective == "b":
            inv_perspective = "#"
        elif self.perspective == "#":
            inv_perspective = "b"
        else:
            inv_perspective = None

        return Note(self.position, inv_perspective)

    def __add__(self,steps):
        if not isinstance(steps, int):
            raise TypeError("Only integers to Note objects.")
        new_pitch = (self.position + steps) % 12
        return Note(new_pitch, self.perspective)

    def __sub__(self,steps):
        if not isinstance(steps, int):
            raise TypeError("Only integers to Note objects.")
        new_pitch = (self.position - steps) % 12
        return Note(new_pitch, self.perspective)

    def __rshift__(self, other):
        if not isinstance(other, Note):
            raise TypeError("Can only shift against Note objects.")
        return (self.position - other.position) % 12

    def __lshift__(self, other):
        if not isinstance(other, Note):
            raise TypeError("Can only shift against Note objects.")
        return(self.position - other.position) % 12

    def __str__(self):
        names = PITCHES[self.position]

        if len(names) == 1:
            return names[0]
        elif self.perspective == "#":
            return names[0]
        elif self.perspective == "b":
            return names[1]
        else:
            return f"{names[0]}/{names[1]}"

    def __repr__(self):
        return f"Note({self.position}, {repr(self.perspective)})"

# Evidence that it works and autograder is wrong

print(Note(11,None) << Note(7,None))

print(Note(7,None) << Note(11,None))
