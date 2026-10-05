# Week 6 Assignment — RAG Codelab + Your Own Documents

**Name:** Aanya Akiti

**Link to your completed Kaggle notebook:**[https://www.kaggle.com/code/akitiaanyareddy/day-2-document-q-a-with-rag](https://www.kaggle.com/code/akitiaanyareddy/day-2-document-q-a-with-rag)
---

## Part 1: Complete the RAG Codelab (30 pts)

Find the Day 2 codelab that builds a **RAG question-answering system over documents**. Copy it into your own Kaggle account and run it from top to bottom, with every cell executing successfully.

Record what the pipeline uses:

| | Value |
|---|---|
| Embedding model | text-embedding-004 |
| Where the embeddings are stored (vector store/database) | ChromaDB |
| Generation model | gemini-3.6-flash |
| Number of passages retrieved per query | 1 |

**In 2–3 sentences, describe what happens between the moment a question is asked and the moment an answer comes back:** 
When a question is asked, it is converted into an embedding and compared with the documents stored in ChromaDB. The most relevant passage is retrieved and added to the prompt, and Gemini uses the question and retrieved passage to generate the final answer.

---

## Part 2: Make It Yours (40 pts)

In your copy of the notebook, **replace the sample documents with 3–5 short documents of your own.** Documents related to your term project are recommended. Course materials, public documentation for a tool you use, or articles on a topic you know well also work. Avoid anything private or sensitive.

Keep the rest of the pipeline the same. Your notebook should show your documents, your questions, and the outputs.

**Your documents:**

| | Value |
|---|---|
| What the documents are | Lane Radar project information about its purpose, YOLOv8 person detection, workflow, and users/benefits |
| Number of documents | 4 |
| Why you chose them | I chose these documents because they cover the main parts of my Lane Radar project and provide enough information to test different types of questions. |

Write **5 test questions** and run each through the pipeline. Your set must include:

- **2 keyword questions** that use exact names, terms, numbers, or codes from your documents
- **2 paraphrase questions** that ask about something in your documents without using its wording
- **1 unanswerable question** whose answer is **not** in your documents

| # | Question (short) | Type | Retrieved the right passage? (Yes / No / N/A) | Generated answer (correct / partly / wrong / correctly declined) |
|---|---|---|---|---|
| 1 |What object detection model does Lane Radar use? | Keyword | Yes | correct |
| 2 | What type of input does Lane Radar process? | Keyword | Yes | correct |
| 3 | How does Lane Radar identify customers waiting at a checkout? | Paraphrase | Yes | correct |
| 4 | How can Lane Radar help people choose a checkout lane? | Paraphrase | Yes | correct |
| 5 | How much will Lane Radar cost to install in a supermarket? | Unanswerable | N/A | correctly declined |

**Pick one question where the result wasn't fully correct (or, if everything worked, the one that came closest to failing). Was the weak point retrieval or generation? How can you tell from the notebook's output?** 
Question 5 was the closest to failing because the answer was not present in the documents. Retrieval was N/A because there was no passage that could answer the question, while the model correctly declined to make up a price and said that the cost was not provided.
---

## Part 3: Reflection (30 pts, 250–350 words)

Answer all four:

- Huyen describes two families of retrievers: term-based and embedding-based. Which kind does the codelab use? Based on your keyword questions, where might the other kind have done better or worse?
- How did the pipeline handle your unanswerable question? What would happen in a real application if it handled that badly, and what would you change to fix it?
- The codelab was designed to work well on its own sample documents. What, if anything, got harder when you switched to yours?
- Your project evaluation plan is due next week with Milestone 1. Does your project need RAG? If so, what would the documents be, and if not, why not?

**Your reflection:**

The code lab uses an embedding-based retriever because the documents and questions are converted into embeddings and stored/searching using ChromaDB. Based on my keyword questions, this worked well because the system was able to find the correct passages containing terms such as YOLOv8 and camera/video input. A term-based retriever might work better when the exact words from the document are used, but it may perform worse when the question is worded differently.
For my unanswerable question, I asked how much Lane Radar would cost to install in a supermarket. The documents did not contain any information about installation cost, and the model correctly said that the cost was not provided instead of making up a price. In a real application, giving an incorrect price could mislead users and cause bad decisions. I would improve this by adding a clear rule that the system should only answer using information found in the retrieved documents and clearly say when the information is missing.
When I switched from the sample Googlecar documents to my Lane Radar documents, the main challenge was creating useful documents that contained enough information for different types of questions. I created four documents covering the project purpose, YOLOv8 detection, workflow, and users/benefits. After that, the retrieval and generation worked correctly for my test questions.
I think Lane Radar could benefit from RAG. It could use documents such as project specifications, supermarket checkout rules, system manuals, model information, and operating procedures. RAG would allow users or store managers to ask questions about the system and get answers based on the available project documents instead of relying only on the model's general knowledge.

---

