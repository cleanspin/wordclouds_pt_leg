# wordclouds_pt_leg
This is a small project to create wordcloud visualizations from the 2019 legislative elections electoral programs of the main Portuguese political parties

Requirements:
pdf2txt
# https://github.com/euske/pdfminer/blob/master/tools/pdf2txt.py
wordcloud_cli
# https://github.com/amueller/word_cloud
python
# dude please...

Desc:
You can find the pdf with the electoral programs on the RAW folder, the txt output after using pdf2txt and splitting into words is on the TXT folder and the final png outputs I made in 1920*1080 are on the OUTPUTS folder.

I used some lists of stopwords I found somewhere (not entirely sure where) and added a few that were specific for this task, such as the parties acronyms and some words that had no contextual meaning, you can find the entire list of stopwords in stopwords.txt. My initial approach would be to remove the stopwords in python using the script nostops.py but since the wordcloud_cli made by amueller allows to pass the stopwords file as argument I decided todo that instead.

Don't forget to vote!
