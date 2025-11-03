def has_duplicates(lst):
    """
    检查列表中是否有重复元素
    参数: lst - 任意列表
    返回: bool - 如果有重复元素返回 True，否则返回 False
    """
    # 学生实现代码区域
    # 提示：可以使用集合或循环比较
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

# 主程序 - 测试函数
if __name__ == "__main__":
    # 学生需要提供测试用例
    test_cases = [
        [1, 2, 3],          # 无重复
        [1, 2, 2],          # 有重复
        ["a", "b", "a"],    # 字符串重复
        []                   # 空列表
    ]
    
    # 测试每个用例
    for test in test_cases:
        result = has_duplicates(test)
        if result:
            print(f"列表 {test} 有重复元素")
        else:
            print(f"列表 {test} 没有重复元素")
