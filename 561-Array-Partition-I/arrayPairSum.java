class Solution {
    public int arrayPairSum(int[] nums) {
        boolean addToSum = true;
        int res = 0;
        Map<Integer, Integer> counts = countFrequencies(nums);
        
        for (int i = -10000; i < 10001; i++) {
            if (counts.containsKey(i)) {
                int count = counts.get(i);
                while (count > 0) {
                    if (addToSum) {
                        res += i;
                    }
                    count--;
                    addToSum = !addToSum;
                }
            }
        }
        return res;
    }
    
    public Map<Integer, Integer> countFrequencies(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }
        
        return counts;
    }
}