class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse = True) #����������ǴӺ���ǰ�жϿ�ʼʱ�䣬��������
        h = [] #���ȶ��У�Ҳ����˵��С����
        ans = 0
        for i in range(1,100001):  #ֱ�������ݷ�Χ����ȻҲ����ȡevents����ʱ������ֵ����Ҫ��дѭ������������
            while events and events[-1][0]==i: #���������
                heapq.heappush(h,events.pop()[1]) #����
            while h:
                cur = heapq.heappop(h)
                if cur>=i:
                    ans+=1 #һ��ֻ�ܲμ�һ��
                    break
            if not events and not h:break #��û����Դ��Ҳû�о�Դ��ֱ�ӽ���
        return ans