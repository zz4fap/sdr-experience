#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Pfa vs. Noise power
# Generated: Wed Jan  9 19:24:29 2013
##################################################

import math
import numpy
import pylab
import random
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

class PfaVsNoisePowerSimu(gr.top_block):
   " This contains the simulation flow graph "
   def __init__(self, dBm, pfa, pfd):
      gr.top_block.__init__(self)

      # Constants
      mu = 0
      samp_rate = 2.4e6
      fft_size = 4096
      samples_per_band = 16
      tcme = 1.9528
      output_pfa = True
      debug_stats = False
      histogram = False
      primary_user_location = 0
      useless_bw = 200000.0

      std_dev = self.convertFromPowerToStdDev(dBm)

      src_data = []
      for j in range(1,fft_size+1):
         src_data = src_data + [random.gauss(mu, std_dev) + random.gauss(mu, std_dev)*1j]

		# Blocks
      src = gr.vector_source_c(src_data)
      s2v = gr.stream_to_vector(gr.sizeof_gr_complex, fft_size)
      fftb = fft.fft_vcc(fft_size, True, (window.blackmanharris(1024)), False, 1)
      ss = howto.spectrum_sensing_cf(samp_rate,fft_size,samples_per_band,pfd,pfa,tcme,output_pfa,debug_stats,primary_user_location,useless_bw)
      self.sink = gr.vector_sink_f()

		# Connections
      self.connect(src, s2v, fftb, ss, self.sink)

   def convertFromPowerToStdDev(self, dBm):
      """ Convert noise power from dBm to standard deviation in voltage """ 
      variance = 10**((dBm - 30)/10)
      return math.sqrt(variance/2)

def simulate_pfa(dBm, pfa, pfd, nTrials):
   """ All the work's done here: create flow graph, run and read out Pfa """
   false_alarm_rate = 0.0
   print "Noise Power = %f dBm" % dBm
   for j in range(1,nTrials+1):
      fg = PfaVsNoisePowerSimu(dBm, pfa, pfd)
      fg.run()
      false_alarm_rate = false_alarm_rate + fg.sink.data()[0]
   return false_alarm_rate/nTrials

if __name__ == "__main__":
   pfa = 0.0001
   pfd = 0.001
   dBm_min = -10
   dBm_max = 30
   dBm_step = 1;
   nTrials = 100000
   dBm_range = numpy.arange(dBm_min, dBm_max, dBm_step)
   pfa_theory = [pfa] * len(dBm_range)
   print "Simulating..."
   pfa_simu = [simulate_pfa(x, pfa, pfd, nTrials) for x in dBm_range]

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
