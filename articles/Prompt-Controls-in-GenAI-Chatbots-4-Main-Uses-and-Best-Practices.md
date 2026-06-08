# Prompt Controls in GenAI Chatbots: 4 Main Uses and Best Practices

**Author:** Feifei LiuFeifei LiuAugust 2, 20242024-08-02

**Topics:** Artificial Intelligence, Design Patterns

**Source:** https://www.nngroup.com/articles/prompt-controls-genai/

---

August 2, 20242024-08-02

Share

Generative AI (genAI) chatbots, such as ChatGPT and Perplexity, rely heavily ontext promptsfrom their users. As these interfaces continue to evolve, AI chatbot designers have started tointroduce additional UI controlsin addition to the simple prompt field and thus createhybrid UIsfor genAI chatbots.

Definition:Prompt controlsare UI components that surround the input field in an AI-chatbot interface. Their role is to expedite and supplement text input.

Prompt controls can be displayed in different formats, such as buttons, tooltips, toggles, cards, and menus.

Prompt controls help users expedite prompting, clarify ambiguity, and get inspiration. They also facilitate followups. Ultimately, they helpovercome the articulation barrierand, thus, lead to more-useful bot responses, benefiting both existing andnew users.

According to our research of prominent text-based genAI chatbots in the US and China, there are four ways in which prompt controls are used in these interfaces:

Unlike pure text-based UIs, prompt controls allow users to discover the different bot capabilities and, as a result, have lowerinteraction costs: people don’t have to ask the bot whether it can do a certain task (“can you” promptsare common among new users).

For instance, inour diary study of an early version of ChatGPT(that couldn’t access the internet or accept uploaded files), one participant wanted the bot to summarize an online report. After several prompt exchanges, he finally understood that he would have to copy and paste the 100-page report. He deemed this approach extremely painful and stopped using the bot for document summarization.

With the current ChatGPT, users can uploaddiverse types of files to supplement their text requests or choose files from online storage services like Google Drive. Still, people need to ask the bot about the types of files it accepts. In contrast, Baidu's Ernie bot indicates the supported file formats in a tooltip as users hovered over the upload icon.

Our research found thatnew users had a difficult time understanding what a genAI bot can do and how it can be used. Visible prompt controls can offer a glimpse into what kinds of tasks genAI can be used for. (Don’t forget that, worldwide, many online users are still new to GenAI. For instance, aReuters survey found that 19% of US participants and 30% of UK participants have never heard of any of most popular GenAI tools, including ChatGPT, Google Gemini, or Microsoft Copilot.)

For example, the Chinese AI chatbot SparkDesk shows a list of plugins next to the prompt. One of them,Smart PPT Generation,generates PowerPoint files; this feature would have been a lot harder to discover without the prompt controls.

A common pattern that is starting to emerge in genAI bots is the inclusion of one or moreconversation starters.These are task examples that aim to teach users what the bot can do.

Some Chinese GenAI tools, like ChatGLM, provided a comprehensive library of prompts calledInspiration Centerin the side panel. About 10 prompts were listed in the panel, allowing users to directly use them or edit the example prompt by clicking theediticon. High-level tags likeWriting, Developers,andParentsat the top of the panel allowed people to browse more prompt examples in that category.

Prompt controls are also used to set constraints to conversations with chatbots. For example, they can specify the scope that users want the bot to focus on or a specific output format.

For instance, theFocusfeature in Perplexity allowed users to scope a specific domain to focus on, narrowing down the conversation from the beginning , like ascoped search experiencewould narrow down search.

The Chinese GenAI chatbot Baidu’s Ernie bot allowed users todesignate output specificationswhen they were working with certain plugins. For instance, after turning on the pluginTreeMind, users could create diagrams such as a fishbone diagram and directly edit the output as needed.

In a diary study with genAI users, we found thathalf of all conversations contained a followup action, and 77% of the conversations included more than 1 exchange. Followups and multi-prompt exchanges were especially likely when peopleexploreda new topic — in these cases, they would use subsequent interactions to acquire more in-depth knowledge on that topic.

Thus, another main function that prompt controls serve is to facilitate the back-and-forth followup process. ChatGPT’s UIfeatured a nice set of followup actionsthat users could take upon receiving an answer:

Sometimes, people also refer to previous responses and ask the bot to modify a specific part, especially when working on text generation and editing tasks (a behavior known as apple-picking). Some chatbots (like the Chinese genAI chatbot ChatGLM) provide an inline quotation feature that decreases the amount of user effort for this interaction. Users need only to highlight and quote, instead of highlighting, copying and pasting in the input field.

Google Gemini went one step further and integrated commonly used simple followup requests such asShorter, Longer,andMore casualinto a modification button. These requests can be helpful for text-generation tasks.

Some chatbots provide relevant followup question suggestions as users start a conversation. These followup questions serve two functions:

For instance, when asked about foldable smartphones, Perplexity provided three related questions and options toSearch VideosandGenerate Images,since foldable smartphones could be demonstrated more effectively via video.

Based on the top usability issues we observed in both US and Chinese genAI chatbots, we offer 4 tips for prompt controls.

We’ve argued thaticons need labelsfor a long time because there are few universally recognized icons. In the context of GenAI tools, pairing icons with descriptive labels is even more importantbecause users tend to have little domain knowledge and have not yet formedmental modelsfor how these bots work and what they can do.In this case, using unconventional icons without accompanying text labels can cause even more confusion.

ChatGLM, a Chinese GenAI chatbot, included straightforward, standard icons for favorites, thumbs-up, thumbs-down, copy, or share at the bottom of each reply. All participants in our study readily understood these icons.

If apps use novel icons to represent new, unfamiliar features, people might not be able to guess what the associated buttons may do and ignore the feature.

For instance, the Baidu’s Ernie mobile app used a magic wand icon beside the input field, to represent a set of prompt examples. None of our study participants understood what that icon meant; one user commented:

“I initially thought [is that] it would show me images, like emojis.”

A previous version of Bing Chat used a broom icon for starting a new conversation. This icon was not easy to understand. Luckily, a more recent version fixed this issue by using a more relevant icon (a conversation icon with a plus sign at the bottom right) together with the labelNew topicupon hovering.

Another common issue we observed was the use of vague, branded names for prompt controls. When labels accompanying icons fail to precisely describe their functionality, they don’t add context effectively. Baidu’s Ernie bot had a plugin namedThink Carefully.One participant asked,

“‘Think Carefully’. So, think carefully about what?”

Another plugin’s label was ambiguous. The Chinese name of the plugin was "一键流影", which was intended to meanOne-click to transfer videos. However, one character in this label,流, has multiple meanings in Chinese, such asstream,flow,circulate, andfluid. A few study participants were uncertain about the plugin's function. Renaming itText to Video(文字转视频) could remove the ambiguity.

Users can feel overwhelmed when presented with lots of new features at once. We can guide them through a new interface by grouping elements that are related (thus, applyingthe Gestalt principle of proximity). Some genAI tools in our study failed to properly group prompt controls, increasing the learning cost and the chance that users would overlook those components.

For instance, a previous version of Baidu’s Ernie bot included a plugin hub, where users could choose to enable specific functionalities of the bot, such as creating a video based on text. However, the list of plugins was overwhelmingly long (10–15 items), and the functions they served varied a lot, including:

In addition, these distinct functions were hidden in the samePluginbutton and named with branded labels, which further lowered their discoverability. In our study, when asked to create a video using the Ernie bot, none of the participants found the hidden text-to-video feature within the plugin hub. Even after the researcher pointed them to the right place, it took them quite a bit to understand what each plugin was for.

Grouping plugins with similar functionality under clearly labeled categories can help users understand their purpose more quickly and smoothly.

In contrast, Perplexity separated 2 features,FocusandAttach, instead of putting them in one contextual menu, since they served different purposes: the former was to set the scope of the conversation, while the latter allowed users to provide more background information. Still, since they both served to ask for user input on context, they were placed next to each other and far away from theSendicon or the toggle to switch toPro.

The last but not least-common mistake made by genAI tools is failing to followexisting design conventions.Unconventional design patterns, even when deployed with good intentions, can cause confusion, increasing the perceived complexity of tools. This is because users’ mental models tend to have strong inertia and are based on their prior experience with thousands ofother products. AsJakob’s law of Internet user experiencesays, users spend most of their time with much more time on other products than yours, so it’s always safer to obey current design conventions unless you have strong reasons to do so again.

In our study, we encountered many cases where violating design conventions caused confusion, both intentionally and unintentionally.

For instance, ChatGLM’s mobile app hijacked the normal gesture of long-pressing a previous entry to show theCopytooltip. Whenever a user performed that gesture, the app would copy and paste the full prompt text. However, this greatly confused study participants and added extra burden for those who wanted to copy only a slice of a previous entry — they had no choice but to copy the full content and delete undesired parts.

In contrast, ChatGPT’s mobile app also repurposed the long press, but in a more thoughtful way that did not completely override the standard functionality. When a user long-pressed part of a previous prompt, it provided a contextual menu with multiple options, including copying the full message or selecting a text snippet.

Sometimes, design conventions are unintentionally violated on new products due to limited time. Though it might be important for the product and market teams to launch novel features as soon as possible, usability shouldn’t be sacrificed in the process.

For instance, in our study, the Ernie bot would tell users that it couldn’t process documents larger than 10MB only after users uploaded a file exceeding the size limit. Moreover, the error message was displayed in a smallnonmodal popupat the top of the screen, far from theUploadbutton (at the bottom right of the screen). One study participant tried to upload the same file multiple times and was confused as to why nothing happened — he totally overlooked the error message, also because the popup was automatically dismissed upon any click or scroll.

Prompt controls in genAI chatbots increase the usability by decreasing the interaction cost, as commonly used commands can be executed with a click instead of typing.

Designers for prompt-based genAI tools should look for opportunities to better integrate prompt controlsinto the conversational interface, withthe goal of minimizing manual input, increasing feature discoverability, and allowing users to easily set scope and other constraints for their conversations, as well as get inspiration, and easily follow up with additional prompts.

Design innovative, trusted, and useful AI products and features

Artificial Intelligence