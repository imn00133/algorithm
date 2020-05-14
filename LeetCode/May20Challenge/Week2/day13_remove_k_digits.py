 # https://leetcode.com/problems/remove-k-digits/
# Solved Date: 20.05.14.


class Solution:
    def remove_k_digits(self, num: str, k: int) -> str:
        stack = []
        for letter in num:
            while k > 0 and stack and stack[-1] > letter:
                stack.pop()
                k -= 1
            stack.append(letter)
        while k:
            stack.pop()
            k -= 1
        if not stack:
            return '0'
        else:
            ans = ''.join(stack)
            return str(int(ans))

    def fast_remove_k_digits(self, num, k):
        stack = []
        for letter in num:
            while k > 0 and stack and stack[-1] > letter:
                stack.pop()
                k -= 1
            stack.append(letter)
        while k:
            stack.pop()
            k -= 1

        ans = ''.join(stack).lstrip('0')
        if not ans:
            ans = '0'
        return ans


def main():
    solution = Solution()
    num = "1234567890"
    k = 9
    print(solution.remove_k_digits(num, k))


if __name__ == '__main__':
    main()
