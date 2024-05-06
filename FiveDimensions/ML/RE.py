import json
import re
import time


start_time = time.time()
with open('test.json', 'r') as f:
    data = json.load(f)

patterns = [
    r'Now answer this question: \" (.*?)\? (Yes|No)',
    r'Question: (.*?)\? (Yes|No)',
    r'Does the news (.*?)\? No or Yes\? (Yes|No)',
    r'Now answer this question: \"(.*?)\"\nOptions:\n- No\n- Yes (Yes|No)',
    r'Does the news headline (.*?)\?\nOptions:\n- Yes\n- No (Yes|No)',
    r'Does the news headline (.*?)\? Yes or No\? (Yes|No)',
    r'Question: (.*?)\nAnswer: (Yes|No)',
    r'what is the answer to the question \"(.*?)\" (Yes|No)',
    r'Does the news headline (.*?)\? (Yes|No)'
]

qa_pairs = []
for block in data:
    input_text = block['input']
    for pattern in patterns:
        matches = re.findall(pattern, input_text)
        if matches:
            count = 0
            for match in matches:
                qa_pairs.append({
                    'id': f"{block['id']}_{count}",
                    'Question': match[0],
                    'Answer': match[1]
                })
                count += 1
            break
with open('res.json', 'w') as f:
    json.dump(qa_pairs, f)
    print('Done!')


with open('res.json', 'r') as f:
    data = json.load(f)
id_set = set()
lis = []
for pair in data:
    id_ = pair['id']
    id_ = re.sub(r'_\d+$', '', id_)
    lis.append(id_)
    id_set.add(id_)

# 打印出去除_num后的id的数量
print(f"Unique id count: {len(id_set)}")
print(len(lis))

# 统计Answer为"Yes","No"的数量
count_no = sum(1 for item in data if item['Answer'] == 'No')
count_yes = sum(1 for item in data if item['Answer'] == 'Yes')

print(f'The number of "Yes" answers is {count_yes}.')
print(f'The number of "No" answers is {count_no}.')
end_time = time.time()
print(f'The code took {end_time - start_time} seconds to run.')
