class Solution {
public:
	bool isAnagram(string s, string t) {
		
		map<char, int> s_map;
		map<char, int> t_map;
		
		for (int i = 0; i < s.size(); i++) {
			s_map[s[i]]++;
		}
		
		for (int i = 0; i < t.size(); i++) {
			t_map[t[i]]++;
		}
		
		if (s_map == t_map)
			return true;
		else
			return false;
				

	}
};