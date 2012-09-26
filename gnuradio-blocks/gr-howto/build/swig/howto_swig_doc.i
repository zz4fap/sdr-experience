
/*
 * This file was automatically generated using swig_doc.py.
 *
 * Any changes to it will be lost next time it is regenerated.
 */




%feature("docstring") howto_peak_location_cf "square a stream of floats.

Return a shared_ptr to a new instance of howto_square_ff.

To avoid accidental use of raw pointers, howto_square_ff's constructor is private. howto_make_square_ff is the public interface for creating new instances."

%feature("docstring") howto_peak_location_cf::howto_peak_location_cf "square a stream of floats.

Params: (sample_rate, ninput_samples)"

%feature("docstring") howto_peak_location_cf::~howto_peak_location_cf "

Params: (NONE)"

%feature("docstring") howto_peak_location_cf::ninput_samples "

Params: (NONE)"

%feature("docstring") howto_peak_location_cf::set_ninput_samples "

Params: (k)"

%feature("docstring") howto_peak_location_cf::sample_rate "

Params: (NONE)"

%feature("docstring") howto_peak_location_cf::set_sample_rate "

Params: (rate)"

%feature("docstring") howto_peak_location_cf::work "

Params: (noutput_items, input_items, output_items)"

%feature("docstring") howto_make_peak_location_cf "square a stream of floats.

Return a shared_ptr to a new instance of howto_square_ff.

To avoid accidental use of raw pointers, howto_square_ff's constructor is private. howto_make_square_ff is the public interface for creating new instances.

Params: (sample_rate, ninput_samples)"

%feature("docstring") howto_spectrum_sensing_cf "Return a shared_ptr to a new instance of howto_square_ff.

To avoid accidental use of raw pointers, howto_square_ff's constructor is private. howto_make_square_ff is the public interface for creating new instances."

%feature("docstring") howto_spectrum_sensing_cf::howto_spectrum_sensing_cf "

Params: (sample_rate, ninput_samples, nsub_bands, pfd, pfa, tcme, debug_far, debug_stats)"

%feature("docstring") howto_spectrum_sensing_cf::segment_spectrum "

Params: (in, vector_number)"

%feature("docstring") howto_spectrum_sensing_cf::sort_energy "

Params: (NONE)"

%feature("docstring") howto_spectrum_sensing_cf::calculate_noise_reference "

Params: (n_zref_segs)"

%feature("docstring") howto_spectrum_sensing_cf::calculate_scale_factor "

Params: (x)"

%feature("docstring") howto_spectrum_sensing_cf::calculate_statistics "

Params: (alpha, zref, I)"

%feature("docstring") howto_spectrum_sensing_cf::~howto_spectrum_sensing_cf "

Params: (NONE)"

%feature("docstring") howto_spectrum_sensing_cf::ninput_samples "

Params: (NONE)"

%feature("docstring") howto_spectrum_sensing_cf::set_ninput_samples "

Params: (k)"

%feature("docstring") howto_spectrum_sensing_cf::sample_rate "

Params: (NONE)"

%feature("docstring") howto_spectrum_sensing_cf::set_sample_rate "

Params: (rate)"

%feature("docstring") howto_spectrum_sensing_cf::nsub_bands "

Params: (NONE)"

%feature("docstring") howto_spectrum_sensing_cf::set_nsub_bands "

Params: (nbands)"

%feature("docstring") howto_spectrum_sensing_cf::pfd "

Params: (NONE)"

%feature("docstring") howto_spectrum_sensing_cf::set_pfd "

Params: (p)"

%feature("docstring") howto_spectrum_sensing_cf::pfa "

Params: (NONE)"

%feature("docstring") howto_spectrum_sensing_cf::set_pfa "

Params: (p)"

%feature("docstring") howto_spectrum_sensing_cf::tcme "

Params: (NONE)"

%feature("docstring") howto_spectrum_sensing_cf::set_tcme "

Params: (tcme)"

%feature("docstring") howto_spectrum_sensing_cf::false_alarm_rate "

Params: (NONE)"

%feature("docstring") howto_spectrum_sensing_cf::correct_rejection "

Params: (NONE)"

%feature("docstring") howto_spectrum_sensing_cf::work "

Params: (noutput_items, input_items, output_items)"

%feature("docstring") howto_make_spectrum_sensing_cf "Return a shared_ptr to a new instance of howto_square_ff.

To avoid accidental use of raw pointers, howto_square_ff's constructor is private. howto_make_square_ff is the public interface for creating new instances.

Params: (sample_rate, ninput_samples, nsub_bands, pfd, pfa, tcme, debug_far, debug_stats)"

%feature("docstring") howto_square2_ff "square2 a stream of floats.

This uses the preferred technique: subclassing gr_sync_block.

Return a shared_ptr to a new instance of howto_square2_ff.

To avoid accidental use of raw pointers, howto_square2_ff's constructor is private. howto_make_square2_ff is the public interface for creating new instances."

%feature("docstring") howto_square2_ff::howto_square2_ff "

Params: (NONE)"

%feature("docstring") howto_square2_ff::~howto_square2_ff "

Params: (NONE)"

%feature("docstring") howto_square2_ff::work "

Params: (noutput_items, input_items, output_items)"

%feature("docstring") howto_make_square2_ff "square2 a stream of floats.

This uses the preferred technique: subclassing gr_sync_block.

Return a shared_ptr to a new instance of howto_square2_ff.

To avoid accidental use of raw pointers, howto_square2_ff's constructor is private. howto_make_square2_ff is the public interface for creating new instances.

Params: (NONE)"

%feature("docstring") howto_square_ff "square a stream of floats.

Return a shared_ptr to a new instance of howto_square_ff.

To avoid accidental use of raw pointers, howto_square_ff's constructor is private. howto_make_square_ff is the public interface for creating new instances."

%feature("docstring") howto_square_ff::howto_square_ff "square a stream of floats.

Params: (NONE)"

%feature("docstring") howto_square_ff::~howto_square_ff "

Params: (NONE)"

%feature("docstring") howto_square_ff::general_work "

Params: (noutput_items, ninput_items, input_items, output_items)"

%feature("docstring") howto_make_square_ff "square a stream of floats.

Return a shared_ptr to a new instance of howto_square_ff.

To avoid accidental use of raw pointers, howto_square_ff's constructor is private. howto_make_square_ff is the public interface for creating new instances.

Params: (NONE)"

%feature("docstring") howto_stream_to_vector "convert a stream of items into a stream of blocks containing nitems_per_block"

%feature("docstring") howto_stream_to_vector::howto_stream_to_vector "

Params: (item_size, nitems_per_block)"

%feature("docstring") howto_stream_to_vector::work "

Params: (noutput_items, input_items, output_items)"

%feature("docstring") howto_make_stream_to_vector "convert a stream of items into a stream of blocks containing nitems_per_block

Params: (item_size, nitems_per_block)"

%feature("docstring") std::allocator "STL class."

%feature("docstring") std::auto_ptr "STL class."

%feature("docstring") std::auto_ptr::operator-> "STL member.

Params: (NONE)"

%feature("docstring") std::bad_alloc "STL class."

%feature("docstring") std::bad_cast "STL class."

%feature("docstring") std::bad_exception "STL class."

%feature("docstring") std::bad_typeid "STL class."

%feature("docstring") std::basic_fstream "STL class."

%feature("docstring") std::basic_ifstream "STL class."

%feature("docstring") std::basic_ios "STL class."

%feature("docstring") std::basic_iostream "STL class."

%feature("docstring") std::basic_istream "STL class."

%feature("docstring") std::basic_istringstream "STL class."

%feature("docstring") std::basic_ofstream "STL class."

%feature("docstring") std::basic_ostream "STL class."

%feature("docstring") std::basic_ostringstream "STL class."

%feature("docstring") std::basic_string "STL class."

%feature("docstring") std::basic_stringstream "STL class."

%feature("docstring") std::bitset "STL class."

%feature("docstring") std::complex "STL class."

%feature("docstring") std::map::const_iterator "STL iterator class."

%feature("docstring") std::multimap::const_iterator "STL iterator class."

%feature("docstring") std::basic_string::const_iterator "STL iterator class."

%feature("docstring") std::set::const_iterator "STL iterator class."

%feature("docstring") std::multiset::const_iterator "STL iterator class."

%feature("docstring") std::string::const_iterator "STL iterator class."

%feature("docstring") std::vector::const_iterator "STL iterator class."

%feature("docstring") std::wstring::const_iterator "STL iterator class."

%feature("docstring") std::deque::const_iterator "STL iterator class."

%feature("docstring") std::list::const_iterator "STL iterator class."

%feature("docstring") std::map::const_reverse_iterator "STL iterator class."

%feature("docstring") std::multimap::const_reverse_iterator "STL iterator class."

%feature("docstring") std::deque::const_reverse_iterator "STL iterator class."

%feature("docstring") std::set::const_reverse_iterator "STL iterator class."

%feature("docstring") std::basic_string::const_reverse_iterator "STL iterator class."

%feature("docstring") std::multiset::const_reverse_iterator "STL iterator class."

%feature("docstring") std::vector::const_reverse_iterator "STL iterator class."

%feature("docstring") std::string::const_reverse_iterator "STL iterator class."

%feature("docstring") std::wstring::const_reverse_iterator "STL iterator class."

%feature("docstring") std::list::const_reverse_iterator "STL iterator class."

%feature("docstring") std::deque "STL class."

%feature("docstring") std::domain_error "STL class."

%feature("docstring") std::exception "STL class."

%feature("docstring") std::ios_base::failure "STL class."

%feature("docstring") std::fstream "STL class."

%feature("docstring") std::ifstream "STL class."

%feature("docstring") std::invalid_argument "STL class."

%feature("docstring") std::ios "STL class."

%feature("docstring") std::ios_base "STL class."

%feature("docstring") std::istream "STL class."

%feature("docstring") std::istringstream "STL class."

%feature("docstring") std::deque::iterator "STL iterator class."

%feature("docstring") std::multimap::iterator "STL iterator class."

%feature("docstring") std::set::iterator "STL iterator class."

%feature("docstring") std::basic_string::iterator "STL iterator class."

%feature("docstring") std::multiset::iterator "STL iterator class."

%feature("docstring") std::vector::iterator "STL iterator class."

%feature("docstring") std::string::iterator "STL iterator class."

%feature("docstring") std::wstring::iterator "STL iterator class."

%feature("docstring") std::list::iterator "STL iterator class."

%feature("docstring") std::map::iterator "STL iterator class."

%feature("docstring") std::length_error "STL class."

%feature("docstring") std::list "STL class."

%feature("docstring") std::logic_error "STL class."

%feature("docstring") std::map "STL class."

%feature("docstring") std::multimap "STL class."

%feature("docstring") std::multiset "STL class."

%feature("docstring") std::ofstream "STL class."

%feature("docstring") std::ostream "STL class."

%feature("docstring") std::ostringstream "STL class."

%feature("docstring") std::out_of_range "STL class."

%feature("docstring") std::overflow_error "STL class."

%feature("docstring") std::priority_queue "STL class."

%feature("docstring") std::queue "STL class."

%feature("docstring") std::range_error "STL class."

%feature("docstring") std::multimap::reverse_iterator "STL iterator class."

%feature("docstring") std::multiset::reverse_iterator "STL iterator class."

%feature("docstring") std::string::reverse_iterator "STL iterator class."

%feature("docstring") std::basic_string::reverse_iterator "STL iterator class."

%feature("docstring") std::wstring::reverse_iterator "STL iterator class."

%feature("docstring") std::map::reverse_iterator "STL iterator class."

%feature("docstring") std::vector::reverse_iterator "STL iterator class."

%feature("docstring") std::set::reverse_iterator "STL iterator class."

%feature("docstring") std::deque::reverse_iterator "STL iterator class."

%feature("docstring") std::list::reverse_iterator "STL iterator class."

%feature("docstring") std::runtime_error "STL class."

%feature("docstring") std::set "STL class."

%feature("docstring") std::smart_ptr "STL class."

%feature("docstring") std::smart_ptr::operator-> "STL member.

Params: (NONE)"

%feature("docstring") std::stack "STL class."

%feature("docstring") std::string "STL class."

%feature("docstring") std::stringstream "STL class."

%feature("docstring") std::underflow_error "STL class."

%feature("docstring") std::unique_ptr "STL class."

%feature("docstring") std::unique_ptr::operator-> "STL member.

Params: (NONE)"

%feature("docstring") std::valarray "STL class."

%feature("docstring") std::vector "STL class."

%feature("docstring") std::weak_ptr "STL class."

%feature("docstring") std::weak_ptr::operator-> "STL member.

Params: (NONE)"

%feature("docstring") std::wfstream "STL class."

%feature("docstring") std::wifstream "STL class."

%feature("docstring") std::wios "STL class."

%feature("docstring") std::wistream "STL class."

%feature("docstring") std::wistringstream "STL class."

%feature("docstring") std::wofstream "STL class."

%feature("docstring") std::wostream "STL class."

%feature("docstring") std::wostringstream "STL class."

%feature("docstring") std::wstring "STL class."

%feature("docstring") std::wstringstream "STL class."