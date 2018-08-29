#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
  ll t,a[100000],b[100000],flag;
  while(1)
  {flag=1;
  cin>>t;
  if(t!=0)
  {
      for(ll i=1;i<=t;i++)
      {
          cin>>a[i];
          b[a[i]]=i;
      }
      for(ll i=1;i<=t;i++)
      {
          if(a[i]!=b[i])
          {
            cout<<"not ambiguous\n";
            flag=0;
          }
      }
      if(flag)
        cout<<"ambiguous\n";


  }
  else
    exit(0);
}
}
