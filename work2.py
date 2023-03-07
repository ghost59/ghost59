"""
project 8.8
Anthony Simmons
03/6/2022
"""

from breezypythongui import EasyFrame
import tkinter.filedialog

class TextEditor(EasyFrame):
    """Demonstartes the use of a file dialog"""

    def __init__(self):
        """Set up the windoq and widgets."""
        EasyFrame.__init__(self, "Text Editor")
        self.fileName = ""
        self.outputArea = self.addTextArea("", row = 0, column = 0, columnspan = 3, width = 80, height = 15)
        self.addButton(text = "New", row = 1, column = 0, command = self.newFile)
        self.addButton(text = "Open", row = 1, column = 1, command = self.openFile)
        self.addButton(text = "Save", row = 1, column = 2, command = self.saveFile)
        
    def newFile(self):
        """Clears the text"""
        self.outputArea.setText("")
        self.fileName = ""
        self.setTitle("Text Editor")
        
    def openFile(self):
        """Pops up and open file dialog"""
        fList = [("Python files","*.py"),("Text files","*.txt")]
        self.fileName = tkinter.filedialog.askopenfilename(parent = self, filetypes = fList)
        if self.fileName != "":
            try:
                with open(self.fileName, 'r') as file:
                    text = file.read()
                    self.outputArea.setText(text)
                    self.setTitle(self.fileName)
            except Exception as e:
                    print(f"An error occurred: {e}")
                    
    def saveFile(self):
        """Pops up and open file. Saves it"""
        if self.fileName == "":
            self.fileName == tkinter.filedialog.asksaveasfilename(parent = self)
        if self.fileName != "":
            try:
                with open(self.fileName, 'w') as file:
                    file.write(self.outputArea.getText())
                self.setTitle(self.fileName)
            except Exception as e:
                print(f"An error occurred: {e}")

def main():
    """Pops the window open"""
    TextEditor().mainloop()

if __name__ == "__main__":
    main()
    
        
                
