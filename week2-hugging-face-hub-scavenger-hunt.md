# Week 2 Assignment: Hugging Face Hub Scavenger Hunt

**Graduate Extension Included**

## Overview

Same fields I walked through in Monday's demo: parameter count/size, architecture family, license, tokenizer/vocab size. Pick 3 models, record those fields, run a tokenizer comparison across languages, check context window against this week's reading, then write a short reflection tying it back to a real project decision.

*Same order I used in Monday's demo: parameter count/size near the top of the card, architecture family in the description, license in the metadata, tokenizer/vocab size in tokenizer_config.json (or just test the model directly in a tokenizer tool).*

## How to Submit

1. Fill out this file directly (replace the `_____` placeholders and bracketed instructions with your answers).
2. Commit this file to the same GitHub repo you created for Assignment 1, using this exact filename: `week2-tokenizer-model-comparison.md`.
3. Push your commit, then submit a link to the file as instructed for this course.

---

## Part 1: Choose 3 Models

1. Go to huggingface.co/models.
2. Pick 3 models that actually make a meaningful comparison — not three near-identical variants of the same model. At least 2 different organizations/families, ideally a mix of sizes (small under ~3B, mid-size, larger).
3. Pick based on your own interests. Got a project idea? Use models you'd actually consider for it.

## Part 2: Record Your Findings

Where to find each field, if you get stuck:
- **Parameter count / size** — near the top of the card, sometimes right in the model's name (e.g. "7B" = 7 billion parameters).
- **Architecture family** — in the description text, or config.json under "Files and Versions."
- **License** — shown as a tag near the top, and always in the YAML metadata block.
- **Tokenizer / vocab size** — check tokenizer_config.json or config.json under "Files and Versions" for vocab_size. Can't find it? Note "not published" — that's a useful observation on its own.

| Model | Link | Parameter count / size | Architecture family | License | Tokenizer / vocab size |
|---|---|---|---|---|---|
| Model 1: Meta-Llama-3-8B | https://huggingface.co/meta-llama/Meta-Llama-3-8B | 8B parameters | Llama 3 / Transformer decoder | Llama 3 Community License | 128,256 |
| Model 2: https://huggingface.co/google/gemma-7b | 7B parameters | Gemma / Transformer decoder | Gemma Terms of Use | 256,000 |
| Model 3: https://huggingface.co/Qwen/Qwen2.5-72B | 72.7B parameters | Qwen2 / Transformer decoder | Qwen License | 152,064 |

## Part 3: Tokenizer Comparison Exercise

Use a tokenizer tool that supports multiple model families (tiktokenizer.vercel.app works) and test all 3 models with the same three inputs:

- **Test sentence (use this exact sentence for all 3 models):** "I love learning about artificial intelligence."
- **Language A:** translate the test sentence into a Latin-script European language — Spanish, French, German, whatever. Same translation across all 3 models.
- **Language B:** translate it into a non-Latin-script language — Japanese, Arabic, Korean, Hindi, your call. Same translation across all 3 models.

| Model | Test sentence tokens | Language A used | Language A tokens | Language B used | Language B tokens |
|---|---|---|---|---|---|
| Model 1 | 7 | Spanish | 9 | Japanese | 12 |
| Model 2 | 8 | Spanish | 8 | Japanese | 9 |
| Model 3 | 7 | Spanish | 9 | Japanese | 11 |

## Part 4: Context Window Check

For each model, look up its context window — the max tokens it can handle in one request. Usually on the card or in the config file.

| Model | Context window (tokens) | Source (URL or where you found it) |
|---|---|---|
| Model 1 | 8,192 | Hugging Face model card – Meta-Llama-3-8B|
| Model 2 | 8,192 | Hugging Face model card – google/gemma-7b|
| Model 3 | 131,072 | Hugging Face model card – Qwen/Qwen2.5-72B|

**Now do the math for at least one model:** Chapter 2 is roughly 62 pages. Using ~500–600 words/page and ~0.75 words/token, estimate the total token count. Would the whole reading fit in that model's context window in one API call, with room left for a response? Show your work and your conclusion.

> [The estimated reading is about 45,467 tokens. Llama 3 8B and Gemma 7B have 8,192-token context windows, so the entire reading would not fit in one API call. Qwen2.5-72B has a 131,072-token context window, so the entire reading would fit, with approximately 85,605 tokens remaining for the response and other prompt content.]

## Part 5: Comparison Reflection (300–400 words)

Answer all four:

- What's the biggest difference between your 3 models — size, architecture, license, tokenizer, something else?
- If you had to pick one for a real project, which one and why? Don't just say "the biggest one" — factor in license restrictions and whether the project actually needs that much size.
- Would your pick change for a multilingual or cost-sensitive use case, based on what you found in Part 3? Why or why not?
- Would your pick change for a use case involving long documents (full reports, long transcripts), based on the context window math in Part 4? Why or why not?

> [-The biggest difference is the size and context window. Llama 3 has 8B parameters, Gemma has 7B, while Qwen has 72B and is much larger than the other two. They also tokenize languages diffirently.     -I would choose Qwen2.5-72B because it is more powerful and can handle more information. However, for a simple project, I would choose a smaller model because it would use fewer resources and could be cheaper.     -Yes, my choice could change. Part 3 showed that the models use different numbers of tokens for different languages. A model that uses fewer tokens could be more efficient and cheaper.   -Yes, I would choose Qwen2.5-72B for long documents. Its 131,072-token context window is much larger, while Llama 3 and Gemma have about 8,192 tokens. Therefore, Qwen can handle much longer documents in one request.]

## Part 6: Graduate Extension — Paper / Technical Report Analysis (300–400 words)

*Graduate students required.*

Pick one of your 3 models that has a linked paper or technical report on its card (most do). Read enough of it to answer:

- One real detail from the paper that's not on the model card — training data composition, a specific benchmark, a stated limitation, whatever you find.
- At least one limitation or tradeoff the authors admit to themselves.
- Your own take: does reading the paper change how much you'd trust this model for a real project vs. just reading the card? Why or why not?

> [Write your analysis here]

## Grading (10 pts total)

| Component | Undergrad | Grad |
|---|---|---|
| Findings table (Part 2, incl. tokenizer field) | 3 pts | 3 pts |
| Tokenizer comparison exercise (Part 3) | 2 pts | 1 pt |
| Context window check (Part 4) | 2 pts | 1 pt |
| Comparison reflection (Part 5) | 3 pts | 2 pts |
| Graduate extension (Part 6) | — | 3 pts |
| **Total** | **10 pts** | **10 pts** |

*If a model's license, architecture, or vocab size isn't clearly labeled, say so in your reflection — not every card is well documented, and noticing that is a useful takeaway on its own.*
