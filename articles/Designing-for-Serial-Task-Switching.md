# Designing for Serial Task Switching

**Author:** Megan ChanMegan ChanMay 23, 20252025-05-23

**Topics:** Behavior Patterns, Psychology and UX

**Source:** https://www.nngroup.com/articles/serial-task-switching/

---

May 23, 20252025-05-23

Share

Be honest. How many tabs do you have open right now? If you’re like me, it’s probably more than you’d like to admit. Serial task switching is a natural behavior that has become part of our daily lives, whether you’re jumping between projects or exploring a thought that just popped into your head. Designing for this reality means helping users stay productive, reduce errors as they switch between tasks, and maintain focus when they choose to concentrate on just one.

To understand serial task switching, let’s first clarify what multitasking really means and why it’s often misunderstood.

Multitaskingis the act of doing two or more tasks at the same time.

This is what most people believe they’re doing when they juggle multiple tasks at once, whether they are answering emails while attending a virtual meeting or listening to a podcast while working. The idea of multitasking implies that the brain can effectively manage multiple cognitive tasks in parallel, distributing attention equally across each one. However, research in cognitive science has shown that true multitasking is a myth.When tasks demand similar cognitive resources, our brain cannot process both simultaneously.

On the web, even simple tasks, like reading or searching, draw on similar cognitive resources, making it nearly impossible to truly multitask without sacrificing performance.In these cases, we are not multitasking, we are serial task-switching.

Serial task-switchingis a rapid switch between two or more tasks. Instead of managing both tasks simultaneously, attention shifts between them.

With serial task switching, attention is fragmented as we rapidly shift between tasks. Each time we switch tasks, the brain must reset and reacquire the context of the new task, which slows down productivity.

Everyonedoes serial task switching. Serial task switching is a natural part of how we interact with our incredibly busy environments.

While constantly shifting between tasks may feel productive, over time, it has several negative effects, including errors, low productivity, and stress.

The more we switch between tasks, the more likely we are to make mistakes. We are striving to retain information from both tasks in our limitedworking memory, so we end up taking into account fewer details from each task, and, as a result, we increase the chance that we’ll ignore something important. For example, writing an email while in a virtual meeting can lead to miscommunications, typos, or missed details in both activities.Error-preventiontools like undo buttons andconfirmation dialogsare especially helpful for recovering from mistakes caused by serial task switching.

While task switching may feel like you’re getting more done in less time, that is not the case. Many studies (such as the one by Bogdan Vasliescu and colleagues on GitHub multitasking) show that people who switch between many tasks take longer to finish them and produce lower-quality work than those who focus on fewer tasks at a time. Constant interruptions prevent us from entering aflow state, where deep work happens. Users may leave several tasks incomplete or poorly executed instead of finishing multiple tasks quickly.

Every time we shift our focus to a different task, the brain has to work a bit harder to refocus and rebuild context. This frequent resetting strains cognitive resources and leaves us feeling overwhelmed. Over time, this cognitive overload makes it hard to concentrate and can lead to stress, as shown by research by Linda Becker and colleagues.

Designing for task switching means creating interfaces that accommodate this behavior and help reduce the errors, productivity losses, and stress it can cause. The following examples show how different design solutions can reduce friction when attention is split.

Interfaces that let users keep multiple resources visible at once can reduce theinteraction costof switching between tasks. These designs don’t eliminate thecognitive loadof task switching, but they help by reducing the cost of jumping back and forth. Common multi-view interface patterns include split screen and picture-in-picture.

Some tools allow users to access multiple resources within a platform at once. Platforms like Google Workspace, Microsoft Office, and Zoom use interactive sidebars and extendable windows to enable users to interact with two activities simultaneously.

Beyond split screen in individual tools, operating systems like Windows and MacOS allow users to split their screens or open multiple windows. For instance, a student might follow along with a lecture in one window, while completing an assignment in another window. Dividing cognitive resources between the two will still be inefficient and distracting, but by having both tasks in front of them, they will at least be able to minimize the effort of switching between them.

Another type of multi-view interface is picture-in-picture. Video platforms offer picture-in-picture mode, which allows video content to remain visible in a small, movable window while users perform other tasks.

Another way to support task switching is by allowing users to continue to use the interface while working on tasks that involve a delay, like waiting for a support agent, processing a file, or loading content. Live-chat tools on websites often allow users to keep shopping, reading, or exploring the site while waiting for a chat agent’s response. This minimizes frustration with the chat agent and supports a more productive use of time.

It’s natural for attention to fragment, but systems can help users stay on track when they decide it’s time to focus. Features likeDo Not DisturborFocus Modecreate a boundary between the user and any potential distractions. By minimizing notifications and external triggers, these tools give users the space to stay engaged.

Note-taking assistants give users the option to revisit important aspects of the conversation later when needed. Tools like Otter.ai and Granola help users stay on track by capturing meeting notes, action items, and Q&A automatically.

Task switching is part of users’ natural behavior, and interfaces should be designed to support that reality.You don’t need to design an operating system or a full productivity suite to support task switching. Thoughtful design choices in everyday tools can make task switching less stressful and less error-prone.

Users often have multiple goals within the same tool, such as referencing past work while completing a task or comparing two pieces of information. Flexible, adjustable layouts help support this behavior by reducing the cost of switching between tasks.

To do this, allow users to arrange their workspace and keep multiple views open at once through features like split-screen layouts, expandable windows, or side-by-side panels. Another option is to use collapsible sections or accordions to let users access relevant content without overwhelming the interface.

With serial task switching, users often bounce back to an app after only a short interruption. They’re not fully recontextualizing, they just need quick indicators to recognize where they are and what they’re looking at.

To keep users oriented, use navigation elements likebreadcrumbsandsection headersfor immediate location awareness.Label buttons and links clearlyso users understand the context of the interface and can move forward confidently. These cues minimize errors and help users resume work without needing to think too hard.

When users encounter a task with a long wait, allow them to continue to complete other tasks using the interface. Interfaces that support parallel tasks help users stay productive.

While designing for parallel tasks, keep tasks that are in progress visible but unobtrusive. Use collapsiblepopupsthat remain visible as the user navigates, and avoid blocking important interface elements.

Task switching increases the chance of mistakes. Interfaces should include safeguards that help users avoid mistakes and recover when they do occur. To design for error prevention and recovery:

These practices will help reduce errors when their attention is divided.

Task switching is inevitable in today’s world, where it often feels like a million things are happening at once. Evaluating your own product with task switching in mind can reveal opportunities to reduce friction while task switching and support focus when users decide to give their full attention to one task. By designing with task switching in mind, we can create experiences that adapt to the way people actually work.

Linda Becker, Helena Kaltenegger, Dennis Nowak, Matthias Weigl, and Nicolas Rohleder. 2023. Biological stress responses to multitasking and work interruptions: A randomized controlled trial.Psychoneuroendocrinology,156, 106358–106358.https://doi.org/10.1016/j.psyneuen.2023.106358

Bogdan Vasilescu, Kelly Blincoe, Qi Xuan, Casey Casalnuovo, Daniela Damian, Premkumar Devanbu, and Vladimir Filkov. 2016. The sky is not the limit: multitasking across GitHub projects. InProceedings of the 38th International Conference on Software Engineering (ICSE '16). Association for Computing Machinery, New York, NY, USA, 994–1005.https://doi.org/10.1145/2884781.2884875[RB19]

Use psychology to predict and explain how your customers think and act

Interaction

Create delightful experiences that touch, convince, or excite your audience

Interaction

Strategically combine content, visuals, and interactive components to design successful web pages

Interaction