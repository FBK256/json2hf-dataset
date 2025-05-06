# 📝 json2hf-dataset

Convert a QA-style **JSON** corpus into a Hugging Face `datasets.Dataset` object
ready for 🤗 Trainer fine-tuning — in a single Python script.

---

## 📖 Overview / 概要
`json2datasetobject.py` は、次のような `question` / `answer` ペアの
JSON ファイルを読み込み、`datasets.Dataset` へ変換して出力します。  
そのまま `Trainer` / `DataLoader` に渡せるため、前処理コードを大幅に削減できます。

```json
[
  { "question": "富士山の標高は？", "answer": "3,776 m" },
  { "question": "日本の首都は？", "answer": "東京" }
]
