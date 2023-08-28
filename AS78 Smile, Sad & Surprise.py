def ASCII_art(emotion):
    if emotion == "happy":
        print("\n (O)(O) \n \____/ \n")
    if emotion == "sad":
        print("\n (O)(O) \n /----\ \n")
    if emotion == "surprise":
        print("\n (O)(O) \n   /\   \n   \/   \n")
    
emotion = input("Are you happy/sad/surprise? ")

ASCII_art(emotion)
