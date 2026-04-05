class BaseWrapper:
    def __init__(self):
        pass  

    def wrap(self, data):
        raise NotImplementedError("This method needs to be overridden")

    def unwrap(self, data):
        raise NotImplementedError("This method needs to be overridden")
    
    def __str__(self):
        return self.__class__.__name__
