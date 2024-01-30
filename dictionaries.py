# Dictionaries are to store data as key-value pairs

band = {"vocals": "plant", "guitar": "Page"}

band2 = dict(vocals="Plant", guitar="page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items in a dict
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)

# change value
band["vocals"] = "Yo"
band.update({"base": "JPJ"})

print(band)

# remove items
print(band.pop("base"))
print(band)

band["drums"] = "Bono"
print(band)

# last item added will be removed
print(band.popitem())
print(band)

# delete & clear
band["drums"] = "Bono"
print(band)
del band["drums"]
print(band)

# to clear the dictionay & make it empty
print(band2)
band2.clear()
print(band2)
del band2

# To copy dictionaries
band3 = band.copy()
band3["drums"] = "Kazi"
print(band)
print(band3)

band4 = dict(band3)
print("good copy")
band4["bass"] = "tanim"
print(band3)
print(band4)

# nested dictionaries

member1 = {"name": "Kazi", "instrument": "vocal"}
member2 = {"name": "Tanim", "instrument": "guitar"}
band = {"member1": member1, "member2": member2}

print(band)
print(band["member1"]["name"])
