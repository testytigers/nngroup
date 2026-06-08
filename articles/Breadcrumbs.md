# Breadcrumbs: 11 Design Guidelines for Desktop and Mobile - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Breadcrumbs: 11 Design Guidelines for Desktop and Mobile</h1>

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

December 23, 2018

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2018-12-23</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Breadcrumbs: 11 Design Guidelines for Desktop and Mobile&amp;body=https://www.nngroup.com/articles/breadcrumbs/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/breadcrumbs/&amp;title=Breadcrumbs: 11 Design Guidelines for Desktop and Mobile&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/breadcrumbs/&amp;text=Breadcrumbs: 11 Design Guidelines for Desktop and Mobile&amp;via=nngroup" data-share-type="Twitter">

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

</span>Support wayfinding by including breadcrumbs that reflect the information hierarchy of your site. On mobile, avoid using breadcrumbs that are too tiny or wrap on multiple lines.

</div>

<div class="article-body">

<p>Breadcrumbs are an important navigational element that supports <strong>wayfinding</strong> — making users aware of their current location within the hierarchical structure of a website. Breadcrumbs are a list of links representing the current page and its “ancestors” (parent page, grandparent page, and so on), typically going all the way back to the site homepage. NN/g has been recommending breadcrumbs since <a href="https://www.nngroup.com/articles/breadcrumb-navigation-useful/">1995</a>, as they provide many benefits to users at almost no cost to the UI.</p>

<p>Breadcrumbs are represented as a trail of links at the top of the page, usually just below the global navigation; the home page (or root node of the hierarchy) is the first link and the links are usually separated by the symbols “&gt;” or “/”.  We recommend the “&gt;” character, though there is no functional difference, and either is acceptable.</p>

<figure class="caption"><img alt="REI breadcrumb trail showing the hierarchy of the site" height="489" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/16/rei-breadcrumb-trail.png" width="974"/>

<figcaption><em>REI.com: A breadcrumb trail <strong>(1)</strong> is displayed in its typical location at the top of the page, just below the global navigation bar. The trail shows the location of the current page within the hierarchy of the site. Each item in the breadcrumb trail is a link to an ancestor page; the “&gt;” character separates the breadcrumbs. In this example, the home page and current page are omitted from the breadcrumb trail, which is not recommended.</em></figcaption>

</figure>

<p>If users reach a deep page after traveling from the homepage through all the ancestor pages of that page, they will have a fairly clear understanding of where they are in the site’s information hierarchy. But when they skip some of these levels (for example, because they arrived to the site by clicking on an external link such as a search-engine result), breadcrumbs orient them and help them find their way to other, possibly more relevant, pages.</p>

<p>A deep page typically shows content on a relatively narrow, specific topic, but the breadcrumb trail can lead users to more-general content in the current page’s parent and grandparent nodes.</p>

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

<a class="ga-article-toc-item" href="#toc-guidelines-for-using-breadcrumbs-on-desktop-1">Guidelines for Using Breadcrumbs on Desktop</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-guidelines-for-using-breadcrumbs-on-mobile-2">Guidelines for Using Breadcrumbs on Mobile</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-summary-3">Summary</a>

</li>

</ul>

</div>

</div><h2 id="toc-guidelines-for-using-breadcrumbs-on-desktop-1">Guidelines for Using Breadcrumbs on Desktop</h2>

<ol>

<li><strong>Breadcrumbs should not replace the global navigation bar or the local navigation within a section.</strong></li>

</ol>

<p>Breadcrumbs are intended to <em>supplement</em> other navigational components, such as a global navigation bar that stretches across the top of every page or a local navigation bar that is often found on the left hand side. Breadcrumbs augment but do not replace those main forms of navigation.</p>

<figure class="caption"><img alt="Unusual breadcrumb that includes a drop down menu" height="1278" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/16/south-dakota-breadcrumbs-combined.png" width="1106"/>

<figcaption><em>Travelsouthdakota.com displays a breadcrumb trail that also serves as section navigation. Instead of a traditional breadcrumb trail (which would be: Home /Explore /Itineraries / Cultural Immersion), the breadcrumb trail includes a tier-1 item (Explore) and the parent page (Itineraries). The link to the parent page is a <a href="http://www.nngroup.com/articles/drop-down-menus/">dropdown menu</a>, with the current page’s siblings (bottom image). A better design would  have a separate UI for the local navigation, to enable users to travel to lateral pages in the current section of the site.</em></figcaption>

</figure>

<ol>

<li value="2"><strong>Breadcrumbs should display the current location in the site’s hierarchical structure, not the session history.</strong></li>

</ol>

<p>Breadcrumbs are not intended to show the history of pages traversed during a session on the site (<em>a la</em> a browser’s native <em>Back</em> button); they are intended to show the hierarchical structure of the site. We’ve noted this for many years, but it still bears repeating; attempting to show a list of the pages a user has accessed, in order, will quickly become long and confusing, with a lot of repetition, and won’t provide any benefit for users who arrive on a deep page directly from an external link, which is one of the key uses of breadcrumbs.</p>

<ol>

<li value="3"><strong>For polyhierarchical sites, breadcrumbs should show a single pathway in the site’s polyhierarchy.</strong></li>

</ol>

<p>Breadcrumbs pose an inherent tension with <a href="https://www.nngroup.com/articles/polyhierarchy/">polyhierarchical</a> sites (in which a page has more than one parent). In such situations, we do not recommend showing two or more breadcrumb trails reflecting the different paths in the polyhierarchy, because they will confuse users and take a lot of space at the top of the page.</p>

<p>If a page has multiple different parents, identify a canonical path to it in the site hierarchy and  show that path in  the breadcrumb trail. Don’t attempt to personalize the breadcrumb trail so that it will reflect each user’s individual path within the site hierarchy, because you will end up sending mixed signals to search engines. And you will still need to designate one path in the hierarchy as the primary trail for those visitors coming from an external link.</p>

<ol>

<li value="4"><strong>Include the current page as the last item in the breadcrumb trail.</strong></li>

<li value="5"><strong>In the breadcrumb trail, the breadcrumb corresponding to the current page should not be a link. </strong></li>

</ol>

<p>You should never have a link that does nothing. The last breadcrumb (denoting the current page) should not be a link. To avoid confusing users, visually differentiate between the current page and the preceding linked breadcrumb items, preferably using underlined or blue text.</p>

<figure class="caption"><img alt="Breadcrumb with no visual differentiation between linked and unlinked items" height="462" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/16/british-red-cross-breadcrumb.png" width="974"/>

<figcaption><em>On the British Red Cross site, there is no visual differentiation between the breadcrumbs that are links and the </em>Volunteer in emergencies<em> item, which is (correctly) not a link.</em></figcaption>

</figure>

<ol>

<li value="6"><strong>Breadcrumbs should include only site pages, not logical categories in your IA.</strong></li>

</ol>

<p>Each node in the breadcrumb trail should be a link to an ancestor page (with the important exception of the link corresponding to the current page, as noted above). If some of the subcategory labels in the global navigation don’t have a separate page dedicated to them do not include these subcategories in the breadcrumb trail.</p>

<p>The ability to “click-and-go” is a crucial part of users’ understanding of breadcrumbs, so all items (except the current page) should represent a place the user can go to.</p>

<figure class="caption"><img alt="Breadcrumb that doesn't include logical categories from the navigation that aren't distinct pages of their own" height="1362" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/16/new-egg-breadcrumbs-combined.png" width="625"/>

<figcaption><em>Newegg.com: The global-navigation megamenu (top) has subcategories that don’t have a page of their own — for example, </em>Commercial Networking <strong>(</strong><em><strong>1)</strong>. On the Wired Networking page (bottom), the breadcrumb trail <strong>(2)</strong> does not include </em>Commercial Networking<em>, because that subcategory does not have an associated page.</em></figcaption>

</figure>

<ol>

<li value="7"><strong>Breadcrumbs aren’t necessary (or useful) for sites with flat hierarchies that are only 1 or 2 levels deep, or sites that are linear in structure.</strong></li>

</ol>

<p>For sites with  flat hierarchies with only 1 or 2 levels of categories, a breadcrumb isn’t needed as a wayfinding device. In this case, consider clearly indicating the top-level section or the category that the page lives within.</p>

<figure class="caption"><img alt="Website with a flat hierarchy that doesn't need breadcrumbs" height="491" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/16/mit-flat-hierarchy.png" width="974"/>

<figcaption><em>MIT’s main website has a flat hierarchy, with only 1 page in each section. While it features a breadcrumb at the top of the page, this breadcrumb isn’t necessary. In the main navigation, the location of the page is highlighted.</em></figcaption>

</figure>

<figure class="caption"><img alt="Linear navigation site with no need for a breadcrumb" border="0" height="581" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/16/npr-color-story.png" width="974"/>

<figcaption><em>NPR features a minisite about the history of color, which is designed as a linear experience, where users will encounter each page in order. This site’s structure is nonhierarchical, and so there is no need (or value) in including a breadcrumb trail.</em></figcaption>

</figure>

<ol>

<li value="8"><strong>Breadcrumb trails should start with a link to the homepage</strong>.</li>

</ol>

<p>Much like our <a href="https://www.nngroup.com/articles/homepage-links/">guidelines</a> for global navigation, links to the homepage (labeled <em>Home</em>) are still necessary. However, note that duplicating the <em>Home</em> link in both the global navigation and the breadcrumb trail is <em>not</em> recommended — one or the other is fine.</p>

<figure class="caption"><img alt="Breadcrumb including a home link in both the navigation and breadcrumb" height="518" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/16/oregon-breadcrumb.png" width="974"/>

<figcaption><em>The Oregon state government website includes a breadcrumb trail, but omits a link to the homepage. However, in this case this is acceptable, as the site also includes a Home link in the global navigation — duplicating that homepage link is not necessary, but it does need to be shown in one of the two places.</em></figcaption>

</figure>

<h2 id="toc-guidelines-for-using-breadcrumbs-on-mobile-2">Guidelines for Using Breadcrumbs on Mobile</h2>

<p>Unfortunately, on mobile, the cost of using breadcrumbs can quickly overwhelm the benefits.</p>

<ol>

<li value="9"><strong>Don’t use breadcrumbs that wrap to multiple lines.</strong></li>

</ol>

<p>On mobile sites, breadcrumbs can quickly wrap to multiple lines, and  eat up valuable space on an already crowded mobile display. A multiline breadcrumb trail does not illustrate the structure of the chain well (particularly when some items take up their own line, and others may have two or more links in a single row)</p>

<p> </p>

<figure class="caption"><img alt="Breadcrumb on a mobile site that is so large it pushes the page title below the fold" height="674" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/16/rei-mobile-breadcrumb.png" width="312"/>

<figcaption><em>REI.com’s mobile site uses so much real estate for the breadcrumb trail that it pushes the name of the product <a href="http://www.nngroup.com/articles/page-fold-manifesto/">below the fold</a>, even on a large mobile device (in this case, an iPhone X).</em></figcaption>

</figure>

<ol>

<li value="10"><strong>Don’t use breadcrumbs that are too small or too crowded together.</strong></li>

</ol>

<p>Some sites attempt to get breadcrumbs take less screen space by making the links smaller or closer together. Unfortunately, this solution doesn’t work on touchscreens: <a href="https://www.nngroup.com/articles/touch-target-size/">tap targets need to be at least 1 cm X 1 cm</a>.</p>

<ol>

<li value="11"><strong>Consider shortening the breadcrumb trail to include only the last level(s).</strong></li>

</ol>

<p>On some pages, a single breadcrumb pointing up a level may be all that is necessary to support the main user goals. For example, on an ecommerce site, if a user lands on a product-detail page (via a Google search, for example), she may wish to see other product options in that same category to comparison shop, so a breadcrumb linking up to the parent level in the hierarchy can support this common task. This solution avoids a long, crowded breadcrumb trail that eats up precious mobile real estate.</p>

<p>Note that this advice conflicts with guideline #8, and should only be done on mobile. On desktop — where there’s more room — always show the full trail.</p>

<figure class="caption"><img alt="Mobile breadcrumb compared with a desktop breadcrumb, where the mobile shows only the last tier in the hierarchy" height="988" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/16/best-buy-breadcrumb-combined.png" width="705"/>

<figcaption><em>Bestbuy.com: The mobile site (top) showed a truncated breadcrumb trail <strong>(1)</strong>, allowing access up to the immediate parent category. The desktop site (bottom) presented the full breadcrumb trail <strong>(2)</strong>. This compromise on mobile supports some wayfinding, but avoids taking up precious real estate.</em></figcaption>

</figure>

<h2 id="toc-summary-3">Summary</h2>

<p>Breadcrumbs are a secondary form of navigation that assists users in getting to content nearby in the hierarchical structure. They are especially useful when users arrive to the site through an external link and don’t start with the homepage. Ensure that all items in the breadcrumb trail are links and that each individual node gets more specific as you progress down into the site. On mobile, breadcrumbs can take up too much space or can be hard to tap; consider shortening the breadcrumb trail if your users’ tasks allow it. </p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Information Architecture" href="/courses/information-architecture/?lm=breadcrumbs&amp;pt=article">

<h4 class="title heading-small">Information Architecture</h4>

<p id="information-architecture" class="description body-small">

Organize and structure information to improve findability and discoverability

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Information Architecture,Navigation,Visual Design,responsive design,screen size</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Information Architecture</span>

<a class="ga-article-related-topic" href="/topic/information-architecture/">Information Architecture</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/navigation/">Navigation</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/visual-design/">Visual Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>