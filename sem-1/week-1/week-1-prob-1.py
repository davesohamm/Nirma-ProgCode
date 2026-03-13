# 25MCD005 SOHAM DAVE WEEK-1 PROBLEM-1 "PLAYLIST"
def find_longest_unique_sequence(total_songs, playlist):
    unique_songs = set()
    start = 0
    longest = 0

    for end in range(total_songs):
        while playlist[end] in unique_songs:
            unique_songs.remove(playlist[start])
            start += 1
        unique_songs.add(playlist[end])
        longest = max(longest, end - start + 1)

    return longest

num_songs = int(input())
song_ids = list(map(int, input().split()))
print(find_longest_unique_sequence(num_songs, song_ids))
