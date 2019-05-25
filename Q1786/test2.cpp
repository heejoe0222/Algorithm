#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
using namespace std;

vector<int> get_pi(const string& str) {
	int m = str.size(),j=0;
	vector<int> pi(m,0);
	for (int i = 1; i < m; i++) {
		while (j > 0 && str[i] != str[j])
			j = pi[j - 1];
		if (str[i] == str[j])
			pi[i] = ++j;
	}
	return pi;
}

vector<int> kmp(const string& str, const string& substr){
	vector<int> answer;
	vector<int> pi = get_pi(substr);
	int n=str.size(),m=substr.size();
	int j=0;
	for(int i=0;i<n;i++){
			while(j>0 && str[i]!=substr[j])
			    j=pi[j-1];
			if(str[i]==substr[j]){
				if(j==m-1){
					answer.push_back(i-m+1);
					j=pi[j];
				}else{
					j++;
				}
			}
	}
	return answer;
}

int main() {
	string str,substr;
	vector<int> answer;

	getline(cin, str);
	getline(cin, substr);

	answer = kmp(str,substr);
	cout << answer.size() <<endl;

	for (vector<int>::size_type i = 0; i < answer.size(); ++i)
		cout << answer[i]+1 << " ";

	return 0;
}
