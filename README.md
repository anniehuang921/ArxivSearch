# ArxivSearch
Based on WebVoyger and RAG to do Arxiv search task.

## About task
Search for recent arXiv papers about AI applications in ESG from the Computer Science category.
```
"task_goal": "Find arXiv papers related to AI applied in Environmental, Social, and Governance (ESG) topics, limited to the Computer Science category, and submitted within the last 7 days. Extract and return the titles of the top 5 papers."
```
Task sample
```
"task_query":"Search the top 1 papers published in the past 3 months about greenhouse gas estimation using machine learning."
```
## Before using
1. Prepare external resource 'data/arXiv.pdf, data/CarbonInventory_AI_manual_updated.md'
2. Run to build such vector store
- python index_manual.py (for CarbonInventory_AI_manual_updated.md)
- python pdf_rag_annotated.py (for arXiv.pdf)
3. Before step2, notice to set your own openai-key in index_manual.py and pdf_rag_annotated.py

## Using 
Follow the WebVoyger using way, such like implement in terminal
```
python -u run.py --test_file ./data/tasks_test.jsonl --api_key sk-YOUROPENAIKEY --max_iter 15 --max_attached_imgs 3 --temperature 1 --fix_box_color --seed 42
```
### Initial Status
We follow this https://github.com/luff543/WebVoyager/tree/main repository to upgrade the assignment.
