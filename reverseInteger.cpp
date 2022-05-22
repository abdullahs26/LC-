class Solution {
public:
    int reverse(int x) {
        int reverse = 0;
        int lastDig = 0;
        
        
        while (x != 0){
        if (reverse > INT_MAX/10 || (reverse == INT_MAX / 10 && lastDig > 7))
        return 0;
        if (reverse < INT_MIN/10 || (reverse == INT_MIN / 10 && lastDig < -8)) 
            return 0;
        lastDig = x % 10;
    
        
        reverse = (reverse*10) + lastDig;   
        x = x/10;    
        }
      
        return reverse;  
        }
    
    
};