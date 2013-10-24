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
import scipy
from scipy.signal import hilbert
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
import matplotlib.pyplot as plt

class PfaVsNoisePowerSimu(gr.top_block):
   " This contains the simulation flow graph "
   def __init__(self, signal, signal_power, snr, pfa, pfd, fft_size):
      gr.top_block.__init__(self)

      # Parameters
      samp_rate               = 2e6
      samples_per_band        = 16
      tcme                    = 1.9528
      output_pfa              = False
      debug_stats             = False
      primary_user_location   = 0
      useless_bw              = 0.0    # As we are not using any of the dongles it can be set as zero, i.e., all the band can be used.
      histogram               = False
      nframes_to_check        = 1
      nframes_to_average      = 1
      downconverter           = 1
      nsegs_to_check          = 6

      # Calculate the power of the noise vector to be generated.
      noise_power = signal_power - snr # in dBW

      # Create AWGN noise
      noise = awgn(fft_size, noise_power)

      effective_noise_power = calculateSignalPower(noise);
      effective_snr = signal_power - effective_noise_power;
      print "effective_noise_power: %f\n" % effective_noise_power
      print "effective_snr: %f\n" % effective_snr

      # Create corrupted signal
      rx_signal = signal[0:fft_size] + noise

		# Blocks
      src = gr.vector_source_c(rx_signal)
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
   return math.sqrt(variance/2.0)

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

def hil(e_fm):
   """ Apply Hilbert Transform to FM Signal """
   hil_fm = hilbert(e_fm)
   return hil_fm

def calculateSignalPower(signal):
   """ Calculates the Power of a given signal in dBW """
   power = 10*numpy.log10(numpy.sum(numpy.abs(signal)**2)/len(signal))
   return power

def simulate_pd(signal, snr, pfa, pfd, nTrials, fft_size):
   """ All the work's done here: create flow graph, run and read out Pfa """
   signal_power = calculateSignalPower(signal)
   detection_rate = 0.0
   if ((fft_size % 8) == 0):
	   print "Pfa = %f" % pfa
	   for j in range(1,nTrials+1):
	      fg = PfaVsNoisePowerSimu(signal, signal_power, snr, pfa, pfd, fft_size)
	      fg.run()
	      detection_rate = detection_rate + fg.sink.data()[0]
	   return detection_rate/nTrials
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

def writeResultToFile(pd_simu, pfa_range, fft_size):
   """ Creates a comma separated file for Matlab importing and reading """
   filename = "pfa_vs_achieved_pd_gnurad_simu_" + str(fft_size) + ".dat"
   f = open(filename, 'w')
   f.write('DesiredPfa,\tAchievedPd\n')
   for i in range(0,len(pfa_range)):
      result = '{:f},\t{:f}\n'.format(pfa_range[i],pd_simu[i])
      f.write(str(result))
   f.close()

if __name__ == "__main__":
   pfa_min = 0.00001
   pfa_max = 0.1
   pfa_step = 0.000001
   pfd = 0.001
   snr = 0 # in dB
   nTrials = 1000
   fft_size_vector = [512, 1024, 2048, 4096]
   pfa_range = numpy.arange(pfa_min, pfa_max+pfa_step, pfa_step)

   # Generate FM Signal
   L = 80000      # Number of samples to be generated.
   fs = 2e6       # Sampling frequency.
   BWfm = 200e3   # in Hz.
   delta_f = 75e3 # Maximum allowed frequency deviation for commercial FM.
   Ac = 10        # Amplitude of the modulated signal.
   NFFT = L/10    # FFT's number of points.
   e_fm = fm(fs, L, delta_f, Ac)

   # Hilbert's transform of the FM signal.
   hil_fm = hil(e_fm)

   for fft_size in fft_size_vector:
	   print "\nSimulating for fft size: %d" %fft_size 
	   pd_simu = [simulate_pd(hil_fm, snr, pfa, pfd, nTrials, fft_size) for pfa in pfa_range]
	   writeResultToFile(pd_simu, pfa_range, fft_size)

	   f = pylab.figure()
	   s = f.add_subplot(1,1,1)
	   s.plot(pfa_range, pd_simu)
	   s.set_title('Pfa Simulation ' + str(fft_size))
	   s.set_xlabel('Desired Pfa')
	   s.set_ylabel('Achieved Pd')
	   s.legend()
	   s.grid()
	   pylab.show()

