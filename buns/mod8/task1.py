class Transport():
  def __init__(self, coordinates, speed, brand, year, number):
    self.coordinates = coordinates
    self.speed = speed
    self.brand = brand
    self.year = year
    self.number = number

  def __str__(self):
    return f'{self.coordinates}, {self.speed}, {self.brand}, {self.year}, {self.number}'

  @property
  def coordinates(self):
    return self.coordinates

  @coordinates.setter
  def coordinates(self, coordinates):
    self.coordinates = coordinates

  @property
  def speed(self):
    return self.speed

  @speed.setter
  def speed(self, speed):
    if speed is int and speed >= 0:
      self.speed = speed

  @property
  def brand(self):
    return self.brand

  @brand.setter
  def brand(self, brand):
    self.brand = brand

  @property
  def year(self):
    return self.year

  @year.setter
  def year(self, year):
    if year is int and year >= 0:
      self.number = year

  @property
  def number(self):
    return self.number

  @number.setter
  def number(self, number):
    if number is int and number >= 0:
      self.number = number



def isInArea(self, pos_x, pos_y, length, width) -> bool:
  '''
  Присутствие транспортного средства в пределах заданнй области
  pos_x, pos_y - координата левого верхнего угла области
  length, width - длина и ширина области
  '''
  end_pos_x = pos_x + width
  end_pos_y = pos_y + length
  return (pos_x <= self.coordinates.X <= end_pos_x) and (pos_y <= self.coordinates.Y <= end_pos_y)


class Passenger():
  def __init__(self):
    self.__passengers_capacity = 0
    self.__number_of_passengers = 0
  @property
  def passengers_capacity(self):
    return self.__passengers_capacity

  @passengers_capacity.setter
  def passengers_capacity(self, passengers_capacity):
    if passengers_capacity is int and passengers_capacity >= 0:
      self.passengers_capacity = passengers_capacity


  @property
  def number_of_passengers(self):
    return self.__number_of_passengers

  @number_of_passengers.setter
  def number_of_passengers(self, number_of_passengers):
    if number_of_passengers is int and number_of_passengers >= 0:
      self.number_of_passengers = number_of_passengers


class Cargo():
  def __init__(self):
    self.__carrying = 0
  @property
  def carrying(self):
    return self.__carrying

  @carrying.setter
  def carrying(self, carrying):
    if carrying is int and carrying >= 0:
      self.carrying = carrying


class Plane(Transport):
  def __init__(self, coordinates, speed, brand, year, number, height):
    super().__init__(coordinates, speed, brand, year, number)
    self.height = height

    @property
    def height(self):
      return self.height

    @height.setter
    def height(self, height):
      if height is not bool and height is not str and height >= 0:
        self.height = height


class Auto(Transport):
  def __init__(self, coordinates, speed, brand, year, number):
    super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
  def __init__(self, name, coordinates, speed, brand, year, number, port):
    super().__init__(coordinates, speed, brand, year, number)
    self.port = port
    self.name = name

    @property
    def name(self):
      return self.name

    @name.setter
    def name(self, value):
      self.name = value

    @property
    def port(self):
      return self.port

    @port.setter
    def port(self, value):
      self.port = value

  class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number):
      super().__init__(coordinates, speed, brand, year, number)


class Bus(Auto, Passenger):
  def __init__(self, coordinates, speed, brand, year, number, number_of_passengers, passengers_capacity):
    super().__init__(coordinates, speed, brand, year, number, number_of_passengers, passengers_capacity)

class CargoAuto(Auto, Cargo):
  def __init__(self, coordinates, speed, brand, year, number, carrying):
    super().__init__(coordinates, speed, brand, year, number, carrying)

class Boat(Ship):
  def __init__(self, coordinates, speed, brand, year, number, port, name):
    super().__init__(coordinates, speed, brand, year, number, port, name)

class PassengerShip(Ship, Passenger):
  def __init__(self, coordinates, speed, brand, year, number, port, name, number_of_passengers, passengers_capacity):
    super().__init__(coordinates, speed, brand, year, number, port, name, number_of_passengers, passengers_capacity)

class CargoShip(Ship, Cargo):
  def __init__(self, coordinates, speed, brand, year, number, port, name, carrying):
    super().__init__(coordinates, speed, brand, year, number, port, name, carrying)

class Seaplane(Plane, Ship):
  def __init__(self, coordinates, speed, brand, year, number, height, port, name):
    super().__init__(coordinates, speed, brand, year, number, height, port, name)

