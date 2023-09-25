"""
program: chords.py
Author: Jewelia Barnwell
Displays chords for a given key with GUI.

"""
from breezypythongui import EasyFrame
import tkinter.font as font
from tkinter import HORIZONTAL

SCALE = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#',
         'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

class chords(EasyFrame):
    """Displays chords for a given key."""

    def __init__(self):
        """sets window"""
        EasyFrame.__init__(self, title = "Chord Progression Builder")

        # widgits
        self.addLabel(text = "key:", row = 0, column = 0)
        self.key = self.addTextField(text = "", row = 0, column = 1, width = 3)
        self.addLabel(text = "Chords available:", row = 0, column = 4, columnspan = 4)
        self.addLabel(text = "I:", row = 1, column = 4)
        self.first = self.addTextField(text = "", row = 1, column = 5, width = 5)
        self.addLabel(text = "ii:", row = 2, column = 4)
        self.second = self.addTextField(text = "", row = 2, column = 5, width = 5)
        self.addLabel(text = "iii:", row = 3, column = 4)
        self.third = self.addTextField(text = "", row = 3, column = 5, width = 5)
        self.addLabel(text = "IV:", row = 4, column = 4)
        self.fourth = self.addTextField(text = "", row = 4, column = 5, width = 5)
        self.addLabel(text = "V:", row = 5, column = 4)
        self.fifth = self.addTextField(text = "", row = 5, column = 5, width = 5)
        self.addLabel(text = "vi:", row = 6, column = 4)
        self.sixth = self.addTextField(text = "", row = 6, column = 5, width = 5)
        self.addLabel(text = "vii°:", row = 7, column = 4)
        self.seventh = self.addTextField(text = "", row = 7, column = 5, width = 5)

        # list box
        self.listBox = self.addListbox(row = 2, column = 0, rowspan = 4, columnspan = 3)
        self.listBox.insert(0, "A")
        self.listBox.insert(1, "A#")
        self.listBox.insert(2, "B")
        self.listBox.insert(3, "C")
        self.listBox.insert(4, "C#")
        self.listBox.insert(5, "D")
        self.listBox.insert(6, "D#")
        self.listBox.insert(7, "E")
        self.listBox.insert(8, "F")
        self.listBox.insert(9, "F#")
        self.listBox.insert(10, "G")
        self.listBox.insert(11, "G#")
        self.listBox.setSelectedIndex(3)

        # button
        self.addButton(text = "Select", row = 7, column = 0, columnspan = 3, command = self.select)
        
        # adjust font
        self.key['font'] = font.Font(size = 20)
        self.first['font'] = font.Font(size = 15)
        self.second['font'] = font.Font(size = 15)
        self.third['font'] = font.Font(size = 15)
        self.fourth['font'] = font.Font(size = 15)
        self.fifth['font'] = font.Font(size = 15)
        self.sixth['font'] = font.Font(size = 15)
        self.seventh['font'] = font.Font(size = 15)
        
    def select(self):
        """responds to selection of item in the list box.
        updates the field."""
        self.key.setText(self.listBox.getSelectedItem())
        index = self.listBox.getSelectedIndex()
        if index > -1:
            self.first.setText(SCALE[index])
            self.second.setText(SCALE[index + 2] + "m")
            self.third.setText(SCALE[index + 4] + "m")
            self.fourth.setText(SCALE[index + 5])
            self.fifth.setText(SCALE[index + 7])
            self.sixth.setText(SCALE[index + 9] + "m")
            self.seventh.setText(SCALE[index + 11] + "°")
            
def main():
    """Instantiate and pops up window"""
    chords().mainloop()

if __name__ == "__main__":
    main()
