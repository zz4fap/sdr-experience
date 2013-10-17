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
   def __init__(self, dbW, pfa, pfd, fft_size):
      gr.top_block.__init__(self)

      # Parameters
      samp_rate               = 2e6
      samples_per_band        = 16
      tcme                    = 1.9528
      output_pfa              = True
      debug_stats             = False
      primary_user_location   = 0
      useless_bw              = 0.0    # As we are not using any of the dongles it can be set as zero, i.e., all the band can be used.
      histogram               = False
      nframes_to_check        = 1
      nframes_to_average      = 1
      downconverter           = 1
      nsegs_to_check          = 6

      # Create AWGN noise
      noise = awgn(fft_size, dbW)

		# Blocks
      src = gr.vector_source_c(noise)
      s2v = gr.stream_to_vector(gr.sizeof_gr_complex, fft_size)
      fftb = fft.fft_vcc(fft_size, True, (window.blackmanharris(1024)), False, 1)
      self.ss = howto.spectrum_sensing_cf(samp_rate,fft_size,samples_per_band,pfd,pfa,tcme,output_pfa,debug_stats,primary_user_location,useless_bw,histogram,nframes_to_check,nframes_to_average,downconverter,nsegs_to_check)
      self.sink = gr.vector_sink_f()

		# Connections
      self.connect(src, s2v, fftb, self.ss, self.sink)

   def getHistogram(self,pos):
      return self.ss.get_histogram(pos)

   def getNumberOfSubBands(self):
      return self.ss.getNumberOfSubBands()

   def get_debug_histogram(self):
      return self.ss.debug_histogram()

def convertFromPowerToStdDev(dbW):
   """ Convert noise power from dbW to standard deviation in voltage """ 
   variance = 10**(dbW/10)
   return math.sqrt(variance/2)

def awgn(size, dbW):
   """ Creates an AWGN channel """ 
   mu = 0
   std_dev = convertFromPowerToStdDev(dbW)
   src_data = []
   for j in range(1,size+1):
      src_data = src_data + [random.gauss(mu, std_dev) + random.gauss(mu, std_dev)*1j]
   return src_data

def fm(fs, L, delta_f, Ac):
   """ FM Signal Generation """
   fc = 20000*(fs/L) # Carrier Frequency
   fm = 600*(fs/L)   # Maximum allowed frequency for commercial FM.
   n = numpy.arange(0, L*(1/fs), 1/fs)
   m_fm = delta_f/fm
   e_fm  = Ac*numpy.sin(2*numpy.pi*fc*n - m_fm*numpy.cos(2*numpy.pi*fm*n))
   return e_fm

def simulate_pfa(dbW, pfa, pfd, nTrials, fft_size):
   """ All the work's done here: create flow graph, run and read out Pfa """
   false_alarm_rate = 0.0
   if ((fft_size % 8) == 0):
	   print "Noise Power = %f dbW" % dbW
	   for j in range(1,nTrials+1):
	      fg = PfaVsNoisePowerSimu(dbW, pfa, pfd, fft_size)
	      fg.run()
	      false_alarm_rate = false_alarm_rate + fg.sink.data()[0]
	   return false_alarm_rate/nTrials
   else:
	   print "Wrong FFT Size!"
	   return 0

def plotHistogram(fg):
   """ Plots the number of false alarms per sub-band """
   nSubBands = fg.getNumberOfSubBands()
   histogram = []
   for i in range(0,nSubBands):
      histogram.append(fg.getHistogram(i))
   plt.stem(range(0,nSubBands), histogram)
   plt.ylabel('Number of FA in a given sub-band')
   plt.xlabel('sub-band')
   plt.draw()

def writeResultToFile(pfa_simu, dbW_range, fft_size):
   """ Creates a comma separated file for Matlab importing and reading """
   filename = "pfa_vs_dbW_gnurad_simu_" + str(fft_size) + ".dat"
   f = open(filename, 'w')
   f.write('dbW,\tPfa\n')
   for i in range(0,len(dbW_range)):
      result = '{:f},\t{:f}\n'.format(dbW_range[i],pfa_simu[i])
      f.write(str(result))
   f.close()

if __name__ == "__main__":
   pfa = 0.0001
   pfd = 0.001
   dbW_min = -30
   dbW_max = 30
   dbW_step = 0.1
   nTrials = 10000
   fft_size_vector = [512, 1024, 2048, 4096]
   dbW_range = numpy.arange(dbW_min, dbW_max+1, dbW_step)
   pfa_theory = [pfa] * len(dbW_range)

   for fft_size in fft_size_vector:
	   print "\nSimulating for fft size: %d" %fft_size 
	   pfa_simu = [simulate_pfa(x, pfa, pfd, nTrials, fft_size) for x in dbW_range]
	   writeResultToFile(pfa_simu, dbW_range, fft_size)

   f = pylab.figure()
   s = f.add_subplot(1,1,1)
   s.semilogy(dbW_range, pfa_theory, 'g-.', label="Theoretical")
   s.semilogy(dbW_range, pfa_simu, 'b-o', label="Simulated")
   s.set_title('Pfa Simulation')
   s.set_xlabel('Noise Power (dbW)')
   s.set_ylabel('achieved Pfa')
   s.legend()
   s.grid()
   pylab.show()

