/////////////////////////
//
///////////////////////////





class Solution {
    public int reverse(int x) {
        //int n;
        int rev = 0;
        int remainder;
        
        while( x != 0){
            remainder = x % 10;
            rev = rev * 10 + remainder;
            x = x/10;
        }
        return rev;
        
    }
}
