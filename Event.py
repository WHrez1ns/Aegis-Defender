class Event:
    def __init__(self):
        self.handlers = []

    def adicionar_handler(self, handler):
        self.handlers.append(handler)

    def remover_handler(self, handler):
        self.handlers.remove(handler)

    def disparar(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)