# Documenting a UX-Benchmarking Study

**Author:** Raluca BudiuRaluca BudiuMay 7, 20232023-05-07

**Topics:** Research Methods

**Source:** https://www.nngroup.com/articles/ux-benchmarking-repository/

---

May 7, 20232023-05-07

Share

As an organization refines the user experience of a product, a common question is whether the newer version of its product is better than what it had before. The answer to that question is usually provided byUX benchmarking, a practice that aims to measure and compare the UX of different versions of the product.

UX benchmarking involvesrunning a set of iterationsof the samesummativestudy(called abenchmark study) on various product versions, with each iteration aiming to capture the UX of the current version of the product. To gauge UX improvements from one version to the next, researchers would have to compare metrics such assuccess rate, task time, anduser satisfactionfor some important tasks. They will also have to go beyond the observed values of the metrics obtained in the two studies and run a statistical analysis to judge whether the observed differences arestatistically significantor due to chance.

Imagine that the first iteration of the benchmark study, which evaluated the original version of the design, was conducted in person, whereas the second iteration wasremote unmoderated. Often, people tend to stay more on task in in-person studies than in remote unmoderated ones, and, as a result, times from remote unmoderated studies tend to be longer. Thus, if we notice a difference in task time or success rates between the two design versions, it could be due not to a better design, but to the way in which the study was conducted.

To soundly compare the results from the two studies, the company needs to compare apples to apples. In other words, the studies need to havethe same methodology and collect the same metrics.

Any company that considers a benchmarking practice should firstdefine the benchmark studyin minute detail and document it so that subsequent versions of the same design could be evaluated using the exact same methodology and metrics.

Usually, the study details and the raw data collected in the study are stored in abenchmark research repository.This repository could be part of theresearchrepositorymaintained by the company or could be separate. However, it should be easily findable and accessible. People who are involved in the UX evaluation of subsequent product versions should be able to refer to both the study information and the raw data from the study when they need them.

There are several aspects of the study that need to be well documented so that anybody will be able to replicate the study in the future. They include:

Differences in study methodology impact the results of the study and ultimately bias our comparison in one direction or the other. All the methodology details— ranging from the type of study to task phrasing — need to be well documented so that researchers who will run the subsequent iterations of your benchmark study will be able to replicate it.

These details include:

Generally, a benchmark study should collect measures regarding thetoptasksthat your users run on your site. These tasks usually remain the same across the product’s lifetime. (If they change, then it makes less sense to compare various versions of your product.) Thus, thesetop tasks should be included in all the iterations of your benchmark study.

There are several aspects of the tasks that need to stay the same across all iterations:

If you change how the task is phrased, it is possible that users may understand it differently and that can ultimately invalidate any comparison with prior versions.

Additionally, in many quantitative studies, when we want participants to place an order or log into an existing account, we may give them a name, an address, or other information that they can in order to perform the task. This information needs to be well documented. (For instance, if you use different names or addresses, these may require different typing times and they may affect your overall task time.)

We normally advocate task randomization in quantitative tests, to avoid introducing any biases in the study. Sometimes, however, it is not possible to randomize all tasks. (For example, if one of the tasks involves logging in, it will probably have to precede the task of accessing specific information in one’s account.) Thus, the order in which the tasks are presented (whether random or not) needs to be documented so it can be replicated in further iterations of the study.

Practice tasks are generally used to get participants comfortable with the study setup and the task domain, and thus mitigate the learning phase inherent to any experiment. (Some people are slower to warm up, others are faster. These individual differences add variability to the data collected in the study; to reduce that variability, quantitative researchers often use 1–2 practice tasks at the beginning of each study.) If you used practice tasks in one study, these should be present in all the iterations.

Another essential component of any study is the participants. It is unrealistic and, for most studies, also undesirable to set the goal of recruiting the same participants for different iterations of your benchmark study. However, even though the participants will differ across study iterations, they should be recruited using the samescreener. Otherwise, it is possible that any differences that you might observe are not due to the design, but rather to participants’ individual characteristics.

Thus, the screener used for the benchmark study should be included with all the other study documents in your research repository.

There are many types of metrics that one can collect in a quantitative study. Some are relatively standard and likely to be used in most quantitative studies — for example, task success, usually defined as a binary metric (0 means success and 1 means failure). Others can be defined by the particular study. For instance, if your study includes asurveythat is specific to your product, the answer to that survey will be a metric specific to your study.

For any kind of metric that you collect,clearly document how that metric is defined.

Even for metrics that feel obvious, likesuccess, you need to specify what counts as success. For example, for the task of subscribing to a monthly newsletter, was success defined as clicking theSubscribebutton or as reaching the page where that button was found?

If you are collectingtasktimes, are you recording only the task-completion times (that is, the times of those participants who successfully completed the task) or are you recording all the task times, whether participants were correct or not? Both these types of time measures are common in quantitative studies, so make sure that all the iterations of the benchmark study use the same.

If you includedratingquestionsor other multiple-choice questions in your study, record the wording for those questions and the possible responses. If you created a multiple-question survey instrument and defined a score for that, explain how the score was calculated. Any changes in the question or the responses could invalidate cross-study comparisons.

Once the first round of the benchmarking study is complete, the researcher will usually analyze the data and present a summary of the findings. It’s not enough to save a copy of the findings in your research repository. Equally important is tosave the raw data— the spreadsheet (or spreadsheets) containing the data points generated by each participant.

(Of course, you should not include in such spreadsheets theparticipants’ identifying information; it’s enough to include a code that corresponds to each participant and the metrics that you collected from them.)

There are several reasons why this data needs to be included in your research repository:

At this point, you may ask: what if you run your benchmark study over many years and your company needs, goals, or offerings shift?

It’s okay to change your benchmark study partially or even completely. In fact, it’s a good idea to periodically evaluate your benchmark study to make sure it answers the right questions. However, if you make changes to the study, you might diminish or completely lose the ability to compare with older versions of the product. In many cases that will not be a substantial problem. The new benchmark study can serve you well to evaluate the usability of subsequent versions of your product even if it doesn’t allow you to compare with what you had before.

Sometimes, you may still be able to use the results from the old study. For example, if you decide to add or remove a task to your list of tasks, it’s unlikely that the change will impact your comparisons. (There are some exceptions — for instance, if that removed task must precede another task that was based on it.)

But if you tweak the wording of a task or change the definition of a metric, any comparison involving that task or metric will not be sound (if the comparison involves prior versions of the design).

A UX-benchmarking practice is based on a benchmark study that is repeated periodically, to evaluate new versions of your design. For this evaluation to be sound, the study setup needs to be always the same. The benchmark-study protocol, participant-recruitment screener, and the raw data should be stored in your research repository, so that researchers will be able to precisely replicate the benchmark study and compare the results obtained from its different iterations.

Use metrics from quantitative research to demonstrate value

Research

Calculate, interpret, and report the numbers from your quantitative UX studies

Research

Study your users’ real-life behaviors and make data-informed design decisions

Research