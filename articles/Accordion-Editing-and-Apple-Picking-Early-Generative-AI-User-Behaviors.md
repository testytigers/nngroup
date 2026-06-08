# Accordion Editing and Apple Picking: Early Generative-AI User Behaviors

**Author:** Sarah Gibbons, Tarun Mugunthan, Jakob NielsenSarah Gibbons,Tarun MugunthanandJakob NielsenSeptember 24, 20232023-09-24

**Topics:** Artificial Intelligence, Behavior Patterns

**Source:** https://www.nngroup.com/articles/accordion-editing-apple-picking/

---

September 24, 20232023-09-24

Share

Chatbots are currently the predominant UI of generative-AI tools for text manipulation. Each individual interaction with AI is a straightforward transaction: you put text in, and AI gives text back. (Other AI tools produce other media forms, such as images, audio, or video, but this article focuses specifically on text-based AI tools.)

In user testing, we have seen that users frequently engage in iterationswhere they refine AI-generated output through additional prompts. This back-and-forth interaction, in combination with the text-only user interface, creates two new user behaviors: the accordion effect and apple picking.

Our goal was to uncover usability issues present in AI-chatbot interfaces. Since these bots have become widely used productivity tools, we conducted a qualitative usability study with professionals and students who use chatbots in their day-to-day work.

We recruited a sample of 8 participants, which included:

Each participant completed 1–2 tasks they brought to the session, followed by custom tasks we designed that matched the nature of their profession. These tasks involved writing, generating ideas, editing text, analyzing information, and designing interfaces. Users used ChatGPT-3.5 to complete these tasks as was representative of their day to day usage.

Sessions were 90 minutes, and participants were asked to create low-, mid-, and high-fidelity outputs using chatbots.

Definition:Accordion editingoccurs when users ask the AI to shrink or expand its outputs, often back to back and repeatedly, to accomplish a singular goal.

Since, unlike images, text is a one-dimensional medium, users are limited to a simple, linear way to interact. Beyond the tone or style of the text, one of the most straightforward characteristics is length: make it longer or shorter, just like the player of an accordion expands and contracts it.

For example, consider a user who wants to create a travel itinerary. They ask the chatbot to first give some recommendations for sightseeing in a new city. Next, they ask for more information on each recommendation by adding a few places to eat near the attraction (expandingthe output). Finally, they ask the chatbot to give the top 5 best options in a specific neighborhood (shrinkingthe output) to complete the travel itinerary.

Users shrink AI outputs with two primary behaviors: forced ranking and word-count reduction.

Behavior

Description

Use Case

Forced ranking

List shortening via a top selection

Creatinglow-to-mid fidelityoutputs and lists, like generating ideas, plans, or options

Word-count reduction

Specifying character or count limits

Users expand AI outputs in two primary ways: by expanding upon an idea given by the bot or by adding missing content.

Behavior

Description

Use Case

Expansion within an idea

Adding to an existing idea

Users expand on a particular paragraph or bullet point to follow up on an idea that ChatGPT gave them. They do so by referencing part(s) of the previous response they want to expand on in the next prompt, alongside an instruction to expand on it.

Addition of missing content

Capturing new ideas

Accordion editing involves the purposeful shrinkingorexpanding of AI outputs, often back to back. However, in many cases, both shrinkingandexpanding are used in combination to create the final desired outputs, hence the accordion analogy.

For example, a user may find missing content in their text and request that ChatGPT add it, thus expanding a specific aspect of the output. But then the user follows by shortening the overall response to fit their required format. Both actions require users to write additional prompts to make the desired changes, often repeatedly.

For some generative-AI goals, accordion editing is intentional and beneficial. With others, it’s the repercussion of not getting the desired output the first few (or several) tries. Some generative-AI tools offer personalized settings and formats to address this issue by allowing users to specify custom preferences that influence all future use. For example, a custom instruction like “Keep it short unless I ask for more detail. Use lists and bold keywords so it’s easy to scan” reduced ChatGPT’s tendency to be verbose.

Some users reduce their amount of back-and-forth accordioning by including a limit (such as the number of points or a word count) in their initial prompts. In many cases, the initial AI output  matched the user’s specifications. However, even if the initial specification was satisfied, many users still engaged in other content-related revisions with the AI.

Thus, our established recommendation for chatbot users remains:be as specific as possibleto combat thearticulation barrierand achieve the output you want.

You are more likely to achieve your goal quickly by specifying:

Definition:Apple pickingoccurs when users reference one or multiple, previous AI-responses in their following prompt to achieve their desired output.

Users frequently want to build on one or more previous responses from ChatGPT by referring to a specific element within one of these previous responses. There’s no easy way to do this. People must type (or copy and paste) text describing or quoting the part of the previous responses that they want to work with. Given the frequency of this behavior, apple picking incurs a significant effort.

Users apple pick by identifying (calling out) an element they either want to:

Behavior

Description

Use Case

Call out to change

When users want to edit a specific point or remove part of an existing response, they reference the part they want to change and then ask ChatGPT to generate a new response version that includes that change.

Writingmid-to-high fidelitycontent like essays, emails, social media posts, plan documents, or article outlines

Call out as context

Sometimes, especially during more complex tasks with many steps, users want to build on previous responses by using them as context for their next prompt. They often do so by manually referencing or pasting parts of prior responses.

Creating text atall levels of fidelity,including ideas, compiled information about a topic, article outlines, plan documents, emails, and social media posts

The process of generating text is iterative, involving the production of many new versions or building on a chain of previous responses. Thus, a large amount of text accumulates within the chat window when using an AI bot. Users cannot hold all this information in theirworking memoryand must often scroll back up to keep track of what the AI tool has generated so far.

Users will frequently need to scroll through a massive wall of text to find points they might want to pick and reference from previous responses. Particularly when each iteration of AI output is long and extends beyond the viewport, they easily getlost when scrollingthrough multiple variants of their work product.  Excessive scrolling is also a problem when users must compare iterations to track the changes between them. This behavior is a significant point of friction, which we observed with all study participants.

Even after iterating and getting a satisfactory answer, most users still edit their final output outside the AI chatbot. This additional step is required because of the limitations of ChatGPT. Currently, ChatGPT struggles to:

When participants asked for time-sensitive information, they were often disappointed because the current iteration of ChatGPT uses a knowledge base that is a few years out of date.

For example, one participant generated a social media post for marketing but called out how ChatGPT doesn’t know what hashtags are trending right now. In another case, a participant added factual information that was not available to ChatGPT.

Some participants wanted to fine-tune parts of the response to match expectations around tone or level of detail and found it difficult to achieve that goal with ChatGPT.

For example, a participant generating a questionnaire added a few more questions manually by editing ChatGPT’s response in a text editor. Another participant removed greetings from the start of an email draft produced by ChatGPT because it was not how she would usually start the email.

Some users were dissatisfied with how ChatGPT formatted a response, especially for high-fidelity outputs. In these cases, we observed participants making changes like formatting text as bullet points or removing unnecessary subheadings.

Many analysts claim that chatbots solve most usability problems through their simple, conversational user interface. You say something, and the computer answers back. You can’t get lost in this linear interaction the way you can on a website. Even better, AI offersintent-based outcome specification: users simply say what they want, and the bot delivers.

In your dreams.In reality, our user study found that users almost always engage in multistep iteration because the AI doesn’t deliver exactly what the user wants — it can only guess at the intent.

At this point,theconversational user interface stops being easy. Users must perform significant extra work to modify the output to suit their needs. Even worse, the current endlessly scrolling chat window offers poor support for the additional behaviors we documented in this study. As we’ve seen, linear or not,people get lost when scrolling.

It should come as no surprise to any UX professional with a minimum awareness of the field’s history that new interaction styles introduce new usability problems, even as they alleviate old ones. Graphical user interfaces (GUI) freed users from having to remember and type command names but at the cost of requiring an information architecture for distributing commands across menus. As a result, poorly designed GUIs made it hard to find known commands and had poor discoverability for new features.

Similarly, AI frees users from the tedious work needed to produce text in a word processor or draw images with visual software. However, currentAI tools have many usability problemsthat could have been avoided through quick-and-simpleusability testinglike our study.

As we have demonstrated,AI is actively creating new user behaviors.This is very similar to the way the immense growth of online information on the web led to theprimacy of searchamong all information-seeking behaviors. New behaviors require new designs to support users.AI tools are currently metaphorically similar to the websites of 1993and will need to get much better.

Accordion editing and apple picking are behaviors directly caused by existing generative AI tools and their limitations. As generative AI tools evolve, these behaviors are likely also to evolve.

Both behaviors solidify the need for the following improvements to AI systems:

Design innovative, trusted, and useful AI products and features

Artificial Intelligence

Strategically combine content, visuals, and interactive components to design successful web pages

Interaction