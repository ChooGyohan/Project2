import urllib.request

url = "https://www.theguardian.com/us-news/2016/nov/09/hillary-clinton-concession-speech-full-transcript"

f = urllib.request.urlopen(url)
data = f.read().decode('utf-8')

begin = data.find("Thank you. Thank you all. Thank you.")
end = data.find("May God bless you and may God bless the United States of America.")
end += len("May God bless you and may God bless the United States of America.")

print("total = ",len(data))
print("begin = ",begin)
print("length = ",end - begin)

speech = data[begin:end]

speech = speech.replace('</div>'," ")
speech = speech.replace('<div'," ")
speech = speech.replace('–'," ")
speech = speech.replace('<p>'," ")
speech = speech.replace('.'," ")
speech = speech.replace(','," ")
speech = speech.replace('</p>'," ")
speech = speech.replace(','," ")
speech = speech.replace('href="https://www'," ")
speech = speech.replace('<br>'," ")
speech = speech.replace('888-6'," ")
speech = speech.replace('637-'," ")

speech = speech.split()


analyze = {}
for word in speech:
    analyze[word] = analyze.get(word, 0) + 1

flist = sorted(analyze.items(), key=lambda kv: kv[1], reverse=True)
print()
print("number of words is ", len(flist))
print()

cnt = 0
for k, v in flist:
    print(k, v)
    if cnt > 100: break
    cnt += 1
