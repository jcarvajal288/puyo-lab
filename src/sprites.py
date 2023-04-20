class Sprites():
    _spritesheet_filename = "../img/chalkpuyo_sprites.png"
    _redPuyoRect = (3, 4, 32, 32)

    def __init__(self, pygame):
        self.pygame = pygame
        try:
            self._spritesheet = pygame.image.load(self._spritesheet_filename).convert_alpha()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {self._spritesheet_filename}")
            raise SystemExit(e)
        self.redPuyo = self.image_at(self._redPuyoRect)
    
    def image_at(self, rectangle, colorkey=None):
        rect = self.pygame.Rect(rectangle)
        image = self.pygame.Surface(rect.size, self.pygame.SRCALPHA)
        image.blit(self._spritesheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
