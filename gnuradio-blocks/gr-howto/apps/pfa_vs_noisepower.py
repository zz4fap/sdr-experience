#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Pfa vs. Noise power
# Generated: Wed Jan  9 19:24:29 2013
##################################################

import math
import numpy
import pylab
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import howto
import wx

def powerToAmplitude(dbm)
   """ Transform from dBm to amplitude in Volts """
   return 10**((dbm - 30)/20)

def simulate_pfa(dBm):
   """ All the work's done here: create flow graph, run, read out Pfa """
   print "Noise Power = %d dBm" % dBm
   fg = PfaVsNoisePowerSimu(dBm)
   fg.run()
   return fg.sink.data()

if __name__ == "__main__":
   pfa = 0.0001
   pfd = 0.001
   dBm_min = -10
   dBm_max = 30
   dBm_range = numpy.arange(dBm_min, dBm_max, 0.5)
   pfa_theory = [pfa] * len(dBm_range)
   print "Simulating..."
   pfa_simu = [simulate_pfa(x) for x in dBm_range]

   f = pylab.figure()
   s = f.add_subplot(1,1,1)
   s.semilogy(dBm_range, pfa_theory, 'g-.', label="Theoretical")
   s.semilogy(dBm_range, pfa_simu, 'b-o', label="Simulated")
   s.set_title('Pfa Simulation')
   s.set_xlabel('Noise Power (dBm)')
   s.set_ylabel('achieved Pfa')
   s.legend()
   s.grid()
   pylab.show()
