# Bottom Sheets: Definition and UX Guidelines

**Author:** Page LaubheimerPage LaubheimerJune 11, 20232023-06-11

**Topics:** Design Patterns, Mobile & Tablet

**Source:** https://www.nngroup.com/articles/bottom-sheet/

---

June 11, 20232023-06-11

Share

Making contextual controls noticeable and easily accessible on mobile devices is a challenge. Small screens necessitate that we hide some information or controls until they are relevant. Bottom sheets are a type of partialoverlaythat is especially suited for mobile devices and that makes temporarily important information readily available but also dismissible.

Bottom sheet:An overlay that is anchored to the bottom edge of a mobile device’s screen and that displays additional details or actions.

Bottom sheets are a form ofprogressive disclosure–- they are typically invoked by a user interaction and provide extra details. Since they intentionally obscure some of the screen, they aren’t suited for displaying always needed information or tools.

Rather, they are used to present extrainformation,contextualcontrols, or both. The advantage of a bottom sheet is that, unlike a separate page (which requiresspatial reorientationfor users and may also force them to hold information in theirworking memory), it preserves some of the user’s current context.

Bottom sheets share a lot of similarities with dialogs and overlays (not surprisingly, since they are a type of overlay). What’s special, however, of bottom sheets compared with other overlays is that they preserve substantial visibility of the underlying information. Thus, bottom sheets are especially usefulwhen users are likely to need to refer to the main, background informationwhile interacting with the information or options presented in the sheet.

A common (but largely incorrect) rationale for using bottom sheets is that they improve reachability for users on mobile devices (i.e., it is often suggested that it is easier to tap items at the bottom of the screen). This is unfortunately not universally true — asusers hold mobile devices in a variety of ways(one-handed, two-handed, and from a variety of different grip points), the bottom of the screen is often not the most easily reachable screen region (the middle of the screen represents the most easily tappable area for the wide variety of ways users hold mobile devices).

Bottom sheets can bemodalornonmodal.

The modal variety works similarly to classicmodalpopups –- they force users to interact with them (or dismiss them) before they can take any other actions. A modal bottom sheet blocks any interactions with the background content while it is visible. A translucent dark scrim is usually placed over the locked-out background content as a signal that it is currently unavailable.

Nonmodal bottom sheets don’t require an interaction –– they sit at the bottom of the screen, and allow the user to interact with the background content. They are appropriate for presenting detailed information or options in parallel with the main information on the screen.

Some bottom sheets are expandable. Users can tap or swipe the bottom sheet up to expand it into a full-screen (or sometimes near full-screen) modal. Typically, bottom sheets start off as nonmodal in their minimized state but become modal when expanded.

In our studies, we observe users having similar struggles with bottom sheets as they do with otheroverlays; these are usually caused by:

Our guidelines below are meant to address these issues.

One problem with bottom sheets, especially when they are expanded to full screen, is that they look like regular pages. As a result, some users may not realize they are in a bottom sheet and might expect to use normal navigation elements (such as the phone’sBackbutton or theBackgesture) to move away from that screen. Unfortunately, this mechanism is not supported by all bottom sheets.

Thus, if, along the user’s journey, a page spawns a bottom sheet or an overlay, this page will break the normal interaction pattern. Moving away from it may or may not be accessible through theBackbutton, and therefore the sheet may cause disorientation. You can prevent this issue by supporting the use ofBackfor dismissing the bottom sheet, thus allowing the users to seamlessly return to the previous view.

Even though most bottom sheets can be dismissed by swiping down (or tapping) on the top grab handle, that element is easy to ignore. Moreover, some users are not aware of this functionality. Plus, the vertical swipe is also prone to swipe ambiguity: depending on where precisely it is initiated, the gesture may close the bottom sheet, may open up the notification drawer, or may display the phone’s control panel.

To make sure that users will be able to reliably dismiss the bottom sheet, include a visible aClose (orX) button on the screen. We recommend providing a clearClosebutton (usually styled as an X or the wordClose) at the top of bottom sheets rather than relying exclusively on the grab handle. An additional advantage of this button is that it facilitatesscreen-readerand keyboard access for users that cannot see or swipe on the screen.

One of the biggest issues with bottom sheets occurs when an app stacks several such sheets on top of each other.

We havepreviously discussed some of the issueswith stacked bottom sheets. Inevitably, users will have to keep track of where they currently are in the rapidly multiplying stack of overlays and will need to be able to discriminate between dismissing the last sheet on the stack and dismissing the whole stack, as in the example below.

We strongly recommendnotusing a bottom sheet to replace typical page-to-page user flows.A bottom sheet is a transient UI element that is not intended to be a stable place for users to return to, or spend significant time on. They are intended for interruptions or a fork in the road, rather than the expected “happy path” the user will usually take. For example, don’t use a sheet to display an ecommerce product-detail page: the user may navigate to related products, reviews, or detailed specifications from that sheet, and a bottom sheet will break longstanding conventions of how users can navigate from page to page.

Finally, we don’t recommend using a bottom sheet when users will likely spend significant time reviewing the information (or options) displayed inside it. A sheet is inherently a transient UI element — it is meant to support quick interactions, and it should not be used for displaying complex content.

Bottom sheets are a mobile-app UI pattern intended to present temporary contextual information while maintaining access to the main content. When used for a few options or some additional information, a bottom sheet can enable quick access to controls; however, they should not be used on top of other bottom sheets or for displaying lengthy content.