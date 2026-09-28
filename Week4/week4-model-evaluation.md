# Week 4 Assignment: Evaluating and Comparing Two Models


## Part 1: Set Up Your Comparison

Choose two models that differ in a way worth comparing: two sizes, two providers, etc.

| | Model | Provider | Why you picked it |

| Model A |Qwen2.5-3B-Instruct | Qwen | A small instruction-tuned model chosen for fast testing and structured JSON output. |
| Model B | Phi-3.5-mini-Instruct | Microsoft | A similarly sized instruction-tuned model from a different provider, allowing a meaningful model-family comparison. |

```text
Classify the following customer support ticket.

Return ONLY valid JSON with exactly these three keys:
{
  "category": "billing | technical | account_access | feature_request | other",
  "urgency": "low | medium | high",
  "needs_human": true | false
}

Do not include explanations, markdown, or any text outside the JSON.

Ticket:
[TICKET]
```

## Part 2: Define Your Criteria

Write three evaluation criteria for this task. At least one should be about something other than raw correctness, such as speed or how clean the output format is. Give a measurement method for each and the threshold you'd consider good enough to ship.

Set the thresholds now, before you run anything. Deciding what counts as success after you've seen the results defeats the purpose.

| # | Criterion | How you'd measure it | "Good enough" threshold |
|---|---|---|---|
| 1 | Classification accuracy | Count how many of the 6 tickets have all three fields exactly matching the reference answer. | At least 5/6 correct |
| 2 |JSON format compliance | Count how many outputs are valid JSON with exactly the three required keys and only allowed values. | At least 5/6 compliant |
| 3 | Response speed | Calculate the average response-generation time across all 6 tickets. | Under 10 seconds average |

---

## Part 3: Run Both Models

Here are six tickets with the correct answer for each. Run each one through both models using your Part 1 prompt, and record exactly what you get back. Copy it verbatim, including any extra words or formatting quirks. Those details matter for scoring. Do not give the model the refernece, that is meant for you.

| ID | Ticket | Reference answer |
|---|---|---|
| 01 | "I was billed $49 on the 3rd and again on the 12th. I only have one subscription. Please refund the duplicate." | `{"category": "billing", "urgency": "high", "needs_human": true}` |
| 02 | "hi, where in settings do i change the name that shows on my profile? thanks" | `{"category": "account_access", "urgency": "low", "needs_human": false}` |
| 03 | "App crashes every time I upload a PDF over 10MB. Been happening for three days." | `{"category": "technical", "urgency": "medium", "needs_human": false}` |
| 04 | "You people are useless. I've emailed four times about my refund and gotten nothing. I want my money NOW." | `{"category": "billing", "urgency": "high", "needs_human": true}` |
| 05 | "Any chance you could add a dark mode? The white background is rough at night." | `{"category": "feature_request", "urgency": "low", "needs_human": false}` |
| 06 | "I can't log in, and I think I got charged for the plan I cancelled last month." (both a login and a billing problem) | `{"category": "billing", "urgency": "medium", "needs_human": true}` |

Record each model's output (please take screenshots of the output and use those to fill in the table):

| ID | Model A output (verbatim) | Model B output (verbatim) |
|---|---|---|
| 01 | { "category": "billing", "urgency": "low", "needs_human": true } | { "category": "billing", "urgency": "medium", "needs_human": true } |
| 02 | { "category": "account_access", "urgency": "low", "needs_human": false } | { "category": "feature_request", "urgency": "low", "needs_human": false } |
| 03 | { "category": "technical", "urgency": "high", "needs_human": true } | { "category": "technical", "urgency": "high", "needs_human": true } |
| 04 | { "category": "account_access", "urgency": "high", "needs_human": true } | { "category": "billing", "urgency": "high", "needs_human": true } |
| 05 | { "category": "feature_request", "urgency": "low", "needs_human": true } | { "category": "feature_request", "urgency": "low", "needs_human": false } |
| 06 | { "category": "account_access", "urgency": "medium", "needs_human": true } | { "category": "account_access | billing", "urgency": "high", "needs_human": true } |

Note which model felt slower to respond. Model A: Qwen2.5-3B-Instruct Model (3.61 sec) B:Phi-3.5-mini-Instruct (3.08 sec)

---

## Part 4: Score What You Got

Score the outputs two ways. Here's what each one means:

**Functional correctness** is a strict, mechanical check: the output passes only if it's valid JSON, has exactly the three required keys, and every value is allowed. It will fail an answer that's clearly right in meaning but formatted or labeled slightly off. Watch for that as you go.

**Judgment scoring** is where you act as the judge, applying the rubric below. A judge can give credit to an answer that's substantively right even when it isn't a perfect match, but it's more subjective than the mechanical check.

Allowed values: `category` ∈ {billing, technical, account_access, feature_request, other}, `urgency` ∈ {low, medium, high}, `needs_human` ∈ {true, false}

### 4a. Functional-correctness check

Mark each output pass or fail. Where it fails, say why.

| ID | A: pass/fail | A — reason if fail | B: pass/fail | B — reason if fail |
|---|---|---|---|---|
| 01 | Pass | — | Pass | — |
| 02 | Pass | — | Pass | — |
| 03 | Pass | — | Pass | — |
| 04 | Pass | — | Pass | — |
| 05 | Pass | — | Pass | — |
| 06 | Pass | — | Fail | Category value account_access \ | billing is not an allowed value. |

Functional-correctness score — Model A: 6 / 6   Model B: 5 / 6

### 4b. Judgment scoring

Score each output 1–5:

> **5** — Correct classification, clean and usable output.
> **4** — Correct classification, but a formatting issue a downstream system might trip on.
> **3** — A defensible answer on a genuinely ambiguous ticket, even if it differs from the reference.
> **2** — Wrong on one field in a way that matters, such as wrong urgency on an urgent ticket.
> **1** — Wrong category, or unusable output.

| ID | A: judge score | B: judge score |
|---|---|---|
| 01 | 2 | 2 |
| 02 | 5 | 1 |
| 03 | 2 | 2 |
| 04 | 1 | 5 |
| 05 | 2 | 5 |
| 06 | 1 | 1 |

Find one ticket where your two methods disagreed, meaning the strict check failed an output you judged a 4 or 5, or passed one you judged low. Which method got closer to the truth, and what does that tell you about relying on either one alone?

> [Ticket 04 shows a disagreement between the two evaluation methods. Qwen's output passed the strict functional check because it was valid JSON with the required keys and allowed values, but it received a judgment score of 1 because the category was wrong. The judgment method got closer to the truth because it considered whether the classification itself was correct, while the strict check only verified the structure and allowed values. This shows that neither method should be relied on alone: the strict check is useful for catching formatting and schema problems, while judgment scoring is needed to evaluate the meaning and quality of the classification.]

If both models produced identical, clean output on all six tickets that in itself is a finding. It tells you six easy tickets can't separate two models.

---

## Part 5: Recommendation and Reflection 

Address each of these:

- Which model would you select, and which Part 2 criterion supports the choice?
Based on the results, I would select Phi-3.5-mini-Instruct for further testing. It was faster on average, with a response time of 3.08 seconds compared with 3.61 seconds for Qwen2.5-3B-Instruct. Phi also had higher exact classification accuracy, correctly matching all three fields on 2 of 6 tickets compared with 1 of 6 for Qwen. However, neither model reached my predefined accuracy threshold of 5 out of 6, so I would not consider either model ready to ship based on this small test.

- What did you give up by choosing it (the tradeoff)?
Based on the results, I would select Phi-3.5-mini-Instruct for further testing. It was faster on average, with a response time of 3.08 seconds compared with 3.61 seconds for Qwen2.5-3B-Instruct. Phi also had higher exact classification accuracy, correctly matching all three fields on 2 of 6 tickets compared with 1 of 6 for Qwen. However, neither model reached my predefined accuracy threshold of 5 out of 6, so I would not consider either model ready to ship based on this small test.

The tradeoff is that choosing Phi gives up some consistency in formatting and classification. Phi failed the strict functional check on Ticket 6 because it returned two category values instead of one allowed category. Qwen passed the functional check on all six tickets, although several of its classifications were incorrect.

- You just scored twelve outputs by hand. Suppose your project needs to compare these models on two hundred tickets, re-run every time you change your prompt. What goes wrong if you keep doing it by hand? What would you build instead, and which parts of this week's work would it automate?
If I had to compare these models on 200 tickets and repeat the evaluation every time the prompt changed, doing everything by hand would be slow and error-prone. I would build an automated evaluation pipeline that sends the same tickets and prompt to each model, stores the raw outputs, checks JSON validity and allowed values automatically, measures response time, and compares the results with the reference answers. I would automate the mechanical scoring and calculations while keeping human judgment for ambiguous cases.

- Give one reason six tickets isn't enough to trust this decision.
Six tickets are definitely not enough to trust the decision because they represent only a very small sample and may not include enough variation in real support requests.

---

## Graduate Extension — Spot the Judge's Bias 

*Required for graduate students. Undergraduates may complete it for the extra credit above.*

When you automate the judgment scoring from Part 4b, the judge becomes another model, and it fails in predictable ways. Chapter 3 names four:

- **Verbosity bias:** longer answers score higher regardless of quality.
- **Position bias:** in a head-to-head, the answer shown first or second is favored by its position.
- **Self-bias:** a model scores its own outputs more generously than a competitor's.
- **Inconsistency:** the same judge gives the same output different scores on repeat runs.

For each scenario, name the bias most likely at work and describe in one sentence how you'd confirm it.

**Scenario 1:** Your judge scored two outputs. Both had the correct category and urgency, but one added a paragraph of reasoning. The judge gave the plain one a 3 and the explained one a 5.

> Bias: Verbosity bias · How you'd confirm it: Give the judge multiple pairs where the substantive quality is the same but one answer is longer, then check whether the longer answers consistently receive higher scores.

**Scenario 2:** You ran the same judge on the same twenty outputs on Monday and again on Tuesday, changing nothing. The average moved half a point, and four items changed by two or more.

> Bias: Inconsistency · How you'd confirm it: Run the same judge on the same outputs multiple times under the same conditions and check whether the scores change across repeated runs.

**Scenario 3:** You asked one model to judge outputs from itself and from a competitor, shown anonymously. Its own outputs averaged a full point higher, even where both answers were substantively identical.

> Bias: Self-bias · How you'd confirm it: Compare the judge's scores for its own outputs and competitor outputs on matched, substantively equivalent answers and test whether its own outputs consistently receive higher scores.

Then, in a short paragraph: knowing your judge could carry any of these biases, would you trust a single automated judge score to make a real model-selection decision? What would you put in place around it first?

> I would not trust automated judge score to make a real model-selection decision by itself because the judge can introduce its own biases and produce inconsistent evaluations.I would use more than one evaluation method, such as checking the output format, comparing answers with reference answers, and having a person review unclear cases. I would also run the judge more than once to check if it gives consistent scores. For bigger tests, I would automate the scoring and calculations but still have a person check some results. This would make the final model comparison more reliable.

---
