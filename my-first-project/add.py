def bubble_sort(arr):
    """
    冒泡排序算法
    
    参数:
    arr -- 需要排序的列表
    
    返回:
    排序后的列表
    """
    n = len(arr)
    
    # 遍历所有数组元素
    for i in range(n):
        
        # 标记此轮是否发生交换，用于优化
        swapped = False
        
        # 最后i个元素已经就位，不需要再比较
        for j in range(0, n-i-1):
            
            # 如果当前元素大于下一个元素，则交换
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # 如果此轮没有发生交换，说明数组已经有序
        if not swapped:
            break
    
    return arr

# 测试代码
if __name__ == "__main__":
    # 测试用例
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)
    
    sorted_array = bubble_sort(test_array.copy())
    print("排序后数组:", sorted_array)
    
    # 更多测试用例
    test_cases = [
        [5, 2, 8, 6, 1, 9, 4],
        [1, 2, 3, 4, 5],  # 已排序
        [5, 4, 3, 2, 1],  # 逆序
        [42],  # 单个元素
        []     # 空数组
    ]
    
    print("\n更多测试用例:")
    for i, test_case in enumerate(test_cases):
        print(f"测试 {i+1}: {test_case} -> {bubble_sort(test_case.copy())}")