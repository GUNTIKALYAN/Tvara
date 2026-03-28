# Tvara Assignment

#### This repo contains implementations for the three required tasks:

 - Task A — DSA: Linked List Cycle II

 - Task B — Gemini API Integration: Simple chatbot API

 - Task C — Vectorization with HuggingFace + FAISS similarity search


 # Task A - Linked List Cycle II
 - Approach: Used Floyd’s Cycle Detection Algorithm (Tortoise and Hare).

 - Logic:
    - Use two pointers (slow and fast)
    - If they meet → cycle exists
    - Reset one pointer to head
    - Move both one step → meeting point = cycle start

Time Complexity: O(n)
Space Complexity: O(1)

Edge Cases Considered:

No cycle
Single node
Cycle at head

 # Task B  - Llama API Integration: Simple chatbot API
 - Design Choices: 
     - Used lightweight API (FastAPI)
     - Clean separation of request/response logic
     - Environment variables for API key security


 # Task C - Vector Search (HuggingFace + FAISS)
  - Document = attention mechanism pdf
  - Model Used: intfloat/e5-small-v2
  - Pipeline:
      - Load embedding model via sentence-transformers
      - Convert text into vector embeddings
      - Store embeddings in FAISS index
      - Perform similarity search
      
  - Process:
  Input: Query string
  Output: Most relevant sentence(s)
