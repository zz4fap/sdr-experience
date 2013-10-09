/* -*- c++ -*- */

#define HOWTO_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "howto_swig_doc.i"


%{
#include "howto_peak_location_cf.h"
#include "howto_spectrum_sensing_cf.h"
%}

GR_SWIG_BLOCK_MAGIC(howto,peak_location_cf);
%include "howto_peak_location_cf.h"

GR_SWIG_BLOCK_MAGIC(howto,spectrum_sensing_cf);
%include "howto_spectrum_sensing_cf.h"

/*class declaration*/
class howto_spectrum_sensing_cf : public gr_sync_block
{
   public:
      int get_histogram(int pos); 
      int getNumberOfSubBands();
      bool debug_histogram();
};
