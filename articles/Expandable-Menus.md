# Expandable Menus: Pull-Down, Square, or Pie? - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">9</span>

<div class="article-header">

<h1 class="article-h1">Expandable Menus: Pull-Down, Square, or Pie?</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Raluca Budiu</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/2023-04-portraits-raluca.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/raluca-budiu/">

Raluca Budiu</a></span>

<p class="publication-date">

May 8, 2016

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2016-05-08</span>

</p>

</div>

</div>

</div>

<div class="article-share">

<a class="article-share-title ga-share" href="#">

<span class="article-share-icon"></span>

<p class="article-share-label body-medium">Share</p>

</a>

<div class="share-links tooltip">

<div class="tip-arrow"></div>

<ul>

<li class="body-medium">

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Expandable Menus: Pull-Down, Square, or Pie?&amp;body=https://www.nngroup.com/articles/expandable-menus/" data-share-type="Email">

<svg

width="24"

viewbox="0 0 24 24"

fill="none"

xmlns="http://www.w3.org/2000/svg"

class="icon"

>

<rect x="2.375" y="5" width="19.25" height="14" rx="0.65625" stroke="currentColor" stroke-width="1.3125"/>

<path d="M21.625 6.75L12.4156 14.285C12.1738 14.4828 11.8262 14.4828 11.5844 14.285L2.375 6.75" stroke="currentColor" stroke-width="1.3125"/>

</svg>Email article

</a>

</li>

<li class="body-medium">

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/expandable-menus/&amp;title=Expandable Menus: Pull-Down, Square, or Pie?&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/expandable-menus/&amp;text=Expandable Menus: Pull-Down, Square, or Pie?&amp;via=nngroup" data-share-type="Twitter">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-x" />

</svg>

Share on Twitter

</a>

</li>

</ul>

</div>

</div>

</div>

<div class="article-container">

<div class="article-content">

<div class="article-summary article-heading-small-light">

<span class="article-summary-label">

Summary:&nbsp;

</span>Selecting an option inside a menu depends on how far away that option is from the menu icon. Drop-down menus, megamenus, pie or radial menus, and marking menus arrange items in different patterns to optimize the reach time.

</div>

<div class="article-body">

<p>Originally developed at PARC back in the 1970s, <strong>menus</strong> are lists of options in a graphical user interface (GUI). They can be either <strong>visible</strong> (sometimes called “menu bars”) or <strong>expandable. </strong>In expandable menus, the list of options is exposed when a <strong>menu</strong> <strong>handle</strong> is clicked or tapped; the menu handle can be a label, an icon, or both. In this article we focus on expandable menus.</p>

<div class="table-of-contents">

<div class="content">

<div class="header">

<div class="toc-header">

<h2 class="toc-title article-heading-small">

In This Article:

</h2>

<span class="expand-icon"></span>

</div>

<a class="current-element" href="#"></a>

</div>

<ul class="toc-items">

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-two-design-problems-for-expandable-menus-1">Two Design Problems for Expandable Menus</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-fitts-law-and-movement-time-2">Fitts’ Law and Movement Time</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-linear-or-pull-down-menus-3">Linear (or Pull-Down Menus)</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-rectangular-or-square-menus-4">Rectangular (or Square) Menus</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-pie-or-radial-menus-5">Pie (or Radial) Menus</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-marking-menus-6">Marking Menus</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-other-types-of-menus-7">Other Types of Menus</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-how-about-touch-8">How About Touch?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-9">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-two-design-problems-for-expandable-menus-1">Two Design Problems for Expandable Menus</h2>

<figure class="caption"><img alt="" height="421" loading="lazy" src="https://media.nngroup.com/media/editor/2016/04/29/linear-menu.png" width="601"/>

<figcaption><em>Internet Explorer menu bar (left) and </em>File<em> menu (right). The </em>File<em> menu is an expandable menu hidden under the handle “File.” The menu option </em>Send<em> is further expandable to display a submenu.</em></figcaption>

</figure>

<p>The two big design problems concerning expandable menus are:</p>

<ul>

<li><strong>How make menus discoverable</strong>, or in other words, how to make the handle look clickable (so people click on it) and have good <a href="https://www.nngroup.com/articles/information-scent/">information scent</a></li>

<li><strong>How to minimize selection time</strong> inside a menu, that is, how to reduce the time to <em>find </em>and <em>click </em>on the right option</li>

</ul>

<p>The selection time itself has two components:</p>

<ol>

<li><strong>The visual-search time:</strong> the time to locate the item of interest among the set of options inside the menu</li>

<li><strong>The movement time</strong>: the time needed to move the cursor (or finger) to the item of interest located by visual search</li>

</ol>

<p><strong>Familiarity</strong> with the type of menu modulates both these components. If users have to first learn how to operate a menu, then this learning time can easily dwarf any savings in selection time unless they will use that same menu many, many times. Also, the initial use of a new interaction method is more error prone, and the time wasted recovering form errors is hugely larger than the time savings from optimizing selection time.</p>

<p>Over the last 35 years, HCI researchers have explored various types of menus and of menu organizations, in the attempt to minimize either the visual-search time or the movement time. This article surveys several menu types and discusses how well they fare with respect to average movement time. But before discussing the different types of menus, let’s see how we can quantify the movement time.</p>

<h2 id="toc-fitts-law-and-movement-time-2">Fitts’ Law and Movement Time</h2>

<p><a href="http://www.asktog.com/columns/022DesignedToGiveFitts.html">Fitts’ law</a> calculates the time it takes people to reach any target, whether using a mouse, a finger, or even their hands to grab an object. What it says is simple and makes intuitive sense: the time it takes people to reach a target depends on:</p>

<ul>

<li>The size of the target (the smaller the target, the longer the time)</li>

<li>The distance to the target (the farther away the target, the longer the time)</li>

</ul>

<figure class="caption"><img alt="" border="0" height="262" loading="lazy" src="https://media.nngroup.com/media/editor/2016/04/29/fitts.png" width="523"/>

<figcaption><em>Fitts’ law says that the time to reach Target A is shorter than the time to reach any of the other targets. Although Targets A and B have the same size, the distance from cursor to A (d1) is shorter than the distance to B (d2), so movement to A will be faster. Target C is placed at the same distance (d1) from the cursor as Target A, but it’s smaller, so it will take longer to move the cursor to it than to A.</em></figcaption>

</figure>

<p>While the <a href="https://www.nngroup.com/articles/touch-target-size/">target size</a> usually informs our design for buttons and other active elements, the distance to target is the component that is usually optimized for menu design.</p>

<h2 id="toc-linear-or-pull-down-menus-3">Linear (or Pull-Down Menus)</h2>

<p>To understand the time it takes to reach a target in a menu, let’s first focus on a mouse-based interaction in a traditional pull-down or drop-down menu. (This type of menu is also called a linear menu because all the menu options are displayed in a list.) We will assume that the menu has been just triggered by clicking on the menu handle. As a result, the menu options are now visible on the screen and the cursor is placed on the menu handle.</p>

<figure class="caption"><img alt="" border="0" height="428" loading="lazy" src="https://media.nngroup.com/media/editor/2016/04/29/linear-menu-distance.png" width="284"/>

<figcaption><em>In a linear menu, the time to reach the first item in the menu is shortest and the time to reach the last element is longest because the distance from the cursor (that is, menu handle) to the first element is the shortest and the distance to the last element is the longest.</em></figcaption>

</figure>

<p>Note that the time it takes to reach the first element in the menu is shorter than the time it takes to reach any other element in the menu — simply because the distance to that first element is shorter than the distance to the second element, which is shorter than the distance to the third element and so on. In fact, the last element in the menu takes the longest time to reach because it’s the farthest away from the handle. This is one of the reasons for which we recommend against overly long menus — it takes a long time for people to select one item from such a menu (plus, sometimes, it is even more challenging if the menu is longer than the window size and users must scroll down the page).</p>

<p>Can we improve the average movement time in a linear menu? One simple improvement is to actually change the position of the list so that the middle element is aligned with the handle instead of the first element. By doing that, you’ve decreased the average distance to a menu element.</p>

<figure class="caption"><img alt="" height="410" loading="lazy" src="https://media.nngroup.com/media/editor/2016/04/29/linear-menu-middle-3.png" width="308"/>

<figcaption><em>By aligning the menu handle with the middle element, you reduce the average movement time to click options inside the menu.</em></figcaption>

</figure>

<p>(Unfortunately it is not always possible to use a menu like this one simply because there may be not enough space above the handle to display half of the options.)</p>

<h2 id="toc-rectangular-or-square-menus-4">Rectangular (or Square) Menus</h2>

<p>Another way to reduce the distance to the menu options is to place them in a rectangle. Hence the <strong>rectangular</strong> (sometimes called square) <strong>menu</strong>, better known as the <a href="https://www.nngroup.com/articles/mega-menus-work-well/"><strong>megamenu</strong></a>.</p>

<figure class="caption"><img alt="" border="0" height="314" loading="lazy" src="https://media.nngroup.com/media/editor/2016/04/29/rei-megamenu-distance.png" width="630"/>

<figcaption><em>The average distance to an item inside a megamenu is smaller than if all the items were placed in a long list one under the other (that is, in a linear menu).</em></figcaption>

</figure>

<p> </p>

<p>It’s easy to show (using a little bit of geometry) that the rectangular menu has better average distance to any random element than the linear menu. Rectangular menus work quite well in terms of optimizing the movement time, and nowadays they are hugely popular on the web.</p>

<h2 id="toc-pie-or-radial-menus-5">Pie (or Radial) Menus</h2>

<p>What if the time to all elements of the menu was the same? That is possible if all the elements are at equal distance from the handle — that is, they are placed on a circle centered in the menu handle. That’s how the <strong>pie (or radial) menu</strong> was born. Believe it or not, the pie menus are quite old: they date from the late 1980s.</p>

<figure class="caption"><img alt="" border="0" height="299" loading="lazy" src="https://media.nngroup.com/media/editor/2016/04/29/onenote-radial.png" width="367"/>

<figcaption><em>One Note pie menu: the handle is in the middle of the circle, and all the menu options are displayed around it. The distance to any of the options is the same.</em></figcaption>

</figure>

<p>Pie menus have never been really popular. Although HCI researchers love them, it turns out that users are not quite familiar with them. A 2010 study showed that in practice they are harder to learn than the more standard linear and rectangular menus, so the movement-time gain is lost due to lack of familiarity with this interface. However, as users become more familiar with the pie menus, these menus do start to show the advantage that researchers have predicted.</p>

<figure class="caption"><img alt="" border="0" height="210" loading="lazy" src="https://media.nngroup.com/media/editor/2016/04/29/yelp-pie.png" width="350"/>

<figcaption><em>Yelp for iPhone uses a “half-pie” menu to display options related to reviewing a service.</em></figcaption>

</figure>

<p>(We wrote an April Fool’s article suggesting that <a href="https://www.nngroup.com/articles/hamburger-menu-vs-pizza/">pizza menus are even better than pie menus</a>. However, that was a joke, and pizza menus aren’t a real design concept.)</p>

<h2 id="toc-marking-menus-6">Marking Menus</h2>

<p>Marking menus are a version of the pie menus that takes advantage of the fact that menu items are uniquely defined by their direction. In other words, when the user starts moving towards a target, you can tell what the target is going to be before the target is hit, just by looking at the direction of the movement.</p>

<p>Marking menus have two “modes”: in <em>normal mode</em>, the menu gets expanded when the handle is clicked, and then you can select an option either by clicking an item (like in a regular pie menu) or by moving the cursor (or the finger) towards the desired item. In the <em>expert mode</em>, however, the menu does not get displayed: the user simply starts moving the cursor in the direction of the target (this action is called “making a mark”, hence the name “marking menu”) and the system interprets that gesture as the selection of the corresponding target. The expert mode makes sense for applications that receive heavy use, where users learn the arrangement of the menu options in the menu and don’t need to see them displayed (for instance, Kurtenbach and Buxton showed in 1994 that the expert mode is preferred by users in the context of a task that required more than 9 hours of audio editing per user).</p>

<p> </p>

<figure class="caption"><img alt="" border="0" height="322" loading="lazy" src="https://media.nngroup.com/media/editor/2016/04/29/pinterest-marking-menu.png" width="700"/>

<figcaption><em>Pinterest for iPad uses a marking menu that has only the normal mode. Once the user presses the menu handle, the menu gets expanded and the user can select an option by moving the finger in the direction of that option. As soon as the user lifts the finger, the highlighted option is selected and the menu disappears.</em></figcaption>

</figure>

<p>Marking menus are well suited for contextual use, being more efficient because users do not need to travel the whole route to the target, but they can just start moving towards the target. In expert mode, the menu also saves users an extra step (that of expanding the menu and inspecting the items inside). Of course, the expert mode is too error-prone for less skilled users, since they don’t get visual confirmation of their choices.</p>

<h2 id="toc-other-types-of-menus-7">Other Types of Menus</h2>

<p>HCI researchers have experimented with many variations on these menus in their attempt to minimize movement time inside the menu (an example included a linear menu in which elements farther away from the handle got larger target areas to compensate for the increase in distance). Most of these never found their way in real-world interfaces because, in spite of their nice theoretical properties, they were unfamiliar and hard to get used to, so they never became popular on the web.</p>

<h2 id="toc-how-about-touch-8">How About Touch?</h2>

<div>

<p>Although Fitts’ law does apply to touch interfaces, one assumption that does not transfer easily when it comes to menu design is that of the initial cursor position. With the mouse, one can assume that immediately after opening a menu, the cursor is still on the handle. But with a touchscreen it’s very possible that after a menu has been opened, the finger position is no longer on the handle or even above it. (This is true in particular for mobile handheld devices —phones and tablets; for <a href="https://www.nngroup.com/articles/very-large-touchscreen-ux-design/">very large touchscreens</a> (e.g., tabletops), where often the entire body needs to be moved to get to an area, it is possible that the user and the hands are still in closer proximity of the handle.) Keeping the finger above the menu handle is usually unproductive because it obscures part of the screen. Plus, many times the handle actually disappears or is moved to a different area of the screen.</p>

<p> </p>

<figure class="caption"><img alt="" border="0" height="1061" loading="lazy" src="https://media.nngroup.com/media/editor/2016/04/29/gmail-menu-both.png" width="700"/>

<figcaption><em>Gmail for iPad: The hamburger icon (top screenshot) expands a sliding menu that pushes the menu handle (the hamburger) towards the middle of the page (bottom screenshot). Even if the finger position were to stay unchanged after the menu got expanded, the user would have to move it out of the way to see the elements inside the menu. (The blue area approximately represents the finger.) </em></figcaption>

</figure>

<p>Thus, many of the considerations we discuss in this article do not necessarily apply. The interesting question for touch handhelds is where the menu is displayed in relation to the most likely position of the hands and fingers, and how to optimize menu reach time relative to that positon.</p>

<p>That being said, there is one exception: marking menus in the normal mode (like the one in the Pinterest app displayed above). Marking menus are well suited for touch interfaces, because they don’t require a precise reach of the target (which tends to be problematic with touchscreen interfaces due to our <a href="https://www.nngroup.com/articles/mouse-vs-fingers-input-device/">fat fingers</a>). To preserve the movement-time advantage, they do require that the finger stay put on the handle and then move in the direction of the desired option. The disadvantages of this constraint are two: (1) there is a certain physical strain associated with keeping the finger in the same spot for a given amount of time to inspect the menu elements; (2) the finger does block part of the screen, so often these menus work best as circle fragments.</p>

<p>Pie and marking menus have encountered their moment of glory in the era of touchscreen devices. We see more and more versions of these menus in touch apps. Finally, these menus are in a good position to overcome the unfamiliarity obstacle and translate their theoretical advantages to the real world. However, many of these menus are not optimally designed. Remember, a normal pie menu (like in the Yelp app above), where the menu stays on the screen when the finger is lifted from the handle and the user can select an option by tapping on the desired item, does not gain you the movement-time benefits.</p>

<h2 id="toc-conclusion-9">Conclusion</h2>

</div>

<p>Movement time in an expandable menu is governed by Fitts’ law. Linear menus are best when the number of menu options is small; as the number increases, rectangular menus (or megamenus) are more appropriate. Marking menus are well suited for touchscreens, and, like pie menus, optimize the reach time to individual options, but are only now starting to become more familiar due to their popularity on touchscreen devices. If you’re considering a new, less familiar menu because it has good movement time (or any other desirable quality), reserve it for cases with high-frequency use or wait until the design has become more familiar.</p>

<div>

<h3><strong>References</strong></h3>

<p>D. Ahlström, A. Cockburn, C. Gutwin, and P. Irani. 2010. Why it's quick to be square: modelling new and existing hierarchical menu designs. ACM CHI’10, 1371-1380. DOI=<a href="http://dx.doi.org/10.1145/1753326.1753534">http://dx.doi.org/10.1145/1753326.1753534</a></p>

<p>G. Kurtenbach, and W. Buxton, W. 1994. User learning and performance with marking menus. ACM CHI '94, 258-264. DOI=<a href="http://dx.doi.org/10.1145/191666.191759">http://dx.doi.org/10.1145/191666.191759</a></p>

</div>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">menus,Human Computer Interaction,Interaction Design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Human Computer Interaction</span>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/interaction-design/">Interaction Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>