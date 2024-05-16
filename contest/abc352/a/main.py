def solve(station_num, current_station, go_station, target_station):
  if current_station < go_station:
    for i in range(current_station, go_station + 1):
      if i == target_station:
        return 'Yes'
  elif current_station > go_station:
    for i in range(current_station, go_station - 1, -1):
      if i == target_station:
        return 'Yes'
  return 'No'

def main():
  N, X, Y, Z = map(int, input().split())
  print(solve(N, X, Y, Z))

if __name__ == "__main__":
  main()