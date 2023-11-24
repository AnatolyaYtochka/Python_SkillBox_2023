import re
import doctest
def checkPasswordCorrectness(password: str) -> bool:
  """
    Функция проверяет корректность пароля
    Args:
      password: str, пароль
    Returns:
      bool: True - пароль корректен, False - пароль некорретен

    >>> checkPasswordCorrectness('rtG&3FG#Tr^e')
    True
    >>> checkPasswordCorrectness('a^A1@*@1Aa')
    True
    >>> checkPasswordCorrectness('oF^a1D@y5%e6')
    True
    >>> checkPasswordCorrectness('enroi#$*rkdeR#$*092uwedchf34tguv394h')
    True
    >>> checkPasswordCorrectness('пароль')
    False
    >>> checkPasswordCorrectness('password')
    False
    >>> checkPasswordCorrectness('qwerty')
    False
    >>> checkPasswordCorrectness('lOngPa$$W0Rd')
    False
    >>> checkPasswordCorrectness('rtG#3FG#Tr#e')
    False
    >>> checkPasswordCorrectness('r8G&3F8G#T1^')
    False
    >>> checkPasswordCorrectness('re8G&3F8?#T1^')
    False
    >>> checkPasswordCorrectness('rп8G&3F8?#T1^')
    False
    >>> checkPasswordCorrectness('rпG&F?#T^')
    False
    >>> checkPasswordCorrectness('rG^3FG#T$e')
    True
    """

  if re.search('(?=[A-Za-z\d^$%@#&*]{8,})(?=(?:.*[a-z].*){2,})(?=(?:.*[1-9].*)+)(?=[^,.!?]*$).*$', password) and len(set(re.findall(r'[$%@#&^*]', password))) >= 3:
    return True
  return False

doctest.testmod(verbose=True)

