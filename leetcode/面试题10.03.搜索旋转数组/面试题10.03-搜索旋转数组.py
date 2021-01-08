class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:                                         # ѭ����������left==right
            mid = (left + right) >> 1
            if nums[left] < nums[mid]:                              # �����ֵС����ֵ��˵������������� 
                if nums[left] <= target and target <= nums[mid]:    # ���Ŀ������ߵ����������У��ұ߽��ƶ���mid
                    right = mid
                else:                                               # ����Ŀ�����Ұ�ߣ���߽��ƶ���mid+1
                    left = mid + 1
            elif nums[left] > nums[mid]:                            # �����ֵ������ֵ��˵����߲��������Ұ������
                if nums[left] <= target or target <= nums[mid]:     # ���Ŀ������ߣ��ұ߽��ƶ���mid
                    right = mid
                else:                                               # ����Ŀ�����Ұ�ߵ����������У���߽��ƶ���mid+1
                    left = mid + 1
            elif nums[left] == nums[mid]:                           # �����ֵ������ֵ���������Ѿ��ҵ���Ŀ�꣬Ҳ�������������ظ�ֵ
                if nums[left] != target:                            # �����ֵ������Ŀ�꣬˵����û�ҵ�����Ҫ��һ�����ظ�ֵ
                    left += 1                                        
                else:                                               # �����ֵ����Ŀ�꣬˵���Ѿ��ҵ�����ߵ�Ŀ��ֵ
                    right = left                                    # ���ұ߽��ƶ���left��ѭ������
        return left if nums[left] == target else -1