# Don’t Use Split Buttons for Navigation Menus - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">8</span>

<div class="article-header">

<h1 class="article-h1">Don’t Use Split Buttons for Navigation Menus</h1>

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

June 25, 2017

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2017-06-25</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Don’t Use Split Buttons for Navigation Menus&amp;body=https://www.nngroup.com/articles/split-buttons-navigation/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/split-buttons-navigation/&amp;title=Don’t Use Split Buttons for Navigation Menus&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/split-buttons-navigation/&amp;text=Don’t Use Split Buttons for Navigation Menus&amp;via=nngroup" data-share-type="Twitter">

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

</span>Menu on hover, category landing page on click: we discuss challenges and solutions for replicating this pattern on touchscreens.

</div>

<div class="article-body">

<p>Desktop sites with a rich information architecture often use both <a href="https://www.nngroup.com/articles/mega-menus-work-well/">mega menus</a> and <a href="https://www.nngroup.com/reports/ecommerce-ux-homepages-and-category-pages/">category landing pages</a> to implement navigation. Mega menus usually present a set of subcategories for a main navigation option, while the category landing pages contain a list of those subcategories plus additional content to better define the category for the user.</p>

<figure class="caption"><img alt="" border="0" height="381" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/15/nordstrom-combined.PNG" width="700"/>

<figcaption><em>Nordstrom.com: Hovering with the mouse on the </em>Women<em> category exposes the mega menu (left) with the associated subcategories. Clicking on the same label leads to the category landing page (right), which includes a list of </em>Women<em> subcategories plus additional content.</em></figcaption>

</figure>

<p>In many desktop designs, <strong>hovering with the mouse on a primary category often exposes the menu</strong>, while <strong>clicking the category takes users to that category’s landing page</strong>. But hover is a gesture not available on touchscreens, so designers must address this asymmetry when they scale their navigation UIs to work across many devices.</p>

<p>To reiterate, the challenge on touchscreens is to allow users to access both the category landing page and the menu in an environment where a single gesture is available to the user: the tap.</p>

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

<a class="ga-article-toc-item" href="#toc-split-buttons-for-navigation-1">Split Buttons for Navigation</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-why-split-buttons-dont-work-for-navigation-2">Why Split Buttons Don’t Work for Navigation</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-what-to-use-instead-of-split-buttons-3">What to Use Instead of Split Buttons?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-4">Conclusion</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-backstory-5">Backstory</a>

</li>

</ul>

</div>

</div><h2 id="toc-split-buttons-for-navigation-1">Split Buttons for Navigation</h2>

<p>The <strong>split button</strong> is a UI element familiar to desktop-application designers; it essentially amounts to having two buttons inside one. A split button consists of a label and a graphical element (most often, a downward-pointing triangle or “arrow”): clicking the label usually performs a default, frequent action, and clicking the arrow displays a <a href="https://www.nngroup.com/articles/drop-down-menus/">dropdown</a> with a set of choices for that action. For example, in Microsoft Word, the underline button is a split button: clicking on the label <strong><em><u>U</u></em></strong> underlines the text, and clicking on the arrow allows you to pick a different style for the underline.</p>

<figure class="caption"><img alt="" border="0" height="207" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/15/word-buttons.png" width="350"/>

<figcaption><em>Three buttons in Microsoft Word: The first two are icons that change the font style, and the third one is a split button. Clicking on the label underlines the current selection, while clicking the arrows displays a list of underline options.</em></figcaption>

</figure>

<p>This design works reasonably well in <a href="https://www.nngroup.com/courses/application-ux/">applications</a>. Even though novices may not understand the distinction between split buttons and regular buttons at first, as they continue using the application, they will eventually learn it. Plus, if the application is well designed and the default action associated to the button label is well chosen, most users may never need the choices provided in the dropdown menu. For example, regular underlines are used vastly more than double or stippled underlines, so the button for underlining in Microsoft Word will satisfy those users who don’t discover that it’s a split button.</p>

<p>After this short detour through the world of desktop-application design, let’s come back to our initial problem: providing access to both category landing pages and mega menus in the absence of hover. It may seem that split buttons provide an ideal solution to this problem: after all, they allow designers to provide two functionalities within the same design element. And indeed, this is exactly the solution employed by quite a few sites.</p>

<p>For example, on the mobile version of City of Cupertino <a href="https://www.nngroup.com/articles/responsive-web-design-definition/">responsive website</a>, tapping the arrows in the main-navigation menu expands that category, while tapping the label takes people to the category landing page. (The mobile site contains explicit instructions within the menu, to alert users to this behavior. Such instructional text is usually a warning sign that usability problems may be present.)</p>

<figure class="caption"><img alt="" height="622" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/15/cupertino.png" width="350"/>

<figcaption><em>Cupertino.org: Tapping on the </em>Business<em> category in the main navigation menu takes users to the category landing page, while tapping the corresponding arrow exposes subcategories of </em>Business<em>. (Note also the instructional text at the top of the navigation menu.)</em></figcaption>

</figure>

<figure class="caption"><img alt="" border="0" height="622" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/15/latimes.png" width="350"/>

<figcaption><em>LATimes.com: Tapping on the category labels inside the navigation menu leads to the category landing page, while tapping the arrow expands a scrolling accordion. Note that LA Times uses this solution for all screen sizes, including the desktop.</em></figcaption>

</figure>

<h2 id="toc-why-split-buttons-dont-work-for-navigation-2">Why Split Buttons Don’t Work for Navigation</h2>

<p>Unfortunately, split buttons are not a good solution to the problem of making both the category landing page and the menu available. There are several reasons for that:</p>

<ul>

<li><strong>Users are unfamiliar with split buttons for navigation</strong>. This pattern is rare on the web, where people don’t expect menu labels to do two different things. Moreover, in many mobile implementations (like in the LA Times and City of Cupertino examples above), the split button looks like an accordion: a standard UI element with well-known behavior. There is no reason to expect that one particular instance will behave differently than all the others on the web.

<p>Even though users of desktop applications eventually learn to use split buttons, most websites don’t have the same level of repeated use, so if your site is one of the few that use this pattern, chances are that people won’t discover it.</p>

<p>To make the split button more discoverable, some sites use a dividing line between the menu label and the arrow, as in the World of Tanks screenshot below. Although it may seem like a reasonable solution, the two targets (the menu label and the arrow) are too close together for touchscreen use due to the <a href="https://www.nngroup.com/articles/touch-target-size/">fat-finger problem</a>.</p>

</li>

</ul>

<figure class="caption"><img alt="" border="0" height="757" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/15/worldoftanks.PNG" width="700"/>

<figcaption><em>WorldofTanks.com: In the navigation bar, some of the primary categories </em>(Game<em>, </em>Clans<em>, </em>Media<em>, </em>Community)<em> are split buttons, with labels leading to corresponding category landing pages, and the arrows expanding pull-down menus. The dual functionality is signaled visually by the vertical separator between the label and the arrow. Unfortunately, on touchscreens the two targets are too close to each other and cannot be selected reliably.</em></figcaption>

</figure>

<p>Increasing discoverability by adding explicit instructional text (as in the City of Cupertino example above) does not work either: most users don’t bother reading explanations inside a menu. After all, they’ve already seen hundreds of menus and know how to use them!</p>

<ul>

<li><strong>Split buttons make the interface seem unpredictable</strong>. We’ve established above that users don’t expect labels and accompanying arrows to have different behaviors (in the same way that <a href="https://www.nngroup.com/articles/4-ios-rules-break/">they don’t expect the <em>Move</em> icon to do something else than the associated label</a>). Still, you may think that there will be no harm done if people don’t discover the dual functionality of these buttons. Most of the time category landing pages and menus contain roughly the same information, and getting to any one of the two will likely be good enough.

<p>Wrong! Although users will probably be able to achieve their goal whether they use the menu or the category landing page, they will be unpleasantly surprised when the site won’t behave as expected. When it comes to touch gestures, users are rarely precise or consistent: sometimes they will tap the arrow and sometimes tap the label, looking for the same result. If the interface does different things after two instances of (seemingly) the same user action, it will seem buggy and erratic.</p>

</li>

<li><strong>Close targets are hard to hit on touchscreens</strong>. Even if people recognized the split buttons in a navigation bar, chances are that they won’t be able to select the two functions reliably on a touchscreen. Whereas on mouse-driven interfaces split buttons may be fairly usable, it is too easy to make <a href="https://www.nngroup.com/articles/slips/">mistakes</a> and accidentally tap the wrong thing when the label and the arrow are too close to each other.</li>

</ul>

<h2 id="toc-what-to-use-instead-of-split-buttons-3">What to Use Instead of Split Buttons?</h2>

<p>If split buttons are problematic, what should designers do to support access to both category landing pages and menus on touchscreens? Here are a few alternatives:</p>

<ul>

<li><strong>Tapping a main category exposes the menu, but access to the category landing page is removed on touchscreens</strong>. Does the category landing page contain significant information, or does it simply replicate the contents of the menu? In the Nordstrom’s example from the beginning of the article, the category landing page does not bring any extra content that is not available elsewhere on the site. In situations like these, it is okay to simply not include a way to access this page in the navigation menu for touchscreen devices. (The link may be available elsewhere on the site.)

<p>Note that we don’t recommend the counterpart to this solution, which is to remove access to the menu on touchscreens. In theory, when users tap on a category item, they could simply be taken to the category landing page. From there, they could select the subcategory of interest. Although this pattern is encountered on the web (see the American Lung Association example below), we normally do not advise using it because it significantly slows down site navigation: each time people tap on a main category, they will have to wait for the corresponding category landing page to load before being able to select a subcategory of interest.</p>

<figure class="caption"><img alt="" border="0" height="500" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/15/lung1.PNG" width="747"/>

<figcaption><em>Lung.org: Hovering on a category in the top navigation bar exposes the corresponding menu. This menu is not accessible on touchscreens. Instead, when tapping the category, users are taken to the category landing page.</em></figcaption>

</figure>

</li>

<li><strong>Tapping a main category exposes the menu; to access the category landing page, provide a link to it inside the menu</strong>.<strong> </strong>This design allows users on all devices to access the category landing page.

<p>This is the solution adopted on HBO’s site. On a mouse-driven device, users can hover on the main categories to see a list of subcategories and can also click on them to go to the category landing page. On a touchscreen tablet, tapping on the items in the main navigation bar simply exposes the menu, allowing users to see the subcategories anywhere on the site. The section’s home is still available through a separate link available in the menu.</p>

<figure class="caption"><img alt="" border="0" height="766" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/15/hbo.PNG" width="700"/>

<figcaption><em>HBO.com: On desktop, hovering over a main navigation categories such as </em>Sports<em> shows the corresponding subcategories. Clicking on the category leads to that section’s landing page. On touchscreens, tapping on a main category exposes the menu. On both desktop and tablets, the category landing page can be accessed through the link labeled </em>Sports Home<em> inside the menu.</em></figcaption>

</figure>

<p>One advantage of this pattern is that designers can get rid of the hover on the desktop as well (displaying the menu on click instead) and can use a single design for both mouse and touchscreen devices. (Hover on desktop can also be problematic — for example, users may trigger menus accidentally while moving the mouse on the screen, or they may accidentally close a menu as they are trying to reach an item inside it.)</p>

<p>If you’re using this pattern, make sure that the link leading to the category landing page has a descriptive name such as <em>All Sports </em>or <em>View all</em> and avoid calling it simply <em>Home </em>(since that name is typically reserved for the site’s homepage).</p>

</li>

<li><strong>Use two taps: first for menu, second for category landing page. </strong>This third solution is used more and more and has a good chance of becoming a new standard for touch. When users first tap on a primary category, they see the submenu; when they tap again, they are taken to the category landing page. (This interaction style is very similar to the use of double-click in mouse-driven user interfaces, which works reasonably well.)

<figure class="caption"><img alt="" border="0" height="721" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/15/delta.PNG" width="700"/>

<figcaption><em>Delta.com: On a tablet, tapping once on </em>Traveling with US<em> expands shows a pull-down menu; tapping again takes users to the category landing page.</em></figcaption>

</figure>

<p>This design pattern is a good example of a mode: the same input (tapping on a category) produces two different outputs depending on the state of the system (it expands the menu if the menu is not already expanded, or it loads the category landing page if the menu is expanded).</p>

<p>However, in spite of its popularity, this solution has some flaws:</p>

<ul>

<li>Lack of discoverability: Users may not realize that they can access the category landing page by tapping again on the same primary category.</li>

<li>Conflict with another touchscreen pattern: Tapping the label of an open menu usually closes the menu. Users will be upset if, instead of dismissing the menu, they will need to wait for the site to load a category landing page that they don’t want.</li>

</ul>

</li>

</ul>

<h2 id="toc-conclusion-4">Conclusion</h2>

<p>If you’re struggling with making both the category landing page and the corresponding subcategories available on touchscreen devices, don’t go for the split menu button. While the solution may seem elegant, it doesn’t work well on touchscreens. Instead, you have three viable alternatives. The preferred and the most straightforward one involves including a link to the category landing page inside the associated menu. Or, show the menu on the first tap on the primary category and then load the category landing page on a second tap. Last but not least, if the category landing page is redundant with the menu, you can remove access to it on touchscreens.</p>

<h2 id="toc-backstory-5">Backstory</h2>

<p>The idea for this article was inspired by the BBC Sport website: tapping on the section menu on that site sometimes exposes the menu content and sometimes takes users to the <em>Sports</em> <em>A–Z</em> page. We initially thought that this behavior was an example of split menu, with the icon expanding the menu and the label linking to the category page. Yet the behavior seems to be quite erratic — sometimes clicking on the label actually expands the menu. We’re not sure if the current design contains a bug or was intended as such, but if the <em>All Sport </em>menu is indeed a split menu, we strongly recommend against replicating it.</p>

<figure class="caption"><img alt="" border="0" height="611" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/15/bbc-all.png" width="700"/>

<figcaption><em>BBC Sport: Tapping on the menu icon sometimes exposes the menu and sometimes takes users to the </em>Sports A–Z<em> page.</em></figcaption>

</figure>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">buttons,responsive design,Mobile &amp; Tablet,Navigation,graphical user interfaces,touch targets</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet</span>

<a class="ga-article-related-topic" href="/topic/mobile-and-tablet-design/">Mobile &amp; Tablet</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/navigation/">Navigation</a>

</li>

</ul>

</div>

</div>

</div>

</div>