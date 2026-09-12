# De la Idea al Despliegue con IA - Course Summary

## Executive Summary

A comprehensive, hands-on software engineering course that teaches:
- **Python fundamentals** through a real Pygame project
- **Test-Driven Development (TDD)** and testing best practices
- **Responsible AI integration** using GitHub Copilot CLI
- **Modern CI/CD practices** with GitHub Actions
- **Complete software delivery lifecycle** from idea to production

Over **8 progressive classes**, students build a complete videogame while learning production-grade engineering practices.

---

## Course Vision

> **The goal is not to create a videogame. The goal is to understand how an idea becomes controlled, verifiable, and automated software that can be delivered to a user.**

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

---

## What Makes This Course Unique

### 1. **Learning by Building**
Every concept is introduced through a real change to a working game. Students don't study CI/CD in isolation—they implement it while building features they can see and play.

### 2. **Test-Driven Development from Day One**
Tests define behavior before implementation. The RED → GREEN → REFACTOR cycle is practiced from Class 1.

### 3. **AI as a Tool, Not a Shortcut**
GitHub Copilot CLI assists with explanation, planning, debugging, and implementation, but students remain responsible for verification. Generated code is not accepted until tested and reviewed.

### 4. **Progressive Automation**
The CI/CD pipeline grows with the project:
- Class 1-2: Local testing
- Class 3: GitHub Actions basics
- Class 4-5: Build and artifacts
- Class 6: Quality gates and reviews
- Class 7: Deployment
- Class 8: Full release automation

---

## The 8 Classes at a Glance

| Class | Duration | Topic | Key Learning |
|-------|----------|-------|--------------|
| **1** | 4-5h | Idea → Test → Code | Python, pytest, TDD, Copilot basics |
| **2** | 4-5h | Git, Features & Debugging | Branches, commits, incremental features |
| **3** | 4-5h | Continuous Integration | GitHub Actions, Ruff, mypy, coverage |
| **4** | 5-6h | Architecture & Testing | Modular design, separation of concerns |
| **5** | 5-6h | Build & Artifacts | Desktop/web builds, downloadable artifacts |
| **6** | 5-6h | Pull Requests & Quality Gates | Professional workflow, individualized feature |
| **7** | 4-5h | Deployment | Browser deployment via Pygbag + GitHub Pages |
| **8** | 4-5h | Continuous Delivery & Release | Versioning, tags, releases, automation |

**Total:** ~40 hours of hands-on learning

---

## Technology Stack

| Component | Tool | Version |
|-----------|------|---------|
| **Language** | Python | 3.11+ |
| **Game Framework** | Pygame | 2.6.1 |
| **Testing** | pytest | 9.1.1 |
| **Coverage** | pytest-cov | 7.1.0 |
| **Linting** | Ruff | 0.16.7 |
| **Type Checking** | mypy | 2.3.1 |
| **Desktop Build** | PyInstaller | 6.22.2 |
| **Web Build** | Pygbag | 0.9.3 |
| **CI/CD** | GitHub Actions | (cloud) |
| **VCS** | Git | (client) |
| **AI Assistant** | GitHub Copilot CLI | (cloud) |
| **Deployment** | GitHub Pages | (cloud) |

---

## Learning Outcomes

After completing this course, students can:

✅ Write Python code following TDD principles  
✅ Use Git effectively for version control and collaboration  
✅ Understand and implement automated testing and coverage  
✅ Set up and maintain CI/CD pipelines  
✅ Use generative AI responsibly as a development tool  
✅ Apply code quality tools (linting, type checking)  
✅ Build, package, and distribute software  
✅ Deploy applications to production  
✅ Manage releases and semantic versioning  
✅ Monitor and maintain deployed software  
✅ Work in a professional software engineering workflow  

---

## Repository Structure

```text
de-la-idea-al-despliegue/
│
├── main                          (course reference)
│   ├── README.md                 (course overview)
│   ├── requirements.txt           (pinned dependencies)
│   ├── docs/
│   │   ├── SUMMARY.md            (this file)
│   │   ├── ARCHITECTURE.md       (design philosophy)
│   │   ├── AI-CONTEXT.md         (AI usage guidelines)
│   │   └── DESIGN-RULES.md       (design patterns - future)
│   └── .gitignore
│
├── develop                       (integration branch)
│   └── (same as main, ready for class branches)
│
├── class/1-foundations           (reference state after class 1)
├── class/2-git-features          (reference state after class 2)
├── class/3-ci-cd-basics          (reference state after class 3)
├── class/4-architecture-testing
├── class/5-build-artifacts
├── class/6-quality-gates
├── class/7-deployment
└── class/8-release               (final project state)
```

---

## Student Workflow

1. **Clone** the instructor repository
2. **Checkout** the class branch (e.g., `class/1-foundations`)
3. **Create** a feature branch (e.g., `feature/player-movement`)
4. **Develop** with tests, commits, and local verification
5. **Push** to their own repository
6. **Create a Pull Request** (if in team setting)
7. **Verify** CI/CD pipeline passes
8. **Merge** and continue to next class

---

## Grading and Evaluation

### Dimensions of Learning (not just "does the game work?")

| Dimension | Weight | Evidence |
|-----------|--------|----------|
| Functionality | 20% | Game features work as specified |
| Testing & TDD | 20% | Tests exist, coverage is adequate |
| CI/CD | 20% | Pipeline is automated, quality gates work |
| Responsible AI Use | 15% | AI was used effectively, not as a substitute for learning |
| Code Quality | 10% | Clean, maintainable, well-structured code |
| Individual Features | 10% | Student's unique contribution to the game |
| Documentation | 5% | AI Development Log, comments, README updates |

### Process Metrics

- Test Pass Rate
- Code Coverage %
- Pipeline Success Rate
- Commits and branches
- Pull Request count and quality
- Time to Green (CI)
- Deployment Success Rate

---

## Success Criteria

A successful student will:

1. **Understand the problem** before writing code
2. **Write tests first** and make them pass
3. **Use Copilot responsibly** — verify, don't blindly accept
4. **Commit frequently** with clear messages
5. **Push to CI/CD** and ensure pipeline is green
6. **Review their own code** for quality and edge cases
7. **Document meaningful AI interactions** in the AI Development Log
8. **Deploy** a working game accessible via URL
9. **Version and release** with proper tagging
10. **Reflect** on the entire software delivery lifecycle

---

## Prerequisites

### Required
- Python 3.11+
- Git installed
- GitHub account
- Familiarity with command line / terminal

### Recommended
- Basic programming experience
- GitHub Copilot access (or willingness to sign up)
- Basic understanding of software testing concepts

### NOT Required
- Prior Pygame experience
- CI/CD experience
- Machine Learning knowledge (this is NOT an ML course)

---

## How to Use This Course

### For Instructors
1. Fork or clone this repository
2. Assign students to work through classes in order
3. Each class has clear goals and acceptance criteria
4. Use the AI Development Log to track responsible AI usage
5. Evaluate using the dimensions above

### For Students
1. Clone the repository
2. Start with `class/1-foundations`
3. Follow the requirements in each class branch
4. Create your own repository as a fork
5. Work through features incrementally
6. Maintain the AI Development Log
7. Progress through all 8 classes

### For Self-Learners
1. Clone this repository
2. Work through each class branch at your own pace
3. Complete all exercises and projects
4. Document your AI interactions
5. Deploy your final project

---

## Resources

### Official Documentation
- [GitHub Copilot CLI](https://docs.github.com/en/copilot/reference/copilot-cli-reference)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [pytest Documentation](https://docs.pytest.org/)
- [Pygbag Documentation](https://pygame-web.github.io/wiki/pygbag/)
- [Semantic Versioning](https://semver.org/)

### Recommended Reading
- *Test Driven Development: By Example* — Kent Beck
- *The Pragmatic Programmer* — Hunt & Thomas
- *A Philosophy of Software Design* — John Ousterhout

---

## Contact & Support

For questions or feedback about this course:
- Review the class-specific documentation
- Check the AI-CONTEXT.md for AI-related guidance
- Refer to ARCHITECTURE.md for design decisions
- Review the DESIGN-RULES.md for patterns (as it develops)

---

**Build software. Test everything. Automate the process. Use AI responsibly.**
