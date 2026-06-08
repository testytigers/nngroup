# Prioritize Smarts over Sentience to Increase Trust with AI

**Author:** Evan SunwallEvan SunwallSeptember 19, 20252025-09-19

**Topics:** Artificial Intelligence

**Source:** https://www.nngroup.com/articles/smarts-emotion-trust-ai/

---

September 19, 20252025-09-19

Share

A common concern from attendees of ourDesigning AI Experiencescourse is how to help users develop trust with artificial intelligence (AI). One technique that designers are frequently tempted to use isanthropomorphism. The rationale is that the more the user sees the AI as a conscious, human-like entity, the more likely they’ll trust it.

But is anthropomorphism an effective tactic? A recent study offers intriguing data about how our beliefs about an AI’s “mind” predict our willingness to trust and rely on its advice.

Psychology researchers Clara Colombatto, Jonathan Birch, and Stephen Fleming wanted to unravel the broad concept of anthropomorphism and explore its effect on trust. They recruited 410 US participants for an experiment with two counterbalanced parts in awithin-subjectsformat.

The researchers asked about their beliefs regarding ChatGPT’s mental abilities. Specifically, the researchers asked questions around:

In addition to these perception questions, the researchers gave participants a simple quiz with 40 general-knowledge questions on population estimates for countries, like: "Does Colombia or Germany have more people?"

Participants were then presented with information that represented “ChatGPT’s choice” on the quiz and were given the opportunity to change their answers. The researchersmeasured how often people “took ChatGPT’s advice”(i.e., changed their answers based on the AI’s choice). Participants were not told if their quiz answer was correct, but 10% of the time, they were asked to recall ChatGPT’s advice for the previous quiz question as a quality-control measure, and a participant’s data was excluded if they failed to answer 70% of these recall questions correctly.

Unbeknownst to the participants,ChatGPT’s choice was not actually AI-generated.It was scripted by the researchers. (This scripting was to control for theconfounding variableof unpredictable accuracy from live ChatGPT responses and ensure that any differences in trust were due to the participant’s beliefs about ChatGPT, rather than the quality of a particular response.)

At the end of the experiment, participants reported their trust in ChatGPT on this population-estimation task and their overall trust in it. They also reported on the frequency of usage of digital assistants (Alexa, Siri), AI companionship apps (Character AI, Replika), and general-purpose AI chatbots (ChatGPT, Gemini, Claude).

A regression analysis of the data revealed two key findings about the link between what people believe about AI, and how much they’ll take its advice.

The researchers speculate that people may be more willing to trust an AI's factual advice when they associate traits like memory and reasoning with it, viewing it as more reliable. In contrast, users may trust AI less when they perceive it as having more emotional traits, and thus more unstable, subjective, or less analytical.

The bottom line is: When it comes to taking AI’s advice, trust is essential.Users are more likely to follow the AI’s advice if they perceive AI as smart, rather than emotional.Thus, if you want to build trust, you should work on creating the impression of intelligence (by providing accurate, relevant answers) instead of just creating the illusion of emotional rapport.

More emerging research suggests that making AI emotional has serious risks beyond user trust and in other contexts.

In the Colombatto et al. study, ChatGPT’s advice was scripted to be about 62% accurate to simulate average human performance. But what if the AI's personality itself affects its reliability?

A recent preprint study by Lujain Ibrahim, Franziska Sofia Hafner, and Luc Rocher found exactly that. The researchers finetuned several LLMs to make them produce warmer and more empathetic responses, which revealed a significanttradeoff.These 'warm' models were far less reliable in their responses and haderror rates 10%–30% higherthan the originals. While finetuning represents a deeper level of model customization than most product teams undertake, the researchers also tested adjusting the LLM’s behavior through a system prompt, which is a far more likely customization approach. The results were similar:instructing the base models to be warmer also produced a 12%–14% drop in reliability.

These warmer models were more likely to promote conspiracy theories, provide incorrect facts, and offer problematic medical advice.Making the AI more caring made it less competent!

The Colombatto study acknowledged that it explored trust during low-stakes factual tasks, leaving the possibility of different results in emotionally sensitive contexts, like companionship or mental health. But there is research to suggest it is unwise there, too. A preprint by Jared Moore, Declan Grabb, and colleagues investigated the high-stakes scenario of using LLMs as replacements for mental-health providers. They found that LLMs' tendency tosycophancyled them to encourage delusional thinking and mishandle severe mental-health crises.

The Ibrahim study found thatwarm, empathetic models were significantly more likely to be sycophantic,which is precisely the quality that makes them untrustworthy and potentially harmful for mental-health needs.An empathetic and emotional AI performs poorly even in contexts where it may seem beneficial.

The insights from this research may raise a few misconceptions about anthropomorphizing AI that are worth clarifying:

When designing AI features or systems to perform work, UX professionals should heed this advice.

Promoting anthropomorphic qualities in a task-oriented AI is a counterproductive strategy. This approach seems like an easy path towards making approachable AI, but it can undermine user trust. Instead,teams working in productivity contexts should develop the AI's analytical, planning, and reasoning capabilities. This path is more challenging, but there are no shortcuts to creating AI experiences that users will actually trust and use.

Clara Colombatto, Jonathan Birch, and Stephen M. Fleming. 2025. The influence of mental state attributions on trust in large language models.Communications Psychology3, 84.https://doi.org/10.1038/s44271-025-00262-1

Jared Moore, Declan Grabb, Kevin Klyman, William Agnew, Stevie Chancellor, Desmond C. Ong, and Nick Haber. 2025. Expressing Stigma and Inappropriate Responses Prevents LLMs from Safely Replacing Mental Health Providers. arXiv preprinthttps://arxiv.org/abs/2504.18412

Lujain Ibrahim, Franziska Sofia Hafner, and Luc Rocher. 2025. Training Language Models to Be Warm and Empathetic Makes Them Less Reliable and More Sycophantic. arXiv preprinthttps://arxiv.org/abs/2507.21919v2

Design innovative, trusted, and useful AI products and features

Artificial Intelligence

The AI-assisted user research workflow

Artificial Intelligence

Leverage AI to enhance creativity, efficiency, and impact in everyday design work

Artificial Intelligence