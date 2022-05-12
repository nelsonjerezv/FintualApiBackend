import requests

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"name": 'nelson1', "views": 51, "likes": 109},
#     {"name": 'nelson2', "views": 52, "likes": 108},
#     {"name": 'nelson3', "views": 53, "likes": 107},
#     {"name": 'nelson4', "views": 54, "likes": 106},
#     {"name": 'nelson5', "views": 55, "likes": 105},
#     {"name": 'nelson6', "views": 56, "likes": 104},
#     {"name": 'nelson7', "views": 57, "likes": 103},
#     {"name": 'nelson8', "views": 58, "likes": 102},
#     {"name": 'nelson9', "views": 59, "likes": 101}
# ]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())


# response = requests.put(BASE + "video/1", {"name": 'nelson', "views": 5, "likes": 10})
# print(response.json())
# input()
# response = requests.put(
#     BASE + "video/2", {"name": 'jack', "views": 5, "likes": 10})
# print(response.json())



# input()
# response = requests.get(
#     BASE + "video/1")
# print(response.json())

# input()
# response = requests.patch(
#     BASE + "video/1", {"likes": 10})
# print(response.json())

# response = requests.patch(
#     BASE + "video/1", {"likes": 102})
# print(response.json())

# input()
# response = requests.delete(
#     BASE + "video/6")
# print(response)

# input()
# response = requests.delete(
#     BASE + "video/2")
# print(response)

# conceptual_assets
# response = requests.get(
#     BASE + "conceptual_assets")
# print(response.json())
# input()

# conceptual_asset's real assets (empty)
# response = requests.get(
    # BASE + "conceptual_assets/9542/real_assets")
# print(response.json())
# input()

# conceptual_asset's real assets (not empty)
# response = requests.get(
    # BASE + "conceptual_assets/1755/real_assets")
# print(response.json())
# input()

# real assets change values in range
response = requests.get(
    BASE + "real_assets/175/days", {"start_date": "2022-01-30", "end_date": "2022-03-30"})
print(response)
# input()

# real assets change values in range for missing data
response = requests.get(
    BASE + "real_assets/8799/days", {"start_date": "10/04/2022", "end_date": "14/04/2022"})
print(response)

# real asset
# response = requests.get(
#     BASE + "real_assets/175")
# print(response.json())
# input()

