"""
Game class - main game controller.
"""

import pygame


class Game:
    """Main game class that handles game loop and state."""
    
    def __init__(self, width=800, height=600, title="Game"):
        """
        Initialize the game.
        
        Args:
            width: Window width in pixels
            height: Window height in pixels
            title: Window title
        """
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
    
    def handle_events(self):
        """Handle input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def update(self, delta_time):
        """
        Update game state.
        
        Args:
            delta_time: Time elapsed since last frame in seconds
        """
        pass
    
    def render(self):
        """Render the game to the screen."""
        self.screen.fill((0, 0, 0))
        pygame.display.flip()
    
    def run(self):
        """Main game loop."""
        while self.running:
            delta_time = self.clock.tick(self.fps) / 1000.0
            
            self.handle_events()
            self.update(delta_time)
            self.render()
