# A Concrete Definition of an AI Agent

**Author:** Caleb SponheimCaleb SponheimApril 3, 20262026-04-03

**Topics:** Artificial Intelligence

**Source:** https://www.nngroup.com/articles/definition-ai-agent/

---

April 3, 20262026-04-03

Share

The word "agent" is being applied to everything. There are agents in your phone, your company Slack, your Notion, andyour banking app. There are agents sendinghate mailanddeleting email inboxes. "Agent" has become a diffuse, ambiguous term that means everything and nothing.

This is a problem. Without a clear definition, practitioners can't evaluate what they're working with or decide whether to trust it. Marketing, sales, engineering, product, and leadership each have a separate definition of what an "AI Agent" is supposed to be. Some of these definitions are grounded in real-world use cases, but most of them float amidst hype and hope. Instead, we at NN/G offer a concrete definition that helps UX professionals design better experiences for their users.

AnAI agentis a system that pursues a goal by iteratively taking actions, evaluating progress, and deciding its own next steps.

Let's break down the key terms in our definition.

Design innovative, trusted, and useful AI products and features

An AI agent works towards some end condition. The goal may be specific ("fix this failing test") or open-ended ("research competitors in the European market and summarize the findings"). What matters is that the agent has a target to work towards: something that shapes which actions it takes and how it evaluates progress.

Examples:

Agents build on their previous work, using the result of a previous step to make progress.

Examples:

Agents act on their environment. Most current AI agents perform digital actions: searching the web, writing code, creating or editing documents, and updating databases. But the capability to act is not limited to the digital world. A self-driving car acts by steering, accelerating, and braking. A humanoid robot acts by manipulating physical objects. As AI agents expand into new domains, the range of possible actions will grow: from managing files to navigating physical spaces to operating equipment. In the agentic process, these actions are considered distinct steps from "thinking" or communicating to the user.

Examples:

A key aspect of an agentic process is reviewing completed and remaining work. This is often done by comparing against a plan and task list.

Examples:

AI agents determine the next set of actions that are needed to make progress towards the goal they are pursuing. In this way, AI agents are self-directed, and their path towards a goal is self-determined. This is in contrast to an LLM, which follows a single or a set of predetermined, rigid steps in a process.

Examples:

Some definitions of agents emphasize additional properties: the ability to perceive an environment, adapt plans in response to unexpected challenges, or maintain memory of previous steps. These are real and important capabilities, but they are not required by our definition; they follow from it.

"Evaluating progress" encompasses perception. A coding agent that reads its own error logs is perceiving its environment; so is a self-driving car processing lidar data. The mechanism of perception varies, but the function (checking the state of things before deciding what to do next) is already part of the agent loop.

This does not mean that any system capable of self-reflection is an agent. An LLM that reflects on its own output is performing a form of evaluation, but evaluation alone is not enough. A system only qualifies as an agent when it also takes actions and decides its own next steps; no single piece of the definition is sufficient on its own.

Adaptation (changing plans when something goes wrong) is implicit in "deciding its own next steps." An agent that can decide its next step can, in principle, decide on a*different*next step when a previous one fails. Whether it*does*so reliably is a question of usefulness, not of identity. (More on this below.)

Memory across steps is implicit in "iteratively." An agent that builds on previous work must, by definition, retain some record of that work. How memory is implemented (context windows, external databases, file systems) varies by system, but the capacity to carry forward state is baked into the iterative loop.

We keep these properties implicit rather than listing them separately because doing so keeps the definition lean enough to be useful as a shared vocabulary. A definition that requires perception, adaptation, memory, self-direction, the capability to act, and iteration risks becoming a checklist that generates more disagreement than clarity.

If you ask a typical AI-based chatbot a question and it responds, you're using a large language model, not an agent. The LLM received your input, generated text, and stopped. There was no iteration, no action beyond producing a reply, and no self-directed next step.

An LLM is a reasoning engine. An agent is a system built around a reasoning engine. The distinction lies in what surrounds the model: tools it can use, actions it can take, and a loop that lets it evaluate its own work and decide what to do next. When an LLM is placed inside that loop (with access to tools like web search, file creation, or code execution) it can become the core of an agent. But the LLM alone is not the agent, just as an engine alone is not a car.

Most AI agents in 2026 are built on large language models, but the definition does not require one. A self-driving car like a Waymo vehicle meets our definition of an AI agent: it pursues a goal, takes actions, evaluates progress, and decides its next steps. Yet it runs on computer-vision and planning systems, not an LLM. What matters is the behavior pattern, not the underlying technology.

To make the distinction between agent and AI chatbot concrete, consider two real responses to the same request. A user asked an AI tool to log into Algolia (a search-analytics dashboard), download the most popular searches from the past month, and export the searches that returned zero results.

The chatbot understood the request. It knew what Algolia was, what the user wanted, and how to get there. But it stopped there. It described the steps and handed them back to the user. The AI agent attempted the work itself. It navigated to the dashboard, clicked into theAnalyticsview, tried to change the date range, failed, adjusted its approach, and tried again. Each of those steps was a decision the agent made based on what had happened so far. That cycle of acting, evaluating, and deciding what to do next is the difference between an AI tool thattells you howand an AI agent thattries to do it for you.

This kind of nonagentic response is becoming harder to find. When we tested the same type of request across several AI products in early 2026, most attempted some form of agentic behavior: using tools, creating files, and iterating on their approach. The products are converging. This does not make our definition useless; it means that most major AI products have crossed the threshold into agent territory. The more practical question, the one most practitioners will face, is not "is this an agent?" but "is this agent any good?"

So, when someone calls a product an "AI agent," ask: Does it iterate? Does it take actions beyond generating text? Does it decide its own next steps? If the answer to any of these is no, you're looking at an LLM: a powerful tool, but not an agent.

Before AI agents, there was automation, and plenty of it. Email spam filters, scheduled smart-light routines, robotic assembly lines, and wire transfers all automate tasks that once required human effort. Understanding where these familiar tools sit in the landscape helps clarify what makes AI agents different.

Two axes capture the key distinctions: capability to act and self-direction.

Capability to act describes how much a system can affect things: digitally, physically, or both. If an LLM can only output text in response to a single query, its capability to act is close to none. A coding agent with access to a terminal and file system has contained capability to act. At the far end, a self-driving car or an autonomous robot operates with relatively unconstrained physical capability to act. According to our definition, an AI agent must have some capability to act, but this can range from editing a document to navigating a city street.

Self-direction describes who decides what happens next: the system or its programmer. In a predetermined process, every action is specified in advance. The system follows a fixed sequence and cannot deviate from it, regardless of what it encounters along the way. Many familiar automations work this way: a spam filter applies rules, a wire transfer follows a set protocol, a robotic arm repeats the same motion. These systems may be sophisticated, but they do not choose their own course of action.

In a self-determined process, the system decides its next action based on what has happened so far. This is the boundary that defines an agent. An email spam filter, no matter how many rules it evaluates, follows a predetermined process: it cannot reflect on its results and change its approach. A coding agent that runs a test, reads the error output, and decides to try a different fix is self-determining. The distinction is not about how many actions a system takes, but about whether the system itself decides what those actions are.

By combining the two main axes into a single chart, we can better understand the landscape in which AI agents are defined alongside other automation solutions.

The purple area above defines AI agents along our axes of capability to act and self-direction. Many automation solutions live in this space. AI-powered systems must have some self-determination and some capability to act to qualify as agents.

The two most prominent examples of AI agents in early 2026 aresearch agentsandcoding agents. A search agent like ChatGPT 5.2-pro goes beyond a single chatbot reply: it browses the web across multiple sites, reads and analyzes documents, and synthesizes findings into a structured report, iterating through dozens of sources before delivering an answer. A coding agent like Claude Code works in a developer's terminal, where it can read an entire codebase, edit files, run tests, and fix errors in a loop, deciding on its own what to try next when something breaks. Both are built on the same language models that power their respective chatbots, but the models alone are not what make them agents. It is the tools, actions, and iterative loops wrapped around those models that qualify them.

A self-driving car, such as a Waymo vehicle, also fits the definition of an AI agent because it operates through a continuous, closed loop of sensing (evaluating progress), thinking (deciding next steps), and acting (taking iterative actions) to complete a ride (the goal).

Another noteworthy example from the chart is thehuman, who exists in a peculiar place outside the bounds of the graph. While humans may not always operate at peak capability to act or self-direct, they have the capacity to do so. Although AI agents have become very powerful, there are no examples yet that can fully replace humans’ self-direction or action potential.

A system can meet the definition of an AI agent and still be terrible at its job. An agent that misunderstands goals, crashes on errors, or requires constant handholding is still an agent: it pursues a goal, takes actions, evaluates progress, and decides next steps. It just does these things poorly. This is a feature of the definition, not a bug: it lets us separate the question "Whatisthis?" from the question "Is thisgood?" A car with a dead battery is still a car. An agent that fails to adapt is still an agent.

Auseful AI agentreliably understands goals, adapts when things go wrong, and achieves outcomes with an acceptable amount of supervision, review, and correction.

"Acceptable" is context-dependent. What constitutes an acceptable level of accuracy and quality in your work will differ based on your product and your users. For example, an AI agent for medical charting should have higher accuracy than a creative-writing AI agent. You define what is "acceptable" for your situation. There is no universal standard for a useful agent: usefulness is always relative to the task, the user, and the alternatives available.

Given a sufficiently defined goal, a useful AI agent can reliably chart a path to that goal according to specified success criteria. A useful AI agent may also request additional details or ask questions to better understand a task or goal before writing a plan and acting.

Errors are bound to happen in any workflow, AI-driven or not. Useful AI agents reliably detect errors and attempt to solve them by taking different courses of action towards a given goal. For example, if editing an existing PDF fails, an AI agent, instead of giving up, may build a new PDF from scratch or convert it to a Word document and then reconvert it to PDF to meet the stated goal.

Most AI outputs require human review and correction; as this effort increases, the benefits of using AI diminish compared to doing the task directly. A useful AI agent minimizes the need for human intervention.

An agent is worth using if itdelivers faster or higher-quality results than the alternative,provided that the saved effort justifies any usage costs.

Ideally, the results would be both produced more quickly and of better quality than before. If you're using an AI agent that doesn't meet either of these requirements, then you should set it aside. If you're designing an AI agent that doesn't speed up or improve a process, it's not ready to ship.

However, it's often hard to know if something is actually better or just shiny and new. Ideally, you should be able to compare it to a gold standard. If that’s not possible, focus on the subjective experience of using the agent: does it feel faster, easier, or of higher quality than previous tools? You can start there.

Just because something is an agent doesn't mean it's useful. An AI product can meet the definition of an AI agent yet be so slow and mediocre that it's not worth using.

For UX practitioners, the question "Is this agent worth using?" translates directly into design and evaluation work. If you are building an agent-powered feature, test whether it actually outperforms the nonagentic version of the same workflow. If you are evaluating an agent someone else built, watch real users interact with it: where do they lose trust, have to correct it, or give up and do the task themselves? The definition tells you what an agentis. Research can tell you whether it belongs in your product.

Here at NN/G, we will continue to build from these definitions to help you evaluate AI tools effectively and manage thehype of the current AI cycle. By early 2026, agents have already made large impacts in the field of software engineering and will continue to make progress in other areas of professional work, including user experience. These definitions are a baseline for further work and a lens through which you can build confidence when working with and designing new AI experiences.

Leverage AI to enhance creativity, efficiency, and impact in everyday design work

Artificial Intelligence

Design innovative, trusted, and useful AI products and features

Artificial Intelligence

The AI-assisted user research workflow

Artificial Intelligence