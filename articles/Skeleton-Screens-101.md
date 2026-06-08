# Skeleton Screens 101

**Author:** Samhita TankalaSamhita TankalaJune 4, 20232023-06-04

**Topics:** Design Patterns

**Source:** https://www.nngroup.com/articles/skeleton-screens/

---

June 4, 20232023-06-04

Share

A skeleton screen is a design pattern used to indicate that a page is loading while providing users with awireframe-like visual that mimics the layout of the page. This specific type ofprogress indicatoris used exclusively for full-page loads.

There are 3 main types of skeleton screens:

These are the most common skeleton screens and look like wireframes, in which the light gray boxes representcontentand images. The structure of the gray boxes mimics the structure of the final page with content. The skeleton screen helps users build amental modelof what will be on the page and even gives some clues as to the underlying information hierarchy.

Some skeleton screens includeanimationsin the form of a pulsating movement, with the use of gradients or elements fading in and out. These are similar to wait animations (or spinners) and signify that the system is still working and still loading content, decreasing users’ perception of a long loading time by keeping users engaged on the content being loaded.

Note that animations of this sort can potentially bedistracting, annoying, or even createaccessibility problemsfor some users.

One variation that we do not recommend is a skeleton screen that displays only the frame of the application without a content wireframe. These minimal skeleton screens only include the header, footer, and the background. This style doesn’t include placeholders of the content, and as a result, doesn’t give users a sense of the general structure of the page. A frame display is not recommended because, if users are forced to wait for too long, they will assume the page isn’t working because the screen is mostly blank.

Skeleton screens help the user understand that the page is loading, while also communicating what the page will look like. Here are a few reasons why you might consider using skeleton screens:

Skeleton screens, progress bars, and spinners all show that the system is loading information, but they serve different purposes and work best in different situations. Here are a few guidelines to help you make the decision on when to use each design.

Spinners or wait animations provide feedback to users that the system is working but don’t give any indication on how long users will have to wait; therefore, they are best used when the page takes 2–10 seconds to load. Similarly, skeleton screens should be used with a wait time that’s under 10 seconds. On the other hand, progress bars are strongly recommended for any page that takes longer that 10 seconds to load because they give users a sense of the state of the system and of how much longer they have to wait. Anything above 10 seconds requires an explicit estimation of duration.

For waiting periods less than 10 seconds, both skeleton screens and spinners could work.How do you decide between the two? Spinners are typically best used on a single module, like a video or a card which is on a dashboard. Skeleton screens (with the exception of frame-display ones) are better when the full screen is loading because the wireframe gives users a sense of what the page will look like and, thus, minimizes cognitive load.

If a page takesless than 1 secondto load, skeleton screens or spinners aren’t necessary, as they likely won’t make a difference to the users’ experience. Using a skeleton screen in such situations can be annoying because the quick flashing page can cause users to feel like they can’t keep up.

Skeleton screens are used to indicate progress only when the process that the system is performing is a full-page load. Whenever some other process (e.g., download, upload, convert a file) is involved, it does not make sense (and could even be confusing) to show a skeleton screen. Instead, show a progress bar or awizardthat walks the user through the steps of the process.

Frame-display skeleton screens display no information about the page layout; they show only a header, footer, and an empty background. They should not be used as a progress indicator because they do not give users any sense that the page is gradually transitioning into its final format. If users end up having to wait for a long time, they will assume the page is not working and abandon it.

Users generally get impatient by long loading periods. Skeleton screens ease the pain of waiting for medium-length durations by showing the page structure in a gradual manner, through placeholders and subtle animations. While skeleton screens are useful, they do not replace performance-optimization efforts. Skeleton screens are simply one extra tool for improving the wait users sometimes have to experience when content is loading.

Thomas Mejtoft, Arvid Långström, and Ulrik Söderström. 2018. The effect of skeleton screens.Proceedings of the 36th European Conference on Cognitive Ergonomics(2018). DOI:http://dx.doi.org/10.1145/3232078.3232086

Trending UX patterns and their impact on the total user experience

Interaction

Components, design patterns, workflows, and ways of interacting with complex data

Interaction

Create and evaluate applications for advanced decision making, complicated workflows, and complex domains

Interaction