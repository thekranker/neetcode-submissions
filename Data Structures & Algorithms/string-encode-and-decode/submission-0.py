class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # 1. calculate the length of each string
        # 2. save the length of each string before each string followed by a separator (#)
        #    that the decoder can parse to know where the string starts
        # 3. return the encoded string with lengths attached

        # create the encoded string that will be added on to
        encoded_string = ""

        # Step 1: calculate the length of each string and append it to 'encoded_string'
        for string in strs:

            # Step 2: Save the length of each string followed by the separator-
            #         and append it to 'encoded_string'
            encode = str(len(string)) + "#" + string
            encoded_string += encode

        # return the encoded string
        return encoded_string


    # Expected Format to Decode - ["5#Hello5#World"]
    def decode(self, s: str) -> List[str]:

        # 1.) Parse the first number leading up to the '#'
        # 2.) Trim the string to the sections after the '#', and append the first parsed
        #     number characters to a String in 'decoded_strs'
        # 3.) Trim the string to leave only what's remaining past the decoded string
        # 4.) Repeat steps 1-3 for the rest of the string until it's fully decoded-
        #     (decoded when the remaining string is empty, base case to check)

        decoded_strs = []

        while (s):
            # Step 1
            index = s.find("#")
            stringLen = int(s[0 : index])

            # Step 2
            decoded_strs.append(s[index + 1 : index + stringLen + 1])

            # Step 3
            s = s[index + stringLen + 1:]
            

        
        return decoded_strs








