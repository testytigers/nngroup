# Promptframes: Evolving the Wireframe for the Age of AI

**Author:** Evan SunwallEvan SunwallMay 17, 20242024-05-17

**Topics:** Artificial Intelligence, Prototyping

**Source:** https://www.nngroup.com/articles/promptframes/

---

May 17, 20242024-05-17

Share

Using placeholder text or images early in your design workflow can help you explore possibilities and cope with evolving requirements.

However, placeholder content (especially the notorious lorem ipsum) can be a barrier to gathering insightful feedback from users and stakeholders. I have personally experienced derailedusability testingsessions because my placeholders provoked unintentional confusion and doubt in my participants. (And folks like Anna Kaley have previously highlighted the benefits of taking acontent-focused approachin early design work.) In UX, remember thatthe content inspires feedback,not the container.

To enable a more efficient feedback loop,I propose a new design deliverable: the promptframe. Use promptframes to create realistic placeholder content faster using AI.

Promptframes unite the classic UX wireframe with prompt writing for generative AI.

Apromptframeis a design deliverable that documents content goals and requirements for generative-AI promptsbased on a wireframe’s layout and functionality.

Promptframes organize and document prompts locationally within an existing wireframe. UX designers can create promptframes early in the design process as they begin crafting interfaces to address requirements. Promptframes describe the goals, purpose, requirements, and other details of the content that goes within various design elements, so that AI can readily assist with content ideation and generation.

Wireframes can sometimes create problems for UX designers:

Promptframes address these issues in several ways:

Conduct your early-stage UX design process normally usingsketches and simple wireframes. This work will serve as the foundation for your promptframes once it is digitized in your design tool.

To illustrate promptframes in the design process, we will use hypothetical examples based on apage from Blue Apron's websitedescribing a special promotional offer for people in community-service roles.

Documenting and sharing context with the generative AI will improve its ability to assist with content creation. ChatGPT is particularly well suited for promptframes due to its support for various output types.

Consider including these important high-level details in your prompts.

Category

Details

Example

Role

The role(s) that the generative AI will play (e.g., content strategist, graphic designer, video producer, data analyst), and the type of content it must create

As an expert Content Strategist, you will generate engaging website copy…

Organization

The organization's mission and how it serves its customers and clients

You work for Blue Apron, a company aiming to make tasty home cooking accessible to everyone…

Objectives

The crossfunctional goals of the experience and what success looks like for the project (e.g., persuading visitors to sign up for a service, successfully scheduling a sales consultation, completing a workflow quickly and confidently)

In general, Blue Apron wants user experiences that increase meal kit subscription sign-up rates, improve customer retention and satisfaction, and streamline the meal selection and checkout process…

Tone of voice

Thetone of voicethat should be used in all generated copy to align with the brand (reuse any tone of voice documentation from marketing or design-system resources if they exist.)

Your copy should inspire confidence in the kitchen, emphasizing simplicity, nutrition, and culinary delight…

Definitions

A glossary of unique terms your organization uses, including its products and services or competitors' names

Mealkit: a collection of pre-measured ingredients with recipes shipped to the customer’s home…

Visual principles

Documented stylistic guidance for any visual assets (e.g., a design system likeShopify Polaris design systemto describe desirable illustrations' color, shape, lines, and other aspects)

Visuals should use vibrant colors that reflect fresh and healthy ingredients…

Variations

The number of divergent variations for all AI output (you will usually want 3–5 variations) (Variations are a crucial advantage of using generative AI, regardless of the generated content, but some AI tools may generate only few, if any, variations to manage their operating costs.)

For each request, you must generate 2-3 divergent variations of outputs, whether textual, visual, or data-driven…

Generative AI also needsuser insightsto be effective. Share written content from high-qualitypersonas or archetypesthat mention user needs, behaviors, goals, pain points, as well as motivations for the product, service, or feature being designed.

All this specificity will give you better results than just using off-the-shelf AI agents that proclaim to fulfill similar content-generation roles. Although this looks like a lot of effort to write or compile, you need to do this only once and can reuse them throughout this project or others.

Remember to leverage AI-tool features that maintain this context. For example, ChatGPT offers a custom-GPT feature that conveniently persists these details. Other AI tools like Gemini or Claude currently don’t support easy reuse of context; for those tools, you will need to capture these details (perhaps in a text document) and feed them into your prompt before discussing project specifics.

With the context and users established with our AI tool, the next step is to document prompts that will direct the AI in content creation. Start by writing down the purpose of the various areas and elements in your design that will contain content.

Always include these details in your prompts:

Here areadditional aspectsto consider for specific types of content:

Some generative AI systems are capable of photorealistic content, but some vendors prohibit its creation as a precaution against abuse and misinformation. Don't waste time trying to work around these prohibitions if your current AI tool won't comply. You may need to use a different AI tool or settle for less than true-to-life images.

Copy and paste the prompts into your AI tool. Then integrate the generated content in the wireframe to start evolving it into a prototype. To keep your work organized, document links to separate AI-tool chats in the promptframe, as you will likely revisit them in future revisions.

When performing this step:

As you conductdesign critiqueswith your collaborators, review the AI-generated content or the prompts that were used. Parts may be added, revised, or dropped — which is normal — but you should always be progressing towards greater content fidelity in all aspects of the design.

Think of the AI-generated content as a provocation for your colleagues — is this content aligned with our project and user's goals? Why or why not? Capture that feedback by revising the prompts. If there's considerable disagreement, consider splitting the design into 2 prototypes for testing.

Remember, promptframing aims to quickly construct atestable design with meaningful content. Consider the tasks you want participants to perform with the proposed design and use them to influence your prompt writing and content-creation strategy.

Following this process should buy you more time, and skilled UX professionals know to reinvest those time-dividends into iteration. Revise your prompts with your research insights and regenerate new content for future testing. Weaker parts should be scrapped or have their prompt revised before rerunning it in the generative AI tool.

Once you have finished iteration, give your successful prototype the "human white-glove treatment" and elevate it with more content, visual, or interactive fidelity.Human effort will still be required to create the final design!However, you should have received a higher volume of richer feedback covering more design ideas, resulting in an overall more effective design. You can even share your prompts with other human collaborators to give them additional context on the prototype.

UX-design tools are currently exploring generative AI. Some vendors make bold claims, but their practical utility to UX professionals is not so bold (see ourreview of the current state of AI tools for UX design.) These tools may someday output robust experiences with basic prompting, but what's likely to happen currently is a mishmash of incoherent material derived from commonplace design patterns needing an excessive amount of rework to be useful.Whether machine or human — garbage in is garbage out.

Promptframes acknowledge that current generative-AI technology can be practical and helpful in the UX-design workflow. But they nudge us to chunk content challenges into well-documented pieces and don't excuse us from thinking and deciding what is needed and why from a user perspective. Instead, they accelerate our ability to check our assumptions with content that users can meaningfully evaluate and give us feedback on.

Perhaps future UX-design tools will offer better support for documenting prompt inputs and their associated generated outputs to help designers create and refine promptframes efficiently within their project's context. Passing a designer’s prompt via an API call to a generative AI platform is simply not enough.

No single UX deliverable can do it all. There are a few precautions to consider specifically with promptframes.

Promptframes, like their wireframe cousins, are not suitable for reviews with executives. People cognitively distant from a project typically need high visual and content fidelity to understand design deliverables. At a minimum, promptframes can convey some forward progress (you've been hard at work making something for this project) but don't expect early-stage promptframes to be particularly helpful in a design review with stakeholders deciding the project's direction or future investment.

Depending on the details provided in the prompts and the generative AI's robustness, the resulting AI-generated content will vary wildly in quality. Images may be inconsistently styled, and copy will undoubtedly need editing. Remember, the goal is not pixel-perfect, launch-ready content but to havesensible content fasterso colleagues or testing participants might reasonably understand and share insightful feedback.

Some organizations regulate the use of generative AI tools to protect their data. Be aware of and adhere to these before using promptframes.

Many UX professionals are a1-person UX teamor work in environments with lowUX maturity, with few resources or specialized collaborators. These folks benefit from augmenting their workflow to accommodate an AI content assistant, particularly if writing or graphic design are not strong skills.

However, what if you can collaborate with a content strategist or UX writer? That’s wonderful! Think of promptframes as a collaborative deliverable with these roles, which are (unfortunately) often included very late in the design process. Use the same general workflow described above to get their feedback and suggestions into the design early so their contributions can be tested along with yours.

Promptframes combine our thinking of content containers with a greater emphasis on the content itself in a way that enables generative AI to accelerate our workflow for user testing and feedback. Lorem ipsum as a placeholder practice is as dead as Latin is as a spoken language. Leave Cicero to the philosophers and use promptframes to rapidly create content your users can understand.

Effectively communicate ideas and findings to managers, collaborators, and other stakeholders

Interaction