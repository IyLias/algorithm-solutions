nclude <iostream>
#include <stdio.h>
#include <algorithm>

#define MAX_VALUE 1000*1000+1

using namespace std;

int dp[1001][3];
int rgb[1001][3];

int main(){

	 int N;
	 scanf("%d",&N);

	 for(int i=1;i<=N;i++)
	    scanf("%d %d %d",&rgb[i][0],&rgb[i][1],&rgb[i][2]);

	 int ans=MAX_VALUE;

	 for(int k=0;k<3;k++){
		        
 		for(int i=0;i<3;i++){
			if(i==k)
				dp[1][i] = rgb[1][k];
			else
				 dp[1][i] = MAX_VALUE;
		}

			     for(int i=2;i<=N;i++){
				             dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + rgb[i][0];
					             dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + rgb[i][1];
						             dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + rgb[i][2];
							         }

			         for(int i=0;i<3;i++){
					         if(i==k) continue;
						         ans = min(ans,dp[N][i]);
							     }

				  }


	      printf("%d\n",ans);

	       return 0;
}
