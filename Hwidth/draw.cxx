void draw(TString var, TString cutAdditional = "1") {

 TFile *_file0 = TFile::Open("latino_1125_ggToH125toWWTo2LAndTau2Nu.root");
//  TFile *_file0 = TFile::Open("latinogg2vv_Hw1_SigOnPeak_8TeV.root");

 TFile *_file1 = TFile::Open("latinogg2vv_Hw1_SigOnPeak_8TeV_newTRG.root");
//  TFile *_file1 = TFile::Open("latino_1125_ggToH125toWWTo2LAndTau2Nu_newTRG.root");

 TTree* t0 = (TTree*) _file0->Get("latino");
 TTree* t1 = (TTree*) _file1->Get("latino");

 TString cut;

 cut = Form ("(%s) * ((!sameflav) * (mll>12 && pt1>20 && pt2>10 && ch1*ch2<0) * (baseW*puW*effW*triggW) * (trigger==1.) * (nextra==0) * (pfmet>20.) * (mpmet>20.) * (bveto_mu==1))",cutAdditional.Data());
 t0->SetLineColor(kRed);
 t0->Draw(var.Data(),cut.Data());
//  t0->Draw(var.Data(),"(mll>12 && pt1>20 && pt2>10 && ch1*ch2<0) * (baseW*puW) * (trigger==1.) * (nextra==0) * (pfmet>20.) * (mpmet>20.) * (bveto_mu==1)");
 float integral = 0;
 TH2F *htemp = (TH2F*)gPad->GetPrimitive("htemp");
 htemp->SetName("htemp0");
 integral = htemp->Integral();
 std::cout << " integral = " << integral << std::endl;


//  mll < 70 && mth>0 && ptll > 45 && (!sameflav) && njet==0 &&   pt1>20 && pt2>10 && (ch1*ch2)<0 && trigger==1. && pfmet>20. && mll>12 && (zveto==1||!sameflav) && mpmet>20. && bveto_mu==1 && nextra==0 && (bveto_ip==1 && nbjettche==0) && (njet==0 || njet==1 || (dphilljetjet<pi/180.*165. || !sameflav )  )  && ( !sameflav || ( (njet!=0 || dymva1>0.88) && (njet!=1 || dymva1>0.84) && ( njet==0 || njet==1 || (pfmet > 45.0)) ) )
   

 t1->SetLineColor(kBlue);
 cut = Form ("(%s) * ((((njet==0) * (13.3258/5.85323)) + ((njet==1) * (5.78547/1.40855)) + ((njet>=2) * (1.79911/0.195922))) * (!sameflav) * (mll>12 && pt1>20 && pt2>10 && ch1*ch2<0) * (baseW*puW*effW*triggW) * (trigger==1.) * (nextra==0) * (pfmet>20.) * (mpmet>20.) * (bveto_mu==1))",cutAdditional.Data());
//  cut = Form ("(%s) * (2.1 * (!sameflav) * (mll>12 && pt1>20 && pt2>10 && ch1*ch2<0) * (baseW*puW*effW*triggW) * (trigger==1.) * (nextra==0) * (pfmet>20.) * (mpmet>20.) * (bveto_mu==1))",cutAdditional.Data());
 
 t1->Draw(var.Data(),cut.Data(),"same");
//  t1->Draw(var.Data(),"(mll>12 && pt1>20 && pt2>10 && ch1*ch2<0) * (5.175 * baseW*puW*effW*triggW) * ( ((njet==0) * (1./0.976)) + ((njet==1) * (1./0.902)) + ((njet>=2) * (1./0.819)) ) * (trigger==1.) * (nextra==0) * (pfmet>20.) * (mpmet>20.) * (bveto_mu==1)","same");
 TH2F *htemp1 = (TH2F*)gPad->GetPrimitive("htemp");
 htemp1->SetName("htemp1");
 integral = htemp1->Integral();
 std::cout << " integral = " << integral << std::endl;
//  t1->Draw(var.Data(),"(mll>12 && pt1>20 && pt2>10 && ch1*ch2<0) * (2.1*baseW*puW*effW*triggW) * (trigger==1.) * (nextra==0) * (pfmet>20.) * (mpmet>20.) * (bveto_mu==1)","same");
// //  t1->Draw(var.Data(),"(mll>12 && pt1>20 && pt2>10 && ch1*ch2<0) * (2.1*baseW*puW) * (trigger==1.) * (nextra==0) * (pfmet>20.) * (mpmet>20.) * (bveto_mu==1)","same");
//  t1->Draw(var.Data(),"(mll>12 && pt1>20 && pt2>10 && ch1*ch2<0) * (baseW*puW) * (trigger==1.) * (nextra==0) * (pfmet>20.) * (mpmet>20.) * (bveto_mu==1)","same");
}


