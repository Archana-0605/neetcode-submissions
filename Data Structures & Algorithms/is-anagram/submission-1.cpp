class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> count(26,0);
        for (char c:s){
            count[c-'a']++;
        }
        for (char d:t){
            count[d-'a']--;
        }
        for (int i = 0; i<count.size();i++){
            if (count[i]!=0){
                return false;
            }
        }
        return true;
        
    }
};
