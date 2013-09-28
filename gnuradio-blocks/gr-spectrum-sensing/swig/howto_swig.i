/* -*- c++ -*- */

#define HOWTO_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "howto_swig_doc.i"


%{
#include "howto_square_ff.h"
#include "howto_square2_ff.h"
#include "howto_peak_location_cf.h"
#include "howto_spectrum_sensing_cf.h"
#include "howto_stream_to_vector.h"
%}

GR_SWIG_BLOCK_MAGIC(howto,square_ff);
%include "howto_square_ff.h"

GR_SWIG_BLOCK_MAGIC(howto,square2_ff);
%include "howto_square2_ff.h"

GR_SWIG_BLOCK_MAGIC(howto,peak_location_cf);
%include "howto_peak_location_cf.h"

GR_SWIG_BLOCK_MAGIC(howto,spectrum_sensing_cf);
%include "howto_spectrum_sensing_cf.h"

//howto_square_ff_sptr howto_make_square_ff ();

/*class declaration*/
class howto_spectrum_sensing_cf : public gr_sync_block
{
   public:
      int get_histogram(int pos); 
      int getNumberOfSubBands();
      bool debug_histogram();
};

GR_SWIG_BLOCK_MAGIC(howto,stream_to_vector);
%include "howto_stream_to_vector.h"
