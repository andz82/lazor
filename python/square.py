#!/usr/bin/env python
import dac

class SquarePointStream(object):
	def produce(self):
		pmax = 15000
		pstep = 750
		cmax = 65535
		while True:
			for x in xrange(-pmax, pmax, pstep):
				yield (x, pmax, cmax, 0, 0)
			for y in xrange(pmax, -pmax, -pstep):
				yield (pmax, y, 0, cmax, 0)
			for x in xrange(pmax, -pmax, -pstep):
				yield (x, -pmax, 0, 0, cmax)
			for y in xrange(-pmax, pmax, pstep):
				yield (-pmax, y, cmax, cmax, cmax)

	def __init__(self):
		self.stream = self.produce()

	def read(self, n):
		return [self.stream.next() for i in xrange(n)]

class NullPointStream(object):
	def read(self, n):
		return [(0, 0, 0, 0, 0)] * n

d = dac.DAC(dac.find_first_dac())

d.play_stream(SquarePointStream())
