#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;cin>>t;
    while(t--){
        int n;cin>>n;
        vector<long long>a(n),ev,od;
        for(int i=0;i<n;i++)cin>>a[i];
        for(auto x:a){
            if(x%2==0)ev.push_back(x);
            else od.push_back(x);
        }
        sort(ev.begin(),ev.end());
        sort(od.begin(),od.end());
        long long ans=0;
        vector<long long>b;
        for(auto x:ev)b.push_back(x);
        for(auto x:od)b.push_back(x);
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                long long g=__gcd(b[i],2LL*b[j]);
                if(g>1)ans++;
            }
        }
        cout<<ans<<"\n";
    }
}
