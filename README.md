# AI Game Course

A comprehensive course on building games with artificial intelligence using Python and Pygame.

## Course Overview

This course teaches game development fundamentals combined with AI concepts through hands-on projects. Students will build progressively complex games that leverage AI for intelligent game agents and NPCs.

## Course Structure

This course is organized into **8 progressive classes**, each building upon the previous one:

| Class | Branch | Topic |
|-------|--------|-------|
| 1 | `class/1-foundations` | Pygame Fundamentals & Game Loop |
| 2 | `class/2-movement` | Game Objects & Movement Systems |
| 3 | `class/3-collision` | Collision Detection & Physics |
| 4 | `class/4-pathfinding` | Pathfinding (A*, Dijkstra) |
| 5 | `class/5-fsm` | Finite State Machines |
| 6 | `class/6-behavior-trees` | Behavior Trees & Decision Making |
| 7 | `class/7-neural-networks` | Intro to Neural Networks for Game AI |
| 8 | `class/8-rl` | Reinforcement Learning Fundamentals |

## Git Workflow

We use **Git Flow** for managing this course:

- `main` - Stable releases with completed classes
- `develop` - Integration branch for classes in progress
- `class/N-*` - Individual class branches

To access a specific class:
```bash
git checkout class/1-foundations
```

### Release Cycle

Each completed class is merged into `develop`, and every milestone (e.g., after 2-3 classes) is released to `main` with a version tag (v1.0, v2.0, etc.).

## Prerequisites

- Python 3.8+
- Basic understanding of Python programming
- Familiarity with object-oriented programming concepts

## Project Structure

- `src/` - Game source code and AI implementations
- `tests/` - Unit tests for game logic and AI algorithms
- `examples/` - Example implementations and tutorials

## Getting Started

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-game-course
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Tests

```bash
pytest tests/
```

### Running the Game

```bash
python src/main.py
```

## CI/CD Pipeline

This project uses GitHub Actions to automatically:
- Check Python syntax and code style (flake8)
- Run unit tests with pytest
- Generate coverage reports

See `.github/workflows/ci.yml` for pipeline configuration.

## Topics Covered

- Pygame game development
- Pathfinding algorithms (A*, Dijkstra)
- Behavior trees
- Finite state machines
- Neural networks for game AI
- Reinforcement learning basics

## License

MIT License - see LICENSE file for details
