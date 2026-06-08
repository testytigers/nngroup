# Indicators, Validations, and Notifications: Pick the Correct Communication Option

**Author:** Kim FlahertyKim FlahertyJanuary 17, 20242024-01-17

**Topics:** Application Design

**Source:** https://www.nngroup.com/articles/indicators-validations-notifications/

---

January 17, 20242024-01-17

Share

In interaction design, a system, whether an application, website, or piece of hardware (anything from asmartwatchto athermostat), should alwayskeep users informed, by providing appropriate feedback. Ensuring that the state of the system is always visible is one of the10 usability heuristics for interface design. Information about system status, such as error messages and notifications of system activity, allows users to fully understand the current context.

The best way to communicate system status varies depending on several key factors:

Three common approaches for status communication include validation, notifications, and status indicators. These terms are used sometimes interchangeably in product design, but they stand for different communication methods that should be used in different circumstances. Understanding the differences between them will help you sharpen your feedback to users by choosing the best option for each need.

An indicator is a way of making a page element (be it content or part of the user interface)stand out to inform the user that there is something specialabout it that warrants the user’s attention. Often, the indicator will denote that there has been some change to the item represented by that element.

Although, as we’ll see later, indicators are used quite frequently to signal validation errors or notifications, they can also be used on their own.  Indicators are visual cues intended to attract users’ attention to a particular piece of content or UI element that is dynamic in nature.  (If something always looks the same, it’s not an indicator, no matter how flamboyantly it’s designed.)

There are at least three possible ways of implementing indicators:

Characteristics of indicators:

Indicators can introduce noise and clutter to your overall interface, and may distract users, so it is important to consider how many (if any) indicators to use in your design.

Consider the following when deciding if an indicator is appropriate:

Validation messages areerror messagesrelated to users’ inputs: they communicate whether the data just entered was incomplete or incorrect. For example, in e-commerce systems, validation messages often involve information such as name, billing address, and credit-card information.

Characteristics of validation:

The way in which validation should be implemented varies based on the unique needs of the form.  However, in general, if the user’s input is incorrect, the system should inform the user by providing an identifiable and clear message that aids in correcting the error. Validation messages should follow theguidelines for error messagesrather than simply identifying the problem, they should tell users how to fix it.  For instance,  don’t  state “Field is blank.” Please enter your street address” is more polite and directs to a solution.

Since validation is contextual, it can be helpful to use anicon indicatoralong with the validation message to help communicate which input(s) are missing or need corrected.

Notifications are informational messages thatalert the user of general occurrences within a system. Unlike validation, notifications maynot be directly tied to user inputor even to the user’s current activity in the system, but they usually inform the user of a change in the system state or of an event that may be of interest. In the case of email, social networks, and mobile-phone applications, notifications can even be delivered while a user is away from the application.

Notifications can becontextual—applying to a specific UI element— orglobal—applying to the system as a whole.

Characteristics of notifications:

There are two main types of notifications, which differ based on whether the user is required to act upon the notification:

Action-required notifications are often urgent and should be intrusive; for instance, they could be implemented as modal popups that interrupt the user, forcing immediate attention and requiring an action to be dismissed.

Passive notifications are typically not urgent and should be less intrusive. A typical implementation of a passive notification may be a badge icon or a small nonmodal popover in a corner of a screen. Passive notifications can easily be missed, since they require no user action. When the information provided by the notification is key to the understanding of the system, an easy-to-ignore passive notification can be problematic.

Notifications have the design challenge that they are not always the immediate and obvious result of a specific user action. In some instances, the user may be in the middle of doing something different and may not be thinking about the issue raised by the notification. This requires notifications to establish more context and provide users with sufficient background information to understand what the notification is about.

(In contrast, with a validation, the user has just done the thing that needs to be corrected. Thus, the validation message doesn’t need to educate users about the task at hand. For example, if an e-commerce checkout form has a field for a credit-card expiration date that was left blank, the validation message doesn’t need to say“Please provide the expiration date for the credit card you want to have charged $29.90 to pay for the blue sleeveless dress you are in the process of buying on Uniqlo.com.”However, a notification the following day that the dress has been shipped from the warehouse would need to say more than“Your package has shipped.”)

If a notification is contextual and relates to a specific element in the interface, an icon indicator on the element can communicate where that notification applies and catch the user’s attention.  For instance, an indicator badge on a mobile-app icon shows that the user has received a notification from the corresponding app.

Using the wrong communication method can have a negative impact on the users’ experience. Let’s refer back to the scenario above where Yelp utilized a green-tag indicator in the search results to indicate that Tea Market had a special deal running. This information is contextual and important to users who have specifically searched for a place to have tea.

You may think that an alternative way of alerting users of potential tea deals would be to send them a notification when such a deal has become available. Wrong! A notification sent irrespective of the current user goal would likely be ignored, and may even annoy users because it will disrupt their current task and be irrelevant to their current needs.

(In general,any type of ad tends to be ignored unless it is related to the users’ aims and mindset.)

Alternatively, a toast (a small nonmodal popup that disappears after a few seconds, like theNew Storiesone used by the Facebook app), while appropriate for passive notifications, would be a bad way to implement an error message, be it validation or otherwise. In fact, one of our mobile users spent 5 minutes waiting for some content to load only because she hadn’t notice the little error message presented at the bottom of the screen that quickly faded away after 5 seconds.

Remember the key differences between the three communication methods are:

Understanding when and how to use each of these feedback tools is important in order to build consistency in the communication to users. By assessing the type of information delivered, we can determine the correct mechanism to use.

Components, design patterns, workflows, and ways of interacting with complex data

Interaction