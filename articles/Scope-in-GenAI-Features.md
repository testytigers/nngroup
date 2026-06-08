# Scope in GenAI Features

**Author:** Kate MoranKate MoranFebruary 28, 20252025-02-28

**Topics:** Artificial Intelligence, Interaction Design

**Source:** https://www.nngroup.com/articles/scope-ai-features/

---

February 28, 20252025-02-28

Share

When designing an AI feature, its scope (how broad or narrow its capabilities are) influences its usability. Our research shows that narrower AI features are (typically) easier for new users to understand and adopt. This article compares broad AI systems like ChatGPT with narrow AI tools like Spotify’s playlist generator, exploring how scope impacts design.

Before beginning to design a UI for any user-facing AI-powered feature, teams should answer these 4 strategic questions:

If, after these considerations, an AI solution still seems the best course of action, the next aspect to consider is the feature’s scope. Scope is a useful way to categorizeinteractive, user-facing AI features or products— in other words, how broad or narrow the AI system’s capabilities are.

The scopeof an AI feature describes the breadth of its data inputs and functionality. The broader the scope, the more variety of inputs the system can accept and the wider the range of possible outputs the system can produce.

Scope can be defined for any type of system, AI or not, user-facing or running in the back end. However, this article focuses on interactive, user-facing AI features.

For an AI feature, its scope is determined by the:

The scope of any given AI feature or product has significant implications for its design and usability.

Some systems, like ChatGPT or Claude, are very broad in scope. They can handle awide variety of tasksand respond to open-ended user inputs.Some canaccept many types of input data,including images, videos, or other file types. Some have access to the live internet, while others operate with static datasets. These broad-scope systems can alsoproduce a variety of outputs.

AI-powered smart assistants and agentic AI tools have even broader scopes, by accessing data and interacting with multiple apps and websites. (Although, at the time of writing, agentic AI’s unreliable performance holds it back from widespread use.)

These systems do have some constraints — for example, they all impose limitations on the size of the input (tokens) they accept. Most also have “safety” constraints around what they can provide information on. (For example, ChatGPT isn’t supposed to tell you how to build a bomb.)

ChatGPT and Perplexity are both very broad-scope AI systems. However, Perplexity is slightly narrower in scope, because (unlike ChatGPT) it is specifically designed for information seeking (it brands itself as an “answer engine”).

Even this slight narrowing in scope has massive design implications. A more specific use case (even if it’s still very broad) allows for a more tailored interface design. Perplexity’s VP of design, Henry Modisett, said as much in ourpodcast conversationlast year:

“Open AI is building a platform that’s going to have to work for all kinds of use cases that we’re not thinking about.”

Henry Modisett, VP of Design at Perplexity AI

Comparing the interfaces of ChatGPT and Perplexity, these differences are clearly visible.

On the opposite side of the spectrum, narrow-scope AI features serve a very specific purpose and generally support a single task or goal. They are not as versatile or powerful as broad-scope AI features, but their purpose is more immediately clear to users.

Let’s look at two narrow-scope features as examples: Spotify’s playlist creator and Photoshop’s generative fill.

Spotify’s AI-powered playlist creator is an example of a moderately narrow AI tool. While it does have a chatbot interface for collecting input, it’s constrained to a single purpose — creating a playlist based on the user’s requests.

Within that scope, users still have plenty of freedom. They can request a specific artist, era, genre, or vibe. But, unlike ChatGPT and Perplexity, they can’t ask Spotify’s playlist generator to, say, write a sonnet about tacos.

Again, this narrower scope allows for a more tailored experience. For example,the prompt suggestions are all specificto this use case and therefore are more likely to be relevant to users.Prompt writing is easier,because the tool already "understands" its purpose and how to achieve it with minimal textual input from the users. People in our study wrote very short, search-style prompts. In some cases, participants only used one or two words.

Because the feature's output(the playlist)is predictible(a small set of songs),it can be structuredin the interface. Before creating the playlist, users can sample, remove, or save suggested songs.

With some narrow AI tools, like Photoshop’s generative-fill feature, text prompting may not be needed at all.

Broad AI Systems

Narrow AI Features

Product Context

More likely to be stand-alone products or chat boxes

Task-specific features within apps or websites

Inputs and Prompts

May accept a wide variety of data and file typesLikely to use an open text field

More restrictions on the instructions or size and types of input

May not accept text or prompt input at all

Functionality

More flexible

More constrained

Interface

Can be very simple -- essentially a chat box

Richer in UI controls; may not be chat-based

In our recent qualitative usability study,narrow-scope AI features tended to perform betterthan open-ended, broad-scope features. With narrower scopes, participants found it easier to:

In general (though not in every instance), participants also provided more-positive feedback about narrowly scoped features.

TripAdvisor’s travel-itinerary planner is on the narrow side of the AI-scope spectrum. As a result, the feature’s UI is a prompt wizard that walks users through selecting a destination, interests, and travel dates. This guidance prevents users from having to formulate a free-text prompt and reducescognitive loadas well as the risk of errors (for example, incorrect dates).

Several of our study participants reported using ChatGPT and other broad AI chats in their work and personal life. However, after they used TripAdvisor’s prompt wizard, two participants admitted that they had never thought to ask tools like ChatGPT for travel-planning help.

A broad AI system’svast capabilities don’t matter if users don’t know they existor don’t know how to use them for that purpose.

In another session, a different participant, who hadn’t seen TripAdvisor’s narrow feature, started planning her trip with ChatGPT. Without that priming, she had to spend time deciding what details to provide in her prompt. “Let’s see,” she said thoughtfully before beginning her prompt. “With AI, it’s like talking to a kid. You have to list everything, so I have to think…”

In her initial prompt, she included the destination (Bali) and asked for advice on what time of year to visit. ChatGPT was easily able to help answer that question, which was not a functionality available in TripAdvisor’s AI feature (a benefit of ChatGPT’s broader scope).

While the participant appreciated that guidance, ChatGPT’s output was difficult to assess and customize. It responded with two hotel options, 4-stars or 5-stars. At least one of these options, St. Regis, was out of her budget — a detail she didn’t think to include in the prompt. The participant ignored the included source links, and instead searched for these on Google.

Compare that simple text output (necessary for such a broad system) to the structured response from TripAdvisor’s feature: because it’s designed for this exact purpose, the results were much easier for participants to explore. Each hotel option was presented next to a map of the travel location, showing its proximity to local sites of interest. When clicked, an overlay with more details about the hotel appeared in-context.

While ChatGPT offered much more functionality than TripAdvisor, it required more effort from users — in both prompting (input) and working with the results (output).

This shouldn’t surprise experienced UX professionals — it’s an example of theflexibility-usability tradeoff, which states that the more flexible a system is, the lower its usability will be. In other words, more features = more complexity = lower usability.

A broader scope of AI features is more challenging for users because it requires them to:

Note thatthis doesn’t mean we should only design simple, low-functionality systems(AI or otherwise). We just need to acknowledge that additional functionality may make those systems more challenging to use and ensure that the tradeoff is justified by our user and business needs. Additionally,narrow-scope AI features are not immune to usability problems— we observed plenty in our study. (We’ll be elaborating on that in future articles soon.)

Interestingly, in traditional designs, increasing functionality usually means increasing the amount ofstuffthat appears in an interface. In AI systems, the opposite is true —a narrow scope offers the possibility of exposing more of the system’s functionalitythrough UI elements, thus making it more approachable to users.

In addition, I think there’s a confounding variable at play here — the understanding of user needs. A narrow-scope AI feature that’s been crafted for a specific purpose is less likely to be a carelessly slapped-on AI feature. To have a narrow use case, someone is more likely to have spent time thinking about the users’ workflows and how AI could benefit them. In contrast, especially in peak AI hype, we’ve seen many broad AI chats crammed into interfaces without much thought about their actual purpose.

This point brings us back where we started and where all AI integration conversations need to start: at the user and business needs. Depending on your product, users, and business, the AI feature you decide to build could sit anywhere on the scope spectrum and be successful. The key to pulling that off will be making sure it’s appropriately scoped for your specific context.

Design innovative, trusted, and useful AI products and features

Artificial Intelligence

Design how users connect, navigate, and engage with your interfaces

Interaction