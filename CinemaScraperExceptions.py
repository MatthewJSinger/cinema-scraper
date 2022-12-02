class CinemaNotFoundError(Exception):
    def __init__(self,f,*args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f'Cinema: {self.f} not found'
