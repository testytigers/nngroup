# User Control and Freedom (Usability Heuristic #3)

**Author:** Maria RosalaMaria RosalaNovember 29, 20202020-11-29

**Topics:** Heuristic Evaluation

**Source:** https://www.nngroup.com/articles/user-control-and-freedom/

---

November 29, 20202020-11-29

Share

Jakob Nielsen’s thirdusability heuristicfor user interface design isuser control and freedom. This principle states:

Users often choose system functions by mistake and will need a clearly marked “emergency exit” to leave the unwanted state without having to go through an extended dialogue. Support undo and redo.

Part of a great user experience is nurturing users’ feeling of control over the user interface (UI) they happen to be using.Users should be able to quickly correct mistakes or backtrack on choices made. The ability to easily get out of trouble encourages exploration, which facilitates learning and discovery of features. It also increases overall use and sales (in the case of exploring a product space). Conversely, when the UI doesn’t support these actions, users feel trapped and typically report dissatisfaction.

There are several UI controls that typically allow people togo back to the previous state of the system:

Whenever users click a link to open a new page, screen or view, they should always be able to go back to where they came from. On the web, users rely on the browser’sBackbutton to navigate to the previous page in usability testing, we often see some users defaulting to the browser’sBackbutton when navigating a website, rather than using the website’s own navigation (such as breadcrumbs). This is one of the reasons why we recommendnot to open links in new tabs indiscriminatelybecause some users don’t notice they are in a new tab and struggle to go back.

Never stop users from leaving your site by disabling the browserBackbutton.Some sites deliberately make their site sticky, preventing users from returning to the search engine. While users will stick around on your site for a few seconds longer if you use this tactic (because they can’t leave), you’ll quickly frustrate them — and good luck getting them to do business with you! This design choice is often the result of prioritizingvanity metricsover tangible UX goals. Instead of trapping users by disabling theBackbutton, sites should offer users valuable content to make them want to stay.

Nonfunctioning browserBackbuttons can also be found on some online forms, because moving backward could break the underlying logic. In some cases, users can use the browserBackbutton but instead of returning to the previous screen, they receive a timeout message and lose their work. Where possible,build forms where userscanuse the browser'sBackbutton. If the design makes this impossible, warn users when they click the browser’sBackbutton and provide them with a chance to cancel this action. Designers should also explore creating aBacklink or a clickable progress bar that help users move back through the form without losing work.

When presented with anoverlay or lightbox, users often get disoriented and think they are on a new page — especially where overlays take up the whole screen. Therefore, to return to the previous screen, users often use the browser’sBackbutton instead of tapping aCloselink orXicon. This action has the effect of taking the user back two steps, rather than one, causing confusion and disorientation.

In a recent mobile usability-testing session, a participant used the browser’sBackbutton on a full-screen overlay and was taken out of the overlayandout of the page he intended to return to. The participant commented, “I don't expect to be taken out of that page (…) If I click Back, it brings me out of the page I was on. It doesn't bring me back to the page that I popped out from.”

When it’s possible that users mistake the overlay for a new screen — whether on desktop or mobile —ensure theBackbutton has the same effect as aCloselink.

In mobile apps, users tend to transfer their knowledge of theBackbutton from their experience with the web and have the same expectation for it: that is a way to move back a step (from whichever direction the user came). Unfortunately, often designers mean it as a way of moving up in the application’s IA. As a result, users can easily get disoriented. In the example below, a user can swipe right to left to read another news story in BBC News’ app (the order corresponds to the way they’re listed vertically on the news listing page). However, users can’t use theBackbutton to return to a story they visited by swiping; using theBackbutton returns users one step up in the IA to the article-listings page, rather than to the previous article they visited.

Like in a physical space,exits should be easy to find and well signpostedso that they will be discovered when needed.

Followdesign standardswhen positioningClose,ExitorCancelsigns, so that users can easily find them where they typically expect them. For example, on a lightbox overlay, users typically expect an ‘X’ icon in the top right corner of the overlay.

In addition to placingExitsigns in expected places, useuniversal iconsso users understand what the link does.Accompany icons with text labelsor substitute icons with plain text. For example, useBackinstead of < andCloseinstead ofX.

Whether a user is beginning a purchase, a transfer of money, or a large download, she should be able to cancel that task at any point. TheCanceloption should be easy to find and quick to execute. Even though in multistep processes users could make use ofBacklinks in the place ofCancel, it’s best to provide aCancellink to avoid unnecessary clicks.

On mobile, some designers try to save space by using theXicon, instead ofCancel. Unfortunately, sometimesXcan be mistaken forClose, rather thanCancel. In some interfaces, it’s important to distinguish the difference between the two to avoid user error. IfXmeansCloseandcancel, then use an explicit text label (Cancel)or provide the user with a warning dialogue to avoid losing users’ work.

When a user makes a change to the status of a system, he should be able to easily undo that. Imagine accidentally deleting a whole paragraph of text and not being able to get it back!

Undocan be supported in many ways on an interface, not just through a simpleUndobutton. For example, if users add an item mistakenly to a shopping basket, they should be able to undo that change by removing the item.

If users are likely to make many actions in short succession, support multipleUndoandRedo. Undoing the last action is often not enough. For desktop users, it’s also a good idea to supportstandard keyboard shortcuts for power users.

Remember theshake-to-undo feature in iOS? This feature is notoriously underused because it is so hard to discover.

For desktop designs, don’t assume your users will know that they can use a keyboard shortcut. It’s a good idea to give users a visible option to undo an action on the UI. This feature should be where users typically expect it. In WYSIWYG (What-You-See-Is-What-You-Get) applications like word processors and design software,Undois usually in the toolbar or in the app’s menus. On web-based applications with nochrome, anUndooption is often contextual — it may appear in a transient snackbar or in acontextual menu.

If anUndooption is contextual, ensure it has good visibility in the UI. On Google Drive, when a user makes a change to a file, a snackbar appears in the bottom left corner of the window to confirm the change has been made and to provide an option to undo. Unfortunately, the message only appears for a few seconds. Users would need to know they want to undo and act quickly in order to make use of this feature. (It’s also possible to use keyboard shortcuts, but these are not listed in the UI.)

To ensure users have a sense of freedom and control using your product, they should be able to easily abandon a task, go back a step, and undo a change they’ve made to the system’s state. By thinking about carefully crafting clear exit points andUndofeatures, you can leave users feeling in control of the experience, rather than at the mercy of your design.

Enhance your judgment and resolve tough design challenges

Management

Foundational concepts that everyone should know

Interaction