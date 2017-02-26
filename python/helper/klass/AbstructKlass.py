from abc import ABC, abstractmethod


class AbstructKlass(ABC):


    @abstractmethod
    def callBack(self):
        raise NotImplementedError("Please Implement the CallBack Method of AbstructKlass.")
