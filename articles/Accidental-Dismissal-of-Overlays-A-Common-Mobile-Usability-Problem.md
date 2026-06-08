# Accidental Dismissal of Overlays: A Common Mobile Usability Problem

**Author:** Raluca Budiu, Sana Behnam, Kate MoranRaluca Budiu,Sana BehnamandKate MoranSeptember 18, 20222022-09-18

**Topics:** Mobile & Tablet, Design Patterns

**Source:** https://www.nngroup.com/articles/accidental-overlay-dismissal/

---

September 18, 20222022-09-18

Share

Overlayshave becomea ubiquitous UI elementon mobile: beyond the annoyingpopupsfor cookie permissions,chat bubbles, coupons offerings, and marketing-subscription offers, you will also find them used fornavigation menus, bottom sheets, product-detail pages, or in-app browsers.

While many mobile overlays take up only a section of the page (partial overlays), allowing some content to be visible in the background, others occupy the full screen and arepractically indistinguishable from a regular page or view.

Depending on whether the user can interact with the background (that is, with the content beneath the overlay), overlays can bemodal or nonmodal. Inmodal overlays, users cannot interact with the background, while innonmodal overlays, they can do so.

One of the major problems with mobile overlays is thatdismissing them can be done through one of the following overlay-dismissal methods:

Because designers vary in which of these overlay-dismissal methods they’ll allow, users sometimes will pick the wrong method, with unexpected and costly consequences. Things are even more complicated when several overlays are stacked on top of each other — in those cases, an overlay-dismissal method may dismiss only the top overlay or the entire stack, with no easy way for users to predict which behavior they’ll get.

Let’s start with an example. In a recent usability study, we had 8 participants interact with a variety of mobile sites and applications that used overlays.  One of our study participants used Walmart’s mobile app to shop for a light fixture. When the participant selected a product from the product-listing page, the product description was shown in an overlay.

In that overlay, he further tapped onCustomer reviews, which displayed another overlay on top of the first one. To go back to the product description, the participant tapped theCloseicon at the top. Unfortunately, that action dismissed the stack of overlays, and the participant was taken back to the list of products, losing his selection. Through no fault of his own, the participant had picked the wrong overlay-dismissal method. In order to navigate back, he was supposed to use either the on-screenBackbutton or the horizontal swipe gesture.

This example illustrates several of the major problems commonly associated with overlays, which are:

The participant in the Walmart example could have used any of the overlay-dismissal methods to get out of theCustomer reviewsoverlay and back to the product-detail overlay: swiping down, swiping horizontally on the left edge of the screen, tapping out, or pressing one of two on-screen buttons: close(x)icon or theBackarrow. He had no way to predict which one would get him his desired result. He guessed the close(x)button, but (unbeknownst to him) the designers had chosen theBackarrow or the horizontalBackswipe for that functionality.

Another common scenario where users may use the wrong method is when overlays look like full pages. In that case, users may use the browser or phone’sBackbutton, or the horizontal swipe gesture to go back to the previous view. But, because the overlay is not technically a separate page and because theBackbutton (at least in its standard implementation) takes people back to the previouspage(and not to the previousview), the result is that users are thrown back farther than they expected. This outcome contributes to a sense disorientation and a lack of control.

That was what happened with another one of our study participants, who was using the LinkedIn app to look for jobs. She searched for GSK, a company that she was familiar with, and went to the company’s webpage within LinkedIn’s in-app browser. On that page, she opened the main navigation menu and selectedCareers.She then went on to explore a subcategory (Experienced professionals),but because it was unsatisfactory, she decided to go back up in the menu. However, instead of using the menu’s<Careersbutton (as designers wanted her to), she used her Android phone’sBackbutton. That gesture closed the in-app browser and took the user all the way back to the company’s LinkedIn page, dismissing the menu in the process and making the user lose all her hard work.

In both the Walmart and the LinkedIn/GSK example, the “correct” button from the designers’ perspective (the on-screenBackbutton) was visible on the screen, but it had competition from two other buttons commonly used for navigating away from a view (theXicon, in the case of the Walmart user, and the phone’sBackbutton for the LinkedIn user).

It’s even more confusing when there are multiple buttons on a page that are labeled in the same way, yet do different things. For example, one Instagram user opened Lowes’s website in an in-app browser shown in an overlay. He visited a product page, which used a different overlay to display available customizations for that product. Both the browser overlay and the product-customization overlay had anxicon that was intended to close the respective overlay. But the user, wanting to go back to the product page, accidentally picked the wrong one and was taken back to the Instagram view instead.

If you provide the user with multiple ways of navigating away from the current view (the swipe gesture, the phone’sBackbutton, an on-screenBackbutton, one or moreClosebuttons) and some of these methods have different effects,there is no guarantee that users will use the right method.When they accidentally choose the wrong method, they’ll be confused and annoyed.

A major reason why choosing the “wrong” overlay-dismissal method can be frustrating is that the mistake often results in lost work for users. When they accidentally move farther back in the process than they mean to, users have to start all over again — or give up. The participant in our Walmart example was taken out of his flow and had to start all over, finding the same product again. This same problem happened with our LinkedIn and Instagram users. Another situation where it’s easy for users to lose work is if they accidentally tap outside of a partial overlay, thus dismissing it. For example, on Overstock.com, if the user accidentally taps outside the modal overlay used for thesequential menu, all their selections of subcategories in that menu will be lost.

A big part of the problems encountered by our Walmart and Instagram users was that there were several layers of overlays on top of each other. The users did not keep track of the many layers and accidentally dismissed the whole stack instead of just the last layer. This is a very frequent occurrence. It tends to happen often when in-app browsers function as overlays but can occur in other situations as well.

For example, another one of our participants used Google Maps to look for local restaurants. The list of restaurants was displayed in a bottom-sheet overlay on top of a map. That bottom sheet could be expanded to take up the whole page. However, when the participant selected one restaurant, its detail page was shown in yet another overlay on top of the first one. To go back to the list of restaurants, the participant used the swipe-down gesture (normally used to close a bottom sheet). But that resulted in closing all the sheets in the stack and taking the user back to the map view of the restaurants, which he did not recognize.

The easiest way to avoid overlay issues is to simply avoid using overlays where possible. Some content is best presented in an overlay, especially when you need to present information in-context. Google Maps’ listing page is a good example of a necessary overlay — the map needed to stay in-view as the user browsed restaurants. But in other cases, overlays are very much unnecessary — for example, Walmart’s product details could easily be in separate pages (as in the Revolve app below) and customer reviews could be either shown on a separate page (also like in the Revolve app) or collapsed in an expandable accordion (as in the Nordstrom app).

This is an especially good idea when the overlay contains only relatively little content that does not require scrolling. In general, if users realize that they are dealing with an overlay rather than a regular page, they will be less likely to try to use the browser’sBackbutton to go back.

However, if your partial overlay requires users to scroll, you may be forcing users to do more work than necessary by not taking advantage of the full screen space. You also make it more likely that they will lose their spot on the page if they accidentally close the overlay.

Even if you end up using the occasional overlay, stay away from overlays on top of overlays, since they increase the chance that the user will accidentally close the whole stack and lose their work.

Overlays that had a clearXbutton were less likely to be closed accidentally (provided that no otherClosebuttons were also shown on the screen). Consider including one of these buttons instead of assuming that users will use gestures like swipe down to close the overlay.

With bottom sheets, do not assume that users will know to swipe down in order to close the bottom sheet. Even though that gesture needs to be supported, you should also allow users to dismiss the overlay using a visibleXbutton.

The Built-InBackButton Should Close the Overlay

Instead of taking the risk that user will accidentally use their browser or phone’sBackbutton or the horizontal swipe gesture to close an overlay, support the use of the built-inBackfor dismissing the overlay.

Thus, you should allow users to use the browser or the phone’sBackbutton or gesture to act as undo and move back from the current view to the previous one.

Overlays are a popular design element on mobile, used for displaying both UI components (e.g., navigation menus) and content. Unfortunately, they can lead to some serious usability issues: they can be dismissed accidentally, thus causing users to lose work and have to retrace their steps in the interface. Stacks of overlays are particularly likely to be closed by mistake.

We recommend that designers stay away from overlays whenever possible and instead attempt to use a different design component (like an accordion or a full page). If overlays must be used, create clear signifiers that allow users to differentiate them from regular pages, display only limited content inside the overlay. For all overlays (including bottom sheets), support the following two methods for dismissing the overlay: a clearClosebutton and the built-in (phone’s or browser’s)Backbutton orBackgesture.

We thank Mayya Azarova, Megan Brown, and Lillian Yang for helping run the test sessions. We also thank Megan Brown for helping tag the qualitative data from the sessions.