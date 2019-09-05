'''BELOW IS THE CODE USED TO FIND THE MOST COMMON
   FIELDS THAT ARE USED
'''
import json


def load_json(filename):
    results = {}

    with open(filename, mode='r', encoding='utf-8') as jfile:
        data = json.load(jfile)
        total = len(data)
        for item in data:
            for field, value in item.items():
                if field not in results:
                    results.update({field: 0})
                else:
                    if value:
                        results[field] += 1
    return total, results


if __name__ == '__main__':
    total, results = load_json('minerals.json')
    results = sorted(results.items(), key=lambda kv: kv[1], reverse=True)
    print(f"Total Minerals: {total}")
    for key, value in results:
        print(f"{key}: {value}")