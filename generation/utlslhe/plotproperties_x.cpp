////////////////////////////////////////////////////////////////////////////////
//
// plotproperties_x
// ----------------
//
// parse LHE files, checking for one or more particles (via PDG id)
// and produce an output root file
//
////////////////////////////////////////////////////////////////////////////////

#include <stdexcept>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include "TFile.h"
#include "TH1D.h"

using namespace std;

void ini_histos();
void nrm_histos();
void skip_header();
void read_event();
void skip_lines(int nlines);

int npart;
double* evtprop;
double** partprop;
ifstream ifile;
TFile* ofile;
TH1D * weights;
TH1D * scale;
vector<int> plotid;
map<pair<int,string>, TH1D*> mhprops;
typedef map<pair<int,string>, TH1D*>::iterator iter;

int main(int argc, char** argv) {
 
  // interpret comand line arguments
  if(argc < 2) return 1;
  string input   = argv[1];
  cout << "Reading from \"" << input << "\"..." << endl;

  for(int i = 2; i < argc; i++) {
    plotid.push_back(atoi(argv[i]));
    cout << "plotid(" << plotid.size()-1 << ") = " << atoi(argv[i]) << endl; 
  }

  partprop=new double*[50];
  for (int i=0;i<50;i++) partprop[i]=new double[50];    
  evtprop=new double[5]; 

  ofile =new TFile("LHEparticleproperties.root","RECREATE");
  ini_histos();

  string line;

  for(int i = 1; i <= 250; i++) {
    TString file;
    file.Form("%s-%04i.lhe", input.c_str(), i);
    cout << "Reading from \"" << file << "\"..." << endl;

    ifile.open(file);
    //check that input file is readable 
    if (!ifile.is_open()) { cout << "File not found." << endl; continue; }
    
    skip_header();
    read_event();
    while (!ifile.eof()) {
      read_event();
    }
    //normalize histos for bin width
    nrm_histos();
    
    // close all files 
    ifile.close();
  }

  ofile->Write();
  ofile->Close();
    
  return 0;
}


void skip_header() {
  string line;
  getline(ifile,line);
  while (0!=line.find("</init>")){
    getline(ifile,line);
  }
  return;
}

void read_event() {
  string line;
  stringstream ss;
  skip_lines(1);
  getline(ifile,line);
  ss<<line;
  ss>>npart>>evtprop[0]>>evtprop[1]>>evtprop[2]>>evtprop[3]>>evtprop[4];
  ss.clear();

  weights->Fill(evtprop[1]);
  scale->Fill(evtprop[2]);

  for (int ipart=0;ipart<npart;ipart++) {
    getline(ifile,line);
    ss<<line;
    ss>>partprop[ipart][0]>>partprop[ipart][1]>>partprop[ipart][2]
      >>partprop[ipart][3]>>partprop[ipart][4]>>partprop[ipart][5]
      >>partprop[ipart][6]>>partprop[ipart][7]>>partprop[ipart][8]
      >>partprop[ipart][9]>>partprop[ipart][10]>>partprop[ipart][11]
      >>partprop[ipart][12];
    ss.clear();
    if (std::find(plotid.begin(), plotid.end(), abs(partprop[ipart][0]))!=plotid.end()) {
      double px=partprop[ipart][6];
      double py=partprop[ipart][7];
      double pz=partprop[ipart][8];
      double e=partprop[ipart][9];
      double m=partprop[ipart][10];
      cout<<"Print object properites for id="
	  << abs(partprop[ipart][0]) << ": "  
	  << e  << "  " 
	  << px << "  "
	  << py << "  " 
	  << pz << "  " 
	  << m  << "  "
	  <<endl;
      if(mhprops[make_pair(abs(partprop[ipart][0]),"e")]!=NULL)
	mhprops[make_pair(abs(partprop[ipart][0]),"e")]->Fill(e);
      if(mhprops[make_pair(abs(partprop[ipart][0]),"pt")]!=NULL)
	mhprops[make_pair(abs(partprop[ipart][0]),"pt")]->Fill(std::sqrt(px*px+py*py));
      if(mhprops[make_pair(abs(partprop[ipart][0]),"m")]!=NULL)
	mhprops[make_pair(abs(partprop[ipart][0]),"m")]->Fill(std::sqrt(e*e-px*px-py*py-pz*pz));
      if(mhprops[make_pair(abs(partprop[ipart][0]),"mdir")]!=NULL)
	mhprops[make_pair(abs(partprop[ipart][0]),"mdir")]->Fill(m);
      
    }
  }
  skip_lines(1);
  return;
}

void skip_lines(int nlines) {
  string line;
  for (int i=0;i<nlines;i++) {
    getline(ifile,line); 
  }
  return;
}

void ini_histos() {
  for(unsigned i=0;i<plotid.size();i++){
    stringstream ss;ss<<"e_"<<plotid[i]; 
    mhprops[make_pair(plotid[i],"e")]  = new TH1D(ss.str().c_str(),"",70,100.,800.);
    ss.str(""); ss<<"pt_"<<plotid[i]; 
    mhprops[make_pair(plotid[i],"pt")] = new TH1D(ss.str().c_str(),"",35,0.,350.);
    ss.str(""); ss<<"m_"<<plotid[i]; 
    mhprops[make_pair(plotid[i],"m")]  = new TH1D(ss.str().c_str(),"",60,160.,190.);
    ss.str(""); ss<<"mdir_"<<plotid[i]; 
    mhprops[make_pair(plotid[i],"mdir")]  = new TH1D(ss.str().c_str(),"",60,160.,190.);
  }
  weights = new TH1D("weights","",2000,-1200.,1200.);
  scale = new TH1D("scale","",2000,-1200.,1200.);
}

void nrm_histos() {
  for(iter it = mhprops.begin(); it!= mhprops.end(); it++) 
    for(int i=0;i<=it->second->GetNbinsX()+1;i++)
      it->second->SetBinContent(i,(it->second->GetBinContent(i)/it->second->GetBinWidth(i)));
}
