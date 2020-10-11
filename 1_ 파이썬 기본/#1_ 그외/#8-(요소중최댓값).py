nums = list(map(int, input("입력: ").rstrip().split(',')))
max_num = nums[0]
for num in nums:
    max_num = num if num > max_num else max_num        
print(max_num)

# 걍 max(nums) 로 해도 됨. (max() : 요소들 중에서 가장 큰 값 반환) 

"""
리스트의 요소중에서 가장 큰 값을 반환하는 코드,
이렇게 보다는 파이썬 내장함수인 max(), min()등을 활용하자.
"""
