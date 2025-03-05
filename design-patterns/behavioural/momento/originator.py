from momento import Momento
from caretaker import UndoRedoManager

class CanvasEditor:
    def __init__(self):
        self.canvas = []

    def editor_functions(self,func):
        self.canvas.append(func)

    def get_editor_function(self):
        print("Canvas is {}".format(self.canvas))

    def save(self):
        return Momento(state=self.canvas)  #saves current state

    def restore(self,momento):
        self.canvas = momento.get_saved_state()



editor = CanvasEditor()
undo_manager = UndoRedoManager()

# Add some shapes and save state
editor.editor_functions("Rectangle")
undo_manager.save_state(editor.save())

editor.editor_functions("Circle")
undo_manager.save_state(editor.save())

editor.editor_functions("Triangle")
undo_manager.save_state(editor.save())

# Show current canvas
editor.get_editor_function()  # Output: Canvas: ['Rectangle', 'Circle', 'Triangle']

# Undo last action (removes "Triangle")
memento = undo_manager.undo()
if memento:
    editor.restore(memento)
editor.get_editor_function()  # Output: Canvas: ['Rectangle', 'Circle']

# Undo again (removes "Circle")
memento = undo_manager.undo()
if memento:
    editor.restore(memento)
editor.get_editor_function()  # Output: Canvas: ['Rectangle']

# Redo (brings back "Circle")
memento = undo_manager.redo()
if memento:
    editor.restore(memento)
editor.get_editor_function()