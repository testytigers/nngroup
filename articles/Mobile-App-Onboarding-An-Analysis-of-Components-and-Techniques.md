# Mobile-App Onboarding: An Analysis of Components and Techniques

**Author:** Alita KendrickAlita KendrickJune 21, 20202020-06-21

**Topics:** Application Design, Design Patterns, Mobile & Tablet

**Source:** https://www.nngroup.com/articles/mobile-app-onboarding/

---

June 21, 20202020-06-21

Share

Imagine being dropped into a new job with no explanation of your primary work tasks or how to accomplish them. You probably wouldn’t be very successful (however that’s measured) or stay for very long, right? Having an effective onboarding process is key to enabling new employees to succeed. Further, each time a new process is introduced, onboarding would again be needed to get everyone to adopt it.

The same is true for user interfaces, particularly when the interface is something intended to be used repeatedly. In this article, we’ll focus on mobile-app onboarding.

We defineonboarding as the process of getting users familiar with a new interface, using dedicated flows and UI elements that are not part of the regular app interface.This includes not only teaching users how to interact with the interface (a common misconception), but also completing any necessary setup. Additionally, onboarding is not limited to first-time users — existing users may also be onboarded when new features or redesigns are released. Thus, onboarding can occur at multiple points in a user’s lifecycle of an app, not just the first launch.

Generally speaking, onboarding is problematic for a few reasons:

Consequently,  we recommend professionalsavoid creating app onboarding whenever possible and instead spend your resources making the UI moreusable.

Users always need (often minimal) time to learn a new app, but that doesn’t mean that all apps require separate onboarding flows or lengthy explanations. For most mobile apps,users should be able to learn the interface by using it and thusinstructional onboarding flows are not necessary. Even for fairly complex mobile apps, it’s often more effective to train users by showing themtips in contextinstead of presenting them with a tutorial that explains the app’s UI — people are simply unlikely to (even try to)remembera lot of information, especially if they are not sure whether they will actually have to use it. Also, while errors are a negative element of user experience,error messages can teach usersa bit more about the app in a “teachable moment” where people have a small degree of motivation to read a few words about how to fix the problem.

There are only a few situations when onboarding screens can be useful in a mobile app:

If you’re still unsure whether your app needs onboarding, test the app with no onboarding before investing money into adding extra screens. Do your users show difficulty using the app (or a new feature) for the first time? If yes, consider first whether you may be able to make some changes to the app design to make it more learnable. If that’s not possible, prototype an onboarding flow and test it. Does it solve your problems? Are people more successful at using the app? Only if the answer is yes, it is worth adding dedicated onboarding to your UI.

There are three frequently encountered components in mobile onboarding flows: feature promotion, customization, and instructions.An onboarding flow may contain one or more of these components.

In what follows, we look at each of these components in mobile apps and we discuss whether they are warranted.

Feature-based onboarding educates users about what the app can do, and, as such, tends to be perceived as marketing.

Avoid feature-promotion onboarding at first launch. Users rarely download an app for no reason; therefore, lengthy promotional onboarding will likely be skipped. The one exception to this rule is when a feature is truly new or advanced, such as the mobile-deposit example mentioned earlier. (Keep in mind though: that technology is no longer new, so today’s apps should not promote it at first launch! How quickly a feature progresses from novelty to well-known will vary, depending on how frequently it’s used and the memorability of its steps.)

Instead of front-loading users with this information, present these types of promotional screens on the app store page, as that is where users will explore new apps and compare features.

In addition to highlighting features on the app store, another solution is tohighlight features while the user is in the app, throughcontextual help. For example, in the Productive app, it’s likely that users will want to see habit statistics only after there’s enough data. Instead of advertising this functionality before users have the means to do anything with it, highlight it when it’s actionable for them. For instance, after a user has logged 7 days’ worth of data around a habit, the app might provide a visual cue (like highlighting the statistics section of the app) and a short bit about what users can do with this data.

Though this type of onboarding is less valid and helpful to a user at the app’s first launch,feature onboarding can be helpful to existing users when new features are released. For example, Chase used a deck-of-cards onboarding flow to introduce its new budgeting feature.

Limit the usage of feature onboarding to what is truly new to users, not what’s been in your app for a while and has low utilization. Consistently highlighting existing features that your users may already be familiar with but aren’t relevant or needed by them can annoy people and make them ignore all such onboarding elements, even those for legitimately new features.

Many applications request user data so they cancustomizethat user’s experience. For example, users might customize the content or visual design of an app. However, not all customization should be done during onboarding.

In particular,visual-design customization, such as selecting a color scheme, doesn’t belong in onboarding.It’s hard for people to know how they will prefer the app to look before actually using it or why a certain visual design may be better than other. (Also, in general, a lot of research shows that people usually stick withdefaults. Instead of making them choose and increasing the cognitive load, do your homework, run a study, and figure out which design is best.)

This is not to say you shouldn’t offer the functionality to customize a visual design, but you can save it for later. It does not deserve priority in your onboarding.

Content customization can create a relevant experience and is more likely to be appropriate for initial app onboarding.There are dozens of examples of content customization in apps. For example, for a language-learning app, picking a language and identifying how proficient you are in that language will be essential in order for the app to be useful.

When prompting users to customize their experience, keep it brief. Explain why you want that data and how it will be used (as in the Fitplan example above). Consider whether you truly need this information for a user to get started and be successful in the app. If you can’t explain why gathering that data is beneficial at launch, this information should be gathered later, once the user can better understand why it’s necessary.

The goal of instructional onboarding is to teach users how to use an interface.Instructional onboarding should not be used to supplement poor design.Resources are better spent for making a UI more usable than for creating instructional content. That said, there are cases where instructions are warranted (for example, the features or workflows are unique to the app, different from standard UI patterns, or legitimately new and unfamiliar to users) or expected (mobile gaming).

Instructional onboarding comes in many forms: deck-of-cards tutorials, contextual help, interactive walkthroughs, and so on.No matter the form, instructional onboarding should be brief, optional, and should only highlight the minimum that users need to know to use the app.The following are examples of instructional-onboarding styles in mobile applications.

Deck-of-cardstutorials usually are presented immediately when the app is launched and provide instructions for how to use its interface in a deck-of-card format (similar to a carousel). This type of onboarding, particularly in relatively simple mobile apps, tends to make the interface appear more complicated than it actually is, and strains user’smemory. Therefore,we don’t recommend deck-of-cards onboarding.That said, if you still choose to implement them, be kind to your users and ensure there’s a highly visible Skip option, minimize the number of cards to only focus on need-to-know information, and focus on one concept per card.

Instructional overlays and coach marksare another type of instructional onboarding, used to show users where some core functionalities are located within the UI and what those elements do. When implementing instructional overlays, ensure the content is timely (like at a user’s first encounter with a feature) and unobtrusive. This type of onboarding pairs well when it accompanies a user trying to complete a task for the first time, and as such, provides extra nuggets of information as the user progresses. For this reason,instructional overlays are often nice-to-have and not need-to-haveelements.

If your app is more complex than some of the previous examples, and you believe instructions are warranted because the design is new or unfamiliar, consider an interactive walkthrough.Interactive walkthroughs enable users to learn by doing (ideally in a low-stakes environment). When done successfully, (i.e., brief and only highlighting what’s new or unfamiliar, as mentioned above) interactive walkthroughs feel more like a practice round and less like a tutorial.

Most mobile apps don’t need instructional onboarding. If you do include it in your app, save it for what’s novel (i.e. the elements and interactions that make your app different from similar apps) and make it short.

Keep onboarding as simple as possible. For most mobile apps, this means putting users directly into the interface. On the other hand, complex apps with unique interaction patterns or those that want user information to tailor the experience may benefit from onboarding flows. With onboarding, focus on what users need to be successful in your app, highlight what’s new or unfamiliar, and keep instructional content brief and unobtrusive.

Components, design patterns, workflows, and ways of interacting with complex data

Interaction