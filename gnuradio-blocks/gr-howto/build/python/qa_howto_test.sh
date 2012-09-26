#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/zz4fap/Dropbox/gnuradio/gr-howto/python
export PATH=/home/zz4fap/Dropbox/gnuradio/gr-howto/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=/home/zz4fap/Dropbox/gnuradio/gr-howto/build/swig:$PYTHONPATH
/usr/bin/python /home/zz4fap/Dropbox/gnuradio/gr-howto/python/qa_howto.py 
