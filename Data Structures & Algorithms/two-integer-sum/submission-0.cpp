class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        // create the hash map
        unordered_map<int, int> map;

        // loop through the arr
        for (int i = 0; i < nums.size(); i++) {

            // check if target - nums[i] equals anything in the set
            if (map.count(target - nums[i]) == 1) {
                return {map[target - nums[i]], i};
            }
            // add the val, nums[i] to the set
            else {
                map[nums[i]] = i;
            }

        }

        // no solution found
        return {};
    }
};
