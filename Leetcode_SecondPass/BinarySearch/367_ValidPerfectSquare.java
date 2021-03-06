class Solution {
    // O(logn), O(1) 
    public static boolean isPerfectSquare(int num) {
        int low = 0;
        int high = num;
        while (low <= high){
            long mid = (high - low)/2 + low;
            if (mid * mid == num) return true;
            else if(mid * mid < num) low = (int) mid + 1;
            else high = (int) mid -1;
        }
        return false;
    }
}