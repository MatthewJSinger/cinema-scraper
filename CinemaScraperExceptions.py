class CinemaNotFoundError(Exception):
    def __init__(self,f,*args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f'Cinema: {self.f} not found'

class NoFilmsFoundError(Exception):
    def __init__(self,f,*args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f'No Films found while searching {self.f}. There may be no film data available for this Cinema'
