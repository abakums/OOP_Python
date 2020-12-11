from abc import ABC, abstractmethod


class Person(ABC):
    def who_am_i(self):
        return 'Hello! I am a person!'

    @abstractmethod
    def get_information(self):
        pass
