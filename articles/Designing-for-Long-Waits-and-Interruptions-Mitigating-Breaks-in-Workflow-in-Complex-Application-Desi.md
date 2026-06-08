# Designing for Long Waits and Interruptions: Mitigating Breaks in Workflow in Complex Application Design

**Author:** Kate KaplanKate KaplanSeptember 5, 20212021-09-05

**Topics:** Application Design, Design Patterns

**Source:** https://www.nngroup.com/articles/designing-for-waits-and-interruptions/

---

September 5, 20212021-09-05

Share

Users ofcomplex applicationsare frequently interrupted during their workflows, starting a task only to have to wait an extended period of time before completing it. These long waits occur for a variety of reasons — for example, the system may need a substantial amount of time to process a request (e.g., run a model, query a database) or the user may need additional information from external sources before proceeding and be forced to wait while information is gathered and before the task can be resumed.

Regardless of circumstance, adhering to the following 5 guidelines can mitigate the frustration thatcomplex-app usersexperience during long waits or interruptions in their workflows:

The rest of this article provides additional details and examples for each of these guidelines.

Users of complex applications often analyze large data sets, run complex models, or query robust information sources — all processes that take a substantial amount of system-processing time. During these relatively long waits,visibility of system statusis particularly important, meaning that the user should be provided with feedback about what is happening within a reasonable amount of time.

Because it’s common for processing times in complex applications to be relatively long (at least compared to everyday online activities  such as adding an item to a shopping cart), complex-app users benefit from a detailed  information about what is happening during system processing and where they stand relative to the end of the process.Progress indicatorsthat provide details such as time elapsed (or steps completed) and time or steps remaining  make long waits more tolerable and increase user confidence.

For example, the geographic-information–system (GIS) application below provides details about the percentage of completed work and the current step (Rasterizing polygon features…) during long periods of system processing.This information helps users understand whether the process is proceeding as they expected, how much longer the process will take, and whether they should wait for the process to complete or begin another task during this time.

When these details are not provided, even frequent, long-term users become confused and frustrated. For example, during one recent contextual-inquiry session, an urban planner attempting to analyze demographic data revealed the uncertainty that lack of progress details can create. As he waited for data to be processed, he described the “progress indicator” the system provided:

Let's see what happens…I know it's doing something as long as it has this thing down here. If this little globe is spinning, it's still doing something. If I see that globe stops spinning, or it doesn't show up, then I know my software probably crashed.

While looped animations such as this one can help users understand that the system is doingsomething, it’s been long-established thatthey are not appropriate for waits exceeding 10 seconds, a common scenario within complex applications. That’s because a busy-state loop animation doesn’t tell users whether it’s worth waiting out the process or they should invest in another task or action during the wait.

To clearly indicate progress to users of complex applications:

During long waits, complex-app users are likely to step away from their work to complete different activities or initiate other tasks within the system; these activities will increase their overallcognitive load. For example, one coastal engineer in a recent study described initiating scores of analyses across 70 computers in a typical day:

Unfortunately, when you have gigabytes and gigabytes of data, they can take hours [to run]…It might take half a day to just do the zonal statistics on [this project]. [I’ll] just clickzonal statisticsand then…walk away for half a day…That's why I have like…70 computers, and I just start processes in different ones and let them run for a while.

To alleviate returning users’ working-memory load and help them recover context, upon completion of a process, provide details that summarize what happened while users were away.

Successdialogs(system messages that alert the user that a process has been successfully completed) can supply useful contextual information such as time elapsed, a timestamp of when the processes was completed, and links to any relevant information related to the completed process (e.g., new records created, related documentation for errors, logs). Using this information, users can learn typical processing times, make better informed decisions about whether they should invest in other tasks during similar processes in the future, and increase confidence that the process executed as expected.

Success dialogs are also an appropriate place to provide details about the results of the executed process — new records that were created, data matches or validations that took place, errors that occurred, or steps that were skipped.

Better yet, success dialogs can provide direct links to any relevant content associated with details when appropriate.

To contextualize success messages for users of complex applications:

Make use ofmodalsfor success dialogs occurring after longs waits (i.e., do not allow them to disappear without explicit user interaction).

Users returning to a particular workflow after an interruption may not remember exactly what information they were looking for, which steps they completed, or why they took a particular sequence of actions. An often overlooked strategy for helping complex-app users remember their previous goals and actions is supplementing working memory with some source ofexternal memory, where users can save and access information needed during their workflow within the system.

One relatively straightforward way to support the creation of an external-memory source it to allow user-generated notes or comments within the application. Using this functionality, users can track their thought processes during complex work.

For example, the decision-modeling software below allows users to create and attach comments to different distribution options as they experiment with running various analyses on their data. These comments can then be viewed in context of the workflow when analyzing the model, helping users recall what they were looking for or why they took these actions.

When users do not have the ability to leave open-ended comments in their workflows, they face undue burden to understand and remember the purpose of objects within complex models or projects. For example, one engineer in a recent study session complained about the lack of ability to add a note to his work:

There are no comments or anything…so you have to open every single item to know, this one is to retrieve data, this one is to [do something else]…And you always constantly have to do that… I should be able to add a note…to say this is here because the VP of sales needs it, or because this means ‘x.’

Without the ability to add open-ended notes, users typically resort to creating and maintaining various external documents — such as a series of spreadsheets — to log their actions and thought processes. These external documents become a burden to manage and reference during complex workflows.

To help users of complex applications track their thought processes:

Efficiency is critical for users of complex applications. Even seemingly small interactions, such as requiring users to click into a couple of extra screens in order to access a list or table before selecting and loading a project, compiles into wasted time and effort for frequent users who switch between projects or files several times a day or even hour.

To support quick task reentrance after breaks in workflow, provide historical content, such as a list of recently viewed files or pages, as soon as possible after the user logs into the application. These lists remind users where they left off and provide some quick entry points back into their workflow. For example, Azure DevOps provides a list of recently accessed content under the headingContinue where you left offwhen the user logs into the program.

When providing a list of recent, favorited, or common items, label the content properly so that users understand what it is, as is done in the example above. In contrast, many applications pin items to a homepage or overview screen without explicitly labeling them  asRecent ContentorContinue where you left off, making it unclear whether theyarefrequentlyorrecentlyaccessed content. Furthermore, it is unclear whether users can customize these items (e.g., pin or unpin items from the area).

Especially for workflows with high information complexity — such as with files that take a long time to load or that may have obscure, hard to remember, system-generated names — it can be useful to also provide a preview for historical content. For example, the application below provides thumbnail images of recent files alongside the recent file names. As the mechanical engineer using the program described, “File preview is nice here, because it takes a long time for these files to load. [There is] lots of lost time if you open the wrong file.”

To help users quickly reenter previously initiated tasks:

Frequently, users will prefer to perform another task, view additional information, or reference other content within the application while a process is running. Don’t trap users into a long wait during these processes by forcing them to be idle while the system works. Allow users the option to run lengthy processes in the background, so that they can continue their work within the application during the time the process is running.

It’s worth nothing that, because processes that run in the background are not highly visible to users, the success dialogs that display at the completion of these processes should be highly salient and discoverable. Modal success dialogs, which must explicitly be dismissed by users, are appropriate because users are likely not paying attention to or thinking about these processes as they continue their work.

Long waits are often inevitable during complex workflows, but there are several strategies for helping users cope with the duration of these waits and supporting task reentrance at the end of them:

These guidelines and more are discussed in our full-day course,Designing Complex Applications for Specialized Domains.

Components, design patterns, workflows, and ways of interacting with complex data

Interaction

Enhance your judgment and resolve tough design challenges

Management