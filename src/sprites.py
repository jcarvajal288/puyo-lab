class Sprites():
    _spritesheet_filename = "../img/chalkpuyo_sprites.png"
    _animation_speed_in_ms = 500
    _red_puyo_rects = ((3, 4, 32, 32),
                    (36, 4, 32, 32),
                    (68, 2, 32, 32),
                    (100, 3, 32, 32))

    def __init__(self, pygame):
        self.pygame = pygame
        try:
            self._spritesheet = pygame.image.load(self._spritesheet_filename).convert_alpha()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {self._spritesheet_filename}")
            raise SystemExit(e)
        self.redPuyos = self.images_at(self._red_puyo_rects)
    
    def image_at(self, rectangle, colorkey=None):
        rect = self.pygame.Rect(rectangle)
        image = self.pygame.Surface(rect.size, self.pygame.SRCALPHA)
        image.blit(self._spritesheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rectangles, colorkey=None):
        return [self.image_at(rect, colorkey) for rect in rectangles]

    def red_puyo(self):
        time_in_ms = self.pygame.time.get_ticks()
        puyo_frame = time_in_ms // self._animation_speed_in_ms % len(self.redPuyos)
        return self.redPuyos[puyo_frame]

