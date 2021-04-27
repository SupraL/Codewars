class Event():
    def __init__(self):
        self.func_dict = {}
    
    def emit(self, *args):
        for func_id in self.func_dict:
            self.func_dict[func_id](*args)
    
    def subscribe(self, func):
        if id(func) not in self.func_dict:
            self.func_dict[id(func)] = func
    
    def unsubscribe(self, func):
        if id(func) in self.func_dict:
            del self.func_dict[id(func)]