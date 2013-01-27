#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Sun Jan 27 16:56:56 2013
##################################################

from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import howto
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 2.4e6
		self.fft_size = fft_size = 4096

		##################################################
		# Blocks
		##################################################
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=4096,
			fft_rate=1000,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0.win)
		self.howto_stream_to_vector_0 = howto.stream_to_vector(gr.sizeof_gr_complex*1, 4096)
		self.howto_spectrum_sensing_cf_0 = howto.spectrum_sensing_cf(samp_rate,fft_size,16,0.001,0.0001,1.9528,True,True,0,300000.0,False)
		self.gr_throttle_0 = gr.throttle(gr.sizeof_gr_complex*1, samp_rate)
		self.gr_sig_source_x_0 = gr.sig_source_c(samp_rate, gr.GR_COS_WAVE, 300000, 1, 0)
		self.gr_null_sink_0 = gr.null_sink(gr.sizeof_float*1)
		self.fft_vxx_0 = fft.fft_vcc(fft_size, True, (window.blackmanharris(1024)), False, 1)

		##################################################
		# Connections
		##################################################
		self.connect((self.fft_vxx_0, 0), (self.howto_spectrum_sensing_cf_0, 0))
		self.connect((self.howto_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
		self.connect((self.howto_spectrum_sensing_cf_0, 0), (self.gr_null_sink_0, 0))
		self.connect((self.gr_sig_source_x_0, 0), (self.howto_stream_to_vector_0, 0))
		self.connect((self.gr_throttle_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.gr_sig_source_x_0, 0), (self.gr_throttle_0, 0))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.howto_spectrum_sensing_cf_0.set_sample_rate(self.samp_rate)
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
		self.gr_sig_source_x_0.set_sampling_freq(self.samp_rate)

	def get_fft_size(self):
		return self.fft_size

	def set_fft_size(self, fft_size):
		self.fft_size = fft_size
		self.howto_spectrum_sensing_cf_0.set_ninput_samples(self.fft_size)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

