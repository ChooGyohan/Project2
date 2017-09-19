fp = open("Obama speech.txt","r")
x = fp.read()
speech = []
speech = list(x.split())
fp.close()

analyze = {}
for word in speech:
    analyze[word] = analyze.get(word, 0) + 1

    # dictionary type에서 get 이 무슨 기능인지 검색으로 함 찾아보세요
    # dictionary type 에서 items() 가 무슨기능인지 검색!

flist = sorted(analyze.items(), key=lambda kv: kv[1], reverse=True)
print("number of words is ", len(flist))
# 이걸 이해하려고 하지말고, 변수만 잘 맞추어 주면 원하는게 나올겁니다. 하여간 이렇게 하면 되는군 선에서 실행시켜보, 본인 재산화 해두고 넘어가세요

cnt = 0
for k, v in flist:
    print(k, v)
    if cnt > 100: break
    cnt += 1
