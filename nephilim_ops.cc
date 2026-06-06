#include "tensorflow/lite/kernels/register.h"
#include <cmath>
constexpr float NU_P=0.17259029f,PHI=1.6180339887f,F0=15.965f;
TfLiteStatus BraidEval(TfLiteContext* c,TfLiteNode* n){
 auto* in=GetInput(c,n,0); auto* out=GetOutput(c,n,0);
 const float* i=GetTensorData<float>(in); float* o=GetTensorData<float>(out);
 float a=i[0],b=i[1],cc=i[2];
 float yz=fmodf(b*cc*PHI,1.0f), xz=fmodf(a*cc*PHI,1.0f);
 float ph=0.01f*sinf(2*M_PI*F0*0.0625f);
 o[0]=fmodf(xz+yz*NU_P+ph,1.0f); return kTfLiteOk;
}
