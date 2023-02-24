package Easy;

public class BestTimeToBuySell {

    public int maxProfit(int[] prices){
        int min_so_far = prices[0];
        int diff = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < min_so_far)
                min_so_far = prices[i];
            else
                diff = Math.max(prices[i] - min_so_far, diff);
        }
        return diff;

    }


}
