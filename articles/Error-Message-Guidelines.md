# Error-Message Guidelines

**Author:** Tim Neusesser, Evan SunwallTim NeusesserandEvan SunwallMay 14, 20232023-05-14

**Topics:** Heuristic Evaluation, Application Design

**Source:** https://www.nngroup.com/articles/error-message-guidelines/

---

May 14, 20232023-05-14

Share

Over 30 years ago, Jakob Nielsen created10 Usability Heuristicsas general guidelines for designing digital products. These heuristics equally apply today as they did back then. Usability heuristic #9 emphasizes the importance of good error-message design: "Help Users Recognize, Diagnose, and Recover from Errors." Effectively handling errors is crucial because it's one of the5 quality components of usable experiences.

Error message: A system-generated interruption to the user's workflow that informs the user of an incomplete, incompatible, or undesirable situation according to the system's implementation.

Quality and error messages rarely go together, though. Product teams can be so focused on designing or engineering the idealistic user path that deviations from that path become a frustrating afterthought.

Error messages must present themselves noticeably and recognizably to users.

Display the error message close to the error's source.Reducecognitive loadby displaying an error indicator adjacent to the interface where the error occurred.Proximityhelps users associate the error message content with the interface elements needing attention.

Use noticeable, redundant, and accessible indicators.Text and highlights that are bold, high-contrast, and red are conventional error-message visuals. Use this styling for the message and for the affected elements needing correction. Another technique for improving noticeability is leveragingcarefully designed animationsto guide the user's visual attention for corrections. Rememberaccessibility guidelinesto aid the roughly 350 million people worldwide with a color-vision deficiency, and never use exclusively color or animation to indicate errors.

Design errors based on their impact.Design your error messages to indicate the problem's severity. For example, sometimes users only need to be warned of unexpected or potentially undesirable outcomes but can otherwise advance their workflow. Differentiate between these "good to know" messages from those posing a barrier to the user's progress. For example, conditionally displayed labels, toast notifications, or banners can be used for issues needing minimal user interaction, whereasmodal dialogsrequire the user's attention and resolution and should be reserved for severe errors.

Avoid prematurely displaying errors.Timing is a crucial aspect of designing effective error messages. Presenting errors too early is ahostile pattern. It’s like grading a test before the student has had a chance to answer. It can make users feel annoyed, belittled, or confused. Don't assume that exploratory interactions (like the user moving text focus from a text box without filling it in) are errors. However, do consider inline, real-time errors for error-prone interactions where users are unlikely to enter the correct information on their first try. This immediate guidance reducesinteraction costsfor correction.

Error messages cannot rely on visuals alone. They must contain copy to elaborate and assist the user with recovering from the error.

Use human-readable language.Error messages should be plainspoken usinglegible and readable text(many writing apps can give you feedback on a message's readability). Avoid technical jargon and use language familiar to your users instead. The Web's most common error message, the 404 page, violates this guideline. Hide or minimize the use of obscure error codes or abbreviations; show them for technical diagnostic purposes only.

Concisely and precisely describe the issue.Generic messages such asAn error occurredlack context. Provide descriptions of the exact problems to help users understand what happened. That said, beware of excessive technical precision and accuracy that can undermine understandability. The user'smental modelof how the system works likely differs from the conceptual model of how it was coded.

Offer constructive advice.Merely stating the problem is also not enough; offer some potential remedies. One example is anOut of stockmessage for an ecommerce website. Include details of when the product will be available again or suggest that users sign up for a restock notification by entering their emails.

Take a positive tone and don't blame the user.Write with a positive and nonjudgmentaltone of voice. Don't usephrasing that blames users or implies they are doing something wrong, such asinvalid,illegal, orincorrect. The proper usage of any system lies with its creators and not with the system's users, so the system must gracefully adapt and not shift blame. Avoid humor since it can become stale if users encounter the error frequently.

Good errors go beyond just explaining but protect the user's effort and time. Offeracceleratorsto resolve the situation or share a bit of instruction to aid users' understanding and hopefully avoid the problem in the future.

Safeguard against likely mistakes.The very worst error messages are those that don't exist. When users make a mistake and receive no feedback, it can create a cascade of misunderstanding, wasted effort, and frustration. Years ago, email apps would dutifully send your email even though it referred to an attachment you forgot to include. Now, most apps will detect this situation and prompt you with an error message before sending it, thus sparing you embarrassment.

Preserve the user's input.Let users correct errors by editing their original action instead of starting over. For example, display the original text entered into a text field even if it does not match the requirements for that field and allow the user to modify it.

Reduce error-correction effort.If possible, guess the correct action and let users pick it from a small list of fixes. For example, instead of just sayingCity and ZIP code don't match,let users click on a button for the city that matches the ZIP code they entered.

Concisely educate on how the system works. Explain to your users how the system works and how to resolve an error. If additional information is required, use hypertextlinks to connect a concise error message to a page with supplementary material or an explanation of the problem. (Don't overdo this, though.)

The above guidelines are essential and applicable to all error messages. That said, there is one last guideline to consider when the system becomes incapable of serving users in any functional capacity:

Mitigate total failure with novelty.Errors areunenjoyable for everyone involvedas they interfere with user and business goals. Yet sometimes users may encounter an error so catastrophic (e.g., overloaded servers) there is no recourse but to wait or try again later. It's these specific moments (which should be rare and avoided at all costs) where blending an apology with something surprising or novel may salvage a disappointing situation that users will likely remember due tonegativity biasand thepeak-end rule. Don't underestimate the challenge of communicating humility and delight — especially if user input is in jeopardy or the context has severe implications for users. Yet this tactic might enhance memorability and sustain user interest with low-stakes experiences until the system resumes functioning.

Interactions between humans and computers are constantly evolving, but there will inevitably be mistakes, misunderstandings, and, thus, a need for error messages. Follow these guidelines to ease these frustrating moments and help the user accomplish their task efficiently and with renewed confidence.

Foundational concepts that everyone should know

Interaction

Components, design patterns, workflows, and ways of interacting with complex data

Interaction