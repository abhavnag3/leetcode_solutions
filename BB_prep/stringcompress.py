class Solution:
    def compress(self, chars: List[str]) -> int:
        
        
        
        i = j = 0
        count = 1
        while i < len(chars):
            count = 1
            while i < (len(chars) - 1) and chars[i] == chars[i + 1]:
                count += 1
                i += 1
            chars[j] = chars[i]
            j += 1
            if count > 1:
                for digit in str(count):
                    chars[j] = digit
                    j += 1
            
            i += 1