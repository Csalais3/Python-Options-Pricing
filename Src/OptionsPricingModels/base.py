from enum import Enum
from abc import ABC, abstractmethod

class OPTION_TYPE(Enum):
    CALL_OPTION = "Call Option "
    PUT_OPTION = "Put Option"

class OptionsPricingModel(ABC):
    "Interface for pricing models"
    
    def calculate_option_price(self, option_type):
        if option_type == OPTIONTYPE.CALL_OPTION.vaue:
            return self.calculate_call_option_price()
        elif option_type == OPTIONTYPE.PUT_OPTION.value:
            return self.calculate_put_option_price()
        else:
            return -1
    
    @classmethod
    @abstractmethod
    def calculate_call_option_price(cls):
        pass
    
    @classmethod
    @abstractmethod
    def calculate_put_option_price(cls):
        pass
    