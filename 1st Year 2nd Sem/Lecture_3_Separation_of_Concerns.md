# CS 12 Lectures 1-2

## [[ LECTURE 2 : SEPARATION OF CONCERNS ]]
: Separating concerns separates our probs into smth smaller and easier to solve

### [ ■ [1] [Classes Recall] ■ ]
: classes has an __init__ function, defining the attributes of its objects
: add self as a parameter for every defined method
: add self. before every local attribute or methods

```python
class ObjectName:
    attribute1 : int
    attribute2 : bool

    # this func must always be defined before any other methods
    def __init__(self, attribute1: int, attribute2: int):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

A = ObjectName(67, True) # self parameter is invisible
```

### [ ■ [2] [Modularization Using Classes] ■ ]
: splitting code into smaller, reisable components (modules) using classes
: makes it easier to modify

### [ ■ [3] [Steps to separate concerns] ■ ]

#### === 1. Identify the necessary parts that can be separated independently ===
: (e.g. In a game, UI, game logic, and output modules can be separated)

### [ ■ [4] [Coupling and Dependencies] ■ ]
1. Dependency (Existential)
: A will not exist without B and C (hence, A is dependent on B and C)

2. Coupling
: A will be changed if B or C is changed (hence, A is coupled with B and C)

### [ ■ [5] [Model-View-Controller (MVC)] ■ ]
: a template that can be used for modularizatioj
1. Model Class : Logic
2. View Class : UI, I/O
3. Controller : Connects View to Model

: in guessing game
Model 

```python
class Model:
    def __init__(self, answer, attempts):
        self.answer = answer
        self.attempts = attempts
    def if_guess_in_bounds(self, guess):
        return 1 <= self.guess <= 100
    def check_guess(self, guess):
        # if conditionals then return a representative values for (too high, too low, correct ans)
    def is_game_done(self):
        return True if attempts == 0 else False 
    def use_attempt(self):
        self.attempts -= 1
        
        
```

    : State/Attribute needed for the game:
    - correct answer
    - num of attempts
    : Cases:
    - Start game
    - make guess
    - check whether the guess if correct
    - check whether the gues is wrong
    
Controller
    - game loop
    - connects to model and view
```python
class Controller:
    def __init__(self, model, view):
        self.model == model
        self.view == view
    def run(self):
        while self.model.is_game_done == False:
            ...
```
    
View
    - terminal I/O management
```python
class View:
    def __init__(self, attempts, answer):
        self.attempts = attempts
        self.answer = answer
    
    def show_final_msg(...):
        ... #print(blabla)
        
    def show_verdict(...):
        ... #print(Too High or Too Low)
        
    def get_guess(...):
        ... # guess = input(blabla)
```

    
```python

```