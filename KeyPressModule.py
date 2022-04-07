import pygame

def init():
    # Init window to receive keypress
    pygame.init()
    window = pygame.display.set_mode((400,400))

def getKey(keyName):
    ans = False
    for _ in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))

    if keyInput[myKey]:
        ans = True
    
    pygame.display.update()
    return ans

def main():
    if getKey("LEFT"): print('left pressed')

if __name__ == "__main__":
    init()
    while True: main()