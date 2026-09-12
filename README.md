# De la Idea al Despliegue con IA

A hands-on course on **AI-assisted software development**, **Python/Pygame**, **testing**, and **CI/CD**. Students progressively build a videogame while learning how an idea becomes tested, integrated, packaged, versioned, released, and deployed software.

> The course does **not** teach Machine Learning. AI is used as a software-engineering assistant, primarily through **GitHub Copilot CLI**.

---

## Course Overview

The course uses a single evolving Pygame project as the learning vehicle. Students work with requirements, tests, Git, GitHub Actions, build artifacts, releases, and deployment while using generative AI in a controlled and verifiable way.

The core engineering loop is:

```text
Requirement
    ↓
Test
    ↓
AI-assisted implementation
    ↓
Review
    ↓
Local verification
    ↓
Commit / Pull Request
    ↓
Continuous Integration
    ↓
Build Artifact
    ↓
Release / Deployment
```

### What you'll learn

- ✅ Python fundamentals through a Pygame project
- ✅ Test-Driven Development (TDD) with `pytest`
- ✅ Effective and responsible use of GitHub Copilot CLI
- ✅ Git branches, commits, diffs, Pull Requests, and reviews
- ✅ Continuous Integration with GitHub Actions
- ✅ Code quality with Ruff, mypy, tests, and coverage
- ✅ Build automation and downloadable artifacts
- ✅ Packaging desktop builds
- ✅ Browser deployment of a Pygame game with Pygbag
- ✅ GitHub Pages deployment
- ✅ Semantic Versioning, Git tags, and GitHub Releases
- ✅ Basic logging and release observability

---

## Course Philosophy

### 1. Learn by building

Every concept is introduced through a real change to the game. The project becomes progressively more complete as the engineering process becomes progressively more automated.

### 2. Tests before implementation

Whenever practical, new behavior starts with a test:

```text
RED → GREEN → REFACTOR
```

Example:

```python
def test_player_moves_right():
    assert move_player(100, 100, "RIGHT") == (105, 100)
```

The test defines the expected behavior before the implementation is accepted.

### 3. AI proposes; tests and engineers verify

Copilot may help explain, plan, debug, refactor, document, or implement code, but generated code is **not considered correct until it has been reviewed and verified**.

The recommended interaction model is:

```text
Explain → Plan → Implement → Verify
```

Example prompts:

```text
Explain why this test is failing.
Do not modify any files.
```

```text
Inspect the current project and propose the minimum changes needed
for this requirement. Identify the tests that should exist first.
Do not modify the code yet.
```

```text
Implement the approved plan without changing existing public interfaces.
Make the minimum changes necessary.
```

```text
Run the relevant tests, review the diff, and identify possible edge cases.
```

### 4. Automation should grow with the project

The pipeline begins with a single test job and evolves into a complete delivery workflow:

```text
Test
 ↓
Lint + Type Check + Coverage
 ↓
Build
 ↓
Artifacts
 ↓
Quality Gates
 ↓
Deployment
 ↓
Versioned Release
```

---

## Course Structure

The course is organized into **8 progressive classes**.

| Class | Branch | Topic | Main Outcome |
|---|---|---|---|
| 1 | `class/1-foundations` | Idea → Test → Code | First Pygame game, pytest, TDD, Copilot basics |
| 2 | `class/2-git-features` | Git, Features & Debugging | Incremental development with branches and AI-assisted debugging |
| 3 | `class/3-ci-cd-basics` | Continuous Integration | GitHub Actions, Ruff, mypy, pytest, coverage |
| 4 | `class/4-architecture-testing` | Architecture & Testability | Modular Pygame code and stronger automated tests |
| 5 | `class/5-build-artifacts` | Build & Artifacts | Desktop/web builds, coverage reports, downloadable artifacts |
| 6 | `class/6-quality-gates` | Pull Requests & Quality Gates | PR workflow, required checks, review, individualized feature |
| 7 | `class/7-deployment` | Deployment | Browser build with Pygbag and deployment to GitHub Pages |
| 8 | `class/8-release` | Continuous Delivery & Releases | Version tags, GitHub Releases, automated deployment, logging |

---

# Class Details

## Class 1 — Idea → Test → Code

### Goals

- Introduce generative AI at a basic level.
- Understand that AI output is probabilistic and must be verified.
- Introduce Python and Pygame through a minimal game.
- Introduce `pytest` and the RED → GREEN → REFACTOR cycle.
- Use GitHub Copilot CLI for explanation and minimal implementation.

### Pen-and-paper exercise

Students receive a simple requirement such as:

```text
The player is at (100, 100).
When RIGHT is pressed, the player moves 5 pixels to the right.
The player cannot leave the screen.
```

They first discuss what information an AI assistant would need in order to produce a correct implementation. The exercise introduces **context, constraints, acceptance criteria, and verification** before using Copilot.

### Practical project

Create a minimal Pygame application with:

- a player;
- movement;
- configurable speed;
- screen boundaries;
- unit tests for game logic.

---

## Class 2 — Git, Features & Debugging

### Goals

- Introduce Git as part of the development workflow.
- Work with commits, branches, diffs, and history.
- Add game features incrementally.
- Use Copilot primarily for explanation, planning, and debugging.

### Example features

- enemies;
- collisions;
- score;
- lives;
- restart behavior.

Every feature should include or update automated tests.

Example debugging prompt:

```text
This test is failing.
Analyze the failure and provide three possible causes.
Do not modify the source code.
```

---

## Class 3 — Continuous Integration

### Goals

Introduce GitHub Actions and move verification from a developer's machine to an automated pipeline.

Initial pipeline:

```text
Push / Pull Request
        ↓
Install dependencies
        ↓
pytest
```

Expanded pipeline:

```text
Push / Pull Request
        │
        ├── Ruff
        ├── mypy
        ├── pytest
        └── coverage
```

Students intentionally introduce a defect, push it, inspect a failing CI run, diagnose the problem with Copilot, correct it, and return the pipeline to green.

---

## Class 4 — Architecture & Testability

### Goals

Evolve the project from a simple Pygame script into a maintainable application.

Target structure:

```text
Game
├── Player
├── Enemy
├── Projectile
├── Collision
├── Score
├── GameState
└── Configuration
```

The key design principle is to separate as much **game logic** as possible from **Pygame rendering and input handling**, allowing the important rules to be tested without launching the graphical interface.

Possible additions:

- projectiles;
- multiple enemies;
- game over;
- progressive difficulty;
- game states.

---

## Class 5 — Build & Artifacts

### Goals

Introduce the idea that a CI pipeline should be able not only to verify the software, but also to **produce reusable outputs**.

Pipeline progression:

```text
Lint
 ↓
Type Check
 ↓
Unit Tests
 ↓
Coverage
 ↓
Build
 ↓
Artifact
```

Example artifacts:

```text
coverage-report.zip
test-results.xml
game-build.zip
web-build.zip
```

Students use GitHub Actions artifacts so build outputs can be downloaded from a workflow execution.

### Desktop packaging

PyInstaller can be introduced to produce a distributable desktop build:

```text
Python / Pygame
      ↓
PyInstaller
      ↓
dist/
      ↓
ZIP
      ↓
GitHub Actions Artifact
```

### Web build preparation

Pygbag is introduced as the mechanism that will later allow the Pygame game to run in a browser.

---

## Class 6 — Pull Requests & Quality Gates

### Goals

Move from direct development to a workflow closer to a professional team:

```text
Feature Branch
      ↓
Pull Request
      ↓
CI
      ↓
Review
      ↓
Merge
```

A Pull Request should not be considered ready while required checks fail.

Suggested quality gates:

- Ruff passes;
- mypy passes;
- unit tests pass;
- coverage threshold is met;
- build succeeds.

### Individual feature

Each student implements a different game feature, for example:

- shield;
- boss;
- double shot;
- health system;
- power-up;
- new enemy behavior;
- progressive difficulty.

The feature should include:

```text
Requirement
Acceptance Criteria
Tests
Implementation
Pull Request
CI Evidence
```

Copilot can be used as a code-review assistant, but the student remains responsible for accepting or rejecting its recommendations.

---

## Class 7 — Deployment

### Goals

Take a tested artifact and deploy it to an environment that can be used by another person.

For this course, the Pygame game is packaged for the browser using **Pygbag** and deployed through **GitHub Pages**.

```text
Python + Pygame
       ↓
Pygbag
       ↓
Web Build
       ↓
GitHub Actions
       ↓
GitHub Pages
```

The first deployment can be manually initiated using `workflow_dispatch` so students can clearly distinguish **build** from **deployment**.

Conceptually:

```text
Continuous Integration → Is the change valid?
Build                  → What can we distribute?
Deployment             → Can users run this version?
```

---

## Class 8 — Continuous Delivery, Versioning & Release

### Goals

Automate the complete journey from a validated change to a versioned release.

Final pipeline:

```text
Pull Request
     ↓
Ruff
     ↓
mypy
     ↓
pytest
     ↓
Coverage
     ↓
Build Desktop
     ↓
Build Web
     ↓
Artifacts
     ↓
Merge
     ↓
Version Tag
     ↓
GitHub Release
     ↓
Production Deployment
```

Students also add basic runtime logging and release metadata so a running build can identify its version and report meaningful errors.

---

## Repository and Branch Strategy

### Instructor repository

`main` is the course home. It contains the general README, common project structure, shared instructions, and stable course-level material.

Each `class/*` branch contains the canonical material or reference state for that class:

```text
main
│
├── class/1-foundations
├── class/2-git-features
├── class/3-ci-cd-basics
├── class/4-architecture-testing
├── class/5-build-artifacts
├── class/6-quality-gates
├── class/7-deployment
└── class/8-release
```

The class branches are intended primarily as **course checkpoints/reference states**, not as a substitute for the student's own development history.

### Student repository

For a course that relies on multiple progressive branches, the recommended approach is to **fork the instructor repository** or clone it and push it to a new student-owned repository. This preserves the branch history needed for the class checkpoints.

A GitHub template repository may also be used for a clean starting repository, but when all template branches are copied GitHub creates those branches with unrelated histories. For this reason, a fork or normal clone is simpler when branch-to-branch history matters.

Example:

```bash
git clone <student-repository-url>
cd de-la-idea-al-despliegue

git branch -a
git checkout class/1-foundations
```

Students should create their own working branch for exercises and features rather than making all changes directly on the instructor class branch.

Example:

```bash
git checkout -b feature/player-movement
```

---

## Versioning Strategy

The project uses **Semantic Versioning (SemVer)**:

```text
MAJOR.MINOR.PATCH
```

Example:

```text
v1.2.3
```

### Version meaning

- **MAJOR** — incompatible or intentionally breaking changes.
- **MINOR** — new backward-compatible functionality.
- **PATCH** — backward-compatible fixes.

During the course, versions before the final release remain in the `0.x` development series.

Suggested educational milestones:

| Milestone | Suggested Version |
|---|---|
| Class 1 complete | `v0.1.0` |
| Class 2 complete | `v0.2.0` |
| Class 3 complete | `v0.3.0` |
| Class 4 complete | `v0.4.0` |
| Class 5 artifacts complete | `v0.5.0` |
| Class 6 quality gates complete | `v0.6.0` |
| Class 7 deployed | `v0.7.0` |
| Class 8 final release | `v1.0.0` |

A defect fixed without adding a feature increments the patch number:

```text
v0.5.0 → v0.5.1
```

A new backward-compatible feature after the final release increments the minor number:

```text
v1.0.0 → v1.1.0
```

A breaking change after the final release increments the major number:

```text
v1.4.2 → v2.0.0
```

### Git tags

Example:

```bash
git tag -a v0.5.0 -m "Class 5: Build artifacts"
git push origin v0.5.0
```

By Class 8, a version tag such as `v1.0.0` should be able to trigger the release workflow:

```text
Tag v1.0.0
     ↓
Validate
     ↓
Build
     ↓
Publish Artifacts
     ↓
Create GitHub Release
     ↓
Deploy Web Build
```

A `CHANGELOG.md` is recommended so students can connect source-code changes to released versions.

---

## Project Structure

A possible project structure is:

```text
.
├── src/
│   ├── game/
│   │   ├── player.py
│   │   ├── enemy.py
│   │   ├── collision.py
│   │   ├── score.py
│   │   └── rules.py
│   ├── pygame_app/
│   │   ├── renderer.py
│   │   ├── input.py
│   │   └── main.py
│   └── config.py
├── tests/
├── assets/
├── docs/
│   └── ai-log.md
├── .github/
│   └── workflows/
├── requirements.txt
└── README.md
```

---

## AI Development Log

Students should maintain a lightweight record of meaningful AI-assisted development decisions in:

```text
docs/ai-log.md
```

Suggested format:

```markdown
## Prompt

Explain why test_player_collision is failing.
Do not modify the code.

## Result

Copilot identified that collision detection was using stale coordinates.

## Decision

The explanation was accepted, but the correction was implemented manually.

## Verification

pytest tests/test_collision.py

5 passed.
```

The goal is not to record every AI interaction, but to capture important examples of **generation, debugging, review, acceptance, rejection, and verification**.

---

## Prerequisites

Recommended:

- Python 3.11+
- Basic programming concepts
- Basic terminal/command-line use
- Git installed
- GitHub account
- GitHub Copilot access for Copilot CLI exercises

Students do **not** need prior experience with CI/CD or Pygame.

---

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd de-la-idea-al-despliegue
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run tests

```bash
pytest
```

### 5. Run coverage

```bash
pytest --cov=src --cov-report=term-missing
```

### 6. Run linting

```bash
ruff check .
```

### 7. Run type checking

```bash
mypy src
```

### 8. Run the game

```bash
python -m src.pygame_app.main
```

> The exact command may evolve as the project architecture changes across class branches.

---

## GitHub Copilot CLI

Copilot CLI is used as an AI-assisted engineering tool during the course.

Typical commands include:

```bash
copilot
```

and repository-specific initialization:

```bash
copilot init
```

Students are expected to review all proposed changes and verify them with tests and CI before accepting them.

---

## CI/CD Pipeline

The GitHub Actions pipeline evolves throughout the course.

### Early course

```text
pytest
```

### Middle of course

```text
Ruff
 ↓
mypy
 ↓
pytest
 ↓
coverage
 ↓
build
 ↓
artifacts
```

### Final course pipeline

```text
Pull Request
     ↓
Quality Gates
     ↓
Build
     ↓
Artifacts
     ↓
Version Tag
     ↓
GitHub Release
     ↓
GitHub Pages Deployment
```

See `.github/workflows/` for the workflows implemented in each class branch.

---

## Deployment Target

The recommended deployment path for this course is:

```text
Pygame
  ↓
Pygbag
  ↓
WebAssembly-compatible browser build
  ↓
GitHub Actions artifact
  ↓
GitHub Pages
```

This allows the final project to be shared through a URL without requiring the evaluator or another student to install Python locally.

Desktop builds may also be published as downloadable GitHub Release assets.

---

## Evaluation Evidence

A student's final repository can provide evidence from multiple dimensions instead of relying only on whether the game runs:

- functionality;
- automated tests;
- test coverage;
- commits and development history;
- Pull Requests;
- CI results;
- build artifacts;
- version tags;
- releases;
- deployed game;
- AI development log;
- documentation.

Useful process metrics may include:

```text
Test Pass Rate
Code Coverage
Pipeline Success Rate
CI Failures
Time to Green
Build Success Rate
Deployment Success Rate
Number of Commits
Pull Request Results
AI-assisted debugging interactions
AI suggestions accepted/rejected
```

---

## References and Technical Documentation

### AI-assisted programming education

- Groothuijsen, S., van den Beemt, A. A. J., Remmers, J. J. C., & van Meeuwen, L. W. (2024). *AI chatbots in programming education: Students' use in a scientific computing course and consequences for learning*. Computers and Education: Artificial Intelligence, 7, 100290. https://doi.org/10.1016/j.caeai.2024.100290
- Sun, D., Boudouaia, A., Zhu, C., & Li, Y. (2024). *Would ChatGPT-facilitated programming mode impact college students' programming behaviors, performances, and perceptions? An empirical study*. International Journal of Educational Technology in Higher Education, 21, 14. https://doi.org/10.1186/s41239-024-00446-5

### Testing and CI/CD education

- Bowyer, J., & Hughes, J. (2006). *Assessing undergraduate experience of continuous integration and test-driven development*. Proceedings of the 28th International Conference on Software Engineering, 691–694. https://doi.org/10.1145/1134285.1134393
- Cadavid, H. F. (2018). *Continuous delivery pipelines for teaching agile and developing software engineering skills*. International Journal of Modern Education and Computer Science, 10(5), 17–26. https://doi.org/10.5815/ijmecs.2018.05.03
- Janzen, D. S., & Saiedian, H. (2006). *On the influence of test-driven development on software design*. Proceedings of the 19th Conference on Software Engineering Education and Training, 141–148. https://doi.org/10.1109/CSEET.2006.25

### Official documentation

- GitHub Copilot CLI: https://docs.github.com/en/copilot/reference/copilot-cli-reference
- GitHub Actions: https://docs.github.com/en/actions
- GitHub Pages custom workflows: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- Pygbag: https://pygame-web.github.io/wiki/pygbag/
- Semantic Versioning: https://semver.org/

---

## License

MIT License — see `LICENSE` for details.

---

## Final Goal

The goal is not only to create a videogame. The goal is to understand and practice the complete software-delivery lifecycle:

```text
IDEA
 ↓
REQUIREMENT
 ↓
TEST
 ↓
AI-ASSISTED DEVELOPMENT
 ↓
CODE
 ↓
GIT
 ↓
CONTINUOUS INTEGRATION
 ↓
BUILD
 ↓
ARTIFACT
 ↓
VERSION
 ↓
RELEASE
 ↓
DEPLOYMENT
```

**Build software. Test everything. Automate the process. Use AI responsibly.**
