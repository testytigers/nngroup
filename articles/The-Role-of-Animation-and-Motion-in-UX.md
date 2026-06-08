# The Role of Animation and Motion in UX

**Author:** Page LaubheimerPage LaubheimerJanuary 12, 20202020-01-12

**Topics:** Design Patterns

**Source:** https://www.nngroup.com/articles/animation-purpose-ux/

---

January 12, 20202020-01-12

Share

In UX, motion and animation can be helpful and communicative, if used with restraint. Motion is most often appropriate as a form ofsubtlefeedbackformicrointeractions, rather than to induce delight or entertain users. In this article, we explore the purposes of useful, unobtrusive feedback animation. In a second (forthcoming) article, we will discuss the details in timing and movement to make these animations appear smooth and natural.

The big advantage (and also drawback) of UI motion is that itattracts user attention. Our peripheral vision (specifically, through the rod-shaped photoreceptors in the human retina) is responsible for detecting motion.  Evolutionarily, the fact that we can detect a movement outside the center of our field of vision is, of course, an advantage: we can discern danger and protect ourselves. But that means that we are sensitive and prone to bedistractedby any type of motion (meaningful or not). That’s why motion in user interfaces can easily become annoying: it’s hard to stop attending to it, and, if irrelevant to the task at hand, it can substantially degrade the user experience (as any web user who has encountered a movingadvertisementcan attest).

Although animationscanbe useful and can builduser expectations about the UI, they should be used with a light touch — primarily as a tool for providing users with easily noticeable, smooth feedback.

When animation is used in a subtle way, it can help users build mental models about how the system works and how they can interact with it.  Animations are less critical for user experience when they are simply time-filling visual stimulations during moments of transition (in fact, it’s these down-time animations that often frustrate participants in usability testing).  Instead of using animations to providesurface-level delight(that quickly sours), animations can be leveraged for usability: as clues about what is currently happening with the system, as signifiers for how UI elements will behave, and as easily understandable spatial metaphors for the user’s location in the information space.

Animations are often helpful as a form of noticeable feedback that an action has been recognized by the system.  A ubiquitous example is the animation of a navigation menu sliding over the page when ahamburgericon is tapped.  Because our visual systems are so attuned to motion, a short animation can ensure that users see the feedback.

Sometimes, static visual feedback is ignored due to change blindness. For example, people may not notice the shopping-cart–badge update after clicking theAdd to cartbutton in the Cuisinart example below. An animation increases the chance of noticing that feedback. (Another alternative would be to make the static feedback more prominent — e.g., through a dialog box or using a bigger badge. Both solutions would likely be more intrusive than a simple animation.)

And animations can also be used as a form of feedbackbeforethe user commits to an action, such as previewing the new location of an item when using drag-and-drop to reorder a list.

Motion can be used to indicate that the interface switched to a different state — for example, because of a mode change.Modesare often a difficult concept to communicate to users, but animation can help in two ways: (1) by making the mode change noticeable; and (2) by providing a conceptual metaphor of the mode transition. For example, morphing a pencil icon into a disk after it was clicked on signals the transition fromEdittoSavemode more clearly than swapping one icon out for the other instantly.

Material Design: A pencil icon that transforms into a + icon helps to communicate the difference between theEditmode and theAdd newmode.

In addition to showing a transition between modes or views of data, animations are also helpful for communicating state changes that are not triggered by users’ actions. For example, loading indicators show that the system is not yet ready to accept input.  One form of this is a “skeleton screen” (a placeholder UI that looks like a wireframe of the loading page, with no content) that is animated by a light glare moving across it.

Hipmunk: While loading flight-search results, Hipmunk offers several animated cues. First, there is an animated chipmunk pretending to fly. (While cute, the chipmunk is not essential for feedback, but is helpful to establish thebrand tone.) However, at the same time, other, more-communicative animations occur: the number of flight results climbs steadily from 0 to 754, indicating that the system is performing multiple federated searches concurrently. Also, a placeholder shows where content will appear as flight results load.  Aprogress bar, along with two animated ellipses, indicates that results are still loading.  Finally, as new results are loaded and the relevance order changes, a subtle animation shows new results appearing within the list and is meant to communicate that the order of the search results is changing dynamically.  However, the number of simultaneous animations is overwhelming: the power of any of these animations to pull the user’s attention is diminished by competition from all the others.

The structure of a complex information space is often challenging to communicate to users without taxing their cognitive resources or taking up too much screen space. Scanning through navigation menus, tree diagrams, or evenbreadcrumbsto figure out where one is in the information hierarchy is a complex type of cognitive work. While animation alone is not a suitable substitute for visible navigation with clear, unbranded labels, it can signal to users the direction in which they are moving within a process or hierarchy; thissupplementalcuecan make navigation through a complex IA more intuitive and understandable.

Zooming animations can help users understand the direction of their journey into a hierarchical information space without looking at a tree diagram. Zooming out shows less detail, but more objects, thus suggesting that the user travels up into the hierarchy, whereas zooming in shows more detail, but fewer objects, creating the impression of going deeper into the hierarchy.

iOS Photos uses a zoom metaphor to show the user’s location in the information space (in this case, represented by my endless library of photos of my dog, Daphne). Going betweenYears, Months, andDayshas a subtle zoom-in or zoom-out animation that helps users understand whether they are going up or down in the hierarchy of photos. This approach helps keep the user’s attention on content (cute dog photos), and not on the navigationchrome.

Likewise, a slide-over animation helps to establish that a user is moving forward or backward within a process such as checkout.

Amtrak shows a subtle slide-over animation to indicate that the user is moving forward through the process of booking a train.

Animations can also prevent disorientation and telling people if they are on the same page or have moved on — particularly on mobile, where context can be lost due to the small screen size.Accordions,anchor links, and menu overlays can be disorienting or confusing if the change appears instantaneously; since a menu overlay fills the entire screen, the relationship between the overlay and the underlying page (e.g., “is this content a new page, or is it something else?”) is hard to understand without an animated cue. (Why does it matter if users know where they are? If they think they are on a new page, they are often tempted to use theBackbutton to navigate to the previous view; unfortunately, in the case of overlays or accordions, that action will take them away from the page instead of simply closing the element.)

WebMD: When opening an accordion on the page, the associated content immediately shows up at the top of the screen (with no animation). The user may think that the new content is on a brand new page. A scrolling animation (showing how the page is moved so that the accordion is at the top of the screen), followed by a moving expansion could help the user to understand that this is not a completely new page, but an accordion within the page’s content.

MetMuseum:Anchor linksare often confusing or disorienting for users, but in this case, the anchor links use a smooth scrolling animation to show (1) that the content is all contained on a single page and  (2) where it is on that page.

Animations help users understand how to interact with UI elements. The direction (or other attributes) of the motion signifies the type of acceptable actions. For example, acardthat expands from the bottom of the screen towards the top signals to the user that it can be closed by pulling down. A new card that comes from the right of the screen signals that it can be closed by swiping it to the right.

Car2Go for iPhone: A short bounce animation is a signifier thatswipingacross the list item reveals options.

Because the human visual system is very sensitive to motion (particularly, to motion that appears to haveanimacy), animation can be used to grab users’ attention, for better or worse. On the one hand, it can make a subtle signifier obvious, but on the other hand, gratuitous animations distract and annoy the user. Further, using animation to hijack the users’ attention or create afear of lossis adark pattern: an unethical application of user-experience principles and cognitive psychology to get users to do something they ordinarily wouldn’t.

Benign: Refinery29 embeds a poll in the middle of a story about social media’s mental health effects and shows a radiating halo on the slider’s knob to reinforce the signifier and catch the user’s attention. This limited use of animation is a relatively benign (though mostly unhelpful) way of catching the user’s attention. Were animations widespread throughout the site, this animation would be a distracting usability problem.

Dark pattern: A flashing countdown clock on warmlydecor.com indicates that a sale is about to end (by a puzzling coincidence, in just under an hour for every single product on the site, no matter when you visit). The clock activates the powerful loss-aversion instinct in users, and the flashing (with a subtle enlarging of the digits as they flash) is very difficult to avoid attending to.

In summary, when UI animations are subtle, unobtrusive, and brief, they can improve the user experience and can communicate feedback and state changes, prevent disorientation, and strengthen signifiers. But they should not be overused, as they can easily become overwhelming and distract users.

Head, V. (2016)Designing Interface Animation. Rosenfeld Media.

Saffer, D. (2014).Microinteractions.O’Reilly Media.

Pratt, J., Radulescu, P., Guo, R.M., & Abrams, R.A. (2010).It's Alive! Animate motion captures visual attention.Psychological Science, 21, 1724–1730