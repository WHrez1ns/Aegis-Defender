class Process:
    def __init__(self, nome, pid):
        self.nome = nome
        self.pid = pid

    def __str__(self) -> str:
        return f'''
        Nome: {self.nome},
        PID: {self.pid}'''
