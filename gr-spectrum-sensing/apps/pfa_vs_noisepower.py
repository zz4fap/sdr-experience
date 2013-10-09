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

class PfaVsNoisePowerSimu(gr.top_block):
   " This contains the simulation flow graph "
   def __init__(self, dBm, pfa, pfd, nTrials):
      gr.top_block.__init__(self)

      # Constants
      samp_rate = 2.4e6
      fft_size = 4096
      samples_per_band = 16
      tcme = 1.9528
      output_pfa = True
      debug_stats = False
      histogram = False
      primary_user_location = 0
      useless_bw = 200000.0
      src_data = [0+0j]*fft_size*nTrials
      voltage = self.powerToAmplitude(dBm);

		# Blocks
      src = gr.vector_source_c(src_data)
      noise = gr.noise_source_c(gr.GR_GAUSSIAN, voltage, 42)
      add = gr.add_vcc()
      s2v = gr.stream_to_vector(gr.sizeof_gr_complex, fft_size)
      fftb = fft.fft_vcc(fft_size, True, (window.blackmanharris(1024)), False, 1)
      ss = howto.spectrum_sensing_cf(samp_rate,fft_size,samples_per_band,pfd,pfa,tcme,output_pfa,debug_stats,primary_user_location,useless_bw,histogram)
      self.sink = gr.vector_sink_f()

		# Connections
      self.connect(src, add, s2v, fftb, ss, self.sink)
      self.connect(noise, (add, 1))

   def powerToAmplitude(self, dBm):
      """ Convert noise power from dBm to amplitude in voltage """
      return 10**((dBm - 30)/20)

def simulate_pfa(dBm, pfa, pfd, nTrials):
   """ All the work's done here: create flow graph, run and read out Pfa """
   print "Noise Power = %f dBm" % dBm
   fg = PfaVsNoisePowerSimu(dBm, pfa, pfd, nTrials)
   fg.run()
   print fg.sink.data()[nTrials-1]
   return fg.sink.data()[nTrials-1]

if __name__ == "__main__":
   pfa = 0.0001
   pfd = 0.001
   dBm_min = -10
   dBm_max = 30
   nTrials = 100
   dBm_range = numpy.arange(dBm_min, dBm_max, 0.5)
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
