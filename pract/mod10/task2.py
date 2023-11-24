import doctest
import re

def checkDateCorrectness(date):
  """
  Функция проверяет корректность введенной даты
    Args:
      date: str, дата
    Returns:
      bool: True - дата корректна, False - дата введена неверно

  >>> checkDateCorrectness('20 января 1806')
  True
  >>> checkDateCorrectness('1924, July 25')
  True
  >>> checkDateCorrectness('26/09/1635')
  True
  >>> checkDateCorrectness('3.1.1506')
  True
  >>> checkDateCorrectness('25.08-1002')
  False
  >>> checkDateCorrectness('декабря 19, 1838')
  False
  >>> checkDateCorrectness('8.20.1973')
  False
  >>> checkDateCorrectness('Jun 7, -1563')
  False
  >>> checkDateCorrectness('31 февраля 2023')
  False
  >>> checkDateCorrectness('31 июня 2015')
  False
  >>> checkDateCorrectness('5-02-1995')
  True
  >>> checkDateCorrectness('2022/09/14')
  True
  >>> checkDateCorrectness('2022.09.14')
  True
  >>> checkDateCorrectness('2022-09-14')
  True
  >>> checkDateCorrectness('September 14, 2022')
  True
  >>> checkDateCorrectness('Sep 14, 2022')
  True
  >>> checkDateCorrectness('2022, Sep 14')
  True
  """
  pattern = r'^(?:(?:0?\d|[12]\d|3[01])([\.\/-])(?:(?<!3[01][\.\/-])0?2|(?<!31[\.\/-])0?[469]|0?[^2469]|12)\1\d{4}|\d{4}([\.\/-])(?:0?2(?![\.\/-]3[01])|0?[469](?!31[\.\/-])|0?[^2469]|12)\2(?:0?\d|[12]\d|3[01])|(?:[0-2]\d|3[01]) (?:января|(?<!3[01] )февраля|марта|(?<!31 )(?:апреля|июня|сентября|ноября)|мая|июля|августа|октября|декабря) \d{4}|(?:Jan(?:uary)?|Feb(?:ruary)?(?! 3[01])|Mar(?:ch)?|(?:Apr(?:il)?|June?|Sep(?:tember)?|Nov(?:ember)?)(?! 31)|May|July?|Aug(?:ust)?|Oct(?:ober)?|Dec(?:ember)?) (?:[0-2]\d|3[01]), \d{4}|\d{4}, (?:Jan(?:uary)?|Feb(?:ruary)?(?! 3[01])|Mar(?:ch)?|(?:Apr(?:il)?|June?|Sep(?:tember)?|Nov(?:ember)?)(?! 31)|May|July?|Aug(?:ust)?|Oct(?:ober)?|Dec(?:ember)?) (?:[0-2]\d|3[01]))$'
  if re.search(pattern, date):
    return True
  return False

doctest.testmod(verbose=True)
