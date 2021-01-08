class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('inf')
        profit1 = profit2 = 0
        for num in prices:
            buy1 = min(buy1,num) #�Ƚϵ�һ���������С�۸�
            profit1 = max(profit1,num-buy1) #��ȡ��һ�ν��׵��������
            buy2 = min(buy2,num-profit1) #��ȡ�ڶ����������С�۸��൱�ڼ�ȥ��һ�ε�����
            profit2 = max(profit2,num-buy2)#��ȡ�ڶ��ν��׵��������
        return profit2