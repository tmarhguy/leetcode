class Solution {
    public int singleNumber(int[] nums) {
        int result = 0; // Initialize result to 0
        for (int num : nums) { // Iterate through each number in the array
            result ^= num; // XOR each number with result
        }
        return result; // The remaining number is the single one
    }
}
