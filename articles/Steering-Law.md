# Accot-Zhai Steering Law: Implications for UI Design - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">5</span>

<div class="article-header">

<h1 class="article-h1">Accot-Zhai Steering Law: Implications for UI Design</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Page Laubheimer</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/2022-portrait-page-3.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list">

Page Laubheimer

</span>

<p class="publication-date">

June 23, 2019 &centerdot; Updated Aug. 7, 2024

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2024-08-07</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Accot-Zhai Steering Law: Implications for UI Design&amp;body=https://www.nngroup.com/articles/steering-law/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/steering-law/&amp;title=Accot-Zhai Steering Law: Implications for UI Design&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/steering-law/&amp;text=Accot-Zhai Steering Law: Implications for UI Design&amp;via=nngroup" data-share-type="Twitter">

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

</span>Dropdowns, hierarchical menus, sliders, or scroll bars involve steering a pointer or a cursor through a tunnel; optimal design for these GUI elements should consider the Steering Law.

</div>

<div class="article-body">

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

<a class="ga-article-toc-item" href="#toc-the-steering-law-1">The Steering Law</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-making-menus-steer-friendly-2">Making Menus Steer-Friendly</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-sliders-scrollbars-and-scrubbers-need-additional-controls-for-precision-3">Sliders, Scrollbars, and Scrubbers Need Additional Controls for Precision</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-be-generous-4">Be Generous</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-summary-5">Summary</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-references-6">References</a>

</li>

</ul>

</div>

</div><h2 id="toc-the-steering-law-1">The Steering Law</h2>

<p>The Accot-Zhai steering law (discovered by HCI researchers Johnny Accot and Shumin Zhai, but also known simply as the steering law) is a corollary of <a href="https://www.nngroup.com/videos/fittss-law/">Fitts’s Law</a>. The steering law is an equation that predicts the efficiency of very common interactions; it describes the particular case of path-steering tasks — that is, when a user must move a pointer through a path with boundaries or a “tunnel.” The equation is:</p>

<figure class="caption"><img alt="Accot-Zhai Steering Law equation, T = a+b(A/W)" height="137" loading="lazy" src="https://media.nngroup.com/media/editor/2019/05/31/steeringlawequation.png" width="391"/>

<figcaption>T <em>is the overall movement time, </em>a<em> and </em>b<em> are constants, A</em> <em>is the length of the tunnel, and </em>W<em> is the width of the tunnel.</em></figcaption>

</figure>

<p>Don’t worry, most UX professionals will never need to use this equation: the main actionable insight is that long, narrow tunnels take more time to navigate than short, wide tunnels.</p>

<blockquote>

<p style="margin-left:.5in">The steering law predicts the time necessary to steer a pointer (such as a mouse cursor) through a bounded tunnel (such as a menu, a scroll bar, or slider). The steering time depends on the length and the width of the tunnel: the longer and the narrower the tunnel, the more time will be required to successfully steer through it.</p>

</blockquote>

<p>According to the steering law, a <strong>tunnel</strong> is any user-interface control that requires the user to move the cursor (or drag a finger on a touchscreen) along a <strong>path that has borders</strong>. Overstepping the border will have some consequence, though since this is a common user error, the consequences will hopefully be mild, such as having the computer stop paying attention while the pointer is outside the tunnel. Some of the most common UI elements that involve this type of interaction include <a href="https://www.nngroup.com/articles/drop-down-menus/">dropdown menus</a> (particularly hierarchical menus with hover-revealed submenus), <a href="https://www.nngroup.com/articles/gui-slider-controls/">parameter-control sliders</a>, scroll bars, video-playback scrubber bars, and video-game elements that require drag and drop in a straight line.</p>

<figure class="caption"><img alt="YouTube's video scrubber playback control" height="212" loading="lazy" src="https://media.nngroup.com/media/editor/2019/05/31/video-scrubber.png" width="732"/>

<figcaption><em>On YouTube, the playback scrubber at the bottom of the video is an example of a tunnel that obeys the Steering Law.</em></figcaption>

</figure>

<p>In most cases, moving outside the tunnel boundaries interrupts the user action: for example, in a hierarchical dropdown menu, if the user moves the cursor outside the menu area, the menu disappears (which is a somewhat harsh penalty, if the tunnel breakage was unintentional). That is why the width of the tunnel is important for how easily the user can steer through — a narrow tunnel makes it easy to accidentally exit the tunnel area.</p>

<figure class="caption"><img alt="macOS hierarchical menu showing a path steering task with 90-degree turns" height="550" loading="lazy" src="https://media.nngroup.com/media/editor/2019/05/31/macos-lshape-menu.png" width="974"/>

<figcaption><em>On MacOS, moving the mouse cursor through a hierarchical menu involves a series of linear path-steering tasks separated by 90-degree turns. Within the main menu, submenus open on hover. Note that the second step in this L-shaped sequence (moving from </em>Find<em> to its child menu) involves the narrowest tunnel, which is slow and difficult for users to move through without errors.</em></figcaption>

</figure>

<figure class="caption"><img alt="macOS hierarchical menu showing typical user diagonal mouse movement patterns" height="550" loading="lazy" src="https://media.nngroup.com/media/editor/2019/05/31/macos-diagonal-menu.png" width="974"/>

<figcaption><em>Many users will attempt to move diagonally from </em>Find<em> to an item in the child menu, but, because in doing so their mouse will cross the area for </em>Spelling and Grammar<em>, the target submenu will be lost and instead the </em>Spelling and Grammar <em>one will be opened. (Note that older versions of MacOS featured a menu designed by NN/g principal Bruce Tognazzini; that menu did not exhibit this behavior, but instead, used a vector-based triangular buffer to allow users to move diagonally. Unfortunately, in the years since, Apple has reverted this excellent bit of interaction design.)</em></figcaption>

</figure>

<p>Why people have trouble maintaining the cursor on a straight path has to do with human physiology: the elbow and wrist, which enable the movement of the hand, describe an arc, not a line. Try it yourself: hold your arm out directly in front of you and move your hand from left to right. You’ll notice that, even if you attempt to keep it moving in a straight line, your arm will always have a subtle arc in the movement. As a result, using one’s hand to move in a long, straight line is physically difficult; the longer the motion, the greater the chance of error. Furthermore, many users (especially older adults and those with disabilities) have unsteady hands, and all mobile users are subject to the bumps and jitters of using a device out in the world.</p>

<h2 id="toc-making-menus-steer-friendly-2">Making Menus Steer-Friendly</h2>

<p>Menus are one of the UI elements most affected by the steering law. Here are a few design choices to make them easy to use.</p>

<p><strong>Keep <a href="https://www.nngroup.com/articles/drop-down-menus/">dropdown menus as short as possible</a>.</strong> Menus with few choices minimize the time and difficulty of steering through the narrow tunnel, and also reduces the time to <a href="https://www.nngroup.com/videos/hicks-law-long-menus/">visually search</a> through a large number of choices.</p>

<p><strong>Avoid hierarchical menus</strong>, particularly hierarchical menus that are more than two-levels deep. Hierarchical menus are inherently a difficult UI to design well due to Steering Law constraints. There will always be a tradeoff between designing the two tunnels associated with a hierarchical menu: the vertical tunnel that corresponds to the main-menu area and the horizontal tunnel, that corresponds to subcategory name that the user has to traverse to open the submenu:</p>

<ul>

<li>The vertical tunnel needs to be short, but that means that each of the items in the menu may have to be given smaller height — which leads to narrow horizontal tunnels.</li>

<li>The vertical tunnel must also be wide, but that leads to longer horizontal tunnels from main-menu option to the corresponding submenu.</li>

</ul>

<figure class="caption"><img alt="Two views of Costco.com hierarchical menus, showing the tradeoff in width vs height of menus" height="777" loading="lazy" src="https://media.nngroup.com/media/editor/2019/05/31/menu-width-optimization-zoom.png" width="1288"/>

<figcaption><em>This hierarchical menu on Costco.com shows the inherent tradeoff of optimizing a hierarchical menu for steering-law effects and compromising between the sizes of the vertical tunnel (left) and the horizontal tunnel (right). A wide menu optimizes the <strong>vertical</strong> tunnel for ease of steering down the menu, especially for menus with many choices. However, by making the menu wide, the length of the <strong>horizontal tunnel</strong> is increased, and moving across the menu to access the corresponding submenu is more fraught with errors. Note that most menus have not been optimized at all for the Steering Law, as they are simply made as wide as the longest text label.</em></figcaption>

</figure>

<p>When a hierarchical menu is absolutely necessary, use a short time delay between mouse hover and when reveal of the child menu (or use a vector-based triangular system to allow for some diagonal movement error). Also include as much padding as reasonably possible above and below each menu item, to increase the width of the tunnel for horizontal movement.</p>

<p>For navigation menus, consider<a href="https://www.nngroup.com/articles/mega-menus-work-well/"> mega menus</a> (or square menus) as an alternative to <a href="https://www.nngroup.com/articles/expandable-menus/">pull-down</a> menus. As mega menus allow for free movement within a wide 2D space, the steering law does not apply (though Fitts’s Law still does, so make sure targets are still large).</p>

<h2 id="toc-sliders-scrollbars-and-scrubbers-need-additional-controls-for-precision-3">Sliders, Scrollbars, and Scrubbers Need Additional Controls for Precision</h2>

<p>When designing other UI elements that involve path-steering tasks, such as sliders, scrollbars, and video playback heads, remember that users will have a hard time achieving precision with such controls. Therefore, for precise tasks, <a href="https://www.nngroup.com/articles/gui-slider-controls/">supplement these UI elements with other secondary controls that support precision.</a> When using a slider to select a parameter value, use the slider as a coarse control (for reaching the general desired region), and provide a secondary fine control (such as numeric input box with <a href="https://www.nngroup.com/articles/input-steppers/">stepper</a> buttons) to choose a specific value. Also, allow users to click anywhere on the slider to jump to the desired position, rather than requiring them to click and drag; this approach enables a user to move freely in 2D space without needing to steer through the tunnel. On touchscreens, think about the overall target size of the slider knob (it should be at least <a href="https://www.nngroup.com/articles/touch-target-size/">1cm x 1cm</a>) and ensure that the user’s finger won’t obscure the slider (or any labels around it).</p>

<h2 id="toc-be-generous-4">Be Generous</h2>

<p>Finally, you can add padding to a tunnel, making its effective width bigger than its visual representation on the screen. The padding will allow some wiggle room for the user to move along the tunnel without dropping out because of a small deviation outside the tunnel’s visual area.</p>

<h2 id="toc-summary-5">Summary</h2>

<p>The steering law states that narrow, long tunnels are more difficult to navigate than short, wide ones. Dropdown menus, hierarchical menus, sliders, and other path-following UI elements should be designed so that the corresponding tunnel is as wide and as short as possible. Remember that such controls are hard to use for precise tasks and consider alternatives (such as mega menus instead of dropdowns or secondary controls for sliders) to prevent errors due to linear path-steering interactions.</p>

<h2 id="toc-references-6">References</h2>

<p>Johnny Accot and Shumin Zhai. 1997. “Beyond Fitts' law: models for trajectory-based HCI tasks,” <em>Proceedings of CHI '97.</em></p>

<p>Sergey Kulikov, I. Scott MacKenzie, Wolfgang Stuerzlinger. 2005. “Measuring the Effective Parameters of Steering Motions,” <em>CHI '05 Extended Abstracts on Human Factors in Computing Systems</em>.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Human Computer Interaction,Interaction Design,menus,interfaces,research papers</span>

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