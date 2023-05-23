class Process:
    def __init__(self, nome, pid, status):
        self.nome = nome
        self.pid = pid
        self.status = status

    def __str__(self) -> str:
        return f'''
        Nome: {self.nome},
        PID: {self.pid},
        Status: {self.status}'''
