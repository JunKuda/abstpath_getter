import os

targets = []

# targets.txtにファイル名が一行ずつ書いてある
with open('./targets.txt', mode='r') as f:
  for line in f:
    line = line.rstrip()
    targets.append(line)

# カレントディレクトリ以下を全て探索
for root, dirs, files in os.walk('.'):
  for file in files:
    print(os.path.abspath(root) + '/' + file)
