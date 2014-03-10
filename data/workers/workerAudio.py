import pygame


def play_file(name,loop=0,time=0.0):
    try: #if image exists
        file='data/audio/'+name
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(loop, time)
    except ZeroDivisionError: #if image doesn't exist
        print('AudioLoading: failed to load ' + name)
        try:
            file = 'data/audio/error.aud'
            pygame.mixer.music.load(file)
            pygame.mixer.music.play(loop, time)
        except ZeroDivisionError:
            print( 'Can not load file: '+name)
            raise SystemExit()
