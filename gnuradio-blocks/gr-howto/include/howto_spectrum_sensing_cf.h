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
#ifndef INCLUDED_HOWTO_SPECTRUM_SENSING_CF_H
#define INCLUDED_HOWTO_SPECTRUM_SENSING_CF_H

#include <gr_sync_decimator.h>
#include <gr_sync_block.h>
#include <gr_sync_interpolator.h>
#include <gr_sync_block.h>
#include <howto_api.h>
#include<boost/math/distributions.hpp>

class howto_spectrum_sensing_cf;

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
typedef boost::shared_ptr<howto_spectrum_sensing_cf> howto_spectrum_sensing_cf_sptr;

/*!
 * \brief Return a shared_ptr to a new instance of howto_square_ff.
 *
 * To avoid accidental use of raw pointers, howto_square_ff's
 * constructor is private.  howto_make_square_ff is the public
 * interface for creating new instances.
 */
HOWTO_API howto_spectrum_sensing_cf_sptr howto_make_spectrum_sensing_cf (float sample_rate, int ninput_samples, int samples_per_band, float pfd, float pfa, float tcme, bool debug_far, bool debug_cdr, bool debug_stats, int band_location, int noutput_samples, int useless_bandwidth);

class HOWTO_API howto_spectrum_sensing_cf : public gr_sync_block
{
private:
  // The friend declaration allows howto_make_spectrum_sensing_cf to
  // access the private constructor.
  friend HOWTO_API howto_spectrum_sensing_cf_sptr howto_make_spectrum_sensing_cf (float sample_rate, int ninput_samples, int samples_per_band, float pfd, float pfa, float tcme, bool debug_far, bool debug_cdr, bool debug_stats, int band_location, int noutput_samples, int useless_bandwidth);

  float d_sample_rate, d_pfd, d_pfa, d_tcme, d_false_alarm_rate, d_correct_rejection_rate, d_correct_detection_rate, d_false_rejection_rate;
  float *segment, *sorted_segment;
  int d_ninput_samples, d_samples_per_band, d_band_location, d_useless_segment, d_usefull_samples, d_nsub_bands, d_noutput_samples, d_useless_bandwidth;
  unsigned int d_false_alarm_counter, d_correct_rejection_counter, d_correct_detection_counter, d_false_rejection_counter, d_trials_counter;
  bool d_debug_far, d_debug_cdr, d_debug_stats;
  gr_complex *new_in;

  howto_spectrum_sensing_cf (float sample_rate, int ninput_samples, int samples_per_band, float pfd, float pfa, float tcme, bool debug_far, bool debug_cdr, bool debug_stats, int band_location, int noutput_samples, int useless_bandwidth);  	// private constructor

  void segment_spectrum(const gr_complex *in, int vector_number);
  bool sort_energy();
  float calculate_noise_reference(int* n_zref_segs);
  float calculate_scale_factor(int x);
  float calculate_statistics(float alpha, float zref, int I);
  float primary_user_detection(float alpha, float zref, int I);

 public:
  ~howto_spectrum_sensing_cf ();	// public destructor

  int ninput_samples () const { return d_ninput_samples; }
  void set_ninput_samples (int k) { d_ninput_samples = k; }
	
  float sample_rate() const {return d_sample_rate;}
  void set_sample_rate(float rate) {d_sample_rate = rate;}

  int samples_per_band() const {return d_samples_per_band;}
  void set_samples_per_band(int nsamples) {d_samples_per_band = nsamples;}

  float pfd() const {return d_pfd;}
  void set_pfd(float p) {d_pfd = p;}

  float pfa() const {return d_pfa;}
  void set_pfa(float p) {d_pfa = p;}
	
  float tcme() const {return d_tcme;}
  void set_tcme(float tcme) {d_tcme = tcme;}
	
  float false_alarm_rate() {return d_false_alarm_rate;}
  float correct_rejection() {return d_correct_rejection_rate;}

  // Where all the action really happens
  int work (int noutput_items,
            gr_vector_const_void_star &input_items,
            gr_vector_void_star &output_items);
};

#endif /* INCLUDED_HOWTO_SPECTRUM_SENSING_CF_H */
