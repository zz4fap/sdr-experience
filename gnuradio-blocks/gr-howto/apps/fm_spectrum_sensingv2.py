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

class SpectrumSensingBlockParameters():

   def __init__(self):
      self.pfa = 0.0001
      self.pfd = 0.001
      self.useless_bw = 400000.0
      self.nframes_to_check = 2
      self.nframes_to_average = 6 
      self.samp_rate = 2.4e6
      self.fft_size = 4096
      self.samples_per_band = 16
      self.tcme = 1.9528
      self.output_pfa = False
      self.debug_stats = False
      self.histogram = False
      self.primary_user_location = 20
      self.nsegs_to_check = 6
      self.downconverter = 1

class PfaVsNoisePowerSimu(gr.top_block):
   " This contains the simulation flow graph "
   def __init__(self, ssblock, freq):
      gr.top_block.__init__(self)

      # Constants
      pfa = ssblock.pfa
      pfd = ssblock.pfd
      tcme = ssblock.tcme
      samp_rate = ssblock.samp_rate
      fft_size = ssblock.fft_size
      samples_per_band = ssblock.samples_per_band
      tcme = ssblock.tcme
      output_pfa = ssblock.output_pfa
      debug_stats = ssblock.debug_stats
      histogram = ssblock.histogram
      primary_user_location = ssblock.primary_user_location
      nsegs_to_check = ssblock.nsegs_to_check
      downconverter = ssblock.downconverter
      useless_bw = ssblock.useless_bw
      nframes_to_check = ssblock.nframes_to_check
      nframes_to_average = ssblock.nframes_to_average

		# Blocks
      self.rtlsdr_source = osmosdr.source_c( args="nchan=" + str(1) + " " + "" )
      self.rtlsdr_source.set_sample_rate(samp_rate)
      self.rtlsdr_source.set_center_freq(freq, 0)
      self.rtlsdr_source.set_freq_corr(0, 0)
      self.rtlsdr_source.set_gain_mode(0, 0)
      self.rtlsdr_source.set_gain(10, 0)
      self.rtlsdr_source.set_if_gain(24, 0)

      s2v = gr.stream_to_vector(gr.sizeof_gr_complex, fft_size)
      fftb = fft.fft_vcc(fft_size, True, (window.blackmanharris(1024)), False, 1)
      self.ss = howto.spectrum_sensing_cf(samp_rate,fft_size,samples_per_band,pfd,pfa,tcme,output_pfa,debug_stats,primary_user_location,useless_bw,histogram,nframes_to_check,nframes_to_average,downconverter,nsegs_to_check)
      self.sink = gr.vector_sink_f()

		# Connections
      self.connect(self.rtlsdr_source, s2v, fftb, self.ss, self.sink)

   def setFrequency(self, frequency):
      self.rtlsdr_source.set_center_freq(frequency, 0)

   def getHistogram(self,pos):
      return self.ss.get_histogram(pos)

   def getNumberOfSubBands(self):
      return self.ss.getNumberOfSubBands()

   def get_debug_histogram(self):
      return self.ss.debug_histogram()

def simulate_pfa(simu_time):
   ssblock = SpectrumSensingBlockParameters()
   for i in range(87, 108):
      for j in range(0,5):
         step = float((2*j+1)*0.1) - 0.2
         freq = float(i + step)*1e6
         print freq
         fg = PfaVsNoisePowerSimu(ssblock, freq)
         fg.start()
         sleep(simu_time)
         fg.stop()
         fg.wait()
         size = len(fg.sink.data())
         soma = numpy.sum(fg.sink.data())
         if fg.get_debug_histogram() == True: plotHistogram(fg)
         print soma/size

def plotHistogram(fg):
   nSubBands = fg.getNumberOfSubBands()
   histogram = []
   for i in range(0,nSubBands):
      histogram.append(fg.getHistogram(i))
   plt.stem(range(0,nSubBands), histogram)
   plt.ylabel('Number of FA in a given sub-band')
   plt.xlabel('sub-band')
   plt.draw()

if __name__ == "__main__":
   nTrials = 1
   #simu_time = nTrials*1.74 # approximately nTrials*1000 samples
   simu_time = 1.74
   simulate_pfa(simu_time)

