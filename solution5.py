# Write code for algorithm 5 below

def palindrome(word):
    
    # base case
    if len(word) < 2:
        return True 
    
    else: 
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        else: 
            return False


sample_word = 'madam'
print(palindrome(sample_word))