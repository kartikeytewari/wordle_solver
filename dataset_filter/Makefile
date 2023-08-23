token_list:
	rg -Iz "^[a-zA-Z]{5}_[A-Z]+\t" ../dataset/n-gram/raw/1-000*-of-00024.gz > ../dataset/n-gram/metadata/token.txt
	python3 recent_freq.py > ../dataset/n-gram/metadata/recent_freq.txt
	join -a 1 ../dataset/wordle/dictionary.txt ../dataset/n-gram/metadata/recent_freq.txt > ../dataset/n-gram/metadata/recent_freq_dictionary.txt
	python3 clean.py > ../dataset/n-gram/metadata/recent_freq_dictionary_clean.txt
