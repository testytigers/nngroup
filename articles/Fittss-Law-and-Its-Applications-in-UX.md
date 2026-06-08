# Fitts's Law and Its Applications in UX

**Author:** Raluca BudiuRaluca BudiuJuly 31, 20222022-07-31

**Topics:** Application Design, Human Computer Interaction, Visual Design

**Source:** https://www.nngroup.com/articles/fitts-law/

---

July 31, 20222022-07-31

Share

Paul Fitts was one of the first psychologists who understood that human error is attributable to poor design as opposed to just human fallacy. He studied airplane-cockpit design during World War II and argued that many losses that had been attributed to human error were, in fact, due to poor design.

In the 1950s, he became influenced by the Shannon’s famousinformation theory. Like George Miller, who applied the concept of channel capacity to human memory and, in the process, came up with thefamous magical number 7as the bandwidth of humanshort-term memory, Fitts aimed to find the bandwidth of human movement — how many repetitive movements could be performed in a given time interval. He did several experiments involving such repetitive movements and as a result he came up with Fitts’s law, one of the most famous laws of human-computer interaction.

Fitts’s law gives us the relationship between the time it takes apointer(such as a mouse cursor, a human finger, or a hand) to move to a particulartarget(e.g., physical or digital button, a physical object) in order to interact with it in some way (e.g., by clicking or tapping it, grasping it, etc.):

whereDis the distance to the target,wis the width of the target (technically, measured along the axis of movement), andaandbare constants that vary depending on the type of pointer (e.g., mouse, finger, etc.).

The quantity

is sometimes called an index of difficulty and is measured in bits. An alternative formulation of Fitts’s law is then:

Technically, Fitts’s law equation uses the width of the target in the direction of the movement, but, for most rectangular targets that are common in user interfaces, we can replace it with the smallest of the target dimensions, whether it’s height or width (as shown by Scott MacKenzie and Bill Buxton in 1992).

If this mathematical equation seems obscure to some of you, its gist is captured by the following two statements below:

The equation includes a logarithm — meaning that the time doesn’t grow linearly with the parameters, but at a slower pace. So, if something is twice as far away, it takes longer to reach it, but not twice as long. That is because movement first accelerates and then decelerates (as described in the next section), meaning that you get to move the pointer at a higher speed during part of the travel time when the distance is longer, and then more slowly as you get closer.

This is exactly the essence of the two-component model described below.

Well before Fitts, at the end of the 19th century, one of the pioneers of human-movement research, R. S. Woodworth, presented his two-component model of upper-limb physical movement. The model said that any goal-directed movement (e.g., performed to acquire a target as opposed to, say, tapping in the rhythm of music) can be decomposed into two components (hence the name):

The first phase is largely driven by the distance to the target — the movement will aim to take the pointer in the direction of the target as fast as possible.The second movement phase is, however, driven mostly by size of the target— the pointer needs toslow down in order to not overshoot and click beyond the target. The smaller the target, the more time tends to be spent in this second phase.

The implications of Fitts’s law can be grouped into 2 distinct categories, corresponding to the two variables that affect the movement time: target size and distance to target.

The most obvious implication of Fitts’s law is: make targets big. Fitts’s law clearly says that people will be faster to click, tap, or hover on bigger targets. Not only that, but error rates go down as target sizes increases.Guidelines for target sizeare usually created by determining the rate of error for various target sizes and identifying the size at which the error rate levels off.

We’ve said many times thaticons need labels. Not only does a text label reduce icon ambiguity and makes it easy to understand, but it also improves movement time to that particular target. Why? It’s simple: any target made up of both an icon and a label will be greater than just an icon and, therefore, according to Fitts’s law, will be easier to acquire. (This, of course, assumes that you do make the entire area clickable and avoid the design mistake of only making the icon itself the active target.)

In the two-component model, the final-movement component can be greatly reduced if the target is very big — or even infinite. With an infinite target, there is no worry that you’ll overshoot since it doesn’t matter where the pointer stops its movement (of course, provided the target area has been reached).

At this point, you may ask: Where in real-world interface design do we have infinite targets? The answer is on thescreen edges, as long as the interaction is mouse-driven. Indeed, the screen edges act as natural walls for the cursor — as soon as the pointer reaches an edge, it cannot move beyond it, regardless of the speed with which that wall has been hit.

So technically, in order to reach a target placed on the edge of the screen, the user doesn’t have to slow down as much as if the target was in the middle of the screen because there is no danger of overshooting – the pointer will be automatically stopped once it hits the edge of the screen.

Operating-system designers have taken advantage of this consequence of Fitts law. In MacOS, application menus are shown at the very top of the screen, on the horizontal edge. This enables the user to reach that area very easily.  In Windows (at least until Windows 8) the start button was placed in the bottom left corner of the screen. In both operating systems, icons for various frequently used applications are placed along the bottom of the screen.

Note, however, that while the edge placement offers an advantage in mouse- or trackball-driven UIs, it offers no advantage for touchscreens. In fact, a study by Daniel Avrahami showed that, for touchscreen devices, it actually takes longer to hit targets placed around the edges, possibly because for touchscreens, it is possible to overshoot and hit beyond the edge of the screen.

If you place targets too close to each other, there is a risk that people will accidentally overshoot and accidentally trigger the wrong target. Note that this is especially likely to happen if the targets are small.

Sometimes designers will pad certain targets, thus increasing the effective target area. However, remember that, even though padding will help prevent some overshooting errors, if people do not realize that a target is padded, they may still cautiously slow down more than necessary as they get closer to the target, in order to make sure they will not go beyond the target area.

The type of menu used for displaying a list of items will play a role in movement time to any of those items. To see why, let’s look at three different menus:a linear menu, a rectangular menu (otherwise known as a mega menu), and a pie menu.

Let’s assume that, when the menu is opened, the pointer is on the menu handle or label. (This is a realistic assumption in mouse-based interfaces. Even though people will occasionally usekeyboard access keysto open up a menu, the more common scenario is that the menu was opened using the mouse.)

In the linear menu, you can see that the distance from the menu handle to the first element in the menu is the shortest and the distance to the last element in the menu is the longest. Therefore, with such a menu, you may consider ordering items according to their frequency of use (with the most frequently accessed ones at the top).

In a rectangular menu, items are arranged along both the horizontal and vertical dimensions and, thus, the average distance to a menu option is lower than if the menu was linear.

Last, in a pie menu, all menu elements are placed on a circle around the handle and thus are equally far away from the handle. As a result, the time to reach any of these options will be the same. (In spite of this great benefit of pie menus, they remain still relatively unused in UI design and, because of that, unfamiliar to users.)

Even for the humble linear menu, if all elements are accessed relatively equally, average movement time can be improved by aligning the handle with the middle of the menu so that the farthest elements are the first and the last, and the closest one is that in the middle.

On mobile, some contextual menus show the associated options in a bottom sheet that appears far away from the menu label. This design is suboptimal, since it forces the users to waste movement time. Ideally, the options should appear close to the label.

If you know that a set of controls will be clicked in a certain order,place them close to each other(but not too close — see guideline above) to minimize the distance between them and optimize overall task time.

For example, theSubmitbutton in a form should be placed next to the last form field.Mobile designs that place theSubmitbutton at the very top of the page, in the page header, not only go against the natural, top-down direction of the users’ workflow, but also result in suboptimal movement time because the user needs to move their finger from the last form field, low on the screen, to the very top of the screen.

Fitts’s law says that the time to move to a target depends on how big it is and on how far away it is.  As you are creating new UI designs, think about optimizing both these variables by creating well-spaced, big targets and positioning them so that they are close to the user’s most probable prior location.

Avrahami, D. 2015.The Effect of Edge Targets on Touch Performance. CHI’15.

Elliott, D., Helsen, W. F., & Chua, R. (2001). A century later: Woodworth's (1899) two-component model of goal-directed aiming.Psychological Bulletin, 127(3), 342–357.https://doi.org/10.1037/0033-2909.127.3.342

Fitts, Paul M. (June 1954). "The information capacity of the human motor system in controlling the amplitude of movement".Journal of Experimental Psychology.47(6): 381–391.doi:10.1037/h0055392

I. Scott MacKenzie and William Buxton. 1992. Extending Fitts' law to two-dimensional tasks. InCHI '92. New York, NY, USA, 219–226. https://doi.org/10.1145/142750.142794

Components, design patterns, workflows, and ways of interacting with complex data

Interaction