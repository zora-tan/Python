import math


def bisection(
    function, a, b
):  # 二分法：[a,b]区间函数为0的点 finds where the function becomes 0 in [a,b] using bolzano

    start = a
    end = b
    if function(a) == 0:  # one of the a or b is a root for the function
        return a
    elif function(b) == 0:#elif=else if
        return b
    elif (
        function(a) * function(b) > 0
    ):  # if none of these are root and they are both positive or negative,
        # then his algorithm can't find the root
        print("couldn't find root in [a,b]")
        return
    else:
        mid = start + (end - start) / 2.0
        while abs(start - mid) > 10 ** -7:  # until we achieve precise equals to 10^-7
            if function(mid) == 0:
                return mid
            elif function(mid) * function(start) < 0:
                end = mid
            else:
                start = mid
            mid = start + (end - start) / 2.0
        return mid 
    #二分法找函数的根：需要找到端点函数值异号的区间，最后找到的区间长度=10^-7的时候停止，记区间中点为根


def f(x):
    return math.pow(x, 3) - 2 * x - 5


if __name__ == "__main__":
    print(bisection(f, 1, 1000))
