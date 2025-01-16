#リスト
club_activities = [
    ["Mike","baseball"],
    ["Nancy","soccer"],
    ["John","music"],
    ["Tom","science"]
    ]
print(club_activities[3][1])
print("---------------")

#for文
print("問題１")
fruits = ["apple", "banana", "grape"]
for i in fruits:
    print(i)
print("問題２")
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i,end=" ")


print("問題３")
for i in range(1,11):
    print(i,end=" ")

print("問題4")
for i in range(1, 6, 2):
    print(i)

print("問題５")
shopping_list  = ["apple", "banana", "orange", "milk"]
for i,name  in enumerate(shopping_list,1):
    print(i,"番目に", name,"を書います")

print("問題6")
names = ["Alice", "Bob", "David"]
for i in names:
    print(i)
else :
    print("以上です。")

print("問題7")
numbers = [1, 2, 3, 4, 5]
for i in range(6, 11):
    numbers.append(i)
print(numbers)

print("問題8")
double_numbers = []
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    double_numbers.append(number * 2)
print(double_numbers)

print("問題9")
lower_char_list = ["a", "b", "c"]
upper_char_list = ["A", "B", "C"]
for a,A in zip(lower_char_list,upper_char_list):
    print(a + A)

print("問題10")
lower_char_list = ["a", "b", "c"]
upper_char_list = ["A", "B", "C"]

for i in range(len(lower_char_list)):
    print(lower_char_list[i] + upper_char_list[i])

#if part2
print("問題7")
number_list = [1, 2, 3, 4, 5, 6]
for number in number_list:
    if number % 2 == 0 and number % 3 == 0:
        print("2と3の公倍数です")
    elif number % 2 == 0:
        print("2の倍数です")
    elif number % 3 == 0:
        print("3の倍数です")
    else:
        print("それ以外です")

#辞書
print("問題6")
students = {
'student1': {'name': 'Alice', 'age': 18, 'grade': 'A'},
'student2': {'name': 'Bob', 'age': 17, 'grade': 'B'},
'student3': {'name': 'Charlie', 'age': 16, 'grade': 'C'}}
d = students["student2"]
print(d["name"],"の年齢は",d["age"],"歳です。")

print("早くできた人")
nested_dict = {
    "user": {
        "name": "Alice",
        "age": 30,
        "location": "Tokyo",
        "preferences": {
            "food": ["sushi", "ramen", "tempura"],
            "music": ["jazz", "classical", "pop"]
        }
    },
    "order": {
        "id": 12345,
        "items": [
            {"name": "Laptop", "price": 1000, "quantity": 1},
            {"name": "Mouse", "price": 50, "quantity": 2}
        ],
        "status": "shipped"
    },
    "company": {
        "name": "TechCorp",
        "address": {
            "street": "123 Main St",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94105"
        },
        "employees": [
            {"name": "Bob", "position": "Manager"},
            {"name": "Carol", "position": "Developer"}
        ]

    }

}
print(nested_dict["user"]["name"])
print(nested_dict["user"]["preferences"]["food"])
L = nested_dict["order"]["items"]
print(L[0]["name"])
print(nested_dict["company"]["address"]["city"])
print(nested_dict["company"]["employees"][1]["position"])
#関数
print("問題４")
emailA = "abcd@aaa.com"
emailB = "xyz.ne.jp"

def email_address_validation(email):
    if "@" in email:
        return True
    else:
        return False
    
print(email_address_validation(emailA))
print(email_address_validation(emailB))

print("問題５")

def list_generate(start,end):
    list1 = []
    for i in range(start,end):
        list1.append(i)
    return list1
print(list_generate(1,6))




