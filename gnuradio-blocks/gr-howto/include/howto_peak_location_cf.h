/* -*- c++ -*- */
/*
 * Copyright 2004 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * GNU Radio is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * GNU Radio is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with GNU Radio; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */
#ifndef INCLUDED_HOWTO_PEAK_LOCATION_CF_H
#define INCLUDED_HOWTO_PEAK_LOCATION_CF_H

#include <gr_sync_decimator.h>
#include <howto_api.h>

class howto_peak_location_cf;

/*
 * We use boost::shared_ptr's instead of raw pointers for all access
 * to gr_blocks (and many other data structures).  The shared_ptr gets
 * us transparent reference counting, which greatly simplifies storage
 * management issues.  This is especially helpful in our hybrid
 * C++ / Python system.
 *
 * See http://www.boost.org/libs/smart_ptr/smart_ptr.htm
 *
 * As a convention, the _sptr suffix indicates a boost::shared_ptr
 */
typedef boost::shared_ptr<howto_peak_location_cf> howto_peak_location_cf_sptr;

/*!
 * \brief Return a shared_ptr to a new instance of howto_square_ff.
 *
 * To avoid accidental use of raw pointers, howto_square_ff's
 * constructor is private.  howto_make_square_ff is the public
 * interface for creating new instances.
 */
HOWTO_API howto_peak_location_cf_sptr howto_make_peak_location_cf (int sample_rate, int ninput_samples);

/*!
 * \brief square a stream of floats.
 * \ingroup block
 *
 * \sa howto_square2_ff for a version that subclasses gr_sync_block.
 */
class HOWTO_API howto_peak_location_cf : public gr_sync_decimator
{
private:
  // The friend declaration allows howto_make_square_ff to
  // access the private constructor.

  friend HOWTO_API howto_peak_location_cf_sptr howto_make_peak_location_cf (int sample_rate, int ninput_samples);

  int d_sample_rate;
  int d_ninput_samples;

  /*!
   * \brief square a stream of floats.
   */
  howto_peak_location_cf (int sample_rate, int ninput_samples);  	// private constructor

 public:
  ~howto_peak_location_cf ();	// public destructor

  int ninput_samples () const { return d_ninput_samples; }
  void set_ninput_samples (int k) { d_ninput_samples = k; }
	
  int sample_rate() const {return d_sample_rate;}
  void set_sample_rate(int rate) {d_sample_rate = rate;} 

  // Where all the action really happens

  int work (int noutput_items,
            gr_vector_const_void_star &input_items,
            gr_vector_void_star &output_items);
};

#endif /* INCLUDED_HOWTO_PEAK_LOCATION_CF_H */
