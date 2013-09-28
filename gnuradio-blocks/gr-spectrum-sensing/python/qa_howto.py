#!/usr/bin/env python
#
# Copyright 2004,2007 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest
import howto_swig

class qa_howto (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_square_ff (self):
        src_data = (-3, 4, -5.5, 2, 3)
        expected_result = (9, 16, 30.25, 4, 9)
        src = gr.vector_source_f (src_data)
        sqr = howto_swig.square_ff ()
        dst = gr.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)

    def test_002_square2_ff (self):
        src_data = (-3, 4, -5.5, 2, 3)
        expected_result = (9, 16, 30.25, 4, 9)
        src = gr.vector_source_f (src_data)
        sqr = howto_swig.square2_ff ()
        dst = gr.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)

    def test_003_peak_location_cf (self):
        src_data = (0+0j,0+0j,5+0j,0+0j,10+0j,0+0j,0+0j,0+0j)
        expected_result = (2.0,0.0)
        src = gr.vector_source_c (src_data)
        sqr = howto_swig.peak_location_cf (4,4)
        dst = gr.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data)

    def test_004_peak_location_cf (self):
        src_data = ((0+0j), (0+0j), (5+0j), (0+0j))
        expected_result = (2.0,)
        src = gr.vector_source_c (src_data)
        sqr = howto_swig.peak_location_cf (4,4)
        dst = gr.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data)

    def test_005_peak_location_cf (self):
        src_data = ((0+0j), (0+0j), (5+0j), (0+0j), (0+0j), (0+0j), (0+0j), (0+0j), (0+0j), (0+0j), (0+0j), (0+0j))
        expected_result = (2.0,0.0,0.0)
        src = gr.vector_source_c (src_data)
        sqr = howto_swig.peak_location_cf (4,4)
        dst = gr.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data)

    def test_006_peak_location_cf (self):
        src_data = (0+0j,5+0j,0+0j,0+0j,0+0j,5+0j,0+0j,0+0j)
        expected_result = (1.0,1.0)
        src = gr.vector_source_c (src_data)
        sqr = howto_swig.peak_location_cf (4,4)
        dst = gr.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data)

    def test_007_peak_location_cf (self):
        src_data = (0+0j,0+0j,5+0j,0+0j,0+0j,0+0j,5+0j,0+0j)
        expected_result = (2.0,2.0)
        src = gr.vector_source_c (src_data)
        sqr = howto_swig.peak_location_cf (4,4)
        dst = gr.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data)

    def test_008_peak_location_cf (self):
        src_data = (0+0j,0+0j,0+0j,0+0j,0+0j,5+0j,0+0j,0+0j)
        expected_result = (0.0,1.0)
        src = gr.vector_source_c (src_data)
        sqr = howto_swig.peak_location_cf (4,4)
        dst = gr.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data)

    def test_009_peak_location_cf (self):
        src_data = (0+0j,10+0j,0+0j,0+0j,0+0j,0+0j,0+0j,10+0j)
        expected_result = (1.0,3.0)
        src = gr.vector_source_c (src_data)
        sqr = howto_swig.peak_location_cf (4,4)
        dst = gr.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data)

    def test_010_peak_location_cf (self):
        src_data = (0+0j,0+0j,0+0j,0+0j,0+0j,0+0j,0+0j,10+0j)
        expected_result = (0.0,3.0)
        src = gr.vector_source_c (src_data)
        sqr = howto_swig.peak_location_cf (4,4)
        dst = gr.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data)

    def test_011_peak_location_cf (self):
        src_data = (0+0j,0+0j,0+0j,0+0j,0+0j,0+0j,0+0j,0+10j)
        expected_result = (0.0,3.0)
        src = gr.vector_source_c (src_data)
        sqr = howto_swig.peak_location_cf (4,4)
        dst = gr.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data)

    def test_012_peak_location_cf (self):
        src_data = (0+0j,0+5j,0+0j,0+0j,0+0j,0+0j,0+11j,0+0j)
        expected_result = (1.0,2.0)
        src = gr.vector_source_c (src_data)
        sqr = howto_swig.peak_location_cf (4,4)
        dst = gr.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data)

    def test_013_spectrum_sensing_cf (self):
        src_data = (0+0j,0+5j,0+0j,0+0j)
        expected_result = (1.0,)
        src = gr.vector_source_c (src_data)
	s2v = gr.stream_to_vector(gr.sizeof_gr_complex, 4)
        sqr = howto_swig.spectrum_sensing_cf (4,4,2,0.001,0.0001)
        dst = gr.vector_sink_f ()
	self.tb.connect(src, s2v, sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data)

    def test_014_spectrum_sensing_cf (self):
        src_data = (0+0j,0+5j,0+0j,0+0j,0+10j,0+5j,8+0j,0+0j)
        expected_result = (1.0,2.0)
        src = gr.vector_source_c (src_data)
	s2v = gr.stream_to_vector(gr.sizeof_gr_complex, 4)
        sqr = howto_swig.spectrum_sensing_cf (4,4,2,0.001,0.0001)
        dst = gr.vector_sink_f ()
	self.tb.connect(src, s2v, sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
	print expected_result
	print result_data
        self.assertFloatTuplesAlmostEqual (expected_result, result_data)

if __name__ == '__main__':
    gr_unittest.main ()
