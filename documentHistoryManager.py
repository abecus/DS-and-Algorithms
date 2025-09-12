class DocumentHistory:
    def __init__(self):
        self.changes_stack = []
        self.redo_stack = []

    def apply_change(self, change: str) -> None:
        self.changes_stack.append(change)
        self.redo_stack.clear()
    
    def undo(self) -> str | None:
        if not self.changes_stack:
            return None
        change = self.changes_stack.pop()
        self.redo_stack.append(change)
        return change

    def redo(self) -> str | None:
        if not self.redo_stack:
            return None
        change = self.redo_stack.pop()  # Redo the last undone change
        self.changes_stack.append(change)
        return change

    def get_changes(self) -> list[str]:
        return self.changes_stack[:]
