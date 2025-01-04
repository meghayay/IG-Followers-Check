import re


def extract_usernames(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # matches usesrnames in the format of Instagram profile URLs
    pattern = r"https://www.instagram.com/([a-zA-Z0-9._]+)/?"

    # get list of matching usernames
    usernames_list = re.findall(pattern, content)

    return set(usernames_list)


followers = extract_usernames("followers.html")
following = extract_usernames("following.html")

not_following_back = following - followers

print("Users not following back:")
if not_following_back:
    for user in not_following_back:
        print(f" https://www.instagram.com/{user}")
else:
    print(" All users are following back.")
