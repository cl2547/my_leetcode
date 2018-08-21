class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i = i+1){
            if (nums[i] >= target){
                return i;
            }
            if (i == nums.size()-1){
                return nums.size();
            }
        }
    }
};