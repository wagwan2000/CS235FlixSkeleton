
class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        return other.__director_full_name == self.__director_full_name

    def __lt__(self, other):
        return self.__director_full_name[0] < other.__director_full_name[0]

    def __hash__(self):
        return hash(self.__director_full_name)
