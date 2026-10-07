import pandas as pd

df = pd.read_csv("day02_usage.csv")
chat = df["Chat"].to_numpy()
video = df["Video"].to_numpy()
study = df["Study"].to_numpy()
games = df["Games"].to_numpy()


print(chat.sum(),video.sum(),study.sum(),games.sum())
print((chat.mean()).round(1),(video.mean()).round(1),(study.mean()).round(1),(games.mean()).round(1))

dif = study - games
df["diffsg"] = dif
# print(df)
print(df["diffsg"].idxmax()+1)
print(df["diffsg"].idxmin()+1)

maxoe = df[["Chat","Video","Study","Games"]].idxmax(axis=1)
print(maxoe)

total = chat + video + study + games
c = (chat*100/total)
v = video*100/total
s = study*100/total
g = games*100/total

print(f"total:{total} \n chat app contribution:{chat.round(3)} \n video : {video.round(3)}  \n study: {study.round(3)} \n games: {games.round(3)}")

dframe = pd.DataFrame(
    {"chat":c,"study":s,"video":v,"games":g}
)

print(dframe.head())

