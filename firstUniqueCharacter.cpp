class Solution {
public:
    int firstUniqChar(string s) {
        map<char,int> map;
        
        // Hold every character and the amount of times it appears in the string
        // in the hashmap.
        for(int i = 0; i < s.length(); i++){
            map[s[i]]++;
        }
        
        // Check if any character appears only once (unique).
        for(int i = 0; i < s.length(); i++){
            if(map[s[i]] == 1){
                return i;
            }
        }
        
        return -1;
    }
};