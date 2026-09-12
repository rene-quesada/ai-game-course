# Course Architecture & Design Philosophy

## Core Design Principles

### 1. **Separation of Concerns**

**Game Logic** should be completely separate from **Pygame Rendering and Input**:

```text
Game Logic Layer (testable)
├── Player
├── Enemy
├── Collision
├── Score
└── GameState

Presentation Layer (Pygame)
├── Renderer
├── InputHandler
└── Display
```

**Why?** This allows us to test all game rules without launching the graphical interface. We can verify correctness at the logic level, then integrate with Pygame knowing the presentation is orthogonal to the game itself.

### 2. **Progressive Complexity**

The project architecture evolves across classes:

**Class 1:**
```python
# Single file, everything in one place
player_x, player_y = 100, 100

def move_player(x, y, direction):
    if direction == "RIGHT":
        return x + 5, y
```

**Class 2-3:**
```
src/
├── game.py       # Game logic
└── pygame_app.py # Pygame rendering
```

**Class 4+:**
```
src/
├── game/
│   ├── player.py
│   ├── enemy.py
│   ├── collision.py
│   └── score.py
├── pygame_app/
│   ├── renderer.py
│   ├── input.py
│   └── main.py
└── config.py
```

### 3. **Test-First Design**

Every feature begins with a test that fails:

```python
def test_player_collision_with_enemy():
    player = Player(100, 100)
    enemy = Enemy(110, 100)
    assert player.collides_with(enemy) == True
```

Only after the test exists does the implementation follow. This ensures:
- Behavior is specified before implementation
- Correctness can be verified
- Edge cases are considered upfront

### 4. **Pure Functions Over Stateful Objects**

Where practical, use pure functions:

```python
# Good: Pure function, testable without state
def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# Also good: Testable object with clear state
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move_right(self, speed):
        self.x += speed

# Avoid: Complex stateful logic mixed with Pygame
# (This is what Class 4 refactors away)
```

---

## Layered Architecture

### Layer 1: Core Game Logic
**Responsibility:** Game rules, physics, state management  
**Dependencies:** None (no external libraries)  
**Testing:** Unit tests only  

```python
# src/game/player.py
class Player:
    def __init__(self, x, y, speed=5):
        self.x = x
        self.y = y
        self.speed = speed
    
    def move_right(self):
        self.x += self.speed
    
    def is_out_of_bounds(self, screen_width):
        return self.x < 0 or self.x > screen_width
```

### Layer 2: Game State & Rules
**Responsibility:** Orchestrating game logic, maintaining invariants  
**Dependencies:** Core Game Logic layer  
**Testing:** Unit tests  

```python
# src/game/game_state.py
class GameState:
    def __init__(self, width, height):
        self.player = Player(width//2, height//2)
        self.enemies = []
        self.score = 0
    
    def update(self, input_events):
        for event in input_events:
            if event == "RIGHT":
                self.player.move_right()
        
        # Check boundary
        if self.player.is_out_of_bounds(width=800):
            self.player.x = max(0, min(self.player.x, 800))
```

### Layer 3: Pygame Application
**Responsibility:** Rendering, input handling, display  
**Dependencies:** Game State & Rules layer  
**Testing:** Integration tests (if at all; mostly manual)  

```python
# src/pygame_app/renderer.py
class GameRenderer:
    def __init__(self, game_state):
        self.game_state = game_state
        self.screen = pygame.display.set_mode((800, 600))
    
    def render(self):
        player = self.game_state.player
        pygame.draw.rect(self.screen, (0, 255, 0), 
                        (player.x, player.y, 20, 20))
```

---

## Data Flow

```text
User Input (Keyboard, Mouse)
    ↓
InputHandler (src/pygame_app/input.py)
    ↓
GameState.update(input_events)
    ↓
[Game Logic runs]
    ↓
GameRenderer.render(game_state)
    ↓
Display updated
    ↓
Repeat
```

---

## Testing Strategy

### Unit Tests (Most)
Test game logic in isolation, no Pygame required:

```python
# tests/test_player.py
def test_player_moves_right():
    player = Player(100, 100, speed=5)
    player.move_right()
    assert player.x == 105
```

Run: `pytest`

### Integration Tests (Some)
Test GameState orchestrating components:

```python
# tests/test_game_state.py
def test_enemy_collision_ends_game():
    state = GameState(800, 600)
    state.player.x = 100
    enemy = Enemy(105, 100)
    state.enemies.append(enemy)
    
    state.update_collisions()
    assert state.is_game_over() == True
```

### Manual Testing (Few)
Only the display layer requires manual play-testing:

```python
# Manual: Start the game, verify visual appearance
# python -m src.pygame_app.main
```

---

## File Organization

```text
de-la-idea-al-despliegue/
│
├── docs/
│   ├── SUMMARY.md              # Course overview
│   ├── ARCHITECTURE.md         # This file
│   ├── AI-CONTEXT.md           # AI usage guidelines
│   ├── DESIGN-RULES.md         # Patterns and conventions
│   └── ai-log.md               # Student's AI interactions
│
├── src/
│   ├── game/
│   │   ├── __init__.py
│   │   ├── player.py           # Player logic
│   │   ├── enemy.py            # Enemy logic
│   │   ├── collision.py        # Collision detection
│   │   ├── score.py            # Score management
│   │   ├── rules.py            # Game rules & constants
│   │   └── game_state.py       # Central state (later classes)
│   │
│   ├── pygame_app/
│   │   ├── __init__.py
│   │   ├── main.py             # Entry point
│   │   ├── renderer.py         # Pygame rendering
│   │   ├── input.py            # Input handling
│   │   └── config.py           # Display config
│   │
│   ├── __init__.py
│   └── config.py               # Global configuration
│
├── tests/
│   ├── __init__.py
│   ├── test_player.py
│   ├── test_enemy.py
│   ├── test_collision.py
│   ├── test_score.py
│   ├── test_game_state.py
│   └── conftest.py             # pytest fixtures
│
├── assets/                      # Images, sounds, etc.
│   ├── sprites/
│   └── sounds/
│
├── .github/
│   └── workflows/
│       ├── test.yml             # CI pipeline
│       ├── lint.yml
│       ├── build.yml
│       └── deploy.yml
│
├── requirements.txt
├── pytest.ini
├── .gitignore
├── README.md
└── LICENSE
```

---

## Dependency Inversion

Pass dependencies to constructors rather than creating them internally:

```python
# ❌ Bad: Tightly coupled, hard to test
class GameState:
    def __init__(self):
        self.player = Player(100, 100)  # Hard-coded
        self.renderer = GameRenderer()   # Can't inject a mock

# ✅ Good: Loose coupling, testable
class GameState:
    def __init__(self, player, renderer=None):
        self.player = player
        self.renderer = renderer  # Can inject mock for testing
```

---

## Configuration Management

Game settings should be in one place, not scattered through code:

```python
# src/config.py
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
ENEMY_SPEED = 3
COLLISION_RADIUS = 20
FPS = 60
```

In classes:

```python
# src/game/player.py
from src.config import PLAYER_SPEED, SCREEN_WIDTH

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = PLAYER_SPEED  # Use config
    
    def is_out_of_bounds(self):
        return self.x < 0 or self.x > SCREEN_WIDTH
```

---

## Evolution Across Classes

### Class 1-2: Simple Structure
- Single or dual-file structure
- Focus on TDD basics
- Minimal separation

### Class 3-4: Modular Design
- Package-based structure
- Clear layer separation
- Testable game logic

### Class 5-6: Quality & Artifacts
- Configuration management
- Build processes
- More sophisticated testing

### Class 7-8: Production-Ready
- Error handling
- Logging
- Observability
- Version metadata

---

## Common Patterns

### The Game Loop
```python
# src/pygame_app/main.py
def run():
    game_state = GameState(800, 600)
    renderer = GameRenderer(game_state)
    clock = pygame.time.Clock()
    
    running = True
    while running:
        events = pygame.event.get()
        
        # Update
        game_state.update(events)
        
        # Render
        renderer.render()
        
        pygame.display.flip()
        clock.tick(60)  # 60 FPS
```

### Testable Game Logic
```python
# tests/test_collision.py
def test_collision_detection():
    player = Player(100, 100, size=20)
    enemy = Enemy(110, 100, size=20)
    
    # No Pygame required
    assert player.collides_with(enemy) == True
```

### Configuration-Driven Behavior
```python
# src/game/player.py
from src.config import PLAYER_SPEED

def move_right(self):
    self.x += PLAYER_SPEED  # Uses config, not hard-coded
```

---

## Anti-Patterns to Avoid

### ❌ God Objects
```python
# Bad: Player does everything
class Player:
    def update(self):
        # Move
        # Draw
        # Handle collision
        # Calculate score
        # Play sound
```

### ✅ Single Responsibility
```python
# Good: Each class has one job
class Player:
    def update(self):
        self.move()

class CollisionDetector:
    def check_player_enemy(self, player, enemy):
        pass

class ScoreManager:
    def add_points(self, amount):
        pass
```

### ❌ Hard-Coded Constants
```python
# Bad
def move_right(self):
    self.x += 5  # Magic number
```

### ✅ Configuration-Driven
```python
# Good
from src.config import PLAYER_SPEED

def move_right(self):
    self.x += PLAYER_SPEED
```

---

## Design Evolution Timeline

| Class | Architectural Focus | Key Change |
|-------|---------------------|-----------|
| 1 | Monolithic → Simple separation | Introduce tests, split game from render |
| 2 | Package structure | Organize by module |
| 3 | Quality layers | Add linting, type checks |
| 4 | Modular design | Refactor into game/pygame_app layers |
| 5 | Build artifacts | Formalize structure |
| 6 | Professional workflow | Quality gates |
| 7 | Production readiness | Configuration, logging |
| 8 | Deployment readiness | Version metadata, observability |

---

## Key Metrics

As you design, keep these in mind:

- **Testability:** How much of the code can be tested without Pygame?
- **Coupling:** How many dependencies does each module have?
- **Cohesion:** How related are the functions in each module?
- **Complexity:** Can you understand a function in under 1 minute?
- **Duplication:** Are you repeating the same logic in multiple places?

---

## Summary

Good course architecture:

✅ Separates game logic from presentation  
✅ Uses pure functions where practical  
✅ Tests game rules without Pygame  
✅ Evolves gradually from simple to sophisticated  
✅ Uses configuration for flexibility  
✅ Follows single responsibility principle  
✅ Enables both unit and integration testing  
✅ Supports easy refactoring  
✅ Makes bugs visible through tests  

This foundation allows the course to progress from "make a game work" (Class 1) to "deliver production software" (Class 8).
