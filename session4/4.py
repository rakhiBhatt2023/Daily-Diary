followers={'john','jennnie','jim'}
fiona_followers={'kim','sia','joe'}
print("Followers:",followers,type(followers))

mutual_followers= followers.intersection(fiona_followers)
print(mutual_followers,type(mutual_followers),id(mutual_followers))



for name in followers:
    print(name)