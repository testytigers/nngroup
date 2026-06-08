# Prompt Structure in Conversations with Generative AI

**Author:** Raluca Budiu, Feifei Liu, Amy Zhang, Emma CioncaRaluca Budiu,Feifei Liu,Amy Zhang, andEmma CioncaNovember 24, 20232023-11-24

**Topics:** Artificial Intelligence

**Source:** https://www.nngroup.com/articles/ai-prompt-structure/

---

November 24, 20232023-11-24

Share

Our study of AI-chatbot interactions shows that most AI prompts contain one or more of several key components. These components help articulate the users’ information need. Prompts that lack certain components can result in long, inefficient conversations, with many query refinements.

Designers can support users by providing AI-interface elements that make it easy to include the different prompt components.

In May and June 2023, we conducted a 2-week diary study involving 18 participants who used ChatGPT 4.0, Bard, and Bing Chat. Participants logged 425 conversations and rated each for helpfulness and trustworthiness. At the end of the study, we conducted in-depth interviews with 14 participants.

The findings of this study are reported in several articles:

Apromptis a discrete input from the user that initiates or guides the chatbot’s response. Aconversationwith an AI chatbot can have one or more prompts.

We identified four components that were often (but not always) part of the AI prompts used in our study:

Not all these components were present in every prompt or in every type of conversation.

The request is the most straightforward part of the prompt —the core of the information need that the user wants to address.

In our study, the request was present in most (but not all) prompts, and many prompts contained only this component. The prompts that did not include a request were usually simple filler prompts such asThank youor prompts that provided additional clarification to an initial request.

The language of the request component typically took the form of a question, implicit request, command, or incomplete sentence.

Different Language Formats for the Prompt Request

Question

“should dogs eat kibble?”

“What are some ways to work from home with young children around?”

Implicit requests(signaled by phrases likeI wantorI need)

“I am looking for a new videogame to play”

“I need a dinner meal plan for 7 days on a budget”

Commands(introduced by phrases likeProvide, Tell me, Give me)

“Give me some ideas around real estate”

“recommend restaurants in South Elgin, Illinois to go for lunch”

Incomplete sentences

“Best strength exercises”

“Tips for doing a successful surprise proposal”

Some of the conversations we observed contained request-only prompts — the prompt consisted of a request without any additional context. Some request-only prompts (e.g.,best strength exercises) resembled a search-engine query.

A common request-only prompt in our study involved asking the bot to provide the best of something — for instance,the cheapest airport, the best way to get from Tokyo to Hakone to see Mount Fuji, the best cures for migraine, the easiest way to add lentils to your diet.

These best-of prompts were often inefficient (because they lacked sufficient details) and resulted in funneling conversations. As explained in our article on AI-conversation types, funneling conversations start with vague, underspecified prompts and require a lot of back-and-forth between the user and the bot., as the user is using subsequent prompts to articulate some of their requirements.

There are two kinds of references that may appear in AI prompts:

This prompt component referencessomething the bot said within the same conversation.

It was common for our study participants to have to mention a part of a previous answer (a behavior called apple-picking). Especially when the referent was a piece of text, the user had to type it again or copy and paste it to remove ambiguity. Sometimes, the user would refer to the structure of the bot’s answer to indicate their interest (e.g.,Change the last word in the last paragraph). These kinds of references could be used independently (like in the example above— last word in the last paragraph) or in conjunction with an actual quote.

Especially on mobile, it was difficult for the user to refer to specific aspects of an earlier bot response. Sometimes, instead of copying the text, the user inadvertently hit theEnterbutton and submitted the query too soon.

Direct manipulationwould vastly improve users’ interactions with bots. Designers can support internal references by allowing usersto select part of an answer and add it to the next query. For example, the user could right-click on a selected part of the answer and add it to the next query, as suggested in our article onapple-picking.

When asking the bot to work on a piece of text (for example, in text-generation or coding activities), users often must copy and paste it from elsewhere. When coding, users occasionally also paste error messages to seek debugging assistance.

Not all references involve copying and pasting the source text. Instead, a user may simply reference an external source by name, without pasting its text in the prompt, because they assume that the AI bot is already familiar with it. For instance, in the following prompt,the user assumed that the lyrics of a popular song did not need to be provided:

Please do a comical play on the lyrics of Holy by Justin Bieber but center the song on Mr. Smith, my dog [...]

Occasionally, users include an external source as an example of the type of output they want from the bot.

For instance, when instructing Bing Chat to revise sections of a resume, one study participant used the prompt:

Review job summary. Match in tone to this: [a previous section of her resume].

Consider how you cansupport easy referencingto parts of the bot’s previous responses, as well as to external sources.

When specifying the format in a prompt,users provide specific attributes they want from the bots’ output.These attributes often included:

Here are some examples of format specifications from our diary study:

Act as an Artificial Intelligence expert and tell me what is necessary to connect Bing to Bard to Anthropic to ChatGPTand give a response in one window.

Translate the following informal note for my house cleaner. Usestandard informal Spanish (Mexico).

can you give avisualizationof the convolutional connections and recurrent connections

Please write me an email thanking a group for attending a meeting including a question/answer section. This email should beprofessionaland not too long.

Understandably, only a few study participants included such specifications in their prompts, as these were often unnecessary for information-seeking conversations. (The exception was when the user wanted a concise, easy-to-read explanation.) Format specifications were more common in task-based conversations, whose output was supposed to be used by the participant for a specific goal (e.g., to include it in a resume or a presentation).

Include aUI feature that allows users to select among different possible output formats, as well as change the format of an answer already received.

For example, for certain text creation queries, Bing Chat offered amake-it-shortersuggested followup prompt. Additionally, the current version of Bard allows users to modify the length, complexity, and tone of voice of an answer.

Format-specification options should be provided at prompt level or conversation level rather than as a global settingthat applies to all conversations.That is because people use AI bots in a variety of contexts and for a wide range of tasks, and their formatting needs will vary according to the task.

For example, the current version of ChatGPT has a global setting that allows users to enter format specifications for all ChatGPT’s answers. Such a setting is unlikely to be helpful becausemany people use AI bots for both work and personal purposes, and they will likely need different kinds of formats for these settings.

Thepromptframing involves a description of the problem that the user wants to solve or of their context. Framing is intended to provide the bot with all the necessary information to generate a satisfactory response. It thus reduces the need for query reformulations.

Certain types of well-defined information needs cannot be satisfactorily addressed without enough framing. However, providing contextual details takes a lot of user effort.

In our study, some conversations started with a prompt that had detailed framing. Some examples include:

I am wanting to start a laundry service in my area. The service would be wash, dry and fold. I would provide pickup and delivery as well. Can you give me some name suggestions?

I am going to Japan for the first time in November for 7-10 days. I will be staying in Toyko and will not be renting a car. What are the top 10 things that I should see.

Framing often included anexplanation of the user’s goal, to ensure that the AI’s response would include the right angle. For example:

I trying to decide which car to purchase. My three choices are a 2023 Kia Telluride, a 2023 Kia Carnival, and a 2023 Jeep Grand Cherokee L. Please compare the 3 in the following categories; safety, cost, and online reviews.

Some framing prompts followedthe roleplaying model, popularized in news and social media. Word phrases used to introduce such prompts includedBe a,Imagine you are, Pretend you are, Act as a.The intent behind these phrases was toreduce ambiguity by setting upfront the domain of the query.

Imagine you are my coach, I am a 130 lb woman and want to get my first pull up. Design a daily program of a few exercises (preferably body weight) that can be done to guarantee that I can get my first pull up in two months.

Be a travel guide. Create me a 4 day itinerary in Chicago including activities and restaurant recommendations with estimated costs

Act as an Artificial Intelligence expertand tell me what is necessary to connect Bing to Bard ta Anthropic to ChatGPT and give a response in one window.

Sometimes, however, the participants misused roleplaying prompts and assumed thatbe Xor similar phrases were magic words that were likely to lead to a good answer. In fact,inviting the bot to play a specific role was not always necessary (or sufficient) to frame their query.

For example, the framing for the following prompt contained a roleplaying component, but that component did not provide any benefit:

Imagine you are a business intelligence analyst or a technology strategist,what are the technical skills that I would need to know?

A similarly detailed answer was provided by the shorter prompt, without framing:

What are the technical skills needed for business-intelligence analysts?

Framing a prompt is a time-consuming task for users.It requires them to think of all the information that the bot might need and then type it out. Some users may find it difficult to explicitly state all the constraints of their query. As a result, many conversations with well-defined information goals start without proper framing.

Note, however, thatnot all prompts need framing. When the information need is broad and is centered on learning, framing may not be necessary. It can be okay to start with an unframed question and then use the bot’s answer to determine the best direction that the conversation should take.

Most of the prompts we encountered in our study had a combination of the components described above. There were, however, a few notable exceptions, discussed below.

Sometimes users were not sure whether their information need fell within the bot’s realm, so they would start a conversation byasking the bot whether it could help with a particular task. This strategy saved users’ time because they didn’t need to bother with entering a complex query if the bot wasn’t able to help.

For example, one user who wanted to analyze some documents started his conversation with:

Are you able to access the 2022 Local Control and Accountability Plan (LCAP) for the Visalia Unified School District?

Once he learned that ChatGPT was not able to do that, he asked further questions to determine how he could get the bot to access those documents, only to eventually give up.

Another participant wasn’t sure whether ChatGPT could help with the creation of a business plan, so he started the conversation by askingCan you help me create a business plan?ChatGPT responded with a detailed structure of a business plan. While this information was accurate, it did require the user to read through a long response that wasn’t specific to his situation.

A better experience would involve the bot prompting the user with query refinements to help them articulate their question, as it did when a different participant asked for help generating a recipe.

Can youprompts are often asked by individuals who are new to AI or who are attempting a task with the bot for the first time. As users become more experienced with AI bots, such questions are likely to become rarer.

Note that sometimes people useCan youlanguage to ask the bot to do something rather than inquiring about its ability. That is usually a query that provides more context than the very basicCan you do thisquery, like in the example below, where a user who wanted their resume rewritten referenced the text that needed to be edited:

Can you rewrite this? Hard-driving business leader offering skills…

Distinguish between the twointents behindCan youlanguage:

Sometimes participants were unsatisfied with the bot’s answer andasked for more options. These kinds of queries usually occurred in conversations where the user had provided a broad, underspecified prompt with little or no framing, usually requesting a list of items (e.g., recommendations). If the items included in the bot’s list failed to elicit the user’s interest, the participant would ask for more options, without attempting to add framing to their prompt.

WithGive me moreprompts,the user effort is minimal at the prompt level, but not at the conversation level— it is likely that they will need to follow up with further prompts or query refinements that include more detail for their question.

Give me moreconversations are least likely to result in success and users may, in fact, be better off by just using a search engine. As one participant put it:

I felt like I wanted more once again like more unique or more creative meals but it kinda kept giving me stuff that I already knew, and then I had to keep asking, like, ‘give me more’, ‘give me more.’ And, so, if I’m already having to ask it to give me more ideas, I feel like I might as well just go into Google and be able to scroll and click on the links that I think are gonna be answering my question how I want it to be.

Bots should attempt to makeGive me moreprompts more specific byasking framing questions and suggesting followup promptsthat help users define their query.

Filler utterances, which include polite phrases likeThank you, Have a good night, Cute,orThat was helpful, haveno real communicative function,but they do have a social function in human-to-human conversations. Such utterances reassure the conversation partner that their message was received and appreciated.

Our participants used fillers fairly often —a sign that they were projecting anthropomorphic qualitiesto the bots.

Some users complained when the bots did not recognize some of the subtler fillers (other thanThank you,That was great,and similar) and, instead, treated them as regular prompts, providing an answer to them. Even though people could choose to ignore a response that they did not need, the response still required their attention.

Tools need todistinguish fillers from information requeststo prevent users from feeling flooded with unwanted information.

The user’s information need is like an iceberg. The visible tip of this iceberg is the direct prompt, while the submerged layers are the critical mass that gives the prompt its true shape and direction. The more of these submerged layers is revealed in the prompt, the more effective the AI can be in meeting the user’s information need.

Including all the different components (request, references, format, and framing) in a prompt can help users get the most precise response. But sometimes this is difficult, due to several reasons:

If you are getting started with generative AI and you want help with a specific task,think of your information need as an iceberg:the more you uncover of that need in your prompts, the higher the chance that the bot will provide something useful.

Prompts likeBest oforGive me moreare very inefficient — if you find yourself using them, it’s a sign that you may be better off with a search engine.

Requests, references, and many format specifications are relatively straightforward for most people (even though some of us may forget about the format when we first ask our questions). However, determining the right framing for a prompt can be tricky. First, uncovering all the contextual information takes effort — you have to think about it, articulate it, and finally type it. (That’s why it helps to havea library of prompts if you’re likely to do the same task several times). Second, providing too many unnecessary details can occasionally sidetrack the bot.

The current focus on prompt engineering and the popularity of roleplay framing in the media leads some users to assume that framing is just asking the bot to play a specific role. In fact,a rich context specification is often essential but does not necessarily mean roleplay.

If the framing for a question is too hard to figure out,enroll the bot’s help— prompt it to ask you questions about additional information that may be necessary for it to provide a specific answer.

However,not all prompts need elaborate framing. If your goal is less well-defined and you’re looking to learn about a new domain or get started in an area, you can safely begin with a general request and then use the bot’s response to determine the direction that the conversation should take.

The structure of the generative-AI prompts and conversations teaches us about what designers can do to improve the overall experience of generative AI and allow users to efficiently address their information needs.

In particular, designers should: