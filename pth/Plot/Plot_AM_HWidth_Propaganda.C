#include "TString.h"
#include "TH1F.h"
#include "TSystem.h"
#include "TInterpreter.h"
#include "TFile.h"

#include "PlotVHqqHggH.C"

#include <iostream>

//---- Filter bins ----
TH1F *
FilterBins (std::vector < int > binsToSelect, TH1F * inputTH)
{
  int numbin = binsToSelect.size ();

  TString name = Form ("%s_new", inputTH->GetName ());
  TString title = Form ("%s", inputTH->GetTitle ());

  TH1F *newTH = new TH1F (name, title, numbin, 0, numbin);
  for (int i = 0; i < binsToSelect.size (); i++)
    {
      newTH->SetBinContent (i + 1,
			    inputTH->GetBinContent (binsToSelect.at (i)));
      newTH->SetBinError (i + 1, inputTH->GetBinError (binsToSelect.at (i)));
    }

  return newTH;
}

TH1F* sumOver(TH1F * inputTH, bool sumoverx, int nx, int ny){

  TString name = Form ("%s_new", inputTH->GetName ());
  TString title = Form ("%s", inputTH->GetTitle ());
  int numbin = sumoverx ? ny : nx ;

  TH1F *newTH = new TH1F (name, title, numbin, 0, numbin);

  if (sumoverx){
    for (int i = 0; i<ny; ++i){
      double summed = 0.;
      double summedError = 0.;
      for (int j = 0; j<nx; ++j){
        summed += inputTH->GetBinContent(j*nx + i + 1);
        summedError += inputTH->GetBinError(j*nx + i + 1)*inputTH->GetBinError(j*nx + i + 1);
      }
      newTH->SetBinContent(i+1, summed);
      newTH->SetBinError(i+1, sqrt(summedError));
    }
  } else {
    for (int i = 0; i < nx; ++i){
      double summed = 0.;
      double summedError = 0.;
      for (int j = 0; j<ny; ++j){
        summed += inputTH->GetBinContent(j+i*nx+1);
        summedError += inputTH->GetBinError(j+i*nx+1)*inputTH->GetBinError(j+i*nx+1);
      }
      newTH->SetBinContent(i+1, summed);
      newTH->SetBinError(i+1, sqrt(summedError));
    }
  }

  return newTH;

}


TGraphAsymmErrors *
FilterBins (std::vector < int > binsToSelect, TGraphAsymmErrors * inputGR)
{
  int numbin = binsToSelect.size ();

  TString name = Form ("%s_new", inputGR->GetName ());
  TString title = Form ("%s", inputGR->GetTitle ());

  TGraphAsymmErrors *newGR = new TGraphAsymmErrors ();
  newGR->SetName (name);

  for (int i = 0; i < binsToSelect.size (); i++)
    {

      double X = i + 0.5;
      double Y = (inputGR->GetY ())[binsToSelect.at (i) - 1];

      double errXUp = inputGR->GetErrorXhigh (binsToSelect.at (i) - 1);
      double errXDown = inputGR->GetErrorXlow (binsToSelect.at (i) - 1);
      double errYUp = inputGR->GetErrorYhigh (binsToSelect.at (i) - 1);
      double errYDown = inputGR->GetErrorYlow (binsToSelect.at (i) - 1);

      newGR->SetPoint (i, X, Y);
      newGR->SetPointError (i, errXDown, errXUp, errYDown, errYUp);

      //     std::cout << " i = " << i << " X = " << X << " Y = " << Y << std::endl;
    }

  return newGR;
}



void
Plot_AM_HWidth_Propaganda (const char *channel, int what)
{

  int which = 0;
//  int which = 1;


  TString nameChannel;
  if (which == 0)
    {
      nameChannel = Form ("of_%s/", channel);
    }				//---- signal injection
  else if (which == 1)
    {
      nameChannel = Form ("of_%s/", channel);
    }

  std::cout << " which = " << which << std::endl;


//  TString folder = Form("sig/");
//  TString cutNameBefore = Form("sig/%shisto_",nameChannel.Data());

  TString folder = Form ("init/");
  TString cutNameBefore = Form ("init/%shisto_", nameChannel.Data ());

  std::cout << " nameChannel   = " << nameChannel.Data () << std::endl;
  std::cout << " cutNameBefore = " << cutNameBefore.Data () << std::endl;

  //  TString folder = Form("bkg/");
  //  TString nameChannel = Form ("of_vh2j/");
  //  TString cutNameBefore = Form("bkg/%shisto_",nameChannel.Data());


  //                            cut_variable 
  TString cutNameAfter = Form ("");

  gROOT->LoadMacro ("PlotVHqqHggH.C+");
  gInterpreter->ExecuteMacro ("LatinoStyle2.C");

  TCanvas *c1 = new TCanvas ("mT", "mT", 550, 660);

  TFile *f[10];
  bool doSignalInjection;


  if (which == 0)
    {
      f[0] =
	new
	TFile (Form
	       ("../mll-mth_8TeV_%s/postFit/Hwidth-%s-of-error-signalInjection.root",
		channel, channel));
      doSignalInjection = true;
    }
  else if (which == 1)
    {
      f[0] =
	new
	TFile (Form
	       ("../mll-mth_8TeV_%s/postFit/Hwidth-%s-of-error-data.root",
		channel, channel));
      doSignalInjection = false;
    }

  PlotVHqqHggH *hs = new PlotVHqqHggH ();

  cout << f[0] << endl;

//  hs->setLabel("mT*");
  hs->setLabel ("mT");
  if (what == 1)
    hs->setLabel ("mll");

  //  hs->setLumi(20);
  //  hs->setLumi(200);
  //  hs->addLabel("#splitline{      WHSC}{     #sqrt{s} = 13 TeV}");

  hs->setLumi (19.4);
  hs->addLabel ("#splitline{     Hwidth}{     #sqrt{s} = 8 TeV}");
//  
  TString name;

  std::vector < int >vectColourBkg;
  std::vector < double >vectSystBkg;
  std::vector < double >vectScaleBkg;
  std::vector < std::string > vectNameBkg;
  std::vector < double >vectNormalizationBkg;
  std::vector < TH1F * >vectTHBkg;

  std::vector < int >vectColourSig;
  std::vector < double >vectSystSig;
  std::vector < double >vectScaleSig;
  std::vector < std::string > vectNameSig;
  std::vector < double >vectNormalizationSig;
  std::vector < TH1F * >vectTHSig;


  std::vector < int > binsToSelect;

//  int NMAXX = 30;  //---- variable bin
//  int NMAXX = 16;  //---- variable bin
//  int NMAXX = 8;  //---- variable bin
//  int NMAXY = 6;  

  int NMAXX = 14;		//---- variable bin
  int NMAXY = 9;

  // what 0 mT
  // what 1 mll

  //---- all ----
  int minNY = 0;
  int minNX = 0;

  int NX = NMAXX;
  int NY = NMAXY;


//  int minNY = 0;
//  int minNX = 6;

//  int NX = NMAXX;
//  int NY = NMAXY;



  for (int iFile = 0; iFile < 1; iFile++)
    {

      std::cout << "iFile = " << iFile << std::endl;

      if (what == 0)
	{
	  ///---- project along Y : sum over X
	  for (int iX = minNX; iX < NX; iX++)
	    {
	      binsToSelect.clear ();
	      for (int iY = minNY; iY < NY; iY++)
		{
		  binsToSelect.push_back (iY * NMAXX + iX + 1);
		  std::cout << " iX*NY+iY+1 = " << iX * NY + iY +
		    1 << std::endl;
		}
	    }
	}
      else
	{
	  ///---- project along X : sum over Y
	  for (int iY = minNY; iY < NY; iY++)
	    {
	      binsToSelect.clear ();
	      for (int iX = minNX; iX < NX; iX++)
		{
		  binsToSelect.push_back (iX * NMAXY + iY + 1);
		  std::cout << " iX*NY+iY+1 = " << iX * NY + iY +
		    1 << std::endl;
		}
	    }
	}
      ///==== signal (begin) ====
      int WHEREAMI = 0;
      std::cout << "I'm here: " << WHEREAMI << std::endl;
      WHEREAMI++;

      int GammaOverGammaSM = 50;
      TString nameSignal = Form ("H off x%d", GammaOverGammaSM);
      TString nameSignalOn = Form ("H on x%d", GammaOverGammaSM);



//    name = Form("%sqqH%s",cutNameBefore.Data(),cutNameAfter.Data());
//    vectTHSig.push_back ( FilterBins(binsToSelect, (TH1F*) f[iFile]->Get(name)) );
//    vectNameSig.push_back ("H m_{H}=125");
//    vectColourSig.push_back(6);
//    vectSystSig.push_back(0.00);
//    vectScaleSig.push_back(1.0000);
// //    vectNormalizationSig.push_back(2.565);
//    std::cout << "I'm here: " << WHEREAMI << std::endl; WHEREAMI++;

      name = Form ("%sggH%s", cutNameBefore.Data (), cutNameAfter.Data ());
      vectTHSig.
	push_back (sumOver( (TH1F *) f[iFile]->Get (name), (what == 1), NX, NY));
      //vectNameSig.push_back (nameSignalOn.Data());
      vectNameSig.push_back ("H m_{H}=125 ");
      vectColourSig.push_back (1);
      vectSystSig.push_back (0.00);
      vectScaleSig.push_back (1.0000);
      std::cout << "I'm here: " << WHEREAMI << std::endl;
      WHEREAMI++;

      ///==== signal (end)  ====



      ///==== background (begin)  ====


      name = Form ("%sVV%s", cutNameBefore.Data (), cutNameAfter.Data ());
      vectTHBkg.
	push_back (sumOver( (TH1F *) f[iFile]->Get (name), (what == 1), NX, NY));
      vectNameBkg.push_back ("WZ/ZZ/VVV");
      vectColourBkg.push_back (858);
      vectSystBkg.push_back (0.00);
      vectScaleBkg.push_back (1.0000);
      vectNormalizationBkg.push_back (0.281);
      std::cout << "I'm here: " << WHEREAMI << std::endl;
      WHEREAMI++;

      name = Form ("%sVVV%s", cutNameBefore.Data (), cutNameAfter.Data ());
      vectTHBkg.
	push_back (sumOver( (TH1F *) f[iFile]->Get (name), (what == 1), NX, NY));
      vectNameBkg.push_back ("WZ/ZZ/VVV");
      vectColourBkg.push_back (858);
      vectSystBkg.push_back (0.00);
      vectScaleBkg.push_back (1.0000);
      vectNormalizationBkg.push_back (0.281);
      std::cout << "I'm here: " << WHEREAMI << std::endl;
      WHEREAMI++;

      name = Form ("%sWJet%s", cutNameBefore.Data (), cutNameAfter.Data ());
      vectTHBkg.
	push_back (sumOver( (TH1F *) f[iFile]->Get (name), (what == 1), NX, NY));
      vectNameBkg.push_back ("W+jets");
      vectColourBkg.push_back (921);
      vectSystBkg.push_back (0.00);
      vectScaleBkg.push_back (1.0000);
      vectNormalizationBkg.push_back (0.667);
      std::cout << "I'm here: " << WHEREAMI << std::endl;
      WHEREAMI++;

      name = Form ("%sVg%s", cutNameBefore.Data (), cutNameAfter.Data ());
      vectTHBkg.
	push_back (sumOver( (TH1F *) f[iFile]->Get (name), (what == 1), NX, NY));
      vectNameBkg.push_back ("V+#gamma/V+#gamma*");
      vectColourBkg.push_back (616 + 1);
      vectSystBkg.push_back (0.00);
      vectScaleBkg.push_back (1.0000);
      vectNormalizationBkg.push_back (1.000);
      std::cout << "I'm here: " << WHEREAMI << std::endl;
      WHEREAMI++;

      name = Form ("%sVgS%s", cutNameBefore.Data (), cutNameAfter.Data ());
      if (f[iFile]->GetListOfKeys ()->Contains (name))
	{
	  vectTHBkg.
	    push_back (sumOver( (TH1F *) f[iFile]->Get (name), (what == 1), NX, NY));
	  vectNameBkg.push_back ("V+#gamma/V+#gamma*");
	  vectColourBkg.push_back (616 + 2);
	  vectSystBkg.push_back (0.00);
	  vectScaleBkg.push_back (1.0000);
	  vectNormalizationBkg.push_back (1.000);
          std::cout << "I'm here loop: " << WHEREAMI << std::endl;
          WHEREAMI++;
	}

      name = Form ("%sTop%s", cutNameBefore.Data (), cutNameAfter.Data ());
      vectTHBkg.
	push_back (sumOver( (TH1F *) f[iFile]->Get (name), (what == 1), NX, NY));
      vectNameBkg.push_back ("Top");
      vectColourBkg.push_back (400);
      vectSystBkg.push_back (0.10);
      vectScaleBkg.push_back (1.0000);
      vectNormalizationBkg.push_back (5.654);
      std::cout << "I'm here: " << WHEREAMI << std::endl;
      WHEREAMI++;


      name = Form ("%sDYTT%s", cutNameBefore.Data (), cutNameAfter.Data ());
      vectTHBkg.
	push_back (sumOver( (TH1F *) f[iFile]->Get (name), (what == 1), NX, NY));
      vectNameBkg.push_back ("DYTT");
      vectColourBkg.push_back (418);
      vectSystBkg.push_back (0.00);
      vectScaleBkg.push_back (1.0000);
      vectNormalizationBkg.push_back (0.377);
      std::cout << "I'm here: " << WHEREAMI << std::endl;
      WHEREAMI++;

      name = Form ("%sWW%s", cutNameBefore.Data (), cutNameAfter.Data ());
      vectTHBkg.
	push_back (sumOver( (TH1F *) f[iFile]->Get (name), (what == 1), NX, NY));
      vectNameBkg.push_back ("WW");
      vectColourBkg.push_back (851);
      vectSystBkg.push_back (0.00);
      vectScaleBkg.push_back (1.0000);
      vectNormalizationBkg.push_back (2.256);
      std::cout << "I'm here: " << WHEREAMI << std::endl;
      WHEREAMI++;

//    name = Form("%sggWW%s",cutNameBefore.Data(),cutNameAfter.Data());
//    if (f[iFile]->GetListOfKeys()->Contains(name)) {
//     vectTHBkg.push_back ( FilterBins(binsToSelect, (TH1F*) f[iFile]->Get(name)) );
//     vectNameBkg.push_back ("WW");
//     vectColourBkg.push_back(853);
//     vectSystBkg.push_back(0.00);
//     vectScaleBkg.push_back(1.0000);
//     vectNormalizationBkg.push_back(2.256);
//    }





      ///==== background (end)  ====



      ///==== data (begin)  ====

      if (doSignalInjection == false)
	{
	  name =
	    Form ("%sData%s", cutNameBefore.Data (), cutNameAfter.Data ());
	  hs->
	    setDataHist (FilterBins
			 (binsToSelect, (TH1F *) f[iFile]->Get (name)));
	}
      else
	{
	  TH1F *tempData = (TH1F *) vectTHBkg.at (0)->Clone ();
	  for (int iBkg = 1; iBkg < vectTHBkg.size (); iBkg++)
	    {
	      tempData->Add ((TH1F *) vectTHBkg.at (iBkg)->Clone ());
	    }
	  for (int iSig = 0; iSig < vectTHSig.size (); iSig++)
	    {
	      tempData->Add ((TH1F *) vectTHSig.at (iSig)->Clone ());
	    }
	  hs->setDataHist (tempData);
	}

      ///==== data (end)  ====


      hs->setBlindBinSx (100);
//    hs->setBlindBinSx(0);
//    hs->setBlindBinDx(10);
      hs->setBlindBinDx (0);

      hs->setCutSx (-999, ">");
      hs->setCutDx (-999, "<");

      name = Form ("%s%smodel_errs", folder.Data (), nameChannel.Data ());
      std::cout << " name = " << name.Data () << std::endl;

      hs->
	set_ErrorBand (*(FilterBins
                                 (binsToSelect, (TGraphAsymmErrors *) f[iFile]->Get (name))));

    }

  std::cout << " * end iFile * " << std::endl;

  hs->set_vectTHBkg (vectTHBkg);
  hs->set_vectNameBkg (vectNameBkg);
  hs->set_vectColourBkg (vectColourBkg);
//  if (which == 4) hs->set_vectSystBkg   (vectSystBkg);    
  hs->set_vectScaleBkg (vectScaleBkg);

  hs->set_vectTHSig (vectTHSig);
  hs->set_vectNameSig (vectNameSig);
  hs->set_vectColourSig (vectColourSig);
  hs->set_vectScaleSig (vectScaleSig);



//  hs->addWeight(NY-minNY); //---- add S/(S+B) weight ---> used only for propaganda plot and data-background
  hs->addWeight1D (NY - minNY);	//---- add S/(S+B) weight ---> used only for propaganda plot and data-background


  double *vedges;
  double
    vedges_mt[] =
    { 60, 70, 80, 90, 100, 110, 120, 140, 160, 180, 200, 220, 240, 260, 280 };
  double vedges_mll[] = { 12, 30, 45, 60, 75, 100, 125, 150, 175, 200 };

  vedges = vedges_mt;
  if (what == 1)
    vedges = vedges_mll;	//mll

  //double vedges[] = { 12, 30, 45, 60, 75, 100, 125, 150, 175, 200 }; 

  std::cout << "  vedges + sizeof(vedges) / sizeof(double) = " << vedges +
    sizeof (vedges) / sizeof (double) << std::endl;


  std::vector < double >vEdges ; //(vedges,
				//vedges + sizeof (vedges) / sizeof (double));

  int nbins = NMAXX;
  if (what == 1)
    nbins = NMAXY;
  for (unsigned int o = 0 ; o < nbins+1; ++o ){
    vEdges.push_back(*(vedges+o));
    std::cout << o << " " << vEdges[o] << std::endl;
  }
  hs->set_vectEdges (vEdges);

  hs->set_divide (0);		//---- if 1 then divide by bin width
  hs->prepare ();

  std::cout << "prepared" << std::endl;
  hs->mergeSamples ();		//---- merge trees with the same name! ---- to be called after "prepare" !
  std::cout << "merged" << std::endl;

  hs->set_addSignalOnBackground (1);	// 1 = signal over background , 0 = signal on its own

  hs->set_mergeSignal (0);	// 1 = merge signal in 1 bin, 0 = let different signals as it is

  hs->setMass (125);

// hs->set_plotSigAlone(true); //---- false = "do not plot signal not-stacked to the background


  hs->set_doLabelNumber (false);

  ///==== draw ====

  TCanvas *c1bis = new TCanvas ("bkgSub", "bkgSub", 500, 500);

  hs->setUnits ("GeV");

  std::cout << "About to draw" << std::endl;
  //----  canvas, rebin, div, shadow, background subtracted canvas ----
  hs->Draw (c1, 1, true, true, c1bis);
  std::cout << "Drawn" << std::endl;  

  const char *namefile = "mT";
  if (what == 1)
    {
      namefile = "mll";
    }

  c1->Print (Form ("../mll-mth_8TeV_%s/%s.pdf", channel, namefile));
  c1->Print (Form ("../mll-mth_8TeV_%s/%s.png", channel, namefile));
  c1->Print (Form ("../mll-mth_8TeV_%s/%s.eps", channel, namefile));

  c1bis->Print (Form ("../mll-mth_8TeV_%s/bkgSub_%s.pdf", channel, namefile));
  c1bis->Print (Form ("../mll-mth_8TeV_%s/bkgSub_%s.png", channel, namefile));
  c1bis->Print (Form ("../mll-mth_8TeV_%s/bkgSub_%s.eps", channel, namefile));

}
