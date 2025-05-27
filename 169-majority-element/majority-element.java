class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;
        int i = 0;

        for (i = 0; i < nums.length; i++){
            if (count == 0){
                candidate = nums[i];
            }

                if (candidate == nums[i]){
                    count ++;
                }
                else{
                    count --;
                }

        }

        return candidate;
        
    }
}