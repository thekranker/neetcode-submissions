class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        
        // create the hash set
        unordered_set<int> set;

        // loop through the arr
        for (int i = 0; i < nums.size(); i++) {
            if (set.count(nums[i]) == 1) {
                return true;
            }
            else {
                set.insert(nums[i]);
            }
        }
        // no duplicates
        return false;
    }
};