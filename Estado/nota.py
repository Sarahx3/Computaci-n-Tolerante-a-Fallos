
class Note:
    def __init__(self, titulo, texto) -> None:
        self.__titulo = titulo
        self.__texto = texto

    def getTitulo(self) -> str:
        return self.__titulo

    def getTexto(self) -> str:
        return self.__texto

        
    