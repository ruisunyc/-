class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        #��ǰ���ֵ�뵱ǰλ����Լ�����ʱ��
        cur = light[0]
        ans = 0
        for i,num in enumerate(light):
            cur = max(cur,num)
            if cur==i+1:
                ans+=1
        return ans