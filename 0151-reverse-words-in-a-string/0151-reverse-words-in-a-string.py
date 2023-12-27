class Solution:
    def reverseWords(self, s: str) -> str:
        stack_words = []
        curr_word = ""
        #add all words to stack
        for char in s:
            if char == " ":
                if curr_word:
                    stack_words.append(curr_word)
                curr_word = ""
                continue
            else:
                curr_word += char
        if curr_word:
            stack_words.append(curr_word)
        # return new sentence accounting for spaces
        new_sentence = ""
        print(stack_words)
        while stack_words:
            new_sentence += stack_words.pop()
            new_sentence += " "
        if new_sentence:
            new_sentence = new_sentence[:-1]
        return new_sentence