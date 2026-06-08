# Converting Search into Navigation - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">3</span>

<div class="article-header">

<h1 class="article-h1">Converting Search into Navigation</h1>

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

March 16, 2013

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2013-03-16</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Converting Search into Navigation&amp;body=https://www.nngroup.com/articles/search-navigation/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/search-navigation/&amp;title=Converting Search into Navigation&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/search-navigation/&amp;text=Converting Search into Navigation&amp;via=nngroup" data-share-type="Twitter">

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

</span>Most users are unable to solve even halfway complicated problems with search. Better to redirect their efforts into more supportive user interfaces when possible.

</div>

<div class="article-body">

<p>Users are <strong>incredibly bad at finding and researching</strong> things on the web. A few years ago, I characterized <a href="https://www.nngroup.com/articles/incompetent-search-skills/" title="Alertbox: Incompetent Research Skills Curb Users' Problem Solving">users' research skills as "incompetent,"</a> and they’ve only gotten worse over time. "Pathetic" and "useless" are words that come to mind after this year's user testing.</p>

<p>In a recent study, for example, a user wanted to buy a highly protective yet girlish phone case as a gift for her daughter. While on Amazon.com, she engaged in random fishing expeditions into the product database, using search queries such as "pink impact resistant iphone 5 cover."</p>

<p>This was by no means the worst query we saw that week; in this case, however, the user never found what she wanted. She tried a few query modifications — which most users won’t attempt — but never questioned her basic research strategy. Nor did she realize that Amazon uses a full-text search that doesn't understand the <em>meaning </em>of a query.</p>

<p>Among the products she found were those that were not pink, not a phone case, and not an iPhone case. At least Amazon's thumbnails are good enough that she didn’t have to click through to most such erroneous hits.</p>

<figure class="caption"><img alt="3 of the product thumbnails from a search on Amazon.com: green and white phone covers and red earbuds" loading="lazy" src="//media.nngroup.com/media/editor/2013/03/16/amazon-product-thumbnails.jpg" style="width: 429px; height: 178px;"/>

<figcaption><em>Excerpts from first page of search results for "pink impact resistant iphone 5 cover" on Amazon.com</em></figcaption>

</figure>

<p><a href="https://www.nngroup.com/articles/amazon-no-e-commerce-role-model/" title="Alertbox: Amazon: No Longer the Role Model for E-Commerce Design">Amazon.com has poor usability</a> in cases like this because of its business model: it carries every product under the sun. Such a design cannot support any one product category optimally, even though the overall site still scores better than almost anybody else on <a href="https://www.nngroup.com/reports/e-commerce-user-experience/" title="Nielsen Norman Group report series: 874 usability guidelines for ecommerce user experience">ecommerce design guidelines</a>.</p>

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

<a class="ga-article-toc-item" href="#toc-easy-search-works-difficult-search-fails-1">Easy Search Works; Difficult Search Fails</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-designing-for-mediocre-searchers-2">Designing for Mediocre Searchers</a>

</li>

</ul>

</div>

</div><h2 id="toc-easy-search-works-difficult-search-fails-1">Easy Search Works; Difficult Search Fails</h2>

<p>In study after study, we see the same thing: most users reach for search, but they don't know how to use it.</p>

<p>It would certainly be nice if schools would get better at <a href="https://www.nngroup.com/articles/life-long-computer-skills/" title="Alertbox: Life-Long Computer Skills">teaching kids how to search</a>. But I don't hold out much hope, because most people have the literary talents of an anteater (I was going to say, "a chimpanzee," but these animals are too smart for my metaphor). Having new and varied vocabulary words spring from their foreheads wasn't a survival skill for ice age hunters, so most people today can't think up good queries without help.</p>

<p>It seems a puzzle why <strong>ever-more users are so search dominant</strong> when they can't search. Perhaps because search actually does <strong>work as a user strategy</strong> in many cases — mainly when people use a web-wide search engine for simple tasks. Indeed, the big search engines (such as Google, Bing, Naver, Baidu, and Yandex) have morphed into <a href="https://www.nngroup.com/articles/search-engines-become-answer-engines/" title="Alertbox: When Search Engines Become Answer Engines">answer engines</a> that often give users what they want right on the SERP (search engine results page).</p>

<p>So, if you have a well-designed search facility, and users are looking for a specific item with a well-defined name, they'll probably be successful. In our <a href="https://www.nngroup.com/reports/ecommerce-ux-search-including-faceted-search/" title="Nielsen Norman Group report: Ecommerce Search Usability Guidelines, Including Faceted Search">testing of search on ecommerce sites</a>, users found what they wanted in their first search attempt 64% of the time. And their overall <strong>success rate with search was 74%</strong>, which is pretty good.</p>

<p>The extra 10% success comes from users attempting multiple queries. Another way to look at this is that the 36% of users who failed their first search succeeded only 28% of the time (10/36 = .28). In other words, the probability of <strong>success drops from 64% to 28%</strong> when we go from an easy to a difficult search problem.</p>

<p>(<strong>Intranets </strong>are a different matter: Because intranet search is usually very poorly implemented, most company employees have learned to limit their use of intranet search. In our recent <a href="https://www.nngroup.com/reports/intranet-searching/" title="Nielsen Norman Group report: Searching the Intranet and the Employee Directory">intranet user testing</a>, employees used search as their initial wayfinding strategy in only <strong>19% of tasks</strong> on average—though with extreme variability between companies with good or bad intranet search.)</p>

<h2 id="toc-designing-for-mediocre-searchers-2">Designing for Mediocre Searchers</h2>

<p><strong>Search suggestions</strong> are a now a popular way to help people overcome their limited generative abilities by showing a drop-down of fully formed potential queries as soon as users type in a few characters that hint at their needs. Although helpful, search suggestions can also be limiting; users often view the drop-down as a mini-SERP and assume that it lists everything the site carries. Thus, if something isn't included in the search suggestions, users might never bother to search for it.</p>

<p>We found a better way to help users overcome their search problems when we tested people shopping at Costco's website. One user wanted to buy a TV set and immediately entered the query <em>television </em>on the Costco homepage. Following is the "search results page" that appeared:</p>

<figure class="caption"><img alt="Screenshot of search results page from Costco that's actually a category page" loading="lazy" src="//media.nngroup.com/media/editor/2013/03/16/costco-serp-category-page.png" style="width: 507px; height: 589px;"/>

<figcaption><em>Costco website as tested: the page shown after searching for "television."</em></figcaption>

</figure>

<p>Not a SERP at all! This is the <a href="https://www.nngroup.com/reports/ecommerce-ux-homepages-and-category-pages/" title="Nielsen Norman Group report: Design Guidelines for Ecommerce Homepages and Category Pages">category page</a> for TV sets. The page includes relevant features for this product category, with relevant facets such as plasma vs. LCD, brands, resolution, and screen size. None of these would appear on a "normal" SERP, which has to handle a variety of result types.</p>

<p>Is Costco cheating? Only if you have a very strict interpretation of the search concept. In our test, users were happy on this site. They got what they asked for — which is exactly what people want.</p>

<p>For sure, you should redirect users from a normal SERP to a category page only when their query is <strong>unambiguous</strong> and exactly matches the category. A search for "3D TV" could go to the subcategory page for these products, but a search for "3D" should generate a regular SERP. (Costco does this correctly, including both 3D televisions and other products relevant to the query.)</p>

<p>Until people begin to grasp the complexities of search and develop skills accordingly, businesses that take such extra steps to help users find what they need will improve customer success — and the bottom line.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Information Architecture" href="/courses/information-architecture/?lm=search-navigation&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Navigation,Search</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Navigation</span>

<a class="ga-article-related-topic" href="/topic/navigation/">Navigation</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/search/">Search</a>

</li>

</ul>

</div>

</div>

</div>

</div>