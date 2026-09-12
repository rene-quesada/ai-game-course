# De la Idea al Despliegue

A comprehensive course on **AI**, **Software Development**, and **CI/CD**, progressing from foundational concepts to production-ready deployments.

## Course Overview

This course teaches software engineering fundamentals, artificial intelligence concepts, and modern DevOps practices through hands-on, progressively complex projects. Students will learn how to take an idea from concept to a deployed, monitored, production system.

**What you'll learn:**
- ✅ Python fundamentals & testing best practices
- ✅ Algorithms and data structures
- ✅ Machine Learning (supervised & unsupervised)
- ✅ Deep Learning and neural networks
- ✅ CI/CD pipelines and automation
- ✅ Deployment strategies and monitoring

## Course Structure

This course is organized into **8 progressive classes**, each building upon the previous one:

| Class | Branch | Topic | Focus |
|-------|--------|-------|-------|
| 1 | `class/1-foundations` | Python & Testing | Fundamentals |
| 2 | `class/2-algorithms` | Algorithms & Data Structures | Fundamentals |
| 3 | `class/3-ci-cd-basics` | Basic CI/CD Setup | CI/CD |
| 4 | `class/4-ml-supervised` | Supervised Machine Learning | AI |
| 5 | `class/5-ml-unsupervised` | Unsupervised Learning & Deep Learning | AI |
| 6 | `class/6-advanced-ml` | Advanced AI Models | AI |
| 7 | `class/7-deployment` | Containerization & Deployment | CI/CD |
| 8 | `class/8-monitoring` | Monitoring & Production | CI/CD |

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
