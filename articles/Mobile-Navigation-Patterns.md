# Basic Patterns for Mobile Navigation - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Basic Patterns for Mobile Navigation: A Primer</h1>

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

November 15, 2015

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2015-11-15</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Basic Patterns for Mobile Navigation: A Primer&amp;body=https://www.nngroup.com/articles/mobile-navigation-patterns/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/mobile-navigation-patterns/&amp;title=Basic Patterns for Mobile Navigation: A Primer&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/mobile-navigation-patterns/&amp;text=Basic Patterns for Mobile Navigation: A Primer&amp;via=nngroup" data-share-type="Twitter">

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

</span>Mobile navigation must be discoverable, accessible, and take little screen space. Exposing the navigation and hiding it in a hamburger both have pros and cons, and different types of sites have different preferred solutions to the mobile-navigation quandary.

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

<a class="ga-article-toc-item" href="#toc-introduction-1">Introduction</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-the-navigation-bar-and-the-tab-bar-2">The Navigation Bar and the Tab Bar</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-the-hamburger-menu-and-variants-3">The Hamburger Menu (and Variants)</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-the-navigation-hub-4">The Navigation Hub</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-5">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-introduction-1">Introduction</h2>

<p><strong><a href="http://www.nngroup.com/articles/search-not-enough/">Navigation complements search</a></strong> for several reasons:</p>

<ul>

<li>sometimes users don’t know what to search for, and need help figuring out the partitioning of the search space;</li>

<li>coming up with a good query and typing it requires more mental effort and higher <a href="http://www.nngroup.com/articles/interaction-cost-definition/"><strong>interaction cost</strong></a> than <a href="http://www.nngroup.com/articles/recognition-and-recall/"><strong>recognizing</strong></a> and tapping a navigation link (and, in fact, <a href="http://www.nngroup.com/articles/incompetent-search-skills/"><strong>users are notoriously bad at formulating good queries</strong></a>);</li>

<li>site search often works a lot more poorly than the search-engines users expect it to.</li>

</ul>

<p>However, on mobile devices, both navigation and search come at a price: they occupy screen space and grab users’ attention, both of which are at an even higher premium on mobile than on desktop. If the screen space is really scarce, a search box or navigation links at the top of the page can interfere with the users’ ability to get to new information fast and may make the user work more. Pay attention to navigation and search, make them accessible and discoverable, but don’t forget one of the basic tenets of <a href="http://www.nngroup.com/articles/mobile-ux/"><strong>mobile usability</strong></a>: prioritize content over <a href="http://www.nngroup.com/articles/browser-and-gui-chrome/"><strong>chrome</strong></a>. This is in fact one of the big challenges of implementing navigation on mobile: <strong>how to prioritize content while making navigation accessible and discoverable.</strong> Different approaches sacrifice either content prioritization or the accessibility of the navigation.</p>

<h2 id="toc-the-navigation-bar-and-the-tab-bar-2">The Navigation Bar and the Tab Bar</h2>

<h3>Top Navigation Bar</h3>

<p><strong>The top navigation bar </strong>is essentially inherited from desktop design. It is simply a bar that enumerates the main navigational options across the top of the screen. This is quite efficient, but has two disadvantages: (1) it works well only when there are relatively few navigation options; (2) it takes up valuable <a href="http://www.nngroup.com/articles/page-fold-manifesto/"><strong>real estate above the fold</strong></a>.</p>

<figure class="caption"><img alt="Washington Post homepage and Google Play Apps Page" height="549" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/09/22/nav-bar.png" width="650"/>

<figcaption><em>The BBC’s website (left) and Google Play for Android (right) both used a top navigation bar for the main navigation. Google Play was able to fit more items in the navigation bar by using a carousel.</em></figcaption>

</figure>

<h3>The Tab Bar</h3>

<p><strong>The tab bar </strong>is a close relative of the top navigation bar specific to apps. It can appear at the top (Android mostly) or at the bottom of the page (iOS mostly). It is usually present on most pages within an app and has the same disadvantages as the navigation bar. One important difference between tab bars and navigation bars is that tab bars are <strong>persistent,</strong> that is, they are always visible on the screen, whether the user scrolls down the page or not. Navigation bars usually start out being present at the top of the page but disappear once the user has scrolled one or more screens down. (A <strong>sticky version of the navigation</strong> bar stays put at the top of the screen, or as the user starts scrolling up, reappears at the top of the page.)</p>

<figure class="caption"><img alt="Facebook newsfeed on iOS and Android" height="567" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/09/22/facebook.png" width="650"/>

<figcaption><em>Facebook on iPhone (left) and Android (right) used a tab bar for the main navigation options. The tab was positioned in accordance with official operating-systems guidelines: at the bottom on iPhone and at the top of the page on Android. Note that the icons are labeled on the left screenshot: a recommended best practice in most cases.</em></figcaption>

</figure>

<p><strong>Tab bars and navigation bars are well suited for sites with relatively few navigation options.</strong> If your site has more than 5 options, it’s hard to fit them in a tab or navigation bar and still keep an optimum <a href="https://www.nngroup.com/articles/touch-target-size/">touch-target size</a>. Solutions such as using a <a href="http://www.nngroup.com/articles/designing-effective-carousels/"><strong>carousel</strong></a> navigation bar or tab bar, like in the Google Play example at the beginning of the article, may work but they are not always appropriate. Out of sight is out of mind, and if the categories are widely different (like the case of an older version of Weather Channel illustrated below), it’s likely that users won’t think to scroll to get to those options, simply because the weak information scent from the visible categories may prevent them from guessing what items are hidden.</p>

<figure class="caption"><img alt="Old version of Weather Channel" height="509" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/09/22/weather1.png" width="640"/>

<figcaption><em>An older version of Weather Channel for Android had a carousel tab bar at the bottom of the screen; the categories in the carousel were not similar or predictable, and thus the ones that were not visible had little discoverability.</em></figcaption>

</figure>

<p><strong>If you decide to use a navigation bar or a tab bar, they should be the main chrome area of the screen and little extra space should be devoted to other </strong><a href="http://www.nngroup.com/articles/utility-navigation"><strong>utility-navigation</strong></a><strong> options or to search. </strong>If the site has 4–5 main navigation options, it may make sense to have them all visible on the screen at all times, especially if these are options that will likely be needed. However, keep in mind that navigation needs to be judged in the context of the overall chrome on a page: even if a site may only have a few top-tier categories, if other utility-navigation links (e.g., shopping cart, account information) and search must also be included, the overall chrome may add up wasting too much space on the page.</p>

<figure class="caption"><img alt='Autozone search results page for "sparks"' height="482" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/09/22/autozone1.png" width="400"/>

<figcaption><em>Autozone.com: Although the site only had 4 main-navigation categories (</em>Shop, Repair Help, Deals<em>, and </em>Find Store<em>), there were a lot more chrome elements present on the page (logo, shopping cart, </em>My Zone<em> link, search box) that all occupied too large an area.</em></figcaption>

</figure>

<h2 id="toc-the-hamburger-menu-and-variants-3">The Hamburger Menu (and Variants)</h2>

<p><strong>The navigation menu</strong> is a menu that contains the main navigation options in a manner that usually hides the detailed options but makes them visible upon request. While the hamburger icon is perhaps the most talked-about signifier for a navigation menu, other labels and/or <a href="http://www.nngroup.com/articles/icon-usability/"><strong>icons</strong></a> can be used for navigation. (In fact, <a href="http://exisweb.net/menu-eats-hamburger"><strong>third-party research</strong></a> seems to suggest that using the word <em>Menu </em>instead of the hamburger icon is slightly more popular with users.) The main advantage of the navigation menu is that it can contain a fairly large number of navigation options in a tiny space and can also easily support submenus, if needed; the disadvantage is that it is less discoverable, since, as the old adage says, “out of sight is out of mind.”</p>

<figure class="caption"><img alt="USA Today homepage and menu contents" height="545" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/09/22/usatoday.png" width="640"/>

<figcaption><em>A hamburger menu was used for the global navigation options on USAToday.com.</em></figcaption>

</figure>

<p>A version of the navigation menu is when the menu has no signifier and is discovered through a gesture. In the Sephora app, on deep pages the menu can be accessed by swiping horizontally on the left edge (a gesture that is problematic in iOS, since, from iOS 7 on, Apple has started pushing the horizontal swipe as <em>Back</em>).</p>

<figure class="caption"><img alt="Sephora deep page and content of menu" height="516" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/09/22/sephora-swipe.png" width="640"/>

<figcaption><em>Sephora for iPhone: There was no visible menu button, but a horizontal swipe on the left edge exposed the menu. Most users would never discover this feature and would restrict themselves to using the visible options</em>.</figcaption>

</figure>

<p><strong>The <a href="https://www.nngroup.com/articles/hamburger-menus/">navigation menu makes the navigation options least discoverable</a> and is best suited for content-heavy, browse-mostly sites and apps.</strong></p>

<p>If users rarely care about navigating to specific sections of the site and are mostly content to digest whatever information is presented to them (as is often the case on news sites), then a navigation menu is appropriate. The navigation menu also has the advantage of stealing a minimum amount of space from content, which is the star of browse-mostly sites.</p>

<p>However, keep in mind that when navigation is hidden under a menu, even though that menu as a whole may be salient enough, users will have to make a decision to open it and check whether the individual navigation options are relevant. While the navigation menu is becoming standard and many mobile users are familiar with it, many people still simply don’t think to open it. Even users who tried the navigation menu at some point during a session may not remember to do so later on.</p>

<p>If you decide to use a navigation menu, you need to think seriously about <a href="http://www.nngroup.com/articles/support-mobile-navigation/"><strong>supporting navigation in other ways</strong></a>, such making the IA structure of your site more discoverable by increasing the cross-section links.</p>

<h2 id="toc-the-navigation-hub-4">The Navigation Hub</h2>

<p><strong>The navigation hub </strong>is a page (usually the homepage) that lists all the navigation options. To navigate to a new location, users have to first go back to the hub and then use one of the options listed there. This navigation approach usually devotes the homepage exclusively to navigation (at the expense of content), and incurs an extra step (back to the hub) for each use of the navigation. <strong>It can work well in task-based websites and apps, especially when users tend to limit themselves to using only one branch of the navigation hierarchy during a single session. </strong></p>

<p>With the homepage as navigation hub, prime real estate will be wasted for chrome and all navigation will have to go through the homepage. While these two may seem as major disadvantages (and they are for most types of sites or apps), they can be less of a problem for those sites and apps used not for browsing and consuming content, but for accomplishing a very specific task (for example, checking in for a flight or changing the settings of the phone). Such sites and apps can take advantage of the homepage-as-navigation-hub pattern, especially if users rarely accomplish more than one task during a single session, and thus they don’t need to traverse the navigation tree often (an action that is relatively difficult and annoying if all navigation must go through the homepage).</p>

<figure class="caption"><img alt="United homepage and flight-search page" height="550" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/09/22/united.png" width="640"/>

<figcaption><em>United used the homepage as a navigation hub. On deep pages, users had to use the on-page </em>Home<em> button to go back to the homepage if they wanted to select a different navigation option.</em></figcaption>

</figure>

<p>In the United example above, most likely you want to <em>either</em> buy a ticket <em>or</em> check in for a flight, but not do both in a single session. Thus, most users won’t have to return to the hub in this example, meaning that it rather serves as an efficient distribution point.</p>

<h2 id="toc-conclusion-5">Conclusion</h2>

<p>Making navigation important and accessible is a challenge on mobile due to the limitations of the small screen and to the need of prioritizing the content over the UI elements. Different basic navigation patterns attempt to solve this challenge in different ways that all suffer from a variety of usability problems. The key is to pick the type of mobile navigation where the (inevitable) downsides will hurt your users the least for the kinds of tasks they are most likely to perform on your site:</p>

<ul>

<li>Hamburger menus accommodate a large number of options, but these options are less discoverable. They are particularly well suited for browse-mostly sites.</li>

<li>Navigation bars and tab bars take space on the page, and work well when the number of navigation options is small.</li>

<li>Sites that are primarily task oriented can use a homepage-as-navigation-hub pattern.</li>

</ul>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Mobile User Experience" href="/courses/usability-mobile-websites-apps/?lm=mobile-navigation-patterns&amp;pt=article">

<h4 class="title heading-small">Mobile User Experience</h4>

<p id="mobile-user-experience" class="description body-small">

Essential UX design principles for small-screen websites and apps

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-interaction" />

</svg>

<p class="ux-specialty interaction-design">Interaction</p>

</div>

</div>

</a>

</li>

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">mobile navigation,Mobile &amp; Tablet,Navigation,Design Patterns</span>

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

<li>

<a class="ga-article-related-topic" href="/topic/design-patterns/">Design Patterns</a>

</li>

</ul>

</div>

</div>

</div>

</div>