# Tesla’s Touchscreen UI: A Case Study of Car-Dashboard User Interface - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">10</span>

<div class="article-header">

<h1 class="article-h1">Tesla’s Touchscreen UI: A Case Study of Car-Dashboard User Interface</h1>

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

May 19, 2019

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2019-05-19</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Tesla’s Touchscreen UI: A Case Study of Car-Dashboard User Interface&amp;body=https://www.nngroup.com/articles/tesla-big-touchscreen/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/tesla-big-touchscreen/&amp;title=Tesla’s Touchscreen UI: A Case Study of Car-Dashboard User Interface&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/tesla-big-touchscreen/&amp;text=Tesla’s Touchscreen UI: A Case Study of Car-Dashboard User Interface&amp;via=nngroup" data-share-type="Twitter">

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

</span>Vehicle controls should be easily accessible and require minimum attention from drivers, while driving-related information should be displayed clearly and understandably.

</div>

<div class="article-body">

<p>For those of us who learned how to drive a few decades ago, driving a modern car is a completely different experience. New cars come with rear-view cameras, obstacle sensors, parking assistance, lane-change assistance, adaptive cruise controls, autopilot driving, and even web browsers. Many of these features should make driving a safer and more comfortable activity. And they will — but only if car designers understand the most basic fact about human attention: it’s limited. And if they design these sophisticated car features so that they don’t take away cognitive resources from the basic task, which is driving.</p>

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

<a class="ga-article-toc-item" href="#toc-soft-buttons-that-demand-attention-1">Soft Buttons That Demand Attention</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-poor-target-design-2">Poor Target Design</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-target-size-3">Target Size</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-map-always-on-screen-4">Map Always on Screen</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc--5"> </a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-understanding-the-information-displayed-can-be-challenging-6">Understanding the Information Displayed Can Be Challenging</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-the-good-7">The Good</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-8">Conclusion</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc--9"> </a>

</li>

</ul>

</div>

</div><h2 id="toc-soft-buttons-that-demand-attention-1">Soft Buttons That Demand Attention</h2>

<p>Tesla’s Model S has few physical controls — all placed on or very close to the steering wheel. Driving-related functions like cruise control, autopilot, wipers, and lights are all accessible through these controls. But most of the “secondary” features (including rear-view camera, cell phone, media player, and climate control) do not have dedicated physical controls. Instead, the main way to select them is through the 17” touchscreen display placed on the dashboard, between the driver and the passenger seats.  While this is a big screen (three times the area of an iPad), it can’t show everything — so,   making matters even more complicated, in Version 9 of Tesla’s operating system, some features are placed inside an <a href="https://www.nngroup.com/articles/expandable-menus/">expandable menu</a>.</p>

<figure class="caption"><img alt="Large touchscreen with a map" height="1104" loading="lazy" src="https://media.nngroup.com/media/editor/2019/05/08/touchscreen.jpg" width="700"/>

<figcaption><em>Tesla Model S touchscreen: The secondary car controls — applications such as car climate, media player, or the rear-view camera — can be accessed from the menu bar at the bottom of the car’s 17” touchscreen display. </em></figcaption>

</figure>

<figure class="caption"><img alt="Closed menu at top; open menu at bottom" height="595" loading="lazy" src="https://media.nngroup.com/media/editor/2019/05/08/close-open-menu.jpg" width="700"/>

<figcaption><em>The arrow icon (third from left in the main menu; top) opens a submenu with additional controls (bottom). To close this menu, users must tap the “X” icon that now has appeared in the original menu in place of the arrow icon.</em></figcaption>

</figure>

<p>While touchscreen dashboards offer more flexibility than real dashboards, they have one big disadvantage: no haptic feedback. In order to reliably touch these buttons, people must look at them. Whereas with a physical button we can learn its location and acquire it without directing much, if any, attention to it (and hence we can play the piano while reading the score or we can  touchtype on a real keyboard), locating a soft button requires us to visually confirm its position.</p>

<p>When soft buttons are hidden under menus, selecting them involves multiple touchscreen interactions, and thus even more time and attention. And, in a car, time spent with the UI is time spent ignoring the road.</p>

<h2 id="toc-poor-target-design-2">Poor Target Design</h2>

<h3>Target Placement Leads to Longer Interaction Times</h3>

<p><a href="https://www.nngroup.com/videos/fittss-law/">Fitts’s Law</a> says that the time for the finger to reach a target depends on the size of that target and the distance to the target. Thus, controls placed farther away from the initial hand position will take longer to acquire than those placed closer.</p>

<p>When my generation learned to drive, the standard hand position was 2–10 (corresponding to numbers 2 and 10 on the clock). With airbags and smaller steering wheels becoming common, National Highway Traffic Safety Administration (NHTSA) has changed its recommendation and now 3–9 has become the safest position.  For both these hand placements, the optimal control positioning would be on the middle left edge of the screen, close to the driver’s right hand. Yet, Model S’s controls are placed at the very bottom of the 17” screen — an area that is next worst possible (after the right edge of the screen).</p>

<figure class="caption"><img alt="A steering wheel and in-car touchscreen" height="525" loading="lazy" src="https://media.nngroup.com/media/editor/2019/05/08/hand-on-wheel.jpg" width="700"/>

<figcaption><em>Version 9 of Tesla’s operating system places the control menu far away from the normal hand position in driving. The red line indicates the distance between the normal right hand position (at 3 o’clock) and the control area.</em></figcaption>

</figure>

<p>Having the controls at the bottom of the screen also means more time for the eyes to move from the windshield to the menu area, and also less of a chance that people will be able to use their peripheral vision to attend to unexpected stimuli that appear on the road when they are busy interacting with (and looking at) the touchscreen.</p>

<p>Within a given menu, the most commonly used options should be the easiest to access. Yet, Tesla’s decisions with respect to the ordering of the controls in the menu are at best dubious. The first option is the access to all the car’s settings and customizations — something that is unlikely to be used often while driving.  The rear-view camera (an essential feature in a car whose rear-windshield view is partially blocked by the backseat headrests) is available under the arrow menu, as is the cell phone. And these arguably frequently used options are not even given priority in that menu: instead of being immediately above the arrow icon (to minimize finger travel time), the <em>Calendar</em>, <em>Energy</em>, and <em>Web</em> (for the web browser) are listed first. (How often will you use these during driving compared to the rear-view camera and the phone?)</p>

<h2 id="toc-target-size-3">Target Size</h2>

<p>The other factor in target-acquisition time is the target size: the larger the button, the faster it will be reached. Yet, with version 9, Tesla decided to make its targets smaller (presumably in order to fit more options in the visible menu bar — 7 in version 8 compared with 10 or 11 in version 9). It’s a temptation that many mobile designers have succumbed to — but unfortunately it does not lead to usable designs.</p>

<figure class="caption"><img alt="" height="1058" loading="lazy" src="https://media.nngroup.com/media/editor/2019/05/08/media-player.jpg" width="700"/>

<figcaption><em>The icons for controlling the media player (</em>Play/Pause, Like, Nex<em>t) are smaller than the recommended 1cm X 1cm touch-target size.  However, the tabs at the bottom of the media-player display (</em>Radio<em>, </em>Streaming<em>, </em>Phone<em>, etc.) are much bigger (and they also include a label and an icon — a practice that we strongly encourage).</em></figcaption>

</figure>

<h3>Accidental Touches</h3>

<p>Because the targets in the control panel are too close to each other, it’s sometimes too easy to touch the wrong target. For example, on many occasions I triggered the seat warmer while trying to change the temperature or tap the climate icon. The seat icon is also easy to accidentally touch when the driver tries to access the most recent app by using a swipe up on the arrow icon (<a href="https://www.nngroup.com/articles/iphone-x/">a gesture shortcut likely inspired by iOS</a>).</p>

<figure class="caption"><img alt="" height="514" loading="lazy" src="https://media.nngroup.com/media/editor/2019/05/08/hand-swipe-up-with-trajectory.jpg" width="700"/>

<figcaption><em>The seat warmer can be accidentally triggered when the user is swiping vertically on the app icon to launch the most recent app (as shown in this screenshot — the dotted red line represents the trajectory of the finger). The same seat icon can be tapped by mistake when the user is trying to adjust the driver-side temperature.</em></figcaption>

</figure>

<h2 id="toc-map-always-on-screen-4">Map Always on Screen</h2>

<p>To allow people to quickly get the information that they need from the screen and then move on, text on car dashboards should be easy to read in a variety of light conditions. <a href="https://www.nngroup.com/articles/let-users-control-font-size/">Text that is too small</a>, appears <a href="https://www.nngroup.com/articles/text-over-images/">on a busy background</a>, or has <a href="https://www.nngroup.com/articles/low-contrast/">low contrast with the background</a> does not usually satisfy these requirements. </p>

<p>Yet, Tesla’s map app is always displayed in the background of all apps.  As a result, the status bar at the very top of the screen can be hard to read, as it blends in with the map text. Moreover, it can be quite irrelevant (and potentially distracting) to a see a brightly colored street appearing between two application windows, like in the screenshot below. Plus, the fact that no application can be brought at the very top of the screen not only takes away user control (and goes against one of the <a href="https://www.nngroup.com/articles/ten-usability-heuristics/">10 usability heuristics</a>) but is also wasteful, forcing users to see at the top a small part of the map that carries very little information.</p>

<p>The map in the background also makes the interaction with the other apps more error prone: if you’re trying to increase the size of an app window, you will have to drag from the top edge of the app’s view. But if you’re not careful and position your finger above the window handle, nothing will happen — because the OS will assume that you are swiping the map instead of maximizing the map window.</p>

<h2 id="toc--5"> <img alt="" border="0" height="624" loading="lazy" src="file:///C:/Users/rbudi/AppData/Local/Temp/msohtmlclip1/01/clip_image016.jpg" width="468"/></h2>

<figure class="caption"><img alt="" height="1131" loading="lazy" src="https://media.nngroup.com/media/editor/2019/05/08/map-in-bck.jpg" width="700"/>

<figcaption><em>The map appears in the background of all apps, potentially interfering with any content displayed above it or with the use of swipe to close or maximize applications. The red traffic markers are visible in the area between the calendar and the media player app, potentially distracting the driver with irrelevant info. (Note also that the calendar app is closed by tapping the "X "in the top left corner, unlike the media-player app which is closed by swiping down from the handle on the top edge of its window.)</em></figcaption>

</figure>

<h2 id="toc-understanding-the-information-displayed-can-be-challenging-6">Understanding the Information Displayed Can Be Challenging</h2>

<p>If you want to change lanes while driving a Tesla, you can use any of the following sources of information:</p>

<ul>

<li>The old-fashioned rear-view mirror plus your side mirrors and turning your head left/right to check lane availability</li>

<li>The rear-view camera (In previous versions of the Tesla OS, you could pin that at the top of the main touchscreen.  Now it’s never at the very top, so, to glance at it, your eyes need to move from the road down to the touchscreen.)</li>

<li>The lane-assist feature on the secondary screen, that displays a red line when you’ve engaged the turn signal but the lane is not available</li>

</ul>

<figure class="caption"><img alt="" height="505" loading="lazy" src="https://media.nngroup.com/media/editor/2019/05/09/lane-assist.jpg" width="700"/>

<figcaption><em>The instrument panel shows whether the car can safely change lanes (top) or not (bottom). Only the lanes immediately adjacent to the vehicle are shown.</em></figcaption>

</figure>

<p>The problem is that none of these information sources are complete (for example, the rear-mirror view is partially blocked by headrests), and by the time you check them all, you’ve already reached your destination. So, what most people end up doing is taking a shortcut to save interaction cost and relying on just one of these sources of information. Which one do you think they’re most likely to pick? The one with the lowest <a href="https://www.nngroup.com/articles/interaction-cost-definition/">interaction cost</a>: the lane assist displayed on the secondary dashboard, which always appears when the turn signal is engaged.</p>

<p>(This is actually an example of successfully unlearning an old, well-rehearsed behavior — app designers who struggle to teach users how to become more efficient should take a lesson from Tesla’s book: if you make it easier than what it was before and you always show it to them at the right time, users will eventually rely on it.)</p>

<p>So, if people end up doing the same task faster, it’s good, right? Well, it would be if this solution was guaranteed to work correctly in all circumstances. In fact, Tesla warns against relying solely on lane assist for lane changes. Even barring sensor errors (which are more common than one would expect), it can be challenging to interpret the displayed information correctly. The problem is that the user may not recognize to what lane the lane-assist cues apply. To understand why, imagine that you are driving on a three-lane road and you want to switch lanes from the rightmost lane to the middle lane. When you engage the turn signal, the car might show that the lane is free. But, as soon as you reach the middle lane, the car will show information about switching into the left lane since your turn signal is still engaged. Yet, users are not always perfectly aware of the location of their car — so as they may check the lane-assist display, engage in a lane switch, then check again the display, notice the red alert (which this time would pertain to switching into the next lane), misinterpret that as referring to their current goal, and panic, swerving the car back into its original lane.</p>

<p>This example points out an important dilemma that car designers and manufacturers face today. New features such as autopilot (or self-driving), lane assist, collision detection and so on have the potential to replace well-learned, traditional driver behaviors such as looking over the shoulder or checking the mirrors that we used to rely on. If these features are functional and using them is are easier than performing the gestures and actions that we learned in driving school, then they will replace those actions (we are creatures of minimum effort: we always take the solution that requires least work — not because we’re lazy, but because we’re efficient). That’s why we hear in the news about people putting on makeup, playing games, or even sleeping at the wheel — because modern cars make it seem safe to do so. Yet, it is our responsibility as designers to create the right mental model and give people the right understanding of how our systems work, in order to make sure that by displacing these old-fashioned behaviors we’re not making driving more dangerous.</p>

<h2 id="toc-the-good-7">The Good</h2>

<p>As we noted above, there are many improvements that could be made to Tesla’s UI. But there are also several elements of good design.</p>

<ol>

<li>The big screen is a plus: it offers the ability to see multiple application windows side by side. Switching apps can be a pain (as it does involve multiple taps and looking at the screen), but the ability to see several of them (e.g., the rear-view camera and the map or the media player) simultaneously makes things easier for the driver.

<p>Driving is a situation where people do need to access multiple sources of information simultaneously (e.g., the map and the rear-view camera) and seeing all those windows at the same time significantly decreases the user’s <a href="https://www.nngroup.com/articles/working-memory-external-memory/">working-memory</a> load. (In contrast, even on the biggest tablets, <a href="https://www.nngroup.com/articles/multitasking-mobile/">people rarely split the screen to show multiple windows at the same time</a>, although this feature has been around for a while.)</p>

</li>

<li>The map app is enriched with Tesla-specific information. For example, even though the app is based on Google Maps, it does have several options specific to Tesla owners:

<ol style="list-style-type:lower-alpha;">

<li>the location of superchargers is automatically displayed on the map</li>

<li>when navigating to a destination, the map shows how much charge will be left in the battery at the time when the destination is reached</li>

<li>the navigation app allows users to receive directions based on the use of the car-pool lanes</li>

</ol>

<figure class="caption"><img alt="" height="1035" loading="lazy" src="https://media.nngroup.com/media/editor/2019/05/09/map.jpg" width="700"/>

<figcaption><em>The map app shows how much charge will be available when the destination is reached.</em></figcaption>

</figure>

</li>

<li>The autopilot and self-navigation systems acknowledge the possibility of failure and require drivers to keep their hands on the steering wheel while active.</li>

<li>Tesla is always connected to the internet and can receive updates through the air. This feature can be viewed both as a plus and as a minus. The good is that bugs can be fixed quickly and deployed to cars in the same way in which a website can change colors from one day to the next. Analytic data about the drivers can be easily connected, bugs can be reported, and problems fixed. Unfortunately, a continuously changing interface can also create potentially fatal issues if users’ expectations formed in prior versions are now suddenly violated. (Plus, one must trust that the car manufacturer will only deploy safe, well-tested versions of the operating system.)</li>

</ol>

<h2 id="toc-conclusion-8">Conclusion</h2>

<p>Modern cars are powerful computers. They can augment drivers’ cognitive and physical abilities with information collected from a variety of sensors; they can also enhance the driving experience with a plethora of convenience features that are one tap away. Yet none of these will truly happen until car designers take into account the decades of designing computer interfaces and follow well-known principles of usability and human psychology.</p>

<p> </p>

<h2 id="toc--9"> </h2>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">car UI,Human Computer Interaction</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Human Computer Interaction</span>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

</ul>

</div>

</div>

</div>

</div>