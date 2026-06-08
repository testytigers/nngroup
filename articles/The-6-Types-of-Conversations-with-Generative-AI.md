# The 6 Types of Conversations with Generative AI

**Author:** Raluca Budiu, Feifei Liu, Emma Cionca, Amy ZhangRaluca Budiu,Feifei Liu,Emma Cionca, andAmy ZhangNovember 10, 20232023-11-10

**Topics:** Artificial Intelligence

**Source:** https://www.nngroup.com/articles/ai-conversation-types/

---

November 10, 20232023-11-10

Share

Through analyzing 425 interactions with generative-AI bots like ChatGPT, Bing Chat, and Bard, we've discovered that conversations could involve many vague, underspecified prompts or few, razor-sharp ones. Why does this matter? First,different conversation types serve distinct information needs and demand varied UI designs. Second,there is no one optimal conversation length— both short and long conversations can be helpful, as they might support different user goals.

In May and June 2023, we conducted a 2-week diary study involving 18 participants who used ChatGPT 4.0, Bard, and Bing Chat. Participants logged a total of 425 conversations and rated each for helpfulness and trustworthiness. At the end of the study, we conducted in-depth interviews with 14 participants.

The findings of this study are reported in several articles:

Several types of conversations emerged from our analysis:

Some conversations involved several prompts and reformulations, whereas others were relatively short.

In what follows, we discuss each of these 6 types of conversations; for each, we provide tips for both users and interface designers of generative AI chatbots.

These conversations areone-prompt, simple queries that are not followed by any refinements. The prompt usually includes the question with no framing or format specification.

In our diary study, the intent behind search-query conversations was the same as for a web search: users were trying to locate a specific piece of information. These conversations were common when people were still trying to understand what the bots could do for them and what they were best at. In such situations, it is likely that users were simply transferring their searchmental modelsto the AI bots.

Examples of search-query conversations from our diary study include:

When these search-query conversations involved Bing, participants often clicked on the suggested links and visited the sites, as they normally would have done when using a search engine.

While short keyword phrases likeRosie Odonnellmight work well for search, they lack enough context to help AI chatbots understand what the user is asking for. Sometimes users realized that a search engine would be better suited for such queries and quit the bot.

Both users and designers need to consider what the best tool is for a given information need. Sometimes, it could be that an AI chatbot won’t do a job as good as a search engine.

Avoid using this type of prompt when working with AI bots like ChatGPT. While search engines perform best with keywords, AI bots need more context to understand what kind of response or output you’re looking for.

Search engines might (for now) give you as good if not better results as AI botsif:

Considerallowing users to easily switch to a search-engine mode or access search-engine results,like Bard does.

In funneling conversations,the user starts with an underspecified, sometimes too vague query and then narrows it down with subsequent questions that specify additional constraints.Often, the user doesn’t realize that they need to be more specific until they receive an unsatisfactory response from the bot.

For example, here is a sequence of queries asked by one user who was trying to find a recipe:

If the user had anticipated all of these requirements, she could’ve achieved her desired result with a single prompt:

I want an easy appetizer recipe for 30 people to serve poolside on Memorial Day Weekend. I’m thinking of some sort of dip. I don’t want to use pork and the appetizer needs to be able to sit outside in the heat.

However, she likely did not consider this full set of constraints until she received the bot’s initial suggestions.

Funneling conversations are often long, as the user might need to input several prompts to refine their query. Sometimes they start with best-of prompts or other basic prompts that lack details. For example, here’s a sequence of prompts from a user interested in figuring out how to prevent her migraines:

Note that,in funneling conversations, the user’s information need is usually specific and well-defined, but poorly articulated. In other words, the user will likely recognize a correct response, but will not be able (or sometimes will not be bothered) to say what that correct response should look like. However,the bot can facilitate query articulation by asking the user helping questions.

In some of the conversations we studied, the bot did ask for clarification. For example, one participant started the conversation withIssue with swimming pool cleaner.ChatGPT asked for specific information about the cleaner and the issue, expediting the funneling process.

Considerexplicitly telling the AI bot to ask helping questionsto improve its output. For example, you may add phrasing such asAsk me questions if you need additional information, to get the bot to help you articulate the different constraints that you may be working with.

To reduce the articulation load in funneling conversations, thebot should ask helping questions that narrow down underspecified queries.

In exploring conversations, the user starts with a general, less-defined query (usually lacking context or output-format specifications) and thenuses the AI to understand the information space and get ideas for new queries.

Exploring conversations differ from funneling conversations in that, in the beginning, the user is not able to formulate a specific enough querybecause they have a less-defined information need and lack the necessary vocabulary or knowledge(rather than because they did not spend the time to think of all the requirements for their information need). The bot’s responses help the user learn about the structure of the information space and give them new terminology and ideas about what to ask next.

An exploring conversation oftenfeels like a conversation with a real teacher;the user acts as a studentlearning byacquiring depth into a topicand asking questions as they learn. The user is building queries based on the information received from the bot.

For example, one user askedWhat is the meaning of life?The bot talked about various kinds of views, including philosophical, religious, and absurdist views. The user then asked to know more about one of these — absurdism. When the bot mentioned the book “The Myth of Sisyphus” by Albert Camus, the user asked for other works by the same author.

In exploring conversations, users can be supported withsuggested followup prompts that naturally build upon the information presented in the bot’s answer.

If the user’s information need is broad and the bot’s response is complex, containing jargon and domain-specific facts or concepts,offer a list of suggested followup promptsthat build upon these details.

The followup prompts can include:

However, detail-oriented suggested followup prompts do not need to be included in all conversations.Conversations with well-defined information needs (such as pinpointing conversations — see below) rarely benefit from such followup prompts.For example, a user rewriting her resume said:

if I'm asking you to put something in my resume, like, I do research in […] B-cell malignancies, I don't necessarily need to ask ‘what are B-cell malignancies.’

In chiseling conversations, the user asksabout different facets of the same topic, fleshing it out from a variety of angleslike a sculptor chisels a sculpture from a piece of stone. Chiseling conversations cast a wide net over a topic to acquirebreadth. They can feel like research on a specific topic, but the research is person-driven rather than driven by the bot’s answers.

Here is a sequence of questions asked in the same chiseling conversation about ADHD:

While these questions are all related to ADHD, they cover various aspects of ADHD and do not explore any one of these in depth. It feels as if the respondent is trying to learn many facts about the topic, without focusing on the logical relationship between these facts.

Another user was doing research on the company Insperity. She asked multiple questions related to different aspects of the company:

Both exploring and chiseling conversations correspond to less-defined information needs and imply learning about a topic. But, while in exploring conversations, the learning involves acquiring depth into the topic, in chiseling conversations the learning is carried out through breadth.

Tips for Designing AI Bots

Like exploring conversations, chiseling conversations benefit from suggested followup queries. However, for chiseling conversations,suggested followup prompts should be broad, inquiring about multiple facets of the same topic or about related topics (e.g.,How about…?).

In contrast, for exploring conversations, these prompts should go indepth, delving into details about a particular concept or fact in the answer.

In pinpointing conversations, the user has a defined topic in mind andcreates a very specific prompt from the very beginning. The prompt often includes context and a format specification.

Summer Cocktail Party: My wife and I are hosting a small cocktail and dinner party welcoming my daughter's future in-laws for a visit to California in late July. The party will be indoors and outdoors by the pool, and we will be grilling something no doubt for the meal. It will be hot in late July so drinks that are refreshing would be order. I am not a professional bartender, but I have been studying "mixology" for the past year and do have all of the bar tools. I know how to make all of the classic cocktails. I would like a summer-themed cocktail menu of four to five drinks with clever names. I will put them on a framed menu on the counter in my outdoor kitchen and bar areas where I will make the drinks.

Sometimes the query might also include pasted text from another source or some other supporting documentation, like in the prompt below, which quoted a previous email chain (names were changed for privacy):

I would like to reach out to Bob to ask if he can do some part-time work for the […] school site visits for my department starting in August through the end of September. Here is some background from an email exchange last year:

You bet! We’ll keep you posted, Bob!

John Smith, Ed.D. Department Administrator College & Career | Leadership Support Services

From: Bob Jones

Date: Monday, September 12, 2022 at 9:50 AM

To: John Smith

Subject: Re: Thank you!

Thank you John! I enjoyed the time I was able to spend with school leaders and with Andrew. With the new requirements and the possibility of more schools added to the three year cohort I would be available next year if you think I could help. Thank you for your confidence!

Bob Jones

Sent from my iPhone

On Sep 12, 2022, at 9:38 AM, John Smith wrote: ﻿

Good Morning, Bob, I wanted to thank you for your support of the [school] visits this year. Your expertise and experience as a former district leader really benefited the process. Even with some new requirements, it was one of our smoothest years ever with your help! I hope you enjoyed this work, too, and will consider leading visits again next year if you’re available. Thanks again for lending us your time in this area!

John

Pinpointing conversations require great effort from the user,who needs to provide all the information necessary for a comprehensive response. They often contain well-specified, “engineered” prompts. However, unlike with other conversation types, the user rarely needs to spend time on query refinements and the result is a shorter, straight-to-the-point exchange.

Funneling conversations can sometimes be converted into pinpointing conversations if the bot asks the user detailed questions about their query, inviting them to specify all those details in their next prompt.

Ask the user forspecific detailsabout their question, as well as about the format of the answer.

Consider giving usersexamples of the information they could providein a prompt if the prompt is too vague or underspecified.

The expanding conversation usually starts with anarrow topic that gets expanded, often because the results from the original prompt were unsatisfactory (e.g., not up to date) or because the user decides they need more detail.

For example, in the following sequence, the user expanded his original query twice.

Example of Expanded Conversation

Start prompt

Expanded prompt:The user realized there was no cheapest airport based on ChatGPT’s response to question #1 and expanded his query.

Expanded prompt:In response to question #2, ChatGPT said that prices will vary depending on various factors, so the user expanded his query again.

When the expanding conversations involved Bing, the expansions were usually selected from the suggested followup queries.

Expanding conversations remind us of what happens when people get zero search results for a search query: they often try to remove one of the criteria of their query in the hope that they will get something good enough. In such situations,search facetshave been shown to help people by guiding them to ask queries that have one or more results.

Similarly, in the context of expanding conversations with AI, suggested followup prompts can show the user how to expand their question to get a meaningful answer. However, suchbroader suggested followup prompts should have a different answer than the original question.

For instance, one study participant used Bing Chat to look forfree events happening in Nashville this weekend. Unsatisfied with the response she received, she expanded her query using a suggested followupWhat are some popular free events in Nashville. Disappointingly, she found the results were very similar. She commented:

I used one of the suggested follow up questions as the chatbot was not providing very specific information regarding Nashville events. It yielded pretty much identical results to the question I had posed. While it was nice to have the prompts below, I feel that they should maybe pose newer information.

When the bot is not able to provide an answer to the user’s query,provide suggested followup prompts that relax some of the criteria in the user’s original question and return an answer.

Some conversations start as one type and then morph into a different one. For example, chiseling conversations may also have exploratory elements that build upon something that the bot has said.

One user had the following exchanges with ChatGPT; they combined chiseling and exploring conversations.

A Conversation Combining Chiseling and Exploring Prompts

Chiseling prompts:The user was trying to find information about various facets of day training with no reference to previous bot answers.

Exploring prompt:The question was triggered by the answer provided by the bot to question #3.

Exploring prompt:The question built upon the bot’s response to question #4.

Chiseling prompt:The questions were unrelated to the previous prompts within the same conversation.

On average,a conversation in our diary study included 3.6 participant-generated prompts(95% confidence interval: 3.3–3.9); the median length was 3.

In general, the higher the number of attempts to do a task, the worse the usability. (For example, if the average number of submit attempts on a form was 3.6, that would mean that the form was pretty bad.)

However, with AI conversations, it is not the case that longer conversations necessarily represent more strenuous attempts at getting information from the bots. In fact, there was no correlation between the length of the conversation and its helpfulness or trustworthiness ratings,as collected from our study.

For certain types of conversations like funneling and pinpointing,the length indicates how well-articulated the initial prompt was.Long funneling chats start with vague prompts that need more detail. Short pinpointing chats begin with detailed prompts that already lay out all the requirements for an acceptable answer. In both such conversations, the user’s information need is constrained and fairly narrow — they need a specific piece of information or a specific output.

For exploring and chiseling conversations, length is part of the conversation’s natureand serves the user’s less well-defined information need. Exploring conversations require a back-and-forth between the bot and the human, with the human learning from the bot and choosing to go deeper and build upon the bot’s response. Chiseling conversations are also long because the goal is to acquire breadth in a subject, therefore requiring the user to ask multiple, loosely related questions about different aspects of given topic. In both these types of conversations, the goal is learning about a topic, and the conversation serves to define the user’s information need.

A special type of short conversation is the search query. This type of conversation was usually more likely to occur when people were still exploring the range of tasks that the AI bot could do for them.

Search queries were common with Bard; that is likely whyconversations with Bard were shorter than conversations with ChatGPT (p <0.001) or Bing (p<0.001).It could be that Bard participants were primed by the prominence of Google as a search engine and tended to use Bard as a proxy for Google search.

A final word about the length of expanding conversations: they can be long or short, depending on how successful the user is in finding a satisfactory prompt that the bot can answer. They can also evolve in other kinds of conversations once the user finds the right way of formulating their query.

Taxonomy of AI Conversations by Information Need

Narrow, Well-Defined Information Need

Broad, Undefined Information Need

Funneling

Pinpointing

Exploring

Search queries

Exploring conversations: acquiring depth of knowledge

Chiseling conversations: acquiring breadth of knowledge

There is no ideal length for all conversations. If the user has a clear, well-defined information need, then a good, detailed, pinpointing prompt will get them what they need fast.

But if the user’s goal is broad and less well-defined, then a single exchange will likely not be enough. The user can use the bot’s responses to learn — either through breadth or depth.

The structure of the generative-AI conversations is teaching us about what designers can do to improve the overall experience of generative AI and allow users to efficiently address their information needs.

Bots should attempt to use the length and the structure of the user’s prompt, as well as the complexity of the answer todetermine the conversation type early in the exchange and adjust behavior accordingly.That is because different conversation types address different information needs and the support provided by the bot needs to be tailored to each need.

Specifically:

Design innovative, trusted, and useful AI products and features

Artificial Intelligence