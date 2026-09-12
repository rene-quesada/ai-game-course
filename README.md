# De la Idea al Despliegue con IA

## Desarrollo de videojuegos con Python, Pygame, GitHub Copilot y CI/CD

Este repositorio contiene los materiales del curso **De la Idea al Despliegue con IA**, un curso práctico orientado al desarrollo moderno de software mediante **Python, Pygame, Git, GitHub, GitHub Copilot CLI y GitHub Actions**.

A lo largo de ocho clases, los estudiantes desarrollarán progresivamente un videojuego utilizando inteligencia artificial generativa como asistente de programación, mientras aprenden prácticas fundamentales de ingeniería de software como:

- Test-Driven Development (TDD).
- Control de versiones con Git.
- Desarrollo mediante branches.
- Pruebas automatizadas.
- Code coverage.
- Linting y análisis estático.
- Continuous Integration (CI).
- Build automation.
- Build artifacts.
- Pull Requests y quality gates.
- Continuous Delivery / Deployment (CD).
- Releases.
- Logging y observabilidad básica.

El objetivo del curso **no es enseñar Machine Learning ni construir modelos de inteligencia artificial**.

La inteligencia artificial se utiliza como una **herramienta de apoyo al proceso de desarrollo de software**, principalmente mediante **GitHub Copilot CLI**.

---

# 1. Filosofía del curso

El curso sigue cuatro principios fundamentales.

## 1.1 Aprender haciendo

Cada concepto se introduce mediante cambios reales sobre un proyecto de software.

Durante las ocho clases, el estudiante construirá progresivamente un videojuego funcional en Pygame.

El proyecto evolucionará aproximadamente de esta forma:

```text
Idea
 ↓
Requirement
 ↓
Test
 ↓
Código
 ↓
Git
 ↓
Continuous Integration
 ↓
Build
 ↓
Artifact
 ↓
Deployment
 ↓
Release
 ↓
Monitoring
```

---

## 1.2 Tests antes que implementación

Siempre que sea posible se utilizará el ciclo:

```text
RED
 ↓
GREEN
 ↓
REFACTOR
```

Antes de implementar una nueva funcionalidad se define el comportamiento esperado mediante pruebas automatizadas.

Ejemplo:

```python
def test_player_moves_right():
    assert move_player(100, 100, "RIGHT") == (105, 100)
```

Inicialmente el test debe fallar.

```text
FAILED
```

Después se utiliza Python y, cuando corresponda, GitHub Copilot para implementar la funcionalidad.

Finalmente:

```text
PASSED
```

---

## 1.3 La IA propone, los tests verifican

GitHub Copilot puede:

- explicar código;
- sugerir implementaciones;
- analizar errores;
- proponer tests;
- ayudar a refactorizar;
- explicar errores de CI;
- generar documentación;
- analizar cambios.

Sin embargo:

> El código generado por IA no se considera correcto hasta que haya sido revisado y verificado.

El flujo recomendado durante el curso será:

```text
Requirement
     ↓
Test
     ↓
Prompt
     ↓
Copilot
     ↓
Review
     ↓
pytest
     ↓
CI
```

---

## 1.4 Explain → Plan → Implement → Verify

Durante el curso se evitarán prompts genéricos como:

```text
Make me a game.
```

En su lugar se utilizará un proceso más estructurado.

### Explain

```text
Explain why this test is failing.
Do not modify the code.
```

### Plan

```text
Inspect the current project.

Propose the minimum changes necessary to implement this requirement.

Identify which tests should be created or modified.

Do not change any files yet.
```

### Implement

```text
Implement the approved plan.

Do not change existing public interfaces.

Make the minimum changes necessary.
```

### Verify

```text
Run the relevant tests.

Review the changes and identify possible edge cases.
```

---

# 2. Tecnologías utilizadas

El curso utiliza principalmente:

| Tecnología | Propósito |
|---|---|
| Python | Lenguaje principal |
| Pygame / pygame-ce | Desarrollo del videojuego |
| pytest | Unit testing |
| pytest-cov | Code coverage |
| Ruff | Linting |
| mypy | Type checking |
| Git | Control de versiones |
| GitHub | Repositorios y Pull Requests |
| GitHub Copilot CLI | Desarrollo asistido por IA |
| GitHub Actions | CI/CD |
| GitHub Actions Artifacts | Build artifacts |
| PyInstaller | Empaquetado desktop |
| Pygbag | Build WebAssembly/browser |
| GitHub Pages | Deployment web |
| GitHub Releases | Distribución de versiones |

---

# 3. Proyecto del curso

Durante las ocho clases se desarrollará un videojuego 2D utilizando Pygame.

El proyecto podrá tomar la forma de un juego estilo:

- Space Defender.
- Dungeon Escape.
- Asteroids.
- Top-down shooter.
- Survival game.

El juego exacto puede variar, pero deberá permitir incorporar progresivamente conceptos como:

```text
Player
Enemies
Movement
Collision
Score
Lives
Projectiles
Power-ups
Game states
Levels
Configuration
Logging
```

La lógica del juego se mantendrá separada, en la medida de lo posible, del rendering de Pygame.

Ejemplo:

```text
src/
├── game/
│   ├── player.py
│   ├── enemy.py
│   ├── collision.py
│   ├── score.py
│   └── rules.py
│
├── pygame_app/
│   ├── renderer.py
│   ├── input.py
│   └── main.py
│
└── config.py
```

Esto permitirá probar la lógica del juego sin depender directamente de la interfaz gráfica.

---

# 4. Organización del repositorio

La rama `main` contiene:

- este README;
- información general del curso;
- instrucciones;
- estructura del proyecto;
- materiales compartidos.

Cada clase tendrá una rama específica.

```text
main
│
├── class-01
├── class-02
├── class-03
├── class-04
├── class-05
├── class-06
├── class-07
└── class-08
```

Cada branch representa el punto de inicio correspondiente a una clase.

---

# 5. Flujo de trabajo del estudiante

Al inicio del curso cada estudiante creará su propio repositorio a partir del proyecto base.

El flujo esperado será:

```text
Course Repository
      ↓
Create student repository
      ↓
Clone
      ↓
Checkout class branch
      ↓
Create working branch
      ↓
Develop
      ↓
Test
      ↓
Commit
      ↓
Push
      ↓
Pull Request
      ↓
CI
```

Ejemplo:

```bash
git clone <student-repository>
cd de-la-idea-al-despliegue

git checkout class-03

git checkout -b feature/class-03
```

---

# 6. Flujo de desarrollo de cada clase

Cada clase seguirá, cuando sea posible, la misma secuencia:

```text
1. Leer requirement

2. Entender acceptance criteria

3. Ejecutar los tests existentes

4. Crear/modificar tests

5. Obtener RED

6. Consultar Copilot cuando sea necesario

7. Revisar la propuesta

8. Implementar

9. Obtener GREEN

10. Refactorizar

11. Ejecutar lint/type checking

12. Commit

13. Push

14. GitHub Actions

15. Pipeline GREEN
```

---

# 7. Estructura de las clases

---

# Class 1 — Idea → Test → Código

## Objetivo

Introducir:

- conceptos básicos de IA generativa;
- prompting;
- Python;
- Pygame;
- testing;
- Test-Driven Development.

## Conceptos

- ¿Qué es IA generativa?
- Contexto.
- Prompt.
- Restricciones.
- Hallucinations / respuestas incorrectas.
- Verificación.
- Python básico.
- pytest.
- TDD.

## Ejercicio inicial

Los estudiantes reciben un requisito sencillo:

```text
El jugador se mueve cinco píxeles hacia la derecha
cuando se presiona RIGHT.
```

Antes de implementar:

```python
def test_move_right():
    assert move_player(100, 100, "RIGHT") == (105, 100)
```

Después se implementa el código necesario para hacer pasar el test.

## Primer uso de Copilot

Ejemplo:

```text
Inspect the failing tests.

Explain what functionality is missing.

Do not modify any files.
```

Posteriormente:

```text
Implement the minimum functionality required
to make the tests pass.
```

## Proyecto

Crear una ventana básica de Pygame con:

- jugador;
- movimiento;
- límites de pantalla;
- velocidad configurable.

## Resultado

```text
Idea
 ↓
Test
 ↓
Code
 ↓
Working Pygame application
```

---

# Class 2 — Git + Features + Debugging

## Objetivo

Introducir desarrollo incremental y control de versiones.

## Conceptos

- Git.
- Repository.
- Commit.
- Branch.
- Diff.
- Merge.
- Debugging.
- Edge cases.

## Features

Agregar progresivamente:

- enemigos;
- colisiones;
- score;
- vidas;
- restart.

Cada feature deberá tener tests asociados.

## Copilot

Copilot se utiliza principalmente para:

### Explicar

```text
Explain this function.
```

### Debugging

```text
This test is failing.

Analyze the failure and provide three possible causes.

Do not change the source code.
```

### Planning

```text
Propose a minimal implementation plan for collision detection.

Identify the tests that should exist before implementing it.
```

## Resultado

Videojuego con varias funcionalidades y desarrollo mediante Git.

---

# Class 3 — Continuous Integration

## Objetivo

Automatizar la validación del proyecto.

## Introducción a GitHub Actions

Primer pipeline:

```text
Push
 ↓
GitHub Actions
 ↓
Install dependencies
 ↓
pytest
```

Después se amplía:

```text
Push / Pull Request
        │
        ├── Install
        │
        ├── Ruff
        │
        ├── mypy
        │
        ├── pytest
        │
        └── coverage
```

## Ejercicio principal

Introducir intencionalmente un defecto.

```text
Local change
 ↓
Commit
 ↓
Push
 ↓
CI FAILS
```

Después utilizar Copilot para investigar el error.

```text
Inspect the CI failure.

Explain the root cause.

Do not make any modifications.
```

Finalmente:

```text
Fix
 ↓
Push
 ↓
CI GREEN
```

## Resultado

El repositorio ya tiene un sistema básico de **Continuous Integration**.

---

# Class 4 — Arquitectura y Testing del juego

## Objetivo

Evolucionar de un script Pygame a una aplicación organizada.

## Conceptos

- separación de responsabilidades;
- módulos;
- funciones puras;
- dependency separation;
- testability;
- refactoring.

## Arquitectura aproximada

```text
Game
│
├── Player
├── Enemy
├── Projectile
├── Collision
├── Score
├── GameState
└── Configuration
```

Se buscará separar:

```text
Game Logic
```

de:

```text
Rendering
```

## Proyecto

Agregar:

- projectiles;
- múltiples enemigos;
- score;
- game over;
- restart;
- dificultad progresiva.

## Resultado

Juego modular con una arquitectura que pueda ser probada y mantenida.

---

# Class 5 — Build & Artifacts

## Objetivo

Introducir el concepto de **build artifact**.

Hasta esta clase el pipeline valida el código.

Ahora comenzará a **producir un resultado reutilizable**.

## Concepto

Un artifact es una salida producida automáticamente por el pipeline.

Ejemplos:

```text
Source Code
    ↓
Pipeline
    ↓
Artifact
```

Artifacts del curso:

```text
coverage-report.zip

game-build.zip

test-results.xml

dist/
```

## Pipeline

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

## GitHub Actions Artifacts

El pipeline deberá almacenar automáticamente resultados como:

```text
game-build
coverage-report
test-results
```

Estos artifacts deberán poder descargarse desde la ejecución del workflow.

## Build desktop

Se puede introducir PyInstaller para producir una versión ejecutable.

Ejemplo conceptual:

```text
Python/Pygame
      ↓
PyInstaller
      ↓
dist/game
      ↓
ZIP
      ↓
GitHub Artifact
```

## Versionado

Introducción sencilla a:

```text
0.1.0
0.2.0
0.3.0
```

y conceptos básicos de Semantic Versioning.

## Resultado

El pipeline deja de limitarse a verificar software.

Ahora:

> **CI también produce software distribuible.**

---

# Class 6 — Pull Requests & Quality Gates

## Objetivo

Introducir un flujo de desarrollo similar al utilizado en equipos profesionales.

El flujo cambia de:

```text
Developer
 ↓
main
```

a:

```text
Developer
 ↓
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

## Quality Gates

Un Pull Request no deberá integrarse si falla:

```text
Lint
Type Check
Unit Tests
Coverage
Build
```

## Copilot como reviewer

Ejemplo:

```text
Review the current diff.

Look specifically for:

- bugs;
- missing tests;
- duplicated logic;
- unnecessary complexity;
- possible edge cases.

Do not modify the code.
```

## Feature individual

Cada estudiante implementará una funcionalidad distinta.

Ejemplos:

- shield;
- boss;
- double shot;
- health;
- power-up;
- new enemy;
- progressive difficulty.

Cada feature deberá incluir:

```text
Requirement
Acceptance Criteria
Tests
Implementation
Pull Request
CI
```

## Resultado

El estudiante completa una modificación utilizando un flujo completo basado en Pull Requests.

---

# Class 7 — Deployment

## Objetivo

Convertir el juego Pygame en una aplicación accesible mediante una URL.

## Pygame en navegador

El proyecto utilizará **Pygbag** para generar una versión WebAssembly compatible con navegador.

Flujo:

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

## Primer deployment

Inicialmente el deployment podrá ejecutarse manualmente.

```text
workflow_dispatch
       ↓
Build
       ↓
Web Artifact
       ↓
Deploy
       ↓
GitHub Pages
```

Ejemplo conceptual de resultado:

```text
https://<username>.github.io/<repository>/
```

## Objetivo pedagógico

Distinguir:

### Continuous Integration

```text
¿El cambio funciona?
```

de:

### Deployment

```text
¿Podemos ejecutar esa versión en un ambiente real?
```

## Environment

Se introduce el concepto:

```text
Development
 ↓
Staging
 ↓
Production
```

Para efectos del curso, GitHub Pages puede funcionar como ambiente desplegado.

## Resultado

Cada estudiante tendrá una versión del juego que puede ejecutarse desde un navegador.

---

# Class 8 — Continuous Delivery

## Objetivo

Automatizar el proceso completo desde código hasta release.

Pipeline final:

```text
Pull Request
     ↓
Lint
     ↓
Type Check
     ↓
Unit Tests
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
Deploy
     ↓
Release
```

## Tags

Se introduce versionado mediante tags.

Ejemplo:

```bash
git tag v1.0.0
git push origin v1.0.0
```

El tag puede iniciar:

```text
Tag v1.0.0
     ↓
GitHub Actions
     ↓
Tests
     ↓
Build
     ↓
Artifacts
     ↓
GitHub Release
     ↓
Production Deployment
```

## GitHub Release

La versión final podrá incluir:

```text
game-windows.zip
game-web.zip
coverage-report
release-notes.md
```

## Continuous Delivery

El objetivo final será comprender:

```text
Code
 ↓
Commit
 ↓
CI
 ↓
Build
 ↓
Artifact
 ↓
Release
 ↓
Deployment
```

---

# 8. Pipeline final del curso

Al terminar la Clase 8 el proyecto deberá implementar aproximadamente:

```text
                    Developer
                        │
                        ▼
                  Feature Branch
                        │
                        ▼
                   Pull Request
                        │
            ┌───────────┴────────────┐
            │                        │
            ▼                        ▼
           Ruff                     mypy
            │                        │
            └───────────┬────────────┘
                        ▼
                     pytest
                        │
                        ▼
                    Coverage
                        │
                        ▼
                      Build
                        │
               ┌────────┴────────┐
               ▼                 ▼
          Desktop Build      Web Build
               │                 │
               └────────┬────────┘
                        ▼
                    Artifacts
                        │
                        ▼
                      Merge
                        │
                        ▼
                     Release
                        │
                        ▼
                     Deploy
                        │
                        ▼
                  GitHub Pages
```

---

# 9. Entregables por clase

Cada clase podrá producir algunos o todos los siguientes elementos:

- Código fuente.
- Unit tests.
- Git commits.
- Prompt log.
- README actualizado.
- GitHub Actions workflow.
- Coverage report.
- Build artifact.
- Pull Request.
- Release.
- Deployment.

---

# 10. AI Development Log

Cada estudiante mantendrá:

```text
docs/
└── ai-log.md
```

El documento registrará los usos más relevantes de IA.

Formato sugerido:

```markdown
## Prompt

Explain why test_player_collision is failing.
Do not modify the code.

## Result

Copilot identified that collision detection was using
the previous player coordinates.

## Decision

Accepted the explanation but implemented the correction manually.

## Verification

pytest tests/test_collision.py

5 passed.
```

El propósito no es registrar cada interacción con la IA, sino aquellas que hayan tenido impacto en el desarrollo.

---

# 11. Evaluación

El funcionamiento del programa no será el único criterio de evaluación.

| Área | Peso sugerido |
|---|---:|
| Funcionalidad | 20% |
| Testing y TDD | 20% |
| CI/CD | 20% |
| Uso razonado de IA | 15% |
| Calidad del código | 10% |
| Feature individual | 10% |
| Documentación | 5% |

Los tests pasando son una condición necesaria, pero no demuestran por sí solos comprensión.

---

# 12. Métricas del proceso

Durante el curso pueden recopilarse métricas como:

```text
Test Pass Rate

Code Coverage

Pipeline Success Rate

CI Failures

Time to Green

Number of Commits

Pull Request Success

Build Success Rate

Deployment Success Rate
```

Para estudiar el uso de IA también se pueden considerar:

```text
AI prompts used

Debugging prompts

Code-generation prompts

Suggested changes accepted

Suggested changes rejected

AI-generated defects detected

AI-assisted defect corrections
```

---

# 13. Resultado final esperado

Al terminar el curso el estudiante habrá desarrollado un videojuego funcional utilizando Python y Pygame y habrá construido alrededor de él un proceso moderno de ingeniería de software.

El estudiante habrá experimentado el flujo completo:

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
PULL REQUEST
 ↓
CONTINUOUS INTEGRATION
 ↓
BUILD
 ↓
ARTIFACT
 ↓
RELEASE
 ↓
DEPLOYMENT
```

El objetivo final no es únicamente:

> "Crear un videojuego".

El objetivo es comprender:

> **cómo una idea se convierte de forma controlada, verificable y automatizada en software que puede ser entregado a un usuario.**

---

# 14. Resumen de las ocho clases

| Clase | Tema | Resultado principal |
|---|---|---|
| 1 | Idea → Test → Código | Primer juego + TDD + Copilot |
| 2 | Git + Features | Juego incremental |
| 3 | Continuous Integration | Pipeline automático |
| 4 | Arquitectura + Testing | Juego modular |
| 5 | Build + Artifacts | Software empaquetado |
| 6 | Pull Requests + Quality Gates | Flujo profesional |
| 7 | Deployment | Juego disponible en navegador |
| 8 | Continuous Delivery + Release | Pipeline completo |

---

# De la Idea al Despliegue

```text
Think
 ↓
Test
 ↓
Code
 ↓
Verify
 ↓
Integrate
 ↓
Build
 ↓
Deliver
 ↓
Observe
```

**Build software. Test everything. Automate the process. Use AI responsibly.**
