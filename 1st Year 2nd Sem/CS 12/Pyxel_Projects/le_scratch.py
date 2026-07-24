'''def find_first_above(lst: list[int], t: int) -> int:
	lo, hi = 0, len(lst) - 1
	result = -1
	while lo < hi: # BUG is somewhere in here
		mid = (lo + hi) // 2
		if lst[mid] > t:
			result = mid
			hi = mid
		else:
			lo = mid + 1
	return result'''

'''def find_first_above(lst: list[int], t: int) -> int:
	lo, hi = 0, len(lst) - 1
	result = -1
	while lo < hi: # BUG is somewhere in here
		#print('looped')
		mid = (lo + hi) // 2
		if lst[mid] < t:
			lo = mid
		elif lst[mid] > t:
			hi = mid
		else:
			return mid
	return None'''

print(find_first_above([1, 3, 5, 7, 9], 4))
#print(find_first_above([1, 3, 5, 7, 9], 1))

'''0, 1, 2, 3, 4 ###

1, 3, 5, 7, 9

1, 3, 5

5'''
apply_twice(animals,) -> return of callable

for a in animals
	sub_param = f(a)
	sub_return = f(sub_param)
	append lang yung sub_return

return <: precon(aka animals)
poodle <: dog < animal

A. animal as list[Animal]
1. no 
2. no 
3. no 
4. no
5.no
6.no
7.no
8.no
9.no

B. animal as list[Dog]
1. no 
2. yes
3. yes
4. no
5. yes
6. yes
7. no
8. no
9. no

C. animal as list[Poodle]
1. no
2. yes
3. yes
4. no
5. yes
6. yes
7. no
8. no 
9. no


'''
$$$

Extra Subtypes
1. Collection immediate subtype of Iterable, 
    parent of followng subtypes EXCEPT Iterator -> Generator

Validating candidate types to expected types
1. Expected Class : valid are same class/subclass
2. Callable([X], Y) : valid are param_type contra X, return_type covar Y
3. f(f(x)) : return_type <: param_type
4. Var to Func : Check if var_type <: func_param_type

binary search edge cases:
1. make sure that every iteration decreases or increases sample space wrt floor div

'''

SOLID Principle Violations

5. 
- Shape class used super() without having a parent class
- 3 value inside super() in Triangle
- Triangle class must set super().(color, sides), then self.sides = 3
- ColoredTriangle didnt inherit color and sides to respective parents properly





from enum import Enum, auto

class Feedback(Enum):
	Wrong = auto()
	Correct = auto()
	NotValid = auto()
	Empty = auto()

class Model:
	def __init__(self, valid_words:Iterable[str]):
		self.valid_words: list[str] = list(valid_words)
		self.previous_word: str | None = None
		self.word_count: int = 0
		self.is_done = False
		super().__init__()
	
	def play_word(self, word:str) -> bool:
		if self.previous_word is None or self.previous_word[-1] == word[0]:
			self.previous_word = word
			self.word_count += 1
			return Feedback.Correct
		else:
			self.is_done = True
			return Feedback.Wrong
	

	def check_prompt(self, word:str):
		if not word:
			return Feedback.Empty
		elif word not in self.valid_words:
			return Feedback.NotValid
		else:
			return None


	
class View:
	def print_feedback(self, feedback: Feedback, word:str, word_count:int):
		dic = {Feedback.Empty:'Enter a word with at least one letter', Feedback.NotValid : f'The word "{word}" is not in the list of valid words.', Feedback.Correct : f'Yatta! You entered "{word}".', Feedback.Wrong : f'You gave {word_count} words!'}
		print(dic[feedback])
			

	def prompt_word(self):
		word = input('Please enter a word: ').rstrip().lower()
		return word


class Controller:
	def __init__(self, model:Model, view:View):
		self.model = model
		self.view = view

	def play_shiritori(self):
		model = self.model
		view = self.view

		while True:
			print("$ loop")
			prompt = view.prompt_word()
			feedback = model.check_prompt(prompt)
			print(f"$ {prompt} : {feedback}")
			if feedback == None:
				verdict = model.play_word(prompt)
				view.print_feedback(verdict, prompt, model.word_count)
				if model.is_done:
					break
			else:
				view.print_feedback(feedback, prompt, model.word_count)

sh = ('apple', 'eggplant', 'tomato', 'okra', 'sitaw', 'bataw', 'patani')

model = Model(sh)
view = View()
controller = Controller(model, view)

controller.play_shiritori()


class Student:
def __init__(self, name: str):
self.name = name
super().__init__()
def label(self) -> str:
return 'Student'
def identifier(self) -> str:
return f"{self.label()}: {self.name}"
class UPStudent(Student):
def __init__(self, name: str, student_no: str):
self.student_no = student_no
super().__init__(name)
def identifier(self) -> str:
identifier = super().identifier()
return f"[{self.student_no}] {identifier}"


class DLSUStudent(Student):
	def __init__(self, name: str, student_no: str):
		self.student_no = student_no
		super().__init__(name)
	def identifier(self) -> str:
		identifier = super().identifier()
		return f"[{self.student_no}] {identifier}"

class WorkingDLSUStudent(DLSUStudent):
	def __init__(self, name: str, student_no: str, salary: int):
		self.salary = salary
		super().__init__(name)
	def identifier(self) -> str:
		identifier = super().identifier()
		return f"{identifier} (salary {self.salary})"
class DCSStudent(UPStudent):
def __init__(self, name: str, student_no: str):
super().__init__(name, student_no)
def label(self) -> str:
return 'DCS Student'
def identifier(self) -> str:
identifier = super().identifier()
return f"[DCS] {identifier}"
def some_students() -> list[Student]:
return [
Student('Piattos'),
DLSUStudent('Nova', 125),
UPStudent('Oishi', '1969-00012'),
DCSStudent('Chippy', '1094-00012'),
]
for student in some_students():
print(student.identifier())