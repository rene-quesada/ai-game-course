"""Tests for the Game class."""

import pytest
import pygame
from src.game import Game


@pytest.fixture
def game():
    """Fixture to create a Game instance for testing."""
    pygame.init()
    g = Game(width=800, height=600, title="Test Game")
    yield g
    pygame.quit()


def test_game_initialization(game):
    """Test that game initializes with correct parameters."""
    assert game.width == 800
    assert game.height == 600
    assert game.title == "Test Game"
    assert game.fps == 60
    assert game.running is True


def test_game_dimensions(game):
    """Test that game screen has correct dimensions."""
    assert game.screen.get_width() == 800
    assert game.screen.get_height() == 600


def test_game_stop():
    """Test that game can be stopped."""
    pygame.init()
    game = Game()
    game.running = False
    assert game.running is False
    pygame.quit()
