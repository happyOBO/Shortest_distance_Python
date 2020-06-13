import pygame

freq = 44100    # sampling rate, 44100(CD), 16000(Naver TTS), 24000(google TTS)
bitsize = -16   # signed 16 bit. support 8,-8,16,-16
channels = 1    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)

# default : pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.mixer.init(freq, bitsize, channels, buffer)
while True :
    music_file = "bgm.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(5)
    # music_file = "minSTRT.mp3"
    # pygame.mixer.music.load(music_file)
    # pygame.mixer.music.play()
    # while pygame.mixer.music.get_busy():
    #     clock.tick(5)
pygame.mixer.quit()