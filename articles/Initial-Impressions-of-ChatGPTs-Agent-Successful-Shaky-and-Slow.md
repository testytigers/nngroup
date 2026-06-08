# Initial Impressions of ChatGPT’s Agent: Successful, Shaky, and Slow

**Author:** Evan SunwallEvan SunwallAugust 8, 20252025-08-08

**Topics:** Artificial Intelligence

**Source:** https://www.nngroup.com/articles/impressions-chatgpt-agent/

---

August 8, 20252025-08-08

Share

OpenAI recently released its agent mode for ChatGPT. Agent mode enables ChatGPT to navigate and manipulate websites designed for human use. This article documents my first impressions of this new interaction paradigm.

While this tool represents a significant step towards mainstream AI-agent use, my simple evaluation revealed that agentic AI still has a long way to go.

Note:On August 7 2025, OpenAI  released GPT-5, the successor to the company’s collection of previous models. OpenAI’s Agent Mode was not updated alongside GPT-5, as they are separately developed AI models.

Watch a recording of this interaction(about 5 minutes). This is a ChatGPT replay of this agent interaction; it's sped up and does not depict the actual duration I experienced.

I chose the everyday task of booking a restaurant reservation. This was my starting prompt to ChatGPT:

Find a restaurant suitable for a business lunch near 3100 Travis St, Houston, TX 77006 for next friday at noon.

Is this ahigh-quality prompt? No.

I kept it terse and deliberately omitted relevant details to simulate real-life use of everyday people who don’t fancy themselves as “prompt engineers.” (Writing highly detailed prompts poses a highinteraction coston users. In some of our recent studies of the prompting strategies of consumers, we’ve noticed that even experienced genAIusers rarely include sufficient context and criteriain their first prompt.)

Remember thatthe computer should adapt to the needs of the human, and not the other way around.I wanted to evaluate what this agent could perform with minimal handholding from a rushed and distracted user.

This realistic-yet-weak prompt should have encouraged ChatGPT to request additional details before beginning. For example:

Instead of asking any of these clarifying questions, ChatGPT jumped immediately into the task with limited context.It focused on the necessary geographic proximity and operating hours but didn’t ask followups on relevant topics that would have significantly influenced its subsequent searches and suggestions. This behavior struck me as unusual, since ChatGPT’s “deep research” mode always asks clarifying questions before investing 8–15 minutes researching and writing a report.

ChatGPT spent 6 minutes conducting research on various restaurants by performing 10 web searches utilizing 96 sources — far more than any human could reasonably use to find a lunch spot for a business meeting. (Though, arguably, a human might not need to consult 96 different sources to make a well-informed decision.)

ChatGPT’s search used mostly sensible sources for the task: Yelp, OpenTable, Instagram, and various restaurant-focused sites, and it took screenshots to document the process. ChatGPT did mention encountering some difficulties using these sites, such as dynamic features, anchor links that interfered with scrolling, and even the dreaded popup-upon-arrival.

Excerpts of ChatGPT’s documented “thinking” during this process:

The open table [sic] might be inaccessible due to dynamic features or cross-late issues. I'll use the computer tool to open it and bypass these limitations.

It seems that scrolling has not progressed as expected, likely due to an anchor.

A pop-up about Oporto is showing, and I need to close it by clicking the 'x'. I'll use the multi-action function to click the cross and close the pop-up window.

ChatGPT eventually suggested 3 restaurants that are viable candidates for a business lunch, based on my expertise as a Houston local. It created a table containing the following information:

There are a few glaring omissions in this list, though: What’s on the menu and how much will it cost?

It would be hard to choose a restaurant based on this information alone, and navigating directly to the restaurant’s website was a little difficult. Sometimes the embedded sourcing pills would link to the mentioned website, but, if the source was a screenshot, it would instead display an image preview that, when clicked, included a link to the website. I found this inconsistent behavior unintuitive.

These screenshots are an effective sourcing technique (an important tactic for trust building with users, which we discuss in our courseDesigning AI Experiences), but more direct access to the websites would have been helpful.

I responded to this table with a choice and direction:

Let’s book a table at Brennan’s.

After I prompted with the desired restaurant, ChatGPTspent a surprising 55 seconds attempting to access the restaurant’s website.It appears it was redirected to a Google Maps page, but it resolved this issue on its own.

ChatGPT then determined that clarifying the guest count was important before proceeding.

I replied with 2 guests but then decided to add a twist: I mentioned that 1 had a shellfish allergy. (Remember, typical users won’t behave methodically and logically! In these agentic interactions, they’ll likely share information whenever it occurs or is asked of them. And they still might not answer with total clarity. I didn’t tell ChatGPTwhohad the shellfish allergy, and it didn’t ask.)

With the restaurant selected, guest count confirmed, and website open, ChatGPT was ready to book the reservation. This step was the most surprising step for several reasons.

First, it took an unusually long time. ChatGPT needed 11 minutes to navigate the restaurant’s web forms, whereas it took me about 2 minutes to perform the same workflow at a casual pace. (Not exactly the magical time saver that AI agents are often purported to be.)

ChatGPT took so long to complete the process that the 10-minute window to hold atable reservation technically timed out. Fortunately, the website processed the reservation anyway, but if the restaurant had been receiving lots of reservations, it could have been rejected and the process would have needed to pivot.

Second, ChatGPT hadsome difficulty manipulating the dropdown time selector. It had trouble scrolling the list to make 12:00 PM visible within the viewport, and then mis-clicked 12:15. To ChatGPT’s credit, it noticed the mistake and clicked 12:00 PM instead, but the agent might experience some challenges, or at least slowdown, with some selector-control implementations.

Third, when the search results returned possible reservations, 12:00 PM was unavailable.ChatGPT then decided to select a 12:15 timeslot insteadand warn me about the change. It even correctly noted alternatives at 11:45 AM and 12:30 PM, too, but if noon had been a firm requirement, then this process would have, again, had to make a big, slow detour.

Finally, andmost impressively, ChatGPT accounted for the shellfish allergy successfully.It identified dietary restrictions as the appropriate option in the booking form and selected the appropriate choice. I didn’t intentionally specify which guest had the allergy, so it defaulted to me.

ChatGPT handled the ambiguity and was able to select from an unconventionally styledarray of toggle-switch controls. Themodal windowcontaining these controls also used unconventional positioning of theCancelandSavebuttons (at the top of the window’s frame instead of the bottom). Could this mean that agents might be less affected by unintuitive designs than humans? Could there be designs that stymie agents but remain usable for humans? The similarities and differences will be intriguing to explore in the future.

Next, ChatGPT correctly identified that I needed to complete the remaining portion of the web form since it involved personal information that I had not previously provided. In agentic AI, this referred to keeping the “human in the loop.”

Human-in-the-loopis an agentic AI design strategy that aims to keep humans actively involved in decision making, instead of letting the agent make choices and act autonomously.

The “takeover” process was straightforward, but the web-browser window was seemingly low-resolution. I couldn’t find a way to resize it, but I was able to enter the necessary details.

Once I handed back control to ChatGPT, it took a minute to review the completed form and then ask meShall I go ahead and submit [the reservation] now?

Once again, ChatGPT was effectively keeping the human in the loop at a decision gate.

Decision gatesare points where an agentic AI requests confirmation from a human before taking significant actions with potential adverse consequences.

Once permission was given, ChatGPT took another 2 minutes to submit the form and confirm the reservation.

ChatGPT recognized that the reservation window had technically expired, which may have slowed its processing, but the restaurant website was seemingly quick and responsive otherwise, so the delay was probably with ChatGPT.

With the reservation confirmation in my inbox (that sadly will have to be cancelled even though it’s a nice restaurant), ChatGPT’s agent mode was successful. Despite being given a weak user prompt, ChatGPT performed some research, found a suitable restaurant, prepared the reservation, and successfully submitted and confirmed it.

But the process was very slow,and it’s important to notice the shaky ground it rests on. Some early probing by ChatGPT could have revealed critical information, such as a food allergy, that might have altered the entire trajectory of the chat.

While it surfaced some useful information, it hewed too heavily on the initial prompt and not enough on the practical details that a restaurant patron would need to know to make an informed dining decision.Pivots and dead ends,like a restaurant that is over budget, serves incompatible food, or is unavailable, would have incurred even more delays.

The halting process over a simple web form implies that more complex experiences would be more error-prone and slow.Plus, any agent handling payment or personal information must keep the user in the loop. While this practice mitigates serious errors, it alsoerodes the agent’s value proposition,and there’s no guarantee that the agent will correctly identify these situations to begin with.

Although just a single anecdotal experience, this author sees ChatGPT’s agent mode as an impressive milestone. But to handle the rigors of everyday use, this agent mode will need to be more inquisitive, much faster, and demonstrate reliability over the long term. Still, we’re entering a new era of computing where machines are becoming fellow users alongside humans.

Design innovative, trusted, and useful AI products and features

Artificial Intelligence

The AI-assisted user research workflow

Artificial Intelligence

Leverage AI to enhance creativity, efficiency, and impact in everyday design work

Artificial Intelligence