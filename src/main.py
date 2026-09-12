"""
Main entry point for the AI Game Course game.
"""

import pygame
from game import Game


def main():
    """Initialize and run the game."""
    pygame.init()
    
    game = Game(width=800, height=600, title="AI Game Course")
    game.run()
    
    pygame.quit()


if __name__ == "__main__":
    main()
