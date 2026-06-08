# How to Conduct a Cognitive Walkthrough Workshop

**Author:** Kim FlahertyKim FlahertyApril 10, 20222022-04-10

**Topics:** Heuristic Evaluation

**Source:** https://www.nngroup.com/articles/cognitive-walkthrough-workshop/

---

April 10, 20222022-04-10

Share

Acognitive walkthroughis a technique used to evaluate thelearnabilityof a system. Unlike user testing, it does not involve users (and, thus, it can be relatively cheap to implement). Likeheuristic evaluations,expert reviews, andPURE evaluations, it relies on the expertise of a set of reviewers to assess the interface.

Although cognitive walkthroughs can be conducted by an individual, they are designed to be done as part of a group in aworkshop settingwhere evaluators walk through a task in a highly structured manner from a new user’s point of view.

Before you start the evaluation, there are a number of decisions to be made up front.

In a group evaluation, you should seek to include 2–6 evaluators of varying roles. Each role brings a different perspective to the walkthrough and, thus, ensures that the evaluation is comprehensive.

Below is a (nonexhaustive) list of individuals you might consider including as evaluators in a cognitive-walkthrough workshop.

When preparing for a cognitive-walkthrough session, you must first define the conditions for the evaluation. There are four questions to answer before you begin:

Even if the user audience for your system may be general, the technique is most effective if you have some high-level context for the users of the interface. For this reason, you should use your userpersonasas the basis for the walkthroughs. If you do not have personas, it’s strongly recommended that you develop personas for use in the walkthrough (and, more generally, for the development of the system).

Personas give you basic information about a type of user’s attitudes, beliefs, prior knowledge, and common behaviors. This information helps you determine whether users will understand the interface and how they will behave, and thus reduce the risk that the evaluators will base their comments on fantasy users. You will conduct one walkthrough per persona.

Websites and applications typically support many user tasks. You will walk through one supported task at a time, so you must decide which tasks are the most important. Consider which tasks are core activities in the system — tasks that many users will engage in or that are so critical that user errors would result in catastrophic or life-threatening consequences.

Define a list of underlying steps that must be taken in the interface to accomplish a task.

We’ll use a sample task from a web-based expense-reporting application, Certify, as an example. Let’s say the cognitive walkthrough we intend to conduct has the following inputs and action sequence:

Below is the sequence of correct actions for her task. Several actions require the user to complete a form or review a page and click Next, in order to streamline the evaluation, we will combine these into a single action.

Be sure to write these action sequences down explicitly for use in the walkthrough.

Because some activities may have various pathways to completion, you may need to start with a primary path and subsequently define alternative paths. It’s best to formally define these steps and variations in advance, to ensure the group is not derailed by debate during the walkthrough.

Cognitive walkthroughs are often done during the development of a new system, so they can be conducted onprototypes of varying levels of fidelity— ranging frompaper prototypesto clickable functional prototypes. They can also be conducted on existing systems to elicit ideas and identify opportunities for improvement. The fidelity of the interface will clearly set limits on the scope of your evaluation. For example, a paper prototype will not allow you to assess the influence of color or realistic imagery on the activity.

Cognitive walkthroughs, like most well-run workshops, rely on clear rules and assignment of participant roles. It’s possible to wait until the beginning of the evaluation session to discuss roles and rules, but doing so in advance of the meeting can maximize the time for evaluation.

To ensure that the meeting is efficient and stays focused on task, communicate basic ground rules for evaluators. With practice, you will learn what ground rules make sense for your team; below we list a few key rules you might start with:

The facilitator will remind everyone of the ground rules during the walkthrough.

The facilitator should ensure that the following materials are ready for use in the session:

Brief the participantsat the beginning of the session. Describe the purpose of the meeting, which task(s) will be evaluated, and on behalf of which personas. Review the basic ground rules and discuss or assign roles for the analysis.

The evaluators’ goal is to determine whether the user is likely to succeed at each step in the predefined action sequence; they should also document why that determination was made.

In order to determine whether the user is likely to succeed, evaluators should discuss 4 key questions (analysis criteria) at each step:

To streamline the recording process during the walkthrough, it is helpful to utilize a recording tool or template for each predefined step in the action sequence of the task. Below is a printable template we recommend for recording the group’s decisions manually. This template and digital-form option are included for download at the end of the article.

The recorder fills in the overarching task and the specific step. For each of the four analysis questions, the recorder marks the appropriate answer —yesorno. For each question, the group should be able to explain why this is the correct answer.

Below we’ll show how the evaluation template might be filled out for 2 of the 3 actions in the action sequence for our expense report example.

Lastly, the recorder circles the overall success/failure determination for the step in the top right corner. The overall success for the step requires a checkmark in theyescolumn for each of the four criteria for analysis. However, for the step to be marked as a failure, it needs anofor only one of the four criteria.

If your team determines that the user would fail at any step of the action sequence, note the problem and proceed to analyze the next step as if the current one had been successful. That is, assume that the system gave feedback for the correct action and is now in the state corresponding to the successful action. (This approach guarantees that, even if the walkthrough identified a problem with one step, subsequent steps can still be analyzed.)

Action

Determination

Select thePlayicon next to the exclamation-pointicon on one of the expenses in error.

Fail

Select theMerge Expenseslink.

Success

Approve the merge in theConfirmationmodal.

Success

The length of a cognitive-walkthrough session is up to the facilitator, the participants involved, and the complexity of the tasks that are analyzed. It’s generally possible to evaluate two full tasks in a 90-minute session.

After the group has finished evaluating each step for the defined tasks, the workshop concludes. The recorder should package up the completed templates for each tasks into a shareable format. The session facilitator should then summarize the overall findings of the session and track the identified areas for improvement in the project-management tool used to track work.

Clayton Lewis, Peter Polson, Cathleen Wharton, John Reiman. 1990. Testing a Walkthrough Methodology for Theory-Based Design of Walk-Up-and-Use Interfaces. InProceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI ’90), April 1-5 1990, Seattle Washington USA, Association for Computing Machinery, New York, NY, 235-242, https://dl.acm.org/doi/10.1145/97243.97279

Cathleen Wharton, John Reiman, Clayton Lewis, Peter Polson. 1994. The cognitive walkthrough: A practitioner’s guide. In Jakob Nielsen, Robert L. Mack (ed.)Usability Inspection Methods, John Wiley & Sons Inc, New York, New NY. DOI: https://dl.acm.org/doi/book/10.5555/189200

Foundational concepts that everyone should know

Interaction