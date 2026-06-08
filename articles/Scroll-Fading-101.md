# Scroll Fading 101

**Author:** Sara PaulSara PaulDecember 8, 20232023-12-08

**Topics:** Interaction Design, Design Patterns

**Source:** https://www.nngroup.com/articles/scroll-fading-101/

---

December 8, 20232023-12-08

Share

Scroll fade is a new design pattern. It refers to an animation that is triggered by scrolling: new elements or content fade in or out once the user scrolls down to a certain point on the page.

Movement (and thus animation) is processedpreattentively: the eyes are automatically drawn to it. As a result, incorrectly deployed animations can be highly distracting.

Because we knowfast user experiences beat glamorous ones, we conducted aqualitativeusability-testing study, in which we tested websites from multiple industries that all use scroll fading. This article discusses our findings and recommendations.

From ourseries of eyetracking studieson how people read online, we know users scan. One tactic for making information more digestible and scannable is to display it in small chunks. Designers can introduce those chunks when users scroll to a particular point on the page.

Definition:Scroll fadingis an animation in which certain page elements appear or change once the user scrolls down to a certain point on the page.

Scroll fading andscrolljackingare two different design patterns that relate to scrolling. The key difference between them is that scroll fading simply triggers an animation when a user scrolls to a particular point on the page, without affecting how the user is able to scroll. In contrast, scrolljacking changes the user’s scroll rate and sometimes the direction of scrolling, overriding the set scroll speed of the operating system.

Scroll fading and scrolljacking  can be used together. In the Reachdesk.com example below, the user’s scroll rate is changed (scrolljacking) and elements on the page fade in upon the user scrolling (scroll fading).

Designers use scroll fading for a few common reasons, outlined below.

Scrolling per se introduces motion to an interface, but the scroll is controlled by the user. Scroll fading introduces a secondary type of motion that is not directly controlled by the user:  an element can appear ("fade in”), disappear (“fade out”), and reappear. This additional motion gives high salience to the element that fades in or out and, thus, draws attention to it.

Scroll fading can be used to highlight important calls to action. Additionally, it can guide the user through the information-dense page via progressive disclosure, thus making the information more digestible.

Product designers might advocate for lazy loading —not loading parts of a page until they are visible to the user. This practiceconserves bandwidthand data and rightly prioritizes fast loading of the elements above the fold. (We know that contentabove the foldshould load nearly immediately becauseusers are willing to wait for only so longbefore moving on). Therefore, website-development teams might load images or other data-intensive resources only when users scroll down far enough.

Designers often leverage scroll fading to show users relevant information at a specific time. Crypto.com in the example below fades in supplementary images of the application that the text in focus describes. Scroll fading worked well in our testing when it added supplementary visual information. However, for some users, large images did not load quickly enough, further illustrating the importance of data-loading optimization.

The third reason why designers leverage scroll fading is to communicate the brand's credibility and trustworthiness. For example, on the University of Texas Austin’s homepage, scrolling down triggers a number-counter animation and shows the user that the information on the site is updated in real time. Multiple users in our study had this perception.

Element persistencein scroll fading refers to an animation that occurs only the first time the user reached that page position. The element remains visible, and the scroll-fading animation does not repeat as the user moves up and down the page.

Element persistence reduces the amount of animation on the page and works better than repeated animations.

Task-oriented users were not negatively impacted by scroll fading when it was accompanied by element persistence. In contrast, lack of persistence was problematic, because the same users did not have the patience to find the exact scroll position that caused the desired information to reappear.

For example, many study participants struggled with the calculator on Crypto.com because the inputs and outputs of the calculator were not displayed in the same viewport. Each time users readjusted the inputs, they had to scroll down and wait for the fade-in scroll animation to show the outputs. The result was wasted time and annoyance.

One participant frustratedly said,Maybe the website should immediately scroll me down . . . and show me this . . . because I have to scroll down and up.

Theillusion of completenesshappens when the user perceives visible content as complete, yet more content exists below the fold. Large hero graphics or videos, expansive white space between content elements, and interruptions in the content flow (e.g., ads) often cause the illusion of completeness.

Our study found that scroll fading can also contribute to the illusion of completeness, especially when combined with other patterns susceptible to creating it.

When information below the fold slowly faded in on a page that already seemed complete, many study participants assumed there was nothing else to be found on the page.

Multiple participants experienced this issue on the Crypto.com page, because the information at the bottom of the page faded in only after the user scrolled far down below the fold. Eventually, because our study participants did spend some time exploring the site, they did discover the information that was faded in, but it’s safe to assume that, in real life, most users would not discover it on their own.

Scroll fading of text can affect how easily people understand it. In general, scroll fading worked well with text that followed thebest practices for writing on the web.

For example, one participant reading through the MagicLinks website moved quickly past the scroll-fading text and then scrolled back up to reread it, because he did not comprehend it. This is partly because the text faded in too slowly and partly because the writing could have been more effective.

In contrast, the scroll-fading text on Apple Card website was easier to understand, because it was short, punchy, and information-packed. The snippets concisely communicated product value in the first few words and supported scanning. Additionally, the Apple Card page design gave considerable visual weight to the text, which contained the card’s key selling points.

The speed with which text faded in also contributed to comprehension. If the scroll-fade speed was too slow, users scanning quickly often skipped it altogether, scrolling past it.Prior researchtells us that a scroll-fade animation that takes more than 500ms is perceived as too slow. When this duration was approached or exceeded, we observed several users scroll past an element before it finished fading in.

In our study, pages with several scroll-fading images often failed to load all the images, confirming the consequences of the data-loading risk described above.

On Cigna.com, even though the text scroll faded in, the images didn’t load and our study participants were left feeling that they missed something. One user said,I don’t like this portion, because it has text but there’s no image beside it. I think an image would probably help enhance the text.  Another participant, who was able to load and view the images, mentioned that the experience of choosing insurance is stressful and the images made a positive difference in decreasing stress and shaping the brand personality.

When scrollfading occurred within ascrolljackedpage section, several study participants became overwhelmed and frustrated. The distracting motion from the scroll-fade animation combined with the lack of control from the scrolljack caused cognitive overload. This occurs in the Reachdesk  clip above, where a study participant encountered text and an image that scroll faded in and out and were also contained inside of a horizontal scrolljack, which rendered the content difficult to read, navigate, and understand.

Our research findings show that scroll fading introduces a mix of usability obstacles, but designers can avoid them and take advantage of its benefits by adhering to the following guidelines.

Users are likely to skip over text if it fades in too slowly. As a result, they may not comprehend what the website offers and whether it addresses their needs. However, too fast fade-in rates can also cause them to not notice the animation. To find the perfect duration, experiment with rates between100–400ms. Adjust and test the rates inusability testing, to determine whether your animation is too fast to be noticed or gradual enough to lead people through the page.

Because many users naturally skip over most scroll-fading text on their first pass down a page, element persistence on scroll fading gives the user a better chance of seeing the content on their way back up to the top of the screen if they missed it or if they need to reread it for comprehension or comparison purposes. Our studyconfirmedthe importance of persisting content to support user efficiency and decrease cognitive load.

If text and images fade in at the same time, they risk pulling the users’ attention in too many directions and overwhelming them. In our study, the most successful examples of scroll fading animated only one element at a time — either the text or the images. On websites where both text and images faded in together, they competed for the user’s attention. Any motion into an interface must carefully be deployed and evaluated. In the Apple.com design, either text or images faded in but not both simultaneously. This practice effectively drew the user’s attention to one place at a time, and it was always the most important place. That page saw the best overall efficiency and comprehension in our study.

Removing excessive whitespace and thereby decreasing the proximity between one content section and the next that fades in makes it less likely that people will fall prey to the illusion of completeness.

Further, leverage theprinciple of closureby making at least part of each subsequent content section visible (like on the Apple Card website), to encourage the user to scroll down to view the full content.

The usability issues observed on desktop were exacerbated on mobile due to the smaller screen lengths, which meant fewer pixels could be viewed at a time and scroll fatigue was increased. For example, on the mobile site of Crypto.com, users had to scroll even more than on desktop to use the website calculator. They had to wait for the calculator output to fade in each time they tested a new input. Furthermore, the illusion of completeness was more severe on mobile due to the whitespace between the calculator and the information below it.

Scroll fading was by and large most successful when the text contained in it was concise and communicated value. This natural alignment with best practices of writing for the web enabled the highest levels of efficiency and comprehension.

Scroll fading can cause serious usability issues when used incorrectly. Used sparingly, at relatively fast speeds, it can draw user attention, improve brand perception, speed up page loading, and divide your content into smaller, digestible nuggets.

Strategically combine content, visuals, and interactive components to design successful web pages

Interaction

Components, design patterns, workflows, and ways of interacting with complex data

Interaction

Create and evaluate applications for advanced decision making, complicated workflows, and complex domains

Interaction