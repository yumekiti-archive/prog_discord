import json

def main():
  with open('tmp.json', 'r') as f:
    data = json.load(f)

  print(data)

if __name__ == '__main__':
  main()