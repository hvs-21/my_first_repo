#include<bits/stdc++.h>
#define int long long
#define maxn 305
#define mm 1000000000
using namespace std;
int n,a[maxn],sum[maxn],dp[maxn][maxn];
signed main(){
    cin>>n;
    for(int i=1;i<=n;i++)cin>>a[i];
    for(int i=1;i<=n;i++)sum[i]+=sum[i-1]+a[i];
    memset(dp,ox3f,sizeof(dp));
    
}