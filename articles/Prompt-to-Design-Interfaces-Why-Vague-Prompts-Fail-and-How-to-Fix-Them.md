# Prompt to Design Interfaces: Why Vague Prompts Fail and How to Fix Them

**Author:** Huei-Hsin WangHuei-Hsin WangDecember 5, 20252025-12-05

**Topics:** Artificial Intelligence, Design Process, Interaction Design

**Source:** https://www.nngroup.com/articles/vague-prototyping/

---

December 5, 20252025-12-05

Share

The rise of GenAI tools has introduced a new paradigm for design work — rather than crafting interfaces bydirectly manipulatingelements in design tools, designers can prompt AI-prototyping tools to generate designs.

When you’re working with AI, the output quality will be largely dependent on the specificity of the prompt. This article discusses common issues with vague text prompts and offers recommendations on how to achieve better results from AI-prototyping tools without undertaking the bulk of the design work yourself.

When weasked AI-prototyping tools to generate a live-training profile page for NN/G course attendees, a detailed prompt yielded quality results resembling what a human designer created, whereas a vague prompt generated inconsistent and unpredictable outcomes across the board. (For more information about the prompts and tools we used,see our description of the study methodology.)

A skilled human designer can take a broad design statement (such as “design a profile page that allows course attendees to do XYZ”), identify and prioritize the information users need to see on the page, choose the design patterns that support users in accomplishing their goals, and arrange elements in a logical layout that is easy to navigate. In contrast, AI struggles with ambiguity and is unable to deliver thoughtful results within a broad context.

While open-ended prompts may be fine for exploring diverse ideas in the early design phase, they fail to produce the precise outputs needed for all other design work.

However, writing long, detailed text prompts is rarely the default strategy in practice becauseproviding comprehensive detail takes timeand manyturn to AI precisely to reduce work.To get the most value from AI prototyping tools, designers need to understand how prompt specificity affects the AI’s output and tailor their prompting strategy to fit the task.

One of the most prominent patterns we saw across prototypes generated with broad prompts is theFrankenstein layout— designs that feelrandomly pieced togetherinstead of thoughtfully structured.

AI-prototyping tools demonstrate a surface-level understanding of individual UI components (e.g.,progress bars,list views). But when these elements are combined to create a page, the layouts often lack hierarchy, displaying a few common characteristics:

AI prototyping tools oftengenerate more elements than necessary in response to broadly scoped prompts.It’s like an inefficient navigation system thatcanget you to the destination but always takes a convoluted route.

Cluttered designs hurt everyone: users’cognitive loadandinteraction costincrease, important content risks being buried, and the system becomes more cumbersome, resulting in slower load times and more complex code for developers to manage.

In our testing, there were several instances wherethe same element or information was displayed multiple times.In contrast, in a real design, screen real estate is precious and user attention is scarce, so design teams rarely tolerate this redundancy. Repetition without purpose onlyadds noiseto the interface and distracts users from the key content.

Users expect information to follow a logical, intuitive sequence — typically moving from general to specific, with related items grouped together. This structure helps users buildmental modelsand reduces the effort needed to parse through and understand content.

MultipleAI-generated designs presented content in an illogical sequence.These disruptions, compounded by poor visual hierarchy, created disjointed layouts with no clear focus or sense of progression.

Visual hierarchyguides users to the most important elements on the page. The larger, more colorful, or more prominent an element, the greater its perceived importance relative to other items.

Whenhierarchy contradicts content priority,users may feel confused or distracted from completing the main tasks. This is a common flaw of AI-generated interfaces, which often place visual emphasis on the wrong element, as the model doesn’t have a contextual understanding of what is essential for the goal.

Another pattern that we noticed in the AI-generated designs wasthe unnecessary use of prominent containers displaying a single piece of numerical information.These containers tended to occupy a large amount of space but communicated little information; moreover, this information was secondary to the main user task.

In this section, we discuss 5 ways of improving the output of a vague text prompt without needing to design in Figma first or write extensive prompts. These strategies can be combined or used separately toincrease your input specificity.

When crafting prompts,clarity and specificitymatter more than sheer length. Many frontier AI models like ChatGPT5 are designed to follow instructions with laser focus.Verbosity without precisionhurts clarity—a concise, well-chosen keyword can often produce better results than a long but vague description.

When using AI-assisted design or coding tools, describe your intent by pointing to established design styles or frameworks instead of using generic visual descriptions likesimple,clean, andmodern. Referencing a recognizable visual design style — likeskeuomorphism,flat design,glassmorphism,orretro / Y2K— helps the model interpret your visual intent. This is where a good understanding of design vocabulary and ofvisual-design fundamentalsbecomes essential.

For example(assumingneobrutalismis the target visual style):

The same principle applies when prompting AI for code generation. Developers often includespecific frameworks and component libraries(e.g.,React,Next.js, orTailwind CSS) early in their prompts to shape the structure and logic of the generated code.

Designers can also reference a famous design system or brand style by its name. That said, avoid asking AI to imitate a specific brand. While it’s tempting to request “design like Apple” or “in Airbnb’s style,” copying an existing brand’s visual identity is not a sustainable strategy.Famous brands don’t guarantee good design.A design that works for a billion-dollar company might fail in your context due to different goals, audiences, or constraints.

High-fidelity mockups are effective for communicating your design vision to AI-prototyping tools, but they take time to create — often more than writing a detailed prompt. When you’re still early in the design process or lack the resources to produce polished assets, uselightweight visual referencesinstead, suchmoodboards, inspiration images, or screenshots of yourdesign system.

Do manage your expectations with this approach. Even though image references are a big step up from text-based descriptions, it’s unlikely for AI to achieve pixel-perfect precision.

When visual precision is essential, connect AI tools directly to your design source. Some tools have built-in features that can retrieve the visual spec and design tokens directly from a Figma frame. Developers can also leverageFigma MCPto pull in design details like design frames, variables, components, and layout data directly into their IDEs. These methods will achieve higher precision than image uploads.

Finally,don’t confuse visual fidelity with design quality.A visually polished AI-generated mockup that aligns with your design system can still be a poor design if the accompanying prompt is vague or underspecified. Evaluate the outcome for usability and clarity — not just for visual polish.

While most AI-prototyping tools support image uploads in addition to text prompting, not all do — and some limit image uploads to paid plans. An alternative is touse a general-purpose chatbot to analyze the visual style or layout of a page in natural language, then convert that description into a design prompt. This text-based approach can also be combined with an image attachment to further reinforce the intended visual direction.

Crafting prompts for AI-prototyping tools is a lot like creatingdesign specsfor handoffs. In both cases, designers need to define not only visual and layout details but also interaction flows, content, and accessibility.

We often recommendacontent-focuseddesign approach— that is,working with realistic data so that visual design supports the key contentrather than the other way around. The same principle applies when using AI-prototyping tools: providing sample content or data guides the AI to generate better designs.

Designers should collaborate with developers and content teams to obtain the data displayed in the interface. When real data isn’t available early in the process, designers can use AIto generate mock data first, then refine the content and iterate on the design based on that data.

When AI interprets images or documents instead of receiving direct input, some contextual details can get lost in translation. Therefore, the more direct the context you provide, the less interpretation the system needs to make — and the higher the accuracy of the output. One of the most direct forms of context you can provide to an AI-prototyping tool is code snippets.

Designers can source code snippets in several ways:

When using external sources,keep in mind that visible code isn’t always free to reuse— always check the licensing or permissions. Stick to code from your own product, shared design-system libraries, or open-source components.

While this method yields the most precise results in AI-prototyping tools, it comes with tradeoffs. Long code snippets can overload the model’s context window, leading to performance issues. Moreover, this approach requires designers to understand basic code structure and assess the quality of the snippet before using it.

Besides prompting AI to generate designs, you can also use it as a creative partner to enhance your prompts. You can use a general-purpose chatbot to:

At the end of the day, there is no shortcut tosolving complex design problems. While strategies discussed in this article can help you improve your prompt specificity and get higher-quality output,they can’t replace the hard work that goes into thinking through design requirements, weighing tradeoffs, and making informed design decisions.

Leverage AI to enhance creativity, efficiency, and impact in everyday design work

Artificial Intelligence

Create user interfaces using essential principles, techniques, and methods of visual design

Interaction

Unearth user pain points to drive breakthrough design concepts

Interaction