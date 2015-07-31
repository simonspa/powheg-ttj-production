###############################################################################
#
# utlslhe Makefile
# ----------------
#
#                           22/05/2014 Alexander Grohsjean <agrohsje@fnal.gov>
#
################################################################################


CXX          = g++

ROOTCXXFLAGS = $(shell $(ROOTSYS)/bin/root-config --cflags)
CXXFLAGS     = -g -O0 -Wall -fPIC -I. -I$(UTLS_DIR) $(ROOTCXXFLAGS)

ROOTLIBS     = $(shell $(ROOTSYS)/bin/root-config --libs)  
BINDIR	     = .

all: lib bin


lib: 


bin: plotproperties


plotproperties: plotproperties_x.cpp
	$(CXX) $(CXXFLAGS) plotproperties_x.cpp $(ROOTLIBS) \
        -o $(BINDIR)/plotproperties_x


clean:
	rm -rf $(BINDIR)/plotproperties_x


################################################################################
# $(OBJS)
################################################################################



