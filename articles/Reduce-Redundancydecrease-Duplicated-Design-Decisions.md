# Reduce Redundancy: Decrease Duplicated Design Decisions - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">2</span>

<div class="article-header">

<h1 class="article-h1">Reduce Redundancy: Decrease Duplicated Design Decisions</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Jakob Nielsen</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Jakob-Nielsen-tie-800x800.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/jakob-nielsen/">

Jakob Nielsen</a></span>

<p class="publication-date">

June 8, 2002

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2002-06-08</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Reduce Redundancy: Decrease Duplicated Design Decisions&amp;body=https://www.nngroup.com/articles/reduce-redundancydecrease-duplicated-design-decisions/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/reduce-redundancydecrease-duplicated-design-decisions/&amp;title=Reduce Redundancy: Decrease Duplicated Design Decisions&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/reduce-redundancydecrease-duplicated-design-decisions/&amp;text=Reduce Redundancy: Decrease Duplicated Design Decisions&amp;via=nngroup" data-share-type="Twitter">

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

</span>User interface complexity increases when a single feature or hypertext link is presented in multiple ways. Users rarely understand duplicates as such, and often waste time repeating efforts or visiting the same page twice by mistake.

</div>

<div class="article-body">

<p>The article title above is a perfect example of its point: The title <strong> says the same thing twice</strong>. In addition to being too long, it's harder to read than a simple headline like: <em> Do Each Thing Once. </em> Would that it were the only example of its kind. Unfortunately, the problem is widespread.</p>

<p>Take, for example, Microsoft Word. Among its myriad features are both footnotes and endnotes. Furthermore, you can place the footnotes at the bottom of the page or "below the text" (whatever that means) and you can place endnotes at either the end of a section or the end of a document. There is also a feature to convert the footnotes to endnotes and the endnotes to footnotes.</p>

<p>Some authors might well find footnotes and endnotes useful, but the features are offered at the cost of complicating the simple footnote feature. As it stands, to insert a footnote, you face a confusing dialog box with two radio buttons, five pull-down menus, a text-entry field, a counter, and two buttons that bring up additional dialog boxes. Luckily, Microsoft followed a key usability guideline — use appropriate defaults for all dialog box elements — and you can thus ignore the dialog box and hit the enter key. This gives you a normal footnote, just as if you'd been using good old Word 1.05 sixteen years ago.</p>

<p>Unfortunately, many users will be intimidated by the elaborate choices. As is too often the case, <strong> each new feature made the old features more difficult and error-prone</strong>.</p>

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

<a class="ga-article-toc-item" href="#toc-simplicity-1">Simplicity</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-good-redundancy-alternative-navigation-paths-2">Good Redundancy: Alternative Navigation Paths</a>

</li>

</ul>

</div>

</div><h2 id="toc-simplicity-1">Simplicity</h2>

<p>Simplicity may be the single most important usability guideline. The less stuff you show users, the less they'll have to scan and comprehend, and the better the odds that they'll pick the correct option at any given stage. Duplicating features adds significant overhead to both the scanning process and the comprehension process.</p>

<p>Furthermore, because users don't <em> know </em> for sure when a feature is duplicated, they'll have to spend additional time <strong> figuring out whether the duplicate is a new feature or an old feature</strong>. In user testing, we frequently observe users clicking a second link to a page, even though they'd already visited that page earlier through a different link. Wasted effort.</p>

<p>Developers typically add <a href="https://www.nngroup.com/articles/duplicate-links/">duplicate links</a> with the best of intentions, often after usability results show that users overlooked certain links. Unfortunately, this treats the symptom rather than the disease, and does so in a manner that makes the patient more ill.</p>

<p>If users overlook a link, you can move it or make it more prominent rather than duplicate it. However, a truer solution might be to downplay other distracting design elements.</p>

<p>To achieve simplicity and improve usability, the approach opposite of duplication often works best: Remove features and links that are less important to users. Personalization, for example, used to be about displaying <strong> more information</strong>. On mobile devices, however, personalization will be about <strong> reducing choices </strong> to only those that the individual user needs at a given time.</p>

<h2 id="toc-good-redundancy-alternative-navigation-paths-2">Good Redundancy: Alternative Navigation Paths</h2>

<p>One of the few cases where users actually benefit from a small amount of redundancy is in the <strong> navigational paths through an information architecture</strong>. It is not always best to restrict users to a single route to a given destination.</p>

<p>Consider an example task from one of our <a class="old" href="/reports/ecommerce-user-experience/" title="Nielsen Norman Group: 207 design guidelines for ecommerce usability"> e-commerce usability</a> studies: Visit an e-commerce site and buy a baby seat for your car. Some users might assume the seat was a car product, since they'd be installing it in their car. If so, they'd never find it on the site we tested, because car seats for babies were considered baby products and found only in that area of the site.</p>

<p>It's impossible to design a perfect information architecture in which all users associate each item with a single category and take the one and only true path to the destination every time. Can't be done. A few <strong> cross-reference links </strong> on opportune pages are a lifesaver and can stop garden-pathing before users give up.</p>

<p>Still, too many cross-references will create an overly complex interface and prevent users from understanding where they are and what options they have at that location. It's thus essential to limit cross-references to those alternatives that are both most important to users at their current location and most likely to help them overcome navigational dislocation.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Navigation,complexity</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Navigation</span>

<a class="ga-article-related-topic" href="/topic/navigation/">Navigation</a>

</li>

</ul>

</div>

</div>

</div>

</div>