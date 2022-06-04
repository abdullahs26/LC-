class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lfn = INT_MAX; // holds the lowest price so far
        int profit = 0; // holds final profit
        int profitToday = 0; // holds the profit if we were to sell today
        
        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] < lfn) {
                lfn = prices[i];   
            }            
            profitToday = prices[i] - lfn;
            
            if (profitToday > profit)
                profit = profitToday;
        }        
        return profit;
        
        
    }
};