class Solution {
    public boolean isPalindrome(int x) {
        int add = 0;
        int reverse = 0;
        int number = x;
        
        if (x < 0)
            return false;
    
        while (number != 0){
            add = number % 10;
            reverse = reverse*10 + add;
            number = number/10;
        }
        
        if (reverse == x)
            return true;
        else
            return false;
        
        
        
    }
}