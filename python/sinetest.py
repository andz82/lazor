#!/usr/bin/env python

import math
import dac

class SineTest(object):
  def produce(self):
    pmax = 32000
    pstep = 400
    cmax = 65535
    amplitude = 5000
    step = 500
    direction = 0
    while True:
      if(amplitude < -15000):
        direction = 1
      if(amplitude > 15000):
        direction = 0
      if direction == 0:
        amplitude = amplitude - step
      if direction == 1:
        amplitude = amplitude + step
      for x in xrange(-pmax, -pmax+(1*pmax/4), pstep):
        yield (x, amplitude*math.sin(math.pi*x/pmax), cmax, 0,0)
      for x in xrange(-pmax+(1*pmax/4)-1, -pmax+(2*pmax/4), pstep):
        yield (x, amplitude*math.sin(math.pi*x/pmax), 0, cmax,0)
      for x in xrange(-pmax+(2*pmax/4)-1, -pmax+(3*pmax/4), pstep):
        yield (x, amplitude*math.sin(math.pi*x/pmax), 0, 0,cmax)
      for x in xrange(-pmax+(3*pmax/4)-1, -pmax+(4*pmax/4), pstep):
        yield (x, amplitude*math.sin(math.pi*x/pmax), 0, cmax,cmax)
      for x in xrange(-pmax+(4*pmax/4)-1, -pmax+(5*pmax/4), pstep):
        yield (x, amplitude*math.sin(math.pi*x/pmax), cmax, 0,cmax)
      for x in xrange(-pmax+(5*pmax/4)-1, -pmax+(6*pmax/4), pstep):
        yield (x, amplitude*math.sin(math.pi*x/pmax), cmax, cmax,0)
      for x in xrange(-pmax+(6*pmax/4)-1, -pmax+(7*pmax/4), pstep):
        yield (x, amplitude*math.sin(math.pi*x/pmax), 0, 0,0)
      for x in xrange(-pmax+(7*pmax/4)-1, -pmax+(8*pmax/4), pstep):
        yield (x, amplitude*math.sin(math.pi*x/pmax), cmax, cmax,cmax)
      for x in xrange(pmax, -pmax, -4000):
        yield (x, 0, 0, 0, 0)

  def __init__(self):
    self.stream = self.produce()

  def read(self, n):
    return [self.stream.next() for i in xrange(n)]

class NullPointStream(object):
  def read(self, n):
    return [(0, 0, 0, 0, 0)] * n

d = dac.DAC(dac.find_first_dac())
d.play_stream(SineTest())
