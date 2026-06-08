# Checkboxes: Design Guidelines

**Author:** Maddie BrownMaddie BrownJune 28, 20242024-06-28

**Topics:** Design Patterns

**Source:** https://www.nngroup.com/articles/checkboxes-design-guidelines/

---

June 28, 20242024-06-28

Share

There are ample options for different kinds of fields when designing digital forms. Each serves a specific purpose, from radio buttons to dropdowns to open text fields. But if you want to offer users the flexibility of selecting one, multiple, or no items from a list,checkboxesare your friend.

Acheckboxis a UI element that allows users to select between two states: checked and unchecked. When appearing in nested checkbox lists, a checkbox could also display a third, so-called “indeterminate” state, indicating that some but not all children of that checkbox were selected.

There are three distinct checkbox applications, and each functions slightly differently.

This type of checkbox appears by itself. There are no other checkboxes around it, and it is frequently cordoned off in its own visually distinctive container. The checkbox and its label, in this case, demand attention and consideration on their own.

Standalone checkboxes are often used when a user must agree to an app’s terms and conditions. In this case, the checkbox field is typicallyindicated as required with a text label or red asterisk. The user is unable to move on without selecting their agreement.

Another common application is opting into email or SMS notifications in a checkout flow.

This is the most common application of checkboxes.In a checkbox list, each checkbox functions independently.The selection or deselection of a checkbox does not affect the selection status of others in the list. A checkbox list allows users the unique ability to select one, several, all, or no items from a list.

A checkbox list is useful when you want to allow users to select any number of items from a list, and you do not have reason to believeSelect Allwill be a common selection.

Selecting ingredients in a food-ordering app or parameters in a faceted-search functionality are common applications of a checkbox list.

Nested checkboxes use a parent checkbox followed by a sublist of indented child checkboxes. This layout affords additional functionality beyond the previous applications because:

Nested checkboxes are useful when you expect many users to select all the checkboxes in a list.

For example, in an airline check-in flow, the app might ask the user to “Select which passengers you’d like to check in.” In this case, a parent checkbox might be labeled “All passengers,” with child checkboxes for each individual passenger. The most common use case would be a person checking in their entire party, so using nested checkboxes aids the user experience.

In digital-form design, several elements allow for selecting particular items from a list. It is important to know which one is right for your needs.

Checkboxes differ from, but are often confused with,radio buttons. Amongst a list of radio buttons, only one button may be selected at a time. In order words, the selection of a nonselected radio button will, in turn, deselect any other previously selected option.

Example Uses

Available Items

Available selections

Selection functionality

Checkbox List

Selecting which pizza toppings you’d like

Multiple

0 – all

Independent of each other

Standalone Checkbox

Agreeing to a privacy policy

2 (selected/unselected)

1

Mutually exclusive

Nested Checkboxes

Selecting passengers to check into a flight

Multiple

0 – all

Parent selection is dependent on child selections

Radio Buttons

Selecting which pizza crust type you’d like

Few options

1

Mutually exclusive

Dropdowns

Selecting your title (e.g., Mr., Mrs., Ms., Miss, Mx)

Multiple

1

Mutually exclusive

Toggle Switches

Turning dark mode on and off

2 (on / off)

1

Mutually exclusive

Users expect checkboxes to look like checkboxes:squares (with or without rounded corners), with a checkmark to communicate selection.Designers should adhere to these conventions.

Never use circles as checkboxes. These are easily confused with radio buttons and should be avoided.

Don’t force users to click or tap on a too-small box to make their selection. Include a perimeter around the checkbox and make the label clickable to allow for adequate touch-target size (at least 1 cm x 1 cm).

Ensure that all your label statements are worded positively. Negatively worded statements force users to contemplate double negatives, leading to errors.

In the bad example below, when the itemDo not send me marketing updatesis unchecked, it essentially translates toDon’tdo not send me marketing updates— in other words,send me marketing updates.

Present your list of checkbox items in a logical order to aid scannability and comprehension. Consider using subheads to break up a long list of checkboxes if possible.

While many people understand that checkboxes allow for the selection of multiple items, confusion persists. Consider your use case and target audience, and whether including the phraseSelect all that applywould be valuable.

Do users need to select at least one item from the list? Or to select no more than 3?

Clearly state any requirements in the instructions and providereal-time visual feedbackwhen the requirements have been satisfied or violated.

Some designers display checkbox items horizontally to save vertical space on the page. This approach decreases scannability and sometimes makes it difficult to align the labels with the appropriate checkbox. Display your list vertically.

When presenting a checkbox for users to opt into various promotions, such as receiving marketing emails, many designers preset the default state of the checkbox to selected, forcing the user to take the action of unselecting the box to opt-out.

This is adeceptive patternand should be avoided.

Similarly, when displaying checkboxes indicating agreement with legal statements such as terms and conditions, always set the checkbox's default state to unselected.

Offering users the ability to select a checkbox requires a crystal-clear understanding of the selected and unselected states. If these states are not intuitive to the user, consider using alternative UI elements such as radio buttons or dropdowns.

Essential UX design principles for small-screen websites and apps

Interaction

Create and evaluate applications for advanced decision making, complicated workflows, and complex domains

Interaction

Components, design patterns, workflows, and ways of interacting with complex data

Interaction