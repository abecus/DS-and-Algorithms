class FileSystem:
    
    def __init__(self):
        self.root = {}
    
    def add_directory(self, path: str) -> bool:
        dir_existed = True
        node = self.root
        
        for p in path.split('/'):
            if p not in node:
                dir_existed = False
                node[p] = {}
            node = node[p]
        
        return not dir_existed
    
    def add_file(self, path: str, content: str) -> bool:
        node = self.root
        for p in path.split('/'):
            if p not in node:
                if '.' in p:
                    node[p] = content
                    return True
                return False
            
            node = node[p]
    
    def get_content(self, path: str) -> str | None:
        node = self.root
        for p in path.split('/'):
            if p not in node:
                return None
            node = node[p]
            
        if isinstance(node, str):
            return node
        return None
    
    def delete(self, path: str) -> bool:
        prev = None
        node = self.root
        for p in path.split('/'):
            if p not in node:
                return False
            prev = node
            node = node[p]
        
        del prev[p]
        return True
        
