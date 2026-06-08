# Listboxes vs. Dropdown Lists

**Author:** Anna KaleyAnna KaleyApril 12, 20202020-04-12

**Topics:** Application Design, Interaction Design, Web Usability

**Source:** https://www.nngroup.com/articles/listbox-dropdown/

---

April 12, 20202020-04-12

Share

Many UI controls allow users to select options; they includecheckboxes,radio buttons,toggle switches,steppers, listboxes, anddropdowns. In this article, I’ll define listboxes and dropdown lists, discuss when to use each element, and cases where either will suffice.

In their simplest form, a listbox contains three main parts: acontainer box, alist of items, and alabel. Users can click on the items enclosed in the container box to select one or many from the list. A listbox may scroll, depending on how many items it contains and the viewable area. Sometimes, listboxes include checkboxes to clearly imply that multiselect functionality is available. More complex listboxes allow users to resize the container box, reorder the list of items, and make selections by moving items from one listbox to another.

There are 4 variations of listboxes that can be classified according to selection type. Each of these listboxes can be scrollable or not.

Multiselect listbox:Users can select or deselect one or more items by holding down theShift,Command, orControlkey while clicking on items.

Multiselect listbox with checkboxes:This type of listbox includes checkboxes to make multiple selection more obvious.

Multiselect, dual listboxes:This type of listbox consists of two listboxes. The listbox on the left holds available options and the listbox on the right represents selected items. TheAddbutton moves an item from the available list to the selected list and theRemovebutton moves a selected option back to available list, to deselect it. Users can also move options up and down to reorder elements in the list.

In their simplest form, dropdown lists contain four main parts: acontainer box, adownward-facing arrow button, alist of items, and alabel. Users can click on the down-arrow to display a list of mutually-exclusive items from which they can select only one. Like listboxes, dropdowns may scroll depending on how many items they contain when expanded. With dropdown lists, the selected option or default value remains visible in the container box, while the other list items appear only after clicking on the down-arrow. Selecting an item or clicking outside of the dropdown list will close it.

Listboxes and dropdown lists make a form compact — especially when many options are available, and  presenting those options as a list of standalone radio buttons or checkboxes would take up an unnecessary amount of screen space. Using a listbox or a dropdown list can alsoreduce errorsby constraining the options to those in the list and ensuring that users enter data in the proper format.

Listboxes and dropdown lists are used for selection in both native applications and websites. They aren’t intended to execute commands or trigger the display of modal windows, dialog boxes, or dynamic controls. On ecommerce sites, listboxes are often used to house filters that cascade down the left side of a category page, while a dropdown list may house the values by which a user can sort the products.

For scrollable listboxes and dropdown lists, it’s important to consider their size as it relates to theSteering Law. The Steering Law predicts how long it will take a user to move a cursor or a finger through a bounded area known as a tunnel. The steering time depends on the length and the width of the tunnel, where shorter, wider tunnels are faster and easier for users to navigate through than longer, narrower tunnels. Thereby, limiting the number of items contained in scrollable listboxes and dropdowns, and ensuring they’re designed to be as wide and as short as possible will help users review and navigate with speed and ease. When dropdown lists grow too long and narrow, the user is more likely to accidentally move their cursor outside of the bounded area, which will close the dropdown and force them to start the selection process all over again.

Though relatively seldom used, listboxes carry advantages beyond supporting single selection, multiselection, and housing many options without taking up excessive screen space. Other advantages of listboxes include:

Lowinteraction cost:Listboxes don’t require users to click on anything to reveal the options inside before making a selection (but they may require users to scroll the list if there are too many items).

Increased item visibility:The ability to see multiple options at once can speed up decision making and increase selection accuracy.

Single and multicolumn views:because listboxes aren’t limited to a single column, more options can be made visible if the listbox width allows. However, horizontal scrolling should be avoided in multicolumn listboxes.

Overview and reordering:with multiselect, dual listboxes, users maintain some control over the order in which items are displayed and get a clear overview of the items selected, which is helpful when the listbox contains several options.

Here are some disadvantages of listboxes:

Screen space:Even though they’re compact, they do tend to take up more screen space than dropdown lists.

Unfamiliarity:Users may not know how to interact with listboxes right away — specifically, they may not know how to choose multiples if checkboxes are not included in multiselect listboxes. Holding down theControl,Command, orShiftkey to select and deselect multiple items is not something general web users do often. That’s why it’s important to include checkboxes in multiselect listboxes, unless they focus unwanted attention on multiselect functionality or add unnecessary screen clutter.

Users may not be able to see all of the selected options at once:If there are many more items available beyond what’s visible in the viewable area, users may lose the ability to see all selected items simultaneously. To avoid this drawback, show selected items above the listbox as tokens or highlight the selected items in a nonscrollable list.​

Dropdown lists are used more frequently than listboxes; they take up less screen space but can hold just as many items as listboxes. Other advantages of dropdown lists include:

The ability to give users an optimal option,selected by default.

Downplaying alternative options and changes:Because dropdown lists hide the other available options, they work well to downplay alternatives and underemphasize the ability to make changes. (This is advantageous in cases where the default will satisfy most users and where the alternative options may be dangerous or confusing to nonexpert users.)

Familiarity:Dropdown lists are familiar selection mechanisms for most users since they are widely used both on the web and in native apps.

A disadvantage of dropdown lists are that they require a click to reveal the options inside. Other disadvantages of dropdown lists include:

They’re subject to overstuffingand can be cumbersome to scroll through when they contain too many options.

They slow users downwhen they’re used to capture readily known values. For example, when entering a birthdate or credit-card expiration date, typing in a form field is usually faster and easier than interacting with dropdown lists.

Discreet:Because they are so compact, users may accidentally overlook dropdown lists in forms, web pages, and applications.

Easy to dismiss:Accidentally deviating the cursor from the box closes the dropdown and people have to start the selection process all over again.

Compared to using standalone checkboxes or radio buttons, it’s better to use a listbox or dropdown list when there are 5 or more items from which users can choose. Additional factors such as the amount of screen space available, whether the user can select one or many items, and if there’s a need to downplay or encourage changes all need to be considered when deciding between a listbox, a dropdown list, or another selection control. Use the criteria in the table below to help you decide which element to use or when either will suffice.

When including a listbox or dropdown list in your design, always display the options in a logical order. That may meangrouping related items together, placing the most commonly selected item first, or organizing the options in alphabetical order. Always place numbers and dates in sequential order.

Components, design patterns, workflows, and ways of interacting with complex data

Interaction

Use psychology to predict and explain how your customers think and act

Interaction

Strategically combine content, visuals, and interactive components to design successful web pages

Interaction