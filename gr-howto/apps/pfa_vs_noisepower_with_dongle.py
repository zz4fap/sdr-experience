#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Pfa vs. Noise power with USB Dongle as Source.
# Generated: Sun Jan 20 10:20:29 2013
##################################################

import math
import numpy
import pylab
import random
from time import sleep
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import baz
import howto
import wx

class PfaVsNoisePowerSimu(gr.top_block):
   " This contains the simulation flow graph "
   def __init__(self, pfa, pfd, freq):
      gr.top_block.__init__(self)

      # Constants
      samp_rate = 2.4e6
      fft_size = 4096
      samples_per_band = 16
      tcme = 1.9528
      output_pfa = True
      debug_stats = False
      primary_user_location = 0
      useless_bw = 200000.0

		# Blocks
      rtl2832_source = baz.rtl_source_c(defer_creation=True, output_size=gr.sizeof_gr_complex)
      rtl2832_source.set_verbose(True)
      rtl2832_source.set_vid(0x0)
      rtl2832_source.set_pid(0x0)
      rtl2832_source.set_tuner_name("")
      rtl2832_source.set_default_timeout(0)
      rtl2832_source.set_use_buffer(True)
      rtl2832_source.set_fir_coefficients(([]))
      rtl2832_source.set_read_length(0)
      if rtl2832_source.create() == False: raise Exception("Failed to create RTL2832 Source: rtl2832_source_0")
      rtl2832_source.set_sample_rate(samp_rate)
      rtl2832_source.set_frequency(freq)
      rtl2832_source.set_auto_gain_mode(True)
      rtl2832_source.set_relative_gain(True)
      rtl2832_source.set_gain(1)

      s2v = gr.stream_to_vector(gr.sizeof_gr_complex, fft_size)
      fftb = fft.fft_vcc(fft_size, True, (window.blackmanharris(1024)), False, 1)
      ss = howto.spectrum_sensing_cf(samp_rate,fft_size,samples_per_band,pfd,pfa,tcme,output_pfa,debug_stats,primary_user_location,useless_bw)
      self.sink = gr.vector_sink_f()

		# Connections
      self.connect(rtl2832_source, s2v, fftb, ss, self.sink)

def simulate_pfa(pfa, pfd, freq, simu_time):
   """ All the work's done here: create flow graph, run and read out Pfa """
   fg = PfaVsNoisePowerSimu(pfa, pfd, freq)
   fg.start()
   sleep(simu_time)
   fg.stop()
   fg.wait()
   size = len(fg.sink.data())
   soma = numpy.sum(fg.sink.data())
   return soma/size

if __name__ == "__main__":
   pfa = 0.0001
   pfd = 0.001
   freq = 80.0e6
   nTrials = 10
   simu_time = nTrials*1.74 # approximately nTrials*1000 samples
   fa_rate = simulate_pfa(pfa, pfd, freq, simu_time)
   print fa_rate

