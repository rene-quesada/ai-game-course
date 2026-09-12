# AI Context & GitHub Copilot Usage Guidelines

## Philosophy: AI as a Tool, Not a Shortcut

GitHub Copilot CLI is available throughout this course as a software engineering assistant. The goal is to learn **responsible and effective use of generative AI**, not to bypass learning.

### Core Principle

> **AI proposes. Tests verify. Engineers decide.**

Generated code is **not considered correct** until it has been reviewed, tested, and verified.

---

## When to Use Copilot (Do Use)

### 1. **Explaining Code**

**Prompt:**
```text
Explain what this function does and why it might fail.
```

**Why:** Helps you understand intent and potential issues without modifying anything.

**Example:**
```text
[Your code]

Copilot: "This function calculates the Euclidean distance between two points.
However, it doesn't handle the case where the two points are identical,
which could cause unexpected precision issues."
```

### 2. **Planning Implementation**

**Prompt:**
```text
I need to implement collision detection between a player and enemies.
Propose a minimal plan:
- What functions should I write?
- What should each function do?
- What tests should exist first?
Do not modify any code yet.
```

**Why:** Helps structure your approach before coding.

**What to do:**
1. Read the plan carefully
2. Agree or disagree with the approach
3. Ask clarifying questions
4. Proceed only when you understand it

### 3. **Debugging Issues**

**Prompt:**
```text
This test is failing:

[Test code]
[Error message]

Analyze the failure and suggest three possible causes.
Do not modify the source code.
```

**Why:** AI can spot patterns in errors quickly.

**What to do:**
1. Read each possibility
2. Check your code against each
3. Create a hypothesis
4. Test your hypothesis
5. Fix the root cause (not just the symptom)

### 4. **Code Review Assistance**

**Prompt:**
```text
Review this diff for potential bugs, missing tests, and edge cases.
Do not modify the code.

[Your changes]
```

**Why:** Extra eyes on your work, even if they're AI.

**What to do:**
1. Read the feedback carefully
2. Disagree if the AI is wrong (it often is)
3. Add tests for any edge cases found
4. Only change code if you agree it's necessary

### 5. **Refactoring Suggestions**

**Prompt:**
```text
This function is complex. Suggest ways to simplify it or split it up.
Do not modify the code.

[Your function]
```

**Why:** Helps you see opportunities for improvement.

**What to do:**
1. Understand the suggestion
2. Try refactoring manually
3. Ensure tests still pass
4. Decide if the refactoring is worth it

### 6. **Writing Documentation**

**Prompt:**
```text
Write a docstring for this function that explains its purpose,
parameters, return value, and example usage.

[Your function]
```

**Why:** Documentation is tedious but important. AI can draft it.

**What to do:**
1. Review the draft
2. Ensure it's accurate
3. Edit for clarity
4. Add any missing details

---

## When NOT to Use Copilot (Don't Use)

### ❌ 1. **For Initial Learning**
```text
❌ DON'T: "Generate a Pygame player class"
✅ DO: Understand the concept first, then ask Copilot to explain your implementation
```

### ❌ 2. **To Skip Testing**
```text
❌ DON'T: "Write code that makes this test pass"
✅ DO: Understand the test, code it yourself, ask Copilot only for help with syntax
```

### ❌ 3. **Without Verification**
```text
❌ DON'T: Copy-paste generated code into your project without testing
✅ DO: Run tests before accepting any suggestion
```

### ❌ 4. **For Entire Features**
```text
❌ DON'T: "Implement the entire collision system"
✅ DO: "Explain how to check if two rectangles overlap"
```

### ❌ 5. **To Avoid Edge Cases**
```text
❌ DON'T: Generate code and assume it handles all cases
✅ DO: Write tests for edge cases first, then implement
```

### ❌ 6. **As a Substitute for Code Review**
```text
❌ DON'T: Only ask Copilot to review your work
✅ DO: Review your own code first, then ask Copilot for a second opinion
```

---

## The Recommended Workflow

### Step 1: EXPLAIN (Understanding)
```text
Prompt: "Explain what a collision detection system needs to do."

Copilot provides context and concepts.
You learn the fundamentals.
```

### Step 2: PLAN (Architecture)
```text
Prompt: "Propose a minimal implementation for detecting collision 
between a rectangle and a circle. What functions should I write?"

Copilot suggests structure.
You review the plan.
You agree or revise.
```

### Step 3: TEST (Specification)
```text
You write tests based on the plan:

def test_rectangle_circle_collision():
    rect = Rectangle(x=0, y=0, width=100, height=100)
    circle = Circle(x=150, y=50, radius=30)
    assert rect.collides_with(circle) == True
```

### Step 4: IMPLEMENT (Coding)
```text
Prompt: "Implement the collision detection function to pass these tests:
[Your tests]

Do not change the function signature or return type."

Copilot generates implementation.
You review it.
```

### Step 5: VERIFY (Testing)
```text
pytest tests/test_collision.py

If tests pass → code is accepted
If tests fail → debug, ask Copilot for help, fix
```

### Step 6: REVIEW (Quality)
```text
Prompt: "Review this implementation for edge cases, efficiency, 
and clarity. Do not modify it."

Copilot provides feedback.
You consider the feedback.
You make improvements if needed.
```

### Step 7: REFACTOR (Polish)
```text
Once tests pass and code is reviewed:

Prompt: "Suggest ways to simplify or improve this function."

You refactor manually.
Tests confirm improvements didn't break anything.
```

---

## Example: The Complete Workflow

### Scenario: Implement Player Movement

#### 1. EXPLAIN
```text
You: "Explain how player movement works in a 2D game."

Copilot: "In a 2D game, movement updates the player's x and y coordinates.
Typically:
- Each frame, check for input (keyboard)
- Update position based on input and speed
- Constrain position to screen bounds
- Render the player at the new position"

You: ✓ Now you understand the concept
```

#### 2. PLAN
```text
You: "Propose functions for a player movement system.
What should each do? What tests should exist?
Do not write code."

Copilot: "
1. move_player(x, y, direction, speed) → returns new (x, y)
   Test: def test_move_right()
2. is_out_of_bounds(x, y, width, height) → returns bool
   Test: def test_boundary_check()
3. clamp_position(x, y, width, height) → returns clamped (x, y)
   Test: def test_position_clamped()"

You: ✓ Plan looks good, proceed
```

#### 3. TEST
```python
# tests/test_player.py
def test_move_right():
    x, y = move_player(100, 100, "RIGHT", speed=5)
    assert x == 105
    assert y == 100

def test_move_left():
    x, y = move_player(100, 100, "LEFT", speed=5)
    assert x == 95
    assert y == 100

def test_boundary_left():
    is_out = is_out_of_bounds(-5, 100, width=800, height=600)
    assert is_out == True

def test_clamp_position():
    x, y = clamp_position(-10, 100, width=800, height=600)
    assert x == 0
    assert y == 100

# Run: pytest
# Result: 4 failed (RED)
```

#### 4. IMPLEMENT
```text
You: "Implement these functions to pass the tests:
[Show the tests]

Use only built-in Python. Do not modify the test signatures."

Copilot generates:

def move_player(x, y, direction, speed):
    if direction == "RIGHT":
        x += speed
    elif direction == "LEFT":
        x -= speed
    return x, y

def is_out_of_bounds(x, y, width, height):
    return x < 0 or x > width or y < 0 or y > height

def clamp_position(x, y, width, height):
    x = max(0, min(x, width))
    y = max(0, min(y, height))
    return x, y

You: ✓ Code looks reasonable, let's test
```

#### 5. VERIFY
```bash
$ pytest tests/test_player.py
4 passed
```

#### 6. REVIEW
```text
You: "Review this code for edge cases or improvements.
[Show the code]
Do not modify it."

Copilot: "The move_player function doesn't constrain the position.
Should it? Also, consider UP and DOWN directions.
The is_out_of_bounds check assumes boundaries at 0 and width/height.
Is that what you intend?"

You: ✓ Good catches. Those are design decisions you make.
```

#### 7. REFACTOR
```python
# Updated based on review:
def move_player(x, y, direction, speed):
    if direction == "RIGHT":
        x += speed
    elif direction == "LEFT":
        x -= speed
    elif direction == "UP":
        y -= speed
    elif direction == "DOWN":
        y += speed
    return x, y

# Re-run tests to confirm
```

---

## Documenting AI Usage

Maintain `docs/ai-log.md` to record meaningful AI interactions:

```markdown
## Week 2: Collision Detection

### Prompt
Explain why my collision test is failing.
Do not modify the code.

### Copilot Response
The collision detection is checking player.rect.colliderect(),
but rect hasn't been updated to the new position yet.
You're comparing old collision data.

### Decision
Accepted the explanation.
Decided to refactor to update rect after position changes.

### Verification
pytest tests/test_collision.py
3 passed

### Learning
Reminder: Update all related state when changing a property.
Not just the coordinates, but also derived objects like rects.
```

---

## Red Flags: When AI is Leading You Astray

🚩 **Copilot says:** "Just use this library, it handles everything"  
→ You should ask: "What does this library do? Can I understand it without it?"

🚩 **Copilot says:** "This code is fine" (But tests fail)  
→ You should: Trust the tests over Copilot. Something is wrong.

🚩 **Copilot generated:** 500 lines of complex code  
→ You should: Break it down or ask for simpler approach.

🚩 **Copilot says:** "This handles all edge cases" (But it doesn't)  
→ You should: Write tests for those edge cases.

🚩 **You don't understand:** The generated code  
→ You should: Ask Copilot to explain it, or rewrite it yourself.

---

## Best Practices

### ✅ DO

- ✅ Ask Copilot to **explain** before implementing
- ✅ Write **tests first**, then ask for implementation help
- ✅ **Review** all suggestions before accepting
- ✅ **Verify** with tests before considering code correct
- ✅ **Document** meaningful AI interactions
- ✅ Ask Copilot for **debugging help**, not debugging solutions
- ✅ Use AI for **code review** as a second opinion
- ✅ Ask for **multiple options** before choosing

### ❌ DON'T

- ❌ Copy-paste code without testing
- ❌ Use AI to **skip learning** core concepts
- ❌ Accept generated code **without reviewing**
- ❌ Ignore **test failures** in favor of "AI said it's fine"
- ❌ Ask AI to **solve your problem** instead of helping you solve it
- ❌ Use generative AI as a **substitute for thinking**
- ❌ Accept **hallucinated facts** or library documentation
- ❌ Treat AI-generated code as **automatically correct**

---

## Learning Outcomes from This Approach

By the end of the course, you will:

✅ Understand when AI assistance is valuable  
✅ Know how to interact with AI effectively  
✅ Recognize and correct AI mistakes  
✅ Use testing to verify AI-generated code  
✅ Maintain developer agency and understanding  
✅ Document your AI-assisted development process  
✅ Write code that **you** own and understand  

---

## Summary

**AI is a tool for enhancing your development process, not a replacement for it.**

The right relationship with AI:

```text
YOUR THINKING
    ↓
AI ASSISTANCE
    ↓
YOUR VERIFICATION
    ↓
TESTED CODE
```

Not:

```text
AI DOES IT
    ↓
YOU ACCEPT IT
    ↓
HOPE IT WORKS
```

**Use Copilot to enhance your problem-solving. Stay in control of your code.**
