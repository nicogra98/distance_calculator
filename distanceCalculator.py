from geopy.geocoders import Nominatim
import math
import sys
"""
@Author Nicolas Granados
Distance calculator from any 2 points
ex: python distanceCalculator
"""
#latitude = north and south of equator
#longitude = east and west of equator

def harvesine(set1, set2):
  """
  Calculates the harvesine distance bettween 2 sets of coordinates
  """

  lat1, lon1 = set1
  lat2, lon2 = set2

  dLat = (lat2 - lat1) * math.pi / 180.0
  dLon = (lon2 - lon1) * math.pi / 180.0

  lat1 = (lat1) * math.pi / 180.0
  lat2 = (lat2) * math.pi / 180.0
  

  a = (pow(math.sin(dLat / 2), 2) + pow(math.sin(dLon / 2), 2) * math.cos(lat1) * math.cos(lat2)) 
  rad = 6371
  c = 2 * math.asin(math.sqrt(a)) 
  return rad * c 


if __name__ == "__main__":
  geolocator = Nominatim(user_agent = "DistanceCalculator")
  km = True

  while True:

    name_location1 = input("Please provide the name or coordinates of the first point you want to calculate the distance: ")
    name_location2 = input("Please provide the name or coordinates of the second point you want to calculate the distance: ")

    if input("Do you want the result in miles or kilometers?(k/m)").lower()[0] == "k":
      km = True
    else:
      km = False

    location1 = geolocator.geocode(name_location1)
    location2 = geolocator.geocode(name_location2)

    coordinates1 = (location1.latitude, location1.longitude)
    coordinates2 = (location2.latitude, location2.longitude)

    result = harvesine(coordinates1, coordinates2)

    if km:
      print("The distance between {} and {} is: {} Km".format(name_location1, name_location2, result))
    else:
      result = result / 1.609
      print("The distance between {} and {} is: {} miles".format(name_location1, name_location2, result))

    if input("Do you want to calculate more distances (y/n): ").lower()[0] == "y":
      continue
    else:
      print("Thank you!")
      break