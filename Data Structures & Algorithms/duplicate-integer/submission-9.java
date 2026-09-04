class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> hs = new HashSet<>();
        for (int h: nums) {
            if (hs.contains(h)) {
                return true;
            }
            else {
                hs.add(h);
            }
        } 
        return false;
    }
}