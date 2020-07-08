class Solution:
    def decodeString(self, s: str) -> str:
        curr_string = ''
        curr_num = 0
        stack = []
        
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                stack.append(curr_num)
                stack.append(curr_string)
                curr_string = ''
                curr_num = 0
            elif char == ']':
                prev_string = stack.pop()
                prev_num = stack.pop()
                curr_string = prev_string + curr_string * prev_num
            else:
                curr_string += char
    
        return curr_string