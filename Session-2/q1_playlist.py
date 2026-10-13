
playlist = ["Shape of You", "Blinding Lights", "Believer", "Perfect"]
print(len(playlist))

print("First:", playlist[0])
print("Last:", playlist[-1])

playlist.insert(4,"Dynamite")
print("Updated list:", playlist)

playlist.remove("Believer")
print("Updated list:", playlist)

playlist.sort()
print("Updated list:", playlist)

for i in range(len(playlist)):
    print(i + 1, playlist[i])
