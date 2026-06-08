# Users&#x27; Pagination Preferences and &quot;View All&quot; - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">3</span>

<div class="article-header">

<h1 class="article-h1">Users&#x27; Pagination Preferences and &quot;View All&quot;</h1>

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

April 28, 2013

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2013-04-28</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Users&#x27; Pagination Preferences and &quot;View All&quot;&amp;body=https://www.nngroup.com/articles/item-list-view-all/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/item-list-view-all/&amp;title=Users&#x27; Pagination Preferences and &quot;View All&quot;&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/item-list-view-all/&amp;text=Users&#x27; Pagination Preferences and &quot;View All&quot;&amp;via=nngroup" data-share-type="Twitter">

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

</span>Long listings might need pagination by default, but if users customize the display to View All list items, respect that preference.

</div>

<div class="article-body">

<p><strong>Pagination</strong> is a necessary evil when you have too many items to easily show them all on one screen. <strong>Linear content flows</strong> — such as articles like this — should almost <strong>never be broken up</strong> into multiple screens. It’s better to show the full article on one long screen than to inflict the pain of additional steps on users when all they want to do is read an article, and thus stay within that one item.</p>

<p>Where pagination comes in handy is for <strong>listings</strong>, such as <a href="https://www.nngroup.com/reports/ecommerce-ux-homepages-and-category-pages/" title="E-commerce User Experience Design Guidelines, Vol. 02: Homepages and Category Pages - Nielsen Norman Group report">ecommerce category pages</a>, search engine results pages (SERPs), article archives, and photo galleries. Here, a user’s goal is not to peruse the full list, but rather to find a specific item and click through to that destination page.</p>

<p>Assuming that you can <a href="https://www.nngroup.com/articles/prioritize-good-content-bubbles-to-the-top/" title="Prioritize: Good Content Bubbles to the Top">prioritize the list items</a>, users are likely to find what they want close to the top. To focus users’ attention and improve response time, you can start by showing a fairly short list, and then offer pagination options for progressing further down the list if needed.</p>

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

<a class="ga-article-toc-item" href="#toc-view-all-items-1">View All Items</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-view-n-items-2">View N Items</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-customization-3">Customization</a>

</li>

</ul>

</div>

</div><h2 id="toc-view-all-items-1"><em>View All </em>Items</h2>

<p>Many users like to see all options on a single page, rather than clicking from page to page looking at products. In user testing, we’ve often found a <em>View All</em> option to be helpful to some users. More important, the <em>View All</em> option didn’t bother users who didn’t use it; <strong>when it wasn’t offered, however, some users complained</strong>.</p>

<p><em>View All</em> is particularly important for <strong>lists that cannot be sorted well</strong>, as well as for items that are more a question of individual taste than of specific attributes. In domains such as fashion, art, flowers, and even chocolates, users might well prefer to scan many items than to be limited to a few per page.</p>

<p>As useful as <em>View All</em> is, however, there should be an upper limit to the number of items displayed. Large databases can easily generate thousands — even millions — of hits for certain queries, and it doesn’t make sense to produce listings that stretch that long.</p>

<p>Typically, this upper limit should be around <strong>100 items</strong>, though it can be more or less depending on how easy it is for users to scan items and how much a long page impacts the <a href="https://www.nngroup.com/articles/website-response-times/" title="Website Response Times">response time</a>.</p>

<p><em>View All</em> is usually better than the <a href="https://www.nngroup.com/articles/infinite-scrolling/" title="Infinite Scrolling Is Not for Every Website">annoying infinitely scrolling web pages</a> that keep loading new stuff when you approach the bottom, because these pages don't give users a sense of closure or power over the navigation. For the same reasons, pagination is usually better than infinite scrolling if there are too many items to display on a reasonably long page.</p>

<h2 id="toc-view-n-items-2"><em>View N</em> Items</h2>

<p>Many sites let users choose how many items they’ll see on each page. This is often overkill, as when pop-up menus let users <em>View 10, 20, 30, 40</em> items per screen.</p>

<p>It’s usually better to <strong>offer a single default number</strong> — such as 10 or 20 — and supplement it with <em>View All</em> for people who want more. Instead of a pop-up menu, this design requires only a simple button and is thus much faster to operate.</p>

<p>Alternatively, if <em>View All</em> would generate an unwieldy page, give users the <strong>choice between two numbers</strong>, say 10 and 50, where the second number is <strong>substantially bigger</strong> than the default.</p>

<p>If the choice is between two relatively similar numbers (such as 10 and 20), users might as well click the <em>Next Page</em> button rather than suffer the cognitive overhead of trying to decide their display preference.</p>

<h2 id="toc-customization-3">Customization</h2>

<p>When providing a choice of display options, the computer should almost always <strong>respect the user’s stated preference</strong> and employ it as the default the next time around. I am amazed at how many sites and applications don’t do this and instead force users to repeat their choices again and again.</p>

<p><a href="https://www.nngroup.com/articles/customization-of-uis-and-products/" title="Customization of UIs and Products">Usability research on customization features</a> has shown two things:</p>

<ul>

<li>Most users <strong>don’t want to customize</strong>; they prefer to simply use the default settings. It is thus the designer’s responsibility to pick the optimal <a href="https://www.nngroup.com/articles/the-power-of-defaults/" title="The Power of Defaults">default setting</a> that will benefit the most users, because that’s all most users will ever experience.</li>

<li><a href="https://www.nngroup.com/articles/customization/" title="7 Tips for Successful Customization">Customization features</a> are user interfaces in their own right and <strong>have their own usability problems</strong>, especially when designers go overboard and offer users too many choices.</li>

</ul>

<p>The <em>View All</em> feature doesn’t have these problems, nor does the <em>View 20</em> vs. <em>View 100</em> option. Both cases have many advantages:</p>

<ul>

<li>Customization occurs <strong>in the task context</strong> — right when and where people might want to change the display options — as opposed to requiring an excursion into a <em>Preferences</em> screen.</li>

<li>The choices are <strong>easy to understand</strong> and don’t require instructions.</li>

<li><strong>Executing</strong> the choice is easy, assuming you offer only one alternative to the default display (rather than having users open a pop-up and then face the additional decision of whether to expand from, say, 10 items to 20, 30, or 40).</li>

</ul>

<p><strong>What’s not to like about <em>View All</em> — or <em>View Big-N</em>, if you can’t offer <em>View All</em>? For sure, it’s smart to offer this feature, but please do remember users’ preferences once they’ve gone to the trouble of stating them.</strong></p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=item-list-view-all&amp;pt=article">

<h4 class="title heading-small">The Human Mind and Usability</h4>

<p id="the-human-mind-and-usability" class="description body-small">

Use psychology to predict and explain how your customers think and act

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

<li>

<a class="tile ga-article-related-course" data-course-title="Omnichannel Journeys and Customer Experience" href="/courses/cross-channel-user-experience/?lm=item-list-view-all&amp;pt=article">

<h4 class="title heading-small">Omnichannel Journeys and Customer Experience</h4>

<p id="omnichannel-journeys-and-customer-experience" class="description body-small">

Create a seamless, cohesive cross-channel experience

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

<li>

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=item-list-view-all&amp;pt=article">

<h4 class="title heading-small">Web Page UX Design</h4>

<p id="web-page-ux-design" class="description body-small">

Strategically combine content, visuals, and interactive components to design successful web pages

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Ecommerce,Web Usability</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Ecommerce</span>

<a class="ga-article-related-topic" href="/topic/e-commerce/">Ecommerce</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/web-usability/">Web Usability</a>

</li>

</ul>

</div>

</div>

</div>

</div>