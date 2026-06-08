# Mobile Tutorials: Wasted Effort or Efficiency Boost?

**Author:** Alita KendrickAlita KendrickMarch 8, 20202020-03-08

**Topics:** Application Design, Design Patterns, Mobile & Tablet

**Source:** https://www.nngroup.com/articles/mobile-tutorials/

---

March 8, 20202020-03-08

Share

There are several different methods that mobile apps use to onboard new users: tutorials, interface tours, gamified onboarding, contextual help, and so on. But, do these methods work? In other words, do they have an impact on users’ performance and their success using the interface? And subsequently, is it worth the design and development effort to create these onboarding tools?

We conducted aquantitative usability testwith 70 users and 4 mobile appsthat useddeck-of-cardstutorials as a means to onboard users. This particular type of onboarding was selected as the focus of this study due to its popularity in mobile apps.

Deck-of-cards tutorials contain help or tip screens that provide instructions for how to use an interface and are usually presented when a mobile app is first launched.

Thestudy was conducted as abetween-subject,remote unmoderatedquantitative usability test. We usedUserlyticsas our testing platform and for participant recruitment.

We selected the following apps to test: Movesum, Brainsparker, LaunchCenter Pro, and Sketch.Book. All apps were iPhone apps. These apps are not highly complex applications and did not require specialized expertise or advanced training to use.

These mobile apps were chosen because 1) at the time of the study, they had tutorials, 2) they allowed users to skip or close the tutorial, and 3) the apps were not widely known (which made recruiting easier and prevented prior exposure to the app).

Participants were diverse in age, location, and ethnicities. Besides participant diversity, the most significant factor for our participant recruitment was that they had not previously used or downloaded any of the four apps being tested. All participants were prior iOS users. Thus, these users could be expected to know general basics of mobile-app use, but not the specifics of using the apps in the study. (Note: participants signed up for a “Mobile App Study” and were not made aware of the purpose of the study at the time of recruitment.)

Participants were assigned to one of 2 groups:

In total, we had 70 participants, 35 in each group.

For each app, users were asked to do the following actions (in this order):

For example, here are the instructions for the Movesum app:

Group A: Deck-of-cards tutorial

Group B: Skipped tutorial

At the time of this study, Userlytics did not provide randomization, so we manually randomized the order of the apps being tested, in order to avoid order effects. This was done manually by splitting group A and group B into 6 separate subgroups for which we created separate tests and manually reordered the apps being tested. (If all users tested the apps in the same order, we may have seen better performance in apps tested later in the session, due to participants’ learning.)

Participants were asked to think aloud and mention anything they encountered that made them feel stuck or unsure about how to proceed. However, users were asked to complete the 4 tasks as quickly and accurately as possible.

We collectedtask success,single-ease questionnaire (SEQ), andtask-completion timefor each primary task — these were thedependent variablesin our experiment, with the independent variable being the act of engaging or not in the tutorial. We excluded those trials when participants were not able to download the app or complete the initial instructions. In total, we removed 13 trials (5% of total trials).

We observedcomparable task success rates for the two conditions. Task success across the four apps tested was91%for the those who read the tutorial (n=35) and94%for those who skipped the tutorial (n=35). This difference was not statistically significant (p=0.443):basically, whether people viewed the tutorial or not, they were still very successful at completing the primary task.

Part of the reason for the high success rates may be that the tasks in the mobile apps tended to be fairly simple. One participant in group A said, “to me, I didn’t even have to watch the tutorial, but I guess it’s there if you need it.”

After completing the second task for each app, we asked participants“Overall, how difficult or easy was the task to complete? 1 (very difficult) to 7 (very easy).”Across all the apps, group A, who read the tutorials (n=35), had an average SEQ of4.92while group B, who skipped tutorials (n=35), had an average SEQ of5.49. This difference was statistically significant (p=0.047). In other words,participants who read tutorials perceived tasks (which were explained in the tutorials) as more difficult than those who skipped tutorials.Half a point is a fairly substantial difference on a 1–7 rating scale.

Group A, who read the tutorials, may have reported these tasks as more difficult because tutorials can make apps seem overly complicated.We also observed this effect withcoach marks and instructional overlaysin mobile apps. Users may expect a tutorial for complex applications, but for mobile apps, particularly those labeled as ‘easy’ or ‘intuitive’, a tutorial may shift users’ perception and make them think the app is more complicated than it really is.

In what follows, we report task-completion times — that is times for those trials when users were able to complete the task successfully. (We carried out an analysis including all trials and the results were the same.)

Across all the apps, group A, who read the tutorials had a mean task-completion time of93.49seconds, while group B, who skipped tutorials had a mean task-completion time of85.17seconds.This difference was not statistically significant(p > 0.1): in other words,reading the tutorials did not make users faster at completing the tasks described in the tutorial.

(Because task times tend to be skewed to the right, instead of using the arithmetic mean — the traditional “average” — to describe the set of data, we used thegeometric mean. Confidence intervals reported below are also based on the geometric mean. To understand what the geometric mean is, when it should be used, and how to compute confidence intervals centered around it, see our class onstatistics for UX.)

Note that the task-completion times reported here did not include the upfront time to read the tutorial before using the app. (For example, for the MoveSum app, they reflect the time to use the app to set a target of 6500 steps.) If this reading time had been added, then obviously the total time would have been much higher for users who read the tutorial compared to those who did not. Since tutorial-reading time is a one-time expense, it’s not reasonable to include it in a per-task time metric, but seen from the perspective of total user burden, it’s still a downside for tutorials.

This study focused on 4 iOS applications. Thus, it is technically possible that:

These objections are valid. However, in recent years, we’ve observed that the UIs for Android and iOS devices tend to converge, so there’s little reason to believe that tutorials on Android apps will have a different effect.

Think twice about creating a tutorial for simple applications.Tutorials take time and effort to design and develop, and those would be better spent on making the UI easyto useand thus alleviating the need for a tutorial in the first place. We already know that many participants skip tutorials when they first download an app. But now we’ve found that participants who read tutorials perceive tasks as more difficult and they don’t show any advantage in terms of success rates or task-completion times compared with people who skip the tutorials.If, even when people read these tutorials, they don’t make a positive impact, are these tutorials worth building?

Instead of a tutorial acting like a polished manual, consider whether you need formal onboarding and if you do, consider interactive methods of doing so, likecontextual help.

Components, design patterns, workflows, and ways of interacting with complex data

Interaction

Use metrics from quantitative research to demonstrate value

Research

Calculate, interpret, and report the numbers from your quantitative UX studies

Research