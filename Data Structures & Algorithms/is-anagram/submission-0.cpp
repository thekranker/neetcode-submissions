class Solution {
public:
    bool isAnagram(string s, string t) {

        // base check - O(1)
        if (s.length() != t.length()) { return false; }

        // hash map creation
        unordered_map<char, int> freqS;
        unordered_map<char, int> freqT;

        // populate hash maps
        for (int i = 0; i < s.length() ; i++) {
            freqS[s[i]]++;
            freqT[t[i]]++;
        }
        // return
        return freqS == freqT;
    }
};
