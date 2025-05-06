from transformers import Trainer, TrainingArguments
from datasets import Dataset
import json

#jsonファイルをロードする
with open(input("json file"), "r") as f:
    data = json.load(f)

# データをtransformersのトレーニングデータセットに変換する関数
def convert_to_dataset_format(data):
    dataset = {"question": [], "answer": []}
    for item in data:
        dataset["question"].append(item["question"])
        dataset["answer"].append(item["answer"])
    return dataset

# JSONデータをtransformersのトレーニングデータセット形式に変換
converted_data = convert_to_dataset_format(original_data)
print(converted_data)
# Datasetオブジェクトを作成
train_dataset = Dataset.from_dict(converted_data)
print(train_dataset)

print(type(train_dataset))

