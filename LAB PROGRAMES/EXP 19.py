planets = {
    "mercury": "Closest planet to the Sun",
    "venus": "Hottest planet",
    "earth": "Planet with life",
    "mars": "Red planet",
    "jupiter": "Largest planet",
    "saturn": "Planet with beautiful rings",
    "uranus": "Planet rotating on its side",
    "neptune": "Farthest planet from the Sun"
}

name = input("Enter planet name: ").lower()

if name in planets:
    print(planets[name])
else:
    print("Planet not found")
