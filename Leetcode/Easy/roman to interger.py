class Solution:
	# Function to remove 2 chars by given index of the first char
	def del_substr(i, s):
		return s[:i] + s[i+2:]
	
	def romanToInt(self, s: str) -> int:
		# Roman numeral mapping
		roman = {'I': 1,
				'V': 5,
				'X': 10,
				'L': 50,
				'C': 100,
				'D': 500,
				'M': 1000}        
		# Special cases mapping				
		special = {'IV': 4,
					'IX': 9,
					'XL': 40,
					'XC': 90,
					'CD': 400,
					'CM': 900}
		# Output sum
		output = 0
		# Loop through s to look for special cases
		for i in range(len(s)):
			for i in range(len(s)):
				substr = s[i:i+2]
				if substr in special:
					# Add special cases to output
					output += special[substr]
					# Remove found numbers from s
					s = Solution.del_substr(i, s)
					break
		# Loop through the remaining s and add found numbers to output
		for i in range(len(s)):
			if s[i] in roman:
				output += roman[s[i]]
						
		return output
