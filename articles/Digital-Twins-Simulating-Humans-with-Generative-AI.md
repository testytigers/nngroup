# Digital Twins: Simulating Humans with Generative AI

**Author:** Raluca BudiuRaluca BudiuAugust 1, 20252025-08-01

**Topics:** Artificial Intelligence

**Source:** https://www.nngroup.com/articles/digital-twins/

---

August 1, 20252025-08-01

Share

Let’s face it: research with real users takes time. Recruiting participants, collecting data, and waiting for results are often the most time-consuming stages of the research process. One of the most exciting and promising avenues for improving efficiency across domains —including user research — is the use ofgenerative AI.

Can research be made faster or more scalable with AI? Elsewhere, I’ve outlined the types ofstudies our field must undertaketo understand how generative AI can support UX and behavioral research. Today, I focus on one particularly promising — and sensitive —direction:simulating human behavior using AI models.

Adigital twinis a generative model — typically based on alarge language model (LLM)— that attempts to act as a proxy for a particular person. This model can respond to new questions or situations in roughly the same way the individual would.

Think of it as anartificial cognitive clone:a system that can complete surveys, predict choices, or interact in real time on behalf of a real individual. The twin is trained or primed with personal information — such as demographics, past survey responses, interviews, behavioral logs — and can be used for predictingindividual-levelbehavior (what that particular individual will do) andpopulation-levelbehaviors(what a user group would do).

When simulating humans with AI, we can distinguish between two broad approaches:

In practice, however, the distinction between digital twins and synthetic users is blurred. Imagine a continuum:

Sometimes, synthetic users may be generated based on a little more than demographic information — for example, a generic persona-like description.  And the less specific information is used to create digital twins, the less likely they are to match a specific individual and to act as synthetic users corresponding to a larger group.

Being able to forecast how a particular person will respond to a stimulus has clear value in UX, marketing, and social sciences. Examples include:

Although twins are constructed at the individual level, their outputs could be aggregated to reveal broader population-level trends. They would enable researchers to simulate how entire audiences might respond to a new feature, design, or message — without needing to recruit hundreds or thousands of people in advance.

By applying sampling weights that reflect a target population's structure, digital twins can approximate survey representativeness and support large-scale behavioral testing before any real-world rollout.

The construction of a digital twin depends on how much contextual information is available about the individual and how that information is integrated into the model.

The individual-specific contextual information could include:

Once gathered, this contextual information needs to be fed into the model. That can be done in several ways. The chosen route depends on budget, data availability, the level of technical expertise available, and how narrowly the digital twins will be used.

This approach builds the twin by adding the corresponding personal context to the LLM prompt. While this is easy to implement, it can run into prompt-length limitations when the individual context is too large.

With this method, all the relevant information (such as the individual’s history along with other domain-specific information) is encoded in an external data source. For each prompt, the most relevant documents in the external data sources are retrieved and appended to the prompt, then passed to the LLM.

This allows models to dynamically access rich data — like interview transcripts or response histories — without overloading the prompt.

This approach is the most costly — it involves retraining the model using a smaller domain-specific dataset (e.g., responses from thousands of users of the same product), to adapt it to a particular set of tasks. This process can result in internal model weights that are optimized for this particular domain.

As a result, an individual’s responses may be predicted not only based on their own past actions but also on the past actions of individuals with similar behavior patterns or opinions within the same domain. For example, the model may predict that a particular dog lover would like a fenced yard based on the fact that many dog lovers in the training set had fenced yards.

In our evaluations of synthetic users, we haven’t been very impressed with the performance of currently available simulated humans. They tend to fail to capture the messy, nuanced nature of real human behavior. We find them useful when treated as a desk research tool, rather than considering them as a substitute for talking to your actual customers.

Hypothetically, it’s possible that digital twins may produce more realistic results because they’re based on the nuanced complexity of a single real individual, instead of the aggregated, averaged data representing a group.

In my next article in this series, I’ll review some recent academic studies looking at the predictive power of digital twins and synthetic users; broadly speaking, these studies show a lot of promise for digital twins, especially for practical applications such as filling in missing data in surveys and predicting survey answers based on extensive interviews.

Digital twins raise serious ethical questions that researchers and designers must not overlook.How should consent be managed when reusing a participant’s data to create a long-lasting proxy? Would users agree to having a digital version of themselves created to fill out surveys or predict further behavior?

What are the risks of misrepresentation, especially if a twin is used in contexts beyond its original intent? And how do we ensure that models don’t perpetuate or amplify existing biases in data collection?

These questions are not merely academic. As digital twins move from experimental tools to operational ones, the UX community has a responsibility to address issues of transparency, privacy, and fairness. Used thoughtfully, digital twins could complement traditional methods and extend the reach of UX research into new, faster, and more adaptive territory — but only if we proceed with care and clarity about their limitations.

The AI-assisted user research workflow

Artificial Intelligence

Design innovative, trusted, and useful AI products and features

Artificial Intelligence

Leverage AI to enhance creativity, efficiency, and impact in everyday design work

Artificial Intelligence