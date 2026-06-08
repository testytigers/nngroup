# CARE: Structure for Crafting AI Prompts

**Author:** Kate MoranKate MoranMay 24, 20242024-05-24

**Topics:** Artificial Intelligence

**Source:** https://www.nngroup.com/articles/careful-prompts/

---

May 24, 20242024-05-24

Share

Text-based generative AI tools (like OpenAI’s ChatGPT, Anthropic’s Claude, and Google’s Gemini) can be extremely useful — but only when given the right instructions.

Use the acronymCARE (context, ask, rules, and examples)to remember what information to give AI tools to achieve your desired results. This article demonstrates how to use the CARE framework specifically for UX work.

To get better results from a generative AI chatbot, write your prompts CAREfully.

Include these four key components in your prompts:

While CARE is a helpful mnemonic for remembering the components, you don’t always have to write prompts in this exact order.

You also will not need such detailed prompts for every interaction with generative AI. General information-seeking tasks may not require giving the AI this much information. However, when looking for complex or specific outputs, provide more details to ensure you get results from AI that meet your expectations.

Establish theframingfor your prompt.

For example, imagine we’re using ChatGPT to help us write an error message for a login screen, following the CARE framework to help us write the prompt. To provide the AI chatbot with context, we might explain the situation using the following types of details.

Your job role or experience level

I’m a senior UX designer with 15 years of experience

Where you live

based in Canada

The product you work on

working on an ecommerce site

The type of company you work for

for a large international eyewear retailer that sells sunglasses and prescription eyeglasses.

The project you’re currently working on

I’m currently designing the login screen, where customers sign in to access their accounts.

User profiles, research findings, or deliverables

Our customers are fashion-conscious young adults who value quality, authenticity, and self-expression.

One or more screenshots

Review the attached screenshot to reference the screen I’m currently designing.

The task you’re working on

I’m working on an error message users will see if they attempt to log in with credentials (email and password) that don't match what is in our system.

Focus on what’s relevant for the task. If you were speaking to a new consultant or team member, how would you explain your situation before asking for advice or help?

Depending on the AI tool you’re using, you may not need to enter details about yourself each time you start a new conversation. For example, ChatGPT offers acustom instructionsfeature where you can provide contextual information for the system to remember and consider for all future results.

Additionally, in early 2024, OpenAI introducedpersistent memoryin ChatGPT. With this feature enabled, ChatGPT will learn and remember context about you based on information you’ve shared in past prompts to use in future results (If this sounds creepy, you can turn it off).

This is therequestyou’re asking the AI chatbot to perform. Whether you phrase the ask as a question or command, it’s important to be specific.

For example, you may include the following details in your requests:

Role

You’re a UX writer focusing on intuitive, straightforward, plain language.

Output, Number, and Steps

Follow these steps. Don’t skip any steps.

Format

Present the final 5 options in a table, with the error messages in the first column and your reasoning in the second column.

The steps listed in the table above are an example ofchain-of-thought prompting.

Chain-of-thought promptingis a technique in which a task is broken down into a series of discrete ordered steps, which can help an AI model approach solving the problem more systematically.

Generative AI will produce better results if you provide guardrails and constraints that help it understand what you want it to do or avoid.

For example, when asking AI to help us write error messages for our login screen, we can include guidelines for writing goodUX copyforerror messageswe want the bot to follow. We can also include product or brand-specific rules, such as tone-of-voice guidelines, and design constraints to consider, such as the amount of space in which the copy should fit or a maximum character count.

Best Practices

Use plain language

Don’t be funny or clever

Don’t obscure the message’s meaning

Offer solutions and recommendations

Don’t blame the user

Avoid passive voice

Style Guide

Tone of voice words:

Approachable and conversational, but not too casual or sloppy

Limits

No more than 100 characters

No more than 2 sentences

Whether good or bad, providing examples of what you do (or don’t) want the generative AI chatbot to produce can help it better understand what you need.

For example, if you’re trying to improve an existing error message, include it in your prompt and describe what you don’t like about it or what needs improvement.

Good Example

Provide constructive suggestions for fixing the problem. For example, “Add $12 more for free shipping” works well as a message in the shopping cart because it very clearly specifies what users should do to achieve their goal.

Bad Example

Avoid error messages like this: “Oopsie, we couldn’t log you in.” It’s too casual in a frustrating situation.

Existing Ideas

Our developer suggested the error message, “Invalid credentials; please check your email and password." This sounds a bit too techy and formal.

Providing examples in AI prompts is similar to a popular prompting technique calledfew-shot prompting.While related, the two approaches aren’t exactly the same. Few-shot prompting emphasizes inputting exact input-output examples for the system to reference and respond similarly.

Few-shot promptinginvolves providing a few examples of input-output pairs to help the model understand how it should process similar inputs.

For this example of writing error messages for a login screen, we don’t need to give the AI the input-output pairs -- only the output examples of what we do or don’t want.

In other cases, such as using AI to generate ideas for article titles, we could use few-shot prompting to provide examples, with summaries from several articles as inputs and accompanying title ideas as outputs.

You don’t have to include all the details in the CARE frameworkfor every prompt. Pick out the pieces and order your commands in a way that’s most relevant and helpful for you and the AI chatbot.

In our example using AI to write error messages for the login screen, we could combine the following elements to produce a CAREful prompt.

Background:

I’m a senior UX designer with 15 years of experience working on an ecommerce site for a large international eyewear retailer that sells sunglasses and prescription eyeglasses.

I’m designing the login screen, where customers will sign in to access their account details.

I’m currently working on an error message that will be shown to a user if they attempt to log in with credentials (email and password) that don't match what we have in our system.

Your role:

You’re a UX writer focusing on intuitive, straightforward, plain language.

Steps:

Follow these steps. Don’t skip any steps.

Guidelines:

Follow these guidelines when you generate and evaluate the error messages.

Examples:Provide constructive suggestions for fixing the problem. For example, “Add $12 more for free shipping” works well as a message in the shopping cart because it very clearly specifies what users should do to achieve their goal.

Avoid error messages like this: “Oopsie, we couldn’t log you in.” It’s too casual in a frustrating situation.

Our developer suggested the error message, “Invalid credentials; please check your email and password." This sounds a bit too techy and formal.

Ask me for additional information you need to do this. If there’s nothing else you need, complete the steps.

When I ran this CAREful prompt in ChatGPT (using GPT-4o, the latest model as of this article’s publication), here’s the final table it gave me. A pretty decent set of options!

Error Message

Reasoning

Please check your email and password and try again.

Simple, direct, and provides a clear next step.

The email or password doesn’t match our records. Try again.

Clear explanation and straightforward instruction to retry.

The email or password you entered is invalid. Please re-enter them.

A clear indication of the problem and a solution.

We couldn't log you in. Please check your email and password.

Polite, clear, and provides a next step.

Those credentials don’t match our records. Try again.

Clear and to the point, with an easy-to-follow action.

I find it’s very rare that I can just accept genAI’s output exactly as it’s returned to me. (This is especially true with writing, but I’m picky about that.) Even with a very comprehensive, CAREful prompt, you’ll probably have some additional steps to complete once you get your output.

Tryresetting your password,orcontact usfor help.

If this seems like it’s a lot of work, that’s because it is.With current genAI tools and models, this amount of strategic context is often necessary to achieve good outputs. AI chatbots are praised for their time-saving abilities, but they can be a time suck too. It can take significant amounts of time to craft and iterate on CAREful prompts — sometimes more time than you’d have spent just doing a task the old-fashioned way.

For example, I’m an experienced writer. With all of the steps I’ve outlined above, I could have just written an error message myself with less time and effort. But that may not be the case for someone else with less experience in writing.

Different people will find that genAI is more or less helpful with different tasks.Like most skills, this is another thing you acquire with practice -- a better sense of when this level of in-depth prompting might save you or cost you time.

GenAI tools are better and more useful for certain tasks than others.Writing a CAREful prompt won’t matter if you’re asking ChatGPT to perform a task it just isn’t capable of doing (or doing well). For example, ChatGPT can’t (and shouldn’t) do your taxes for you, whether you prompt it CAREfully or not. Smaller, more focused tasks tend to yield better results.

Keep practicing with CAREful prompts.The more you experiment with generative AI, the more you’ll see how and where it’s useful in your UX work. You’ll also become more keenly aware of where AI tends to fail or get confused. This will help you learn when to use genAI, and how to craft your prompts accordingly.

Leverage AI to enhance creativity, efficiency, and impact in everyday design work

Artificial Intelligence

The AI-assisted user research workflow

Artificial Intelligence

Design innovative, trusted, and useful AI products and features

Artificial Intelligence