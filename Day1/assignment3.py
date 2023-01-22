def isVowel(c) :

	return (c == 'a' or c == 'e' or c == 'i'
			or c == 'o' or c == 'u');


def countSubstringsUtil(s) :

	count = 0;
	mp = dict.fromkeys(s,0);

	n = len(s);

	start = 0;

	for i in range(n) :
		mp[s[i]] += 1;

		while (mp['a'] > 0 and mp['e'] > 0
			and mp['i'] > 0 and mp['o'] > 0
			and mp['u'] > 0) :
			count += n - i;
			mp[s[start]] -= 1;
			start += 1;

	return count;

def countSubstrings(s) :

	count = 0;
	temp = "";

	for i in range(len(s)) :


		if (isVowel(s[i])) :
			temp += s[i];

		else :

			if (len(temp) > 0) :
				count += countSubstringsUtil(temp);
			temp = "";

	if (len(temp) > 0) :
		count += countSubstringsUtil(temp);

	return count;
if __name__ == "__main__" :

	s = "aeioaexaeuiou";

	print(countSubstrings(s));


