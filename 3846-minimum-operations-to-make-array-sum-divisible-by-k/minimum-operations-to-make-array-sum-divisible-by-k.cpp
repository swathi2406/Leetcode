
#include <vector>
#include <numeric>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        int total_sum = std::accumulate(nums.begin(), nums.end(), 0);
        return total_sum % k;
    }
};
