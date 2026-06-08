# 8 Design Guidelines for Complex Applications

**Author:** Kate KaplanKate KaplanNovember 8, 20202020-11-08

**Topics:** Application Design, Design Patterns, Interaction Design

**Source:** https://www.nngroup.com/articles/complex-application-design/

---

November 8, 20202020-11-08

Share

We’ve previouslydefined a complex applicationas any application supporting the broad, unstructured goals or nonlinear workflows of highly trained users in specialized domains. Complex apps certainly vary in the type of workflows and end users they support — from research scientists to military professionals to financial analysts, for example — but they often share similar qualities. For example, complex apps frequently:

Despite the great variance, many of the same challenges exists across all complex applications, both for practitioners creating these complex applications and the end users relying on them for their work.

This article outlines 8 guidelines for complex-application design, given the shared challenges that designers and researchers face while working on these applications.

Research shows that, when introduced to an application or system, users prefer to start using it immediately, undeterred by its level of complexity. Users are more motivated to begin their tasks than spend time consuming tutorials, documentation, or other types of help or setup content. (This phenomena is known as theparadox of the active user.) While it would be risky and inappropriate to rely solely on trial-and-error learning for applications in mission- or safety-critical domains, some degree of learning by doing will always be required, because it’s not possible to cover all uses of a system in a training course or manual.

Support users’ preference to begin exploring the interface immediately by allowing them to learn the interface through trial and error, without that experimentation resulting in loss of work or irreparable damages.

For example, limit users’ ability to carry out a long sequence of actions without seeing the results of those actions. Real-time dashboard construction, where a dashboard-element preview updates in real time as it is constructed, supports this principle. Users do not have to wait until the end of their task to see if the result of their actions matches their intent.

For the most part, even users of complex applications tend to plateau at mediocre performance. In other words, the majority of users do not transition to true expert usage with the systems they use when left to their own devices. Many users willsatisfice, meaning that they will keep using satisfactory (often inefficient) ways of accomplishing tasks, rather than invest time in seeking out optimal solutions for their workflows. This behavior adds up to an incredible chasm in productivity over time, as users spend years or even decades using the same system day-in and day-out in inefficient ways.

Help users transition to more efficient methods and break their ingrained behavioral patterns by finding unobtrusive ways to communicate faster, more efficient methods for their tasks.

For example, instead of relying solely on lengthy tutorials or manuals (even well-written ones), embed in-context learning cues foracceleratorsor additional functions throughout the application. In-context learning cues are those presented to the users only in context of the task at hand.Tooltipsthat suggest a faster method for accomplishing a task as the user hovers over a toolbar menu item support this principle.

Users of complex applications often carry out broad, unstructured goals in nonlinear workflows. For these workflows, users may not know their exact end goal, but rather need to analyze data to look for answers. Even if a well formulated end goal does exist, users often do not follow a known, sequential set of subtasks to reach it. Yet, out of necessity, the system has to have some sort of structure: a physical interface with which users interact and some type of linear process that they complete over time.

Allow users flexibility in their task sequence by avoiding rigid, linear workflows that force users through a set of actions from start to finish with no escape hatches or flexibility in sequence.

For example, provide methods that allow for skipping ahead, looping back to an earlier step, and moving fluidly from any step to any other. For example, a flexible, interactive sequence map within awizardallows users to return to previous steps without losing their progress.

Complex-app users often face long waits and frequent interruptions to their work. Complex data analyses can run for hours, if not days, for example, and the highenvironmental complexitysurrounding most complex-app users can translate to unexpected and jarring interruptions in their work. Even without unplanned interruptions, the complexity and variability in subtasks executed to achieve a goal requires users to hold a lot of information inworking memoryduring tasks, which can be easily lost as they pivot directions.

Offload working-memory burden and help users resume tasks after interruptions or breaks in workflow by enabling users to keep a record of their actions and thought processes during their work.

Allowing users to add and store open-ended notes about particular data sets, charts, or other elements is one way to support this principle. For example, during complex data modeling or analysis, user-entered comments can remind users at later points in time why they created a model and what question they were attempting to answer when they did so.

Complex-app users typically work across multiple tools and multiple workspaces. Even if users rely mostly on one specialized application for the majority of their work, they frequently switch applications for a number of reasons; for example, to gather data from online databases, find and reference articles or other external documentation, or make their own notes and commentary in other applications when the primary software does not support that action. Even within the primary application, users may transition between different environments or workspaces due to software addons or other optional packages that enable various specialized functions within the application.

Reduce the burden of tool switching by supporting the transition from one environment to another, both inside and outside the primary application.

One way to reduce the burden of tool switching is by simply accepting this ecosystem and designing connection points between the primary application and frequently used third-party tools. For example, complex work often requires collaboration and reporting. Built-in functions for exporting data sets to Excel or images to PowerPoint enable users to save precious time otherwise spent converting data or screenshotting images as they attempt to compile reports and presentations.

Complex apps are often designed to accommodate a broad range of uses. The same analytics-monitoring software used by an environmental agency to measure and track honey-bee production might also be used by an automotive company to monitor machine failure, for example. This diversity of usage scenarios makes complex applications very powerful on the one hand, but often very cluttered, on the other. Additionally, complex applications must often support both novice and expert users at the same time, and expert users may need advanced features that infrequent or novice users rarely access.

Help users manage the choice, feature and function overload prevalent within complex applications by minimizing the appearance of clutter within the interface without reducing the capability of the application.

Staged disclosure, where options are shown to the user only when they are relevant to the task at hand or the item in focus, is one way to reduce clutter. For example, displaying advanced parameters or settings only after a related field is checked in a complexformor wizard is an example of staged disclosure relevant to complex applications.

Even when clutter is effectively reduced within an interface, not all elements and information can (or should) be displayed at once. Some information must be deferred to secondary levels; however, that secondary information is often necessary to contextualize and make decisions about information on the primary level.

Ease the transition between primary and secondary information and help users contextualize primary information by allowing users to access and view supplemental information without leaving the primary screen or environment.

Dashboards often support this principle, for example, by allowing users to view more precise quantitative data in a tooltip when the user hovers over a specific point in a chart or graph.

Many of the tasks performed by complex-app users require a high degree of visual search. To name a few examples: Users may have to locate and distinguish relevant data across tabular views in huge tables. System alerts must draw attention to relevant parts of the interface so that users can notice and rectify underlying conditions in a timely manner. Simply viewing and attempting to comprehend data visualizations on a dashboard has a significant visual-search component, as well. The sheer amount of competing information and elements within complex application can hinder these tasks.

Help users find and act upon important information by making critical elements visually salient, (i.e., making them stand out from surrounding elements). It’s worth noting that making important information stand out does not always mean adding emphasis to that information (e.g., a bright color or a heavier font weight). Removing nonessential elements can be equally or even more effective at making important information visually salient.

For example, removing superfluous graphics or visual elements that serve no purpose can make the data left behind stand out. A dashboard module that eliminates nondistinctive, unintelligible illustrations from data elements supports this principle by lessening the burden of visual search for the user attempting to locate data across the dashboard.

Complex applications are diverse, supporting a board range of user types and workflows; however, similar challenges exist across such complex applications, regardless of domain. Optimize complex applications by following these 8 design guidelines:

Create and evaluate applications for advanced decision making, complicated workflows, and complex domains

Interaction

Components, design patterns, workflows, and ways of interacting with complex data

Interaction

Enhance your judgment and resolve tough design challenges

Management