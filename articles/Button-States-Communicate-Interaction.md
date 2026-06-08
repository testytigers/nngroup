# Button States: Communicate Interaction

**Author:** Kelley GordonKelley GordonApril 25, 20252025-04-25

**Topics:** Interaction Design, Visual Design, Design Patterns, Accessibility, Web Usability

**Source:** https://www.nngroup.com/articles/button-states-communicate-interaction/

---

April 25, 20252025-04-25

Share

Buttonsare coreuser-interface elementsthat, when clicked or tapped, execute an action. When designed correctly, buttons set accurate user expectations and help them understand how to interact with the interface. In addition to clear button labels, effective signaling of button states is critical for a good design.

You’ve probably experienced that annoying situation when you try to click on a button, but nothing happens. How do you know when you can click on a button versus when you can’t? Designers usually communicate that type of information through subtle visual cues that indicate to users the state of the button: whether it’s clickable or not, whether it has been pressed, whether it has been hovered on.

The most commonly used button states are:

Theenabledstate, also sometimes called the default state,indicates that the button can be pressed or otherwise interacted with.When a button is in this state, it’s available to be clicked or tapped, and will perform its intended action.

When a button is available and active, we usually want it to catch users’ attention — especially if it’s a primary or call-to-action button.

Typical styles forenabledbuttons have the following visual characteristics:

Learn how to build interfaces that users understand and enjoy engaging with in Interaction Design.

Opposite of theenabledstate is thedisabledstate. This stateindicates that the button's action is unavailable— the button can't currently be clicked or tapped.In thedisabledstate, the button's appearance doesn't change when users try to interact with it.

For example, if a user has not filled in all required fields in aform, the form’sSubmitbutton may not be active.

Typical styles fordisabledbuttonshave the following visual characteristics:

Labels fordisabledstates don’t need to be as high-contrast as those forenabledstates, but you still want people to be able to read them. On the other hand, you don’t want the contrast to be as high as to trick people into thinking the button is clickable. If you are designing button states, it’s a good idea to test them with real users to make sure they are usable and visually distinct.

Disabledbutton states should also have theARIA-disabled: trueattribute added to the code. This attribute will allow the button to still receive tab focus but will indicate to screen readers that the button is inactive, thus announcing to users itsdisabledstate.

Thehoverstate is triggered when a user moves their mouse cursor over a button or other design element and is meant toindicate that the button is clickable.(This state will obviously not be visibleto users who do not use a mouse — for example, mobile users.) To prevent the color change from happening when users don’t mean to hover over a button (for example, because they are moving their mouse across the screen) a slight delay (around 150–200ms) should be added to this state.

Typicalhoverstateshave the following visual characteristics:

Thefocus(orkeyboard-focus) statehelps people know which active button has the keyboard focus.When a user uses theTabkey to move across various active elements on a page, the focus state indicates which element is currently selected (and could be activated by using theEnterkey). The focus state should appear pretty quickly (around 100-150ms) after the user uses the keyboard. Otherwise, the user may end up tabbing on the keyboard again and may miss the desired button.

By default, afocusstate is signaled by a blue outline around the element. However, you can easily customize how the focus element looks like, to fit your visual-design needs or brand standards.

That being said, I strongly recommend that you stick to the stroke or outline to indicate focus, as opposed to relying on color change alone, for two reasons. First, this indicator is the default signal and many users expect it. Second, color change alone may not be perceived by some people with vision impairments.

Thepressedstate indicates that the user has tapped or clicked a button. It is meant to give the user feedback that the action they performed was registered by the system and usually appears as a very slight color change or a very short and minimal animation. Thepressedstate should appear within 100–150ms for the user to register that the pressing action is instantaneous. If this feedback is not timely, users will press the button multiple times and potentially cause issues.

In addition to these 5 core button states—enabled, disabled, hover, focus, andpressed—there are a few more fundamental states to include in a design system.

This button state lets users know that the action corresponding to that button is being performed.It is used for actions that tend to take a longer amount of time to complete (for example, because they require some backend verification or the loading of a larger document).

Theloadingstate typically uses the enabled state and adds a loading spinner or indicator to the left of the button label. Once loading is complete and the action is performed, oftentimes, you will see the spinner animate to a check icon to visually show that the action was successful.

Theselectedstate is associated with checkboxes or radio buttons, and it indicates that the user selected that option. Note that this state isnota button state, but we include it here because sometimes it is confused with the buttonpressedstate.

A button style refers to how the button is visually represented in the interfaces and how much visual emphasis it gets. In an interface, it’s typical to distinguish among three (or more) different button styles: primary, secondary, and tertiary, depending on the button’s importance in the UI. The same button can be in different states at different times, depending on the user’s actions or the system’s state. But one button will have only one style.

Primary buttons have the most visual emphasis to grab user attention and direct them to an important or common action such ascompose,create,save, andcheckout. Primary buttons are typically solid, filled buttons.

Secondary buttons have a medium visual emphasis and are meant for actions that are less important or commonly used. These are actions likecancelandreply. Secondary styles are typically outline buttons.

Tertiary buttons have the least amount of visual emphasis and are dedicated to optional or supplementary actions (e.g.,viewmore).

While button states are crucial to designing good, usable buttons, another equally important aspect of a button is its label.Labels should clearly describe what the button will do, while being substantial and succinct enough to stand alone.Avoid generic labels such asContinueorNext.These small bits of UX copy massively contribute to the findability and accessibility of your site’s functionality.

Design how users connect, navigate, and engage with your interfaces

Interaction

Strategically combine content, visuals, and interactive components to design successful web pages

Interaction

Organize and structure information to improve findability and discoverability

Interaction