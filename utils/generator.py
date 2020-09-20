import datetime

import rstr
import random
from faker import Faker

import pandas as pd

class GenUtil:
  def __init__(self, seed=0):
    Faker.seed(seed)
    self.fake = Faker()

    random.seed(a=seed)
    self.random = random
    self.rstr = rstr

  @classmethod
  def gen_date(self, *, lower_bound: str, upper_bound: str) -> datetime.date:
    """Generate date type dummy data

    Args:
      lower_bound: lower bound of the data range (only YYYY-MM-DD format)
      upper_bound: upper bound （same as lower_bound)

    Output:
      a date object within the range
    """
    _lower_bound = datetime.date.fromisoformat(lower_bound)
    _upper_bound = datetime.date.fromisoformat(upper_bound)
    
    return self.fake.date_between_dates(_lower_bound, _upper_bound)


  @classmethod
  def gen_string(self, *, pattern: str) -> str:
    """Generate string type dummy data

      Args:
        pattern: regex pattern used in rstr.xeger()

      Output:
        a str object within the range
    """

    return self.rstr.xeger(pattern)

  @classmethod
  def gen_integer(self, *, lower_bound: str, upper_bound: str) -> str:
    """Generate integer type dummy data

      Args:
        lower_bound: lower bound of the int range
        upper_bound: lower bound of the int range

      Output:
        a integer object within the range
    """

    return self.rstr.xeger(pattern)

