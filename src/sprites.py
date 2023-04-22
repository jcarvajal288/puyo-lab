ANIMATION_SPEED_IN_MS = 500

class Sprites():
    _spritesheet_filename = "../img/chalkpuyo_sprites.png"
    _red_puyo_rects = ((3, 4, 32, 32),
                       (36, 4, 32, 32),
                       (68, 2, 32, 32),
                       (100, 3, 32, 32))
    _green_puyo_rects = ((3, 35, 32, 32),
                         (35, 35, 32, 32),
                         (68, 35, 32, 32),
                         (100, 36, 32, 32))
    _blue_puyo_rects = ((4, 68, 32, 32),
                        (35, 66, 32, 32),
                        (67, 69, 32, 32),
                        (100, 67, 32, 32))
    _yellow_puyo_rects = ((4, 99, 32, 32),
                          (35, 100, 32, 32),
                          (68, 99, 32, 32),
                          (100, 99, 32, 32))
    _purple_puyo_rects = ((3, 132, 32, 32),
                          (35, 132, 32, 32),
                          (69, 131, 32, 32),
                          (101, 131, 32, 32))

    def __init__(self, pygame):
        self.pygame = pygame
        try:
            self._spritesheet = pygame.image.load(self._spritesheet_filename).convert_alpha()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {self._spritesheet_filename}")
            raise SystemExit(e)
        self.red_puyos = self.images_at(self._red_puyo_rects)
        self.green_puyos = self.images_at(self._green_puyo_rects)
        self.blue_puyos = self.images_at(self._blue_puyo_rects)
        self.yellow_puyos = self.images_at(self._yellow_puyo_rects)
        self.purple_puyos = self.images_at(self._purple_puyo_rects)
    
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

    def _char_to_puyo(self, ch):
        if ch == 'r': return self.red_puyos
        if ch == 'g': return self.green_puyos
        if ch == 'b': return self.blue_puyos
        if ch == 'y': return self.yellow_puyos
        if ch == 'p': return self.purple_puyos

    def get_image_pair(self, pair_type):
        return [self._char_to_puyo(p) for p in pair_type]
