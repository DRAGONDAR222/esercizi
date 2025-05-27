from typing import Self, Any
from datetime import *

class TimeRange(tuple):	
	_start: datetime|None # [0..1]
	_end: datetime|None # [0..1]
	# subject to constraint: _start <= _end

	def __new__(cls, start:datetime|str|None, end:datetime|str|None)->Self:	
		# We accept _start == None or _end == None (unbounded time periods)

		values = [ datetime.fromisoformat(x) if isinstance(x, str) else x for x in [start, end] ]
		if values[0] and values[1] and values[0] > values[1]:
			raise ValueError(f"Invalid TimeRange(from={start}, to={end}): 'from' must be <= 'to'")
		return tuple.__new__(cls, values)

	def start(self)->datetime|None:
		return self[0]
	def end(self)->datetime|None:
		return self[1]

	def duration(self)->timedelta|None:
		try:
			return self.end() - self.start()
		except:
			return timedelta.max # we should return timedelta(+infty), but timedelta has no standard representation of +infty

	def is_disjoint(self, other:Self)->bool:

		# case #1:
		# self :        X---------------
		# other: ---X           

		# case #2:
		# self : ---------------X
		# other:                   X----

		# case #3:
		# self :        X-------X
		# other: ---X      or      X----

		if self.start(): #1, #3
			if other.end() and other.end() < self.start():
				return True #1
			
		if self.end(): #2, #3
			if other.start() and other.start() > self.end():
				return True #3

		return False

	def intersects(self, other:Self)->bool:
		return not self.is_disjoint(other)

	def shift(self, delta:timedelta)->Self:
		if not delta:
			return self
		else:
			return TimeRange(
				None if not self.start() else self.start() + delta, 
				None if not self.end() else self.end() + delta)

	def __str__(self)->str:
		return f"{ f'[{self[0]}' if self[0] else '(-infinity'}, { f'{self[1]}]' if self[1] else '+infinity)'}"
	
if __name__ == '__main__':
	tr1:TimeRange = TimeRange(datetime(2025, 5, 1, 10, 0, 0), "2025-05-27T11:00:00")
	tr2:TimeRange = TimeRange("2025-05-01T10:00:00", "2025-05-27T11:00:00")
	print(tr1)
	print(tr2)
	

