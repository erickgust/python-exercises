from pygame import mixer
mixer.init()
mixer.music.load('C:/Users/gus/Downloads/mp3/duzz.mp3')
mixer.music.play()
while mixer.music.get_busy(): pass
