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
import osmosdr
import howto
import wx
import matplotlib.pyplot as plt

class PfaVsNoisePowerSimu(gr.top_block):
   " This contains the simulation flow graph "
   def __init__(self, pfa, pfd, freq, useless_bw, nframes_to_check, nframes_to_average):
      gr.top_block.__init__(self)

      # Constants
      samp_rate = 2.4e6
      fft_size = 4096
      samples_per_band = 16
      tcme = 1.9528
      output_pfa = False
      debug_stats = False
      histogram = False
      primary_user_location = 42
      nsegs_to_check = 6
      downconverter = 1

		# Blocks
      rtlsdr_source = osmosdr.source_c( args="nchan=" + str(1) + " " + "" )
      rtlsdr_source.set_sample_rate(samp_rate)
      rtlsdr_source.set_center_freq(freq, 0)
      rtlsdr_source.set_freq_corr(0, 0)
      rtlsdr_source.set_gain_mode(0, 0)
      rtlsdr_source.set_gain(10, 0)
      rtlsdr_source.set_if_gain(24, 0)

      s2v = gr.stream_to_vector(gr.sizeof_gr_complex, fft_size)
      fftb = fft.fft_vcc(fft_size, True, (window.blackmanharris(1024)), False, 1)
      self.ss = howto.spectrum_sensing_cf(samp_rate,fft_size,samples_per_band,pfd,pfa,tcme,output_pfa,debug_stats,primary_user_location,useless_bw,histogram,nframes_to_check,nframes_to_average,downconverter,nsegs_to_check)
      self.sink = gr.vector_sink_f()

		# Connections
      self.connect(rtlsdr_source, s2v, fftb, self.ss, self.sink)

   def getHistogram(self,pos):
      return self.ss.get_histogram(pos)

   def getNumberOfSubBands(self):
      return self.ss.getNumberOfSubBands()

   def get_debug_histogram(self):
      return self.ss.debug_histogram()

def simulate_pfa(pfa, pfd, freq, useless_bw, simu_time, nframes_to_check, nframes_to_average ):
   """ All the work's done here: create flow graph, run and read out Pfa """
   fg = PfaVsNoisePowerSimu(pfa, pfd, freq, useless_bw, nframes_to_check, nframes_to_average )
   fg.start()
   sleep(simu_time)
   fg.stop()
   fg.wait()
   size = len(fg.sink.data())
   soma = numpy.sum(fg.sink.data())
   print size
   if fg.get_debug_histogram() == True: plotHistogram(fg)
   return soma/size

def plotHistogram(fg):
   nSubBands = fg.getNumberOfSubBands()
   print nSubBands
   histogram = []
   for i in range(0,nSubBands):
      histogram.append(fg.getHistogram(i))
   plt.stem(range(0,nSubBands), histogram)
   plt.ylabel('Number of FA in a given sub-band')
   plt.xlabel('sub-band')
   plt.draw()

if __name__ == "__main__":
   pfa = 0.0001
   pfd = 0.001
   #freq = 31e6
   freq = 94.9e6
   #useless_bw = 350000.0
   useless_bw = 400000.0
   nframes_to_check = 2
   nframes_to_average = 6
   nTrials = 6
   simu_time = nTrials*1.74 # approximately nTrials*1000 samples
   fa_rate = simulate_pfa(pfa, pfd, freq, useless_bw, simu_time, nframes_to_check, nframes_to_average)
   print fa_rate
   plt.show()

