# AI Game Course

A comprehensive course on building games with artificial intelligence using Python and Pygame.

## Course Overview

This course teaches game development fundamentals combined with AI concepts through hands-on projects. Students will build progressively complex games that leverage AI for intelligent game agents and NPCs.

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
