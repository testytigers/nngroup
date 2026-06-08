# CASTLE Framework for Workplace Applications UX

**Author:** Page LaubheimerPage LaubheimerJanuary 29, 20232023-01-29

**Topics:** Analytics & Metrics, Application Design, Intranets

**Source:** https://www.nngroup.com/articles/castle-framework/

---

January 29, 20232023-01-29

Share

Google’sHEART frameworkis a flexible and easy-to-understand way to define metrics for user experience. HEART is an acronym standing forHappiness,Engagement,Adoption, Retention, andTask success; those five areas are key constructs meant to account for the most important aspects of the user experience. Each of those five key constructs is broken down into high-level goals, behavioral signals, and quantifiable metrics.

While this framework is flexible and robust in most circumstances, several of its dimensions (engagement, adoption, and retention) are meaningful only for consumer products, where the user can decide whether to use the product. If you work on products that people use for their work (such asenterprise products,intranets, healthcare systems, government tools, and many other types ofcomplex apps), where the end user may not get to choose whether to use your product, the HEART framework is less applicable.

Retention, for example, is not meaningful when your usersmustuse your product as part of their job. Then user retention will be directly correlated with your employee attrition rate — not a particularly usefulmeasure of the user experience(though, I suppose, a piece of software could be so unusable that employees quit when forced to use it).

Importantly, the HEART framework has no specific requirement that all five dimensions should be used, and you can come up with some creative adaptations for some of these dimensions for example, adoption could be used to measure the rate of discovery for optional advanced features (such as anacceleratorintended to speed up a workflow). However, there is still a lack of specificity and sensitivity in the HEART framework for the things that matter to productivity applications.

As an alternative, we offer a complementary framework intended for products that are compulsory for users: the CASTLE framework.

CASTLE is an acronym for:

C = Cognitive loadA = Advanced feature usageS = SatisfactionT = Task efficiencyL = LearnabilityE = Errors

Much like in the HEART framework, the six dimensions are constructs intended to represent the most important elements of user experience for productivity applications that are used as part of someone’s job. The selection of these constructs has taken into account general user-experience principles and priorities, as well as typical business cases and needs for workplace software.

An important thing to keep in mind with this framework (like with HEART) is that each dimension will require the team to break down the big construct into smaller, measurable ideas. While a big concept such as learnability should be tracked, it is not itself measurable, as it’s too broad and ambiguous. Taking that concept and turning it into a quantifiable metric requires operationally defining what it means for your own product to be learnable (and what behaviors signal that the things you want to happen are indeed happening). To that effect, in the HEART framework, each main concept is usually broken down into goals, signals, measures. Goals are high-level product or feature goals, signals are behaviors that indicate the goals are being fulfilled, and those are further broken down into specific quantifiable measures. Typically, each goal will have several signals (and thus several measures) associated with it. We recommend that you also employ the same goals, signals, measures breakdown with the CASTLE framework.

We discuss each of the 6 main dimensions in detail below.

Cognitive loadrefers to the level of mental effort required to complete key tasks. It includes the user’sworking-memoryburden while they complete workflows, as well as how easily an interrupted task or workflow can be resumed. For example, a repetitive task that requires users to remember which record in a long list they were reviewing whenpogo-stickingbetween list and detail pages would place the user under a fairly high cognitive load. Sifting through a large number of meaningless alerts to find the one that is meaningful would also cause cognitive load. Doing mental math, converting data formats in one’s head, or trying to “translate” information from how the user thinks of it into an unfamiliar data model are other examples of high cognitive-load tasks.

Note that this dimension is noteasilymeasured through analytics, as users’ mental workload is not directly observable. However, it can still be quantified through use of survey instruments such asNASA-TLX, or through expert-based usability-inspection methods likePUREor cognitive walkthroughs.

Below we show an example of how the cognitive-load dimension could be broken down into high-level goals, behavioral signals that indicate the goal is being met, and a quantifiable measure of the construct. Each dimension will typically be broken down into a few goals, which are, in turn, broken down into several signals and measures.

Example

Goal

Signal

Measures

Cognitive Load

Notifications are not too frequent or intrusive.

Users self-reported level of mental workload decreases.

NASA-TLX

Many teams build advanced features and functionality (such asacceleratorsorcustomization) and are later disappointed that these don’t get used as widely as the team hoped (even if they are helpful or useful in theory). In enterprise and complex software, many userssatisfice— once they learn a method to complete a task, they stick to it, without trying to improve on it, even if it’s a poor workaround. The advanced-features dimension covers usage rates ofoptionalfeatures — what proportion of users interact with features that they technically are not required to use but would be beneficial to them. Importantly, this metric is not intended to foster user-education initiatives such asintrusive push revelationsandonboarding tutorials(which often fail to get usage rates up) but, instead, is meant to help the team evaluate thediscoverability,clarity, orusefulnessof these features, and to help prioritize future featureroadmaps.

Example

Goal

Signal

Measures

Advanced features

Data dashboard presents information that is helpful to individual users.

Users customize their dashboard widgets to personal preferences.

Rate of accounts that customize dashboard widgets, most common customization choices (tracked through analytics)

Next, we havesatisfaction, or how the user feels about using the product. Productivity or workplace tools do not always aim todelightusers, but seek to support them in their work, and limit their frustration and discontent. Analytics will not be an appropriate way to measure satisfaction (or any other subjective metric), since it is not directly observable. We recommend a mix of surveys, posttask questionnaires in quantitative usability research, and analytics signals such as “rage clicks” (found in visual analytics tools like Smartlook).

(In rare cases, some limitedsupplementaryuse of biometrics data — such as skin conductance, heart rate, pupil dilation, or facial-expression recognition — can allow us to observe and quantify user reactions without relying on their self-reports, but these kinds of data are expensive to gather and hard to analyze, so you probably will be better off spending the money on collecting traditional metrics.)

Example

Goal

Signal

Measure

Satisfaction

Users enjoy working with the product

Self-reported satisfaction

Questionnaire: SEQ

Task efficiency is fairly straightforward conceptually: it measures how quickly users can successfully complete key workflows. Efficiency can be quantified as time on task or the number of steps that a user must undertake to complete their workflow. Generally, time-on-task measures collected through analytics are unreliable, for two reasons: first, external factors (like interruptions) can skew the time on task (in a way that is not under the control of the designer) and, second, it is very difficult to operationally define when a task has begun and ended in open-ended software that allowsusers flexibility. As a result, we recommend that efficiency measures come fromquantitative usability testing, where the task is clearly defined, and the experiment is controlled toavoid external influences.

Example

Goals

Signals

Measures

Efficiency

Users can complete key tasks without getting sidetracked.

Users complete workflows quickly.

Time on task (measured in quantitative usability testing)

Users complete workflows with the fewest number of steps necessary.

Deviations from “optimal” task procedure (obtained through log analysis)

Learnability covers the effort, time, and resources needed for a new user toonboardandlearn how to use the product effectivelyin their role. Often, complex workplace products have an onboarding period that involves lengthy training classes (with material that will be largely forgotten after the sessions); after the trainings, users need to frequently reference help and documentation. Improving learnability enables new hires to be productive quickly and to remember more from any necessary training they must undergo.

Learnability can be looked at from a variety of angles:task-performance improvements over time, fewer deviations from the “happy path” in a task, less need for reference materials, fewer task repetitions required to reach a baseline level of acceptable performance, and so on. Each of these aspects can be measured in different ways, such as throughquantitative usability testing(measured longitudinally), detailed log file analysis of individual user interactions, orcognitive walkthroughs.

Example

Goal

Signal

Measure

Learnability

Users can recall how to complete a key workflow.

User task performance improves over time.

Time on task (measured longitudinally, in a quantitative usability test withwithin-subjects design)

Finally, the errors dimension covers both data-qualityissues (such as accidentaldata-entry slipsor misunderstanding-drivenmistakes), as well assystem-error messagesthat stop users in their tracks. Instrumentingerror messagesto track how commonly they occur is an important first step, but it is worth exploring more nuanced indicators of errors, such as repetitive behaviors that might indicate that the user is experiencing frustrating loops. For example, autocorrect on iOS may recorrect the same word multiple times in a row after a user dismisses the spelling “correction” — this frustrating error loop would be signaled only by tracking repetitive behaviors (or by doing qualitative usability testing and stumbling over the issue).

Example

Goals

Signals

Measures

Errors

User-entered data improves in accuracy.

Users don’t input values that are outside of an acceptable range.

Validation errors(tracked through analytics)

This framework is meant toguideUX professionals in selecting meaningful metrics to track over time. Like with HEART, you don’t need to track all dimensions; you can pick only those relevant to your context.

There is no single set of metrics that will be universally applicable. Instead, this is a framework to help your team to identifywhatto measure, and then to considerhowto operationally define each of these concepts so that you can track them. I’ve provided examples of scenarios for each dimension, but using this framework will require your team to think critically about how to define these concepts for your context and users.

CASTLE is not intended to replace or supersede HEART, which remains a fantastic framework for many product types; rather, it is meant to fill gaps in situations where HEART isn’t as sensitive or perfectly aligned to the UX team’s goals (such as the aforementioned engagement or retention dimensions for workplace applications). Think of it as a sibling to HEART, with a different focus.

Lastly, it’s important to note that quantitative metrics only provide data on whether the very narrow thing you are measuring is improving, staying steady, or worsening; metrics don’t provide information as towhythat is happening, nor do they tell us how to improve the current state.

Thus, this framework helps you decide what metrics to track in order toquantifythe UX improvements, but it will not provide the sort of rich qualitative data that can help your teamunderstandhowto improve your product’s design. We strongly suggest that all UX teamspair any UX-specific metrics with qualitative research, to understand their users’ needs, goals, pain points, or expectations.

Kerry Rodden, Hilary Hutchinson, Xin Fu. 2010. Measuring the User Experience on a Large Scale: User-Centered Metrics for Web Applications,CHI '10: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM Press.https://doi.org/10.1145/1753326.1753687

Lisa Feldman Barrett, Ralph Adolphs, Stacy Marsella, Aleix M. Martinez, & Seth D. Pollak. (2019). Emotional Expressions Reconsidered: Challenges to Inferring Emotion From Human Facial Movements.Psychological Science in the Public Interest, 20(1), 1–68.https://doi.org/10.1177/1529100619832930

Manuela Unsöld. 2018.Measuring Learnability in Human-Computer Interaction. Master’s thesis. Universität Ulm, Germany.https://core.ac.uk/download/pdf/299377564.pdf

Study your users’ real-life behaviors and make data-informed design decisions

Research

Components, design patterns, workflows, and ways of interacting with complex data

Interaction

Use metrics from quantitative research to demonstrate value

Research