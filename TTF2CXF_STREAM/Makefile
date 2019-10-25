# Makefile for TTF2CXF_STREAM
# Date: 6/28/2013

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
	TARGET=osx
endif

MAC_FREETYPE = $(shell brew --prefix freetype)

osx:
	g++ -o ttf2cxf_stream ttf2cxf_stream.cpp -lm -I$(MAC_FREETYPE)/include/freetype2 -L$(MAC_FREETYPE)/lib -lfreetype

clean:
	-@rm ttf2cxf_stream

