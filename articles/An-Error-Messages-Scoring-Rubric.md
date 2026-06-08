# An Error Messages Scoring Rubric

**Author:** Tim Neusesser, Evan SunwallTim NeusesserandEvan SunwallJune 18, 20232023-06-18

**Topics:** Application Design, Heuristic Evaluation

**Source:** https://www.nngroup.com/articles/error-messages-scoring-rubric/

---

June 18, 20232023-06-18

Share

In the articleError-Message Guidelineswe described 12 guidelines for creating user-friendly error messages. However, guidelines are broad and it can be challenging to apply them objectively. We’ve created an error-message scoring rubric to make these guidelines actionable and informative and help you prioritize UX debt or align stakeholders toward necessary UX improvements.

As attendees of ourDesign Tradeoffs & UX Decision Makingcourse know, evaluating too many factors simultaneously negatively impacts decision-making and ultimately leads to worse decisions. Using a rubric can reduce this problem by asking evaluators to make individual assessments based on common standards. Reviewing the criteria may also provide you with inspiration on how to improve your error messages.

Our error-message scoring rubric is a tool to help you analyze and improve your error messages. The rubric lists 12 error-message guidelines and provides detailed guidance on when to assign a particular score.

The rubric contains 3 dimensions:

Each of these dimensions is further detailed by 4 guidelines that are specific to it. Your error message will be scored for compliance with each guideline. The scoring range contains 4 options:Excellent(4 points),Good(3),Fair(2), andPoor(1).

Once you get a score for each guideline, the scores are added and averaged. Thus, the final score for your error message will be a number between 1 and 4, corresponding to the following letter-grade ranges:

Below are the rubric’sExcellentcriteria for each guideline; dropping some of the criteria downgrades the score. (See our article on Error-Message Guidelines for a detailed discussion of each guideline.)

Download the Microsoft Excel spreadsheet at the top of this article. For an individual error message or a set of error messages found within a workflow or product, observe how the error message(s) presents, review the rubric’s criteria, and then assign a score from 1–4 for each guideline. The spreadsheet will automatically calculate the overall average and give the letter grade.

Here are a few additional tips when using the rubric:

Below are 3 examples where two evaluators leveraged the rubric to assess several error messages. Evaluators independently reviewed the error messages and then averaged their scores.

Situation:Users can change the email address for their account, but they must enter it twice. This error triggers if the email addresses do not match.

Average Score:2.08 (low score)

Points earned by guideline:

VISIBILITY

EXPLANATION

SCORE

The error message is displayed on the same page but is not adjacent to the field that requires attention.

2

The error message is WCAG-AAA compliant, but it lacks clear error indicators, such as iconography, borders, or shading. Additionally, the bold red text for the error message is also used for a warning.

1.5

The message is clearly shown as an error and as a barrier to moving forward.

3

The error message triggers after clicking theSubmitbutton.

4

COMMUNICATION

EXPLANATION

SCORE

The error text is written at a 6th-grade reading level and contains no jargon.

4

The error message does not describe the issue (that the email addresses mismatched) but instead is terse.

1

The error message doesn’t offer any solutions or guidance for resolving the problem.

1

The error message places accountability on the user and has a negative tone.

2

EFFICIENCY

EXPLANATION

SCORE

The system sends confirmation emails to both email addresses that were entered, even though they were not matching. This increases the likelihood of potential mistakes.

2

The entered input is discarded and needs to be re-entered.

1

The user must fully start over the process of changing their email. This increases the effort required from the user to solve the problem.

1

The interface provides some instructional copy and one help resource by linking thehelp desk forum.However, using thehelp desk forumintroduceshigh interaction costs for the user to solve the problem.

2.5

Craigslist – Average Score

2.08

Overall assessment:The message scores decently on visibility due to the conventional red, bold error-message styling. It also correctly displays after the user clicks theSubmit New Email Addressbutton. But theexperience scores lower in communication and efficiency. The error message’s phrasing is terse and subtly faults the user for entering mismatched email addresses. The text inputs are cleared when the error triggers, thus making error correction harder.

Potential improvements:

Situation:This error message appears when no flights match the user’s search request.

Average Score:3.17 (medium score)

Points earned by guideline:

VISIBILITY

EXPLANATION

SCORE

The error message appears on the same page but not adjacent to the fields that need attention.

2

The error message uses text but does not highlight the dates or the destination field.

2

The error hinders users from successfully finding a flight but is styled in a subtle way that may be overlooked.

2

The error message triggers after clicking theSearchbutton.

4

COMMUNICATION

EXPLANATION

SCORE

The error text is written at a 4th-grade reading level and contains no technical jargon.

4

The error message has no spelling or grammar mistakes but is very generic in describing the issue.

3

The error message offers two options to address the situation within the UI. Both options have comparably low interaction costs.

4

The system takes accountability, and the error message conveys a positive tone.

4

EFFICIENCY

EXPLANATION

SCORE

The system does not allow the user to book flights that depart before the previous flight arrives, and thus prevents the user from making a mistake with their booking. Instead, it offers solutions for the previous and the following day.

4

The original input is preserved and editable.

4

The user can easily update the search with the suggested revised search criteria by clicking a button.

4

The system does not provide any information about why there are no flights. The page offers a help link but is far from the error.

1

Google Flights – Average Score

3.17

Overall assessment:This error message performs well in communication. It also scores high in efficiency, retaining the user’s original input and providing easy-to-accept suggestions for alternate dates. Visibility is where this error message loses the most points. The black and grey text blends in with the other interface elements, making the error message hard to recognize.

Potential improvements:

Situation:This warning appears when users change their delivery method fromShip To HometoPick Up In Storeduring checkout. Users must choose one of the two delivery options for all items in their cart.

Average Score:3.67 (high score)

Points earned by guideline:

VISIBILITY

EXPLANATION

SCORE

The warning is shown adjacent to the source of the issue, which is theShipping Optionbutton.

4

The message uses large, bold text and a saturated fill to indicate the warning. It is also WCAG AAA compliant.

3

The warning is visually different from an error message.

4

The warning is shown only after the user decides to change the shipping method.

4

COMMUNICATION

EXPLANATION

SCORE

The error text is written at a 5th-grade reading level and contains no technical jargon.

4

The situation is clearly described in a short sentence and uses wording consistent with the UI (i.e.,bag,item). However, there is a spelling error (Iteminstead ofItems)that might confuse users.

2

Since this is a passive warning, no constructive advice is required to solve the issue.

3

The tone is positive and does not blame the user.

4

EFFICIENCY

EXPLANATION

SCORE

The system effectively informs the user that the shipping method for all items has changed.

4

All items are preserved if the user switches back to the previous shipping option.

4

The warning does not require the user to interact with it or to take any additional action. It can just be consumed and disregarded if it is irrelevant to the user.

4

The warning is sufficient for the user to understand that they can only choose one shipping method for all items in their cart.

4

J.Crew – Average Score

3.67

Overall assessment:This message is a warning — it does not block the user's workflow but may contain important information to reduce user confusion or misunderstandings (in this case, about how J.Crew ships products). It is clearly styled as a warning rather than an error by avoiding the color red, yet it is still prominent enough to catch visual attention.

Although a strong performer overall in each guideline dimension, this message contains a surprising issue — a typo in the phraseAll item in your bag.

Potential improvements:

For those determined UX professionals working inlow UX-maturity environments, identifying UX problems can be hazardous work — they may raise the ire of their colleagues or be accused of basing their analysis on personal opinion. Whileusability testingis the best remedy for such criticism, there are other tactics to leverage. Use this error-message scoring rubric (or similar standards) to demonstrate a systematic and consistent rationale for your analysis. Take inspiration from the error-message guidelines when reporting error-message UX problems: make your analysis highly visible, communicate it constructively, and show how enhancements can improve user and business efficiency.

Foundational concepts that everyone should know

Interaction

Components, design patterns, workflows, and ways of interacting with complex data

Interaction