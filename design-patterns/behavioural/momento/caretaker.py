class UndoRedoManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save_state(self,momento):
        self.undo_stack.append(momento)
        self.redo_stack.clear()


    def undo(self):
        if self.undo_stack:
            last_state = self.undo_stack.pop()
            self.redo_stack.append(last_state)
            return last_state
        return None

    def redo(self):
        if self.redo_stack:
            redo_state = self.redo_stack.pop()
            self.undo_stack.append(redo_state)
            return redo_state
        return None



