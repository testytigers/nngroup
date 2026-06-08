# Site Search Suggestions - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Site Search Suggestions</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Kate Moran</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Kate-Headshot-2022.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/kate-moran/">

Kate Moran</a></span>

<p class="publication-date">

May 20, 2018

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2018-05-20</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Site Search Suggestions&amp;body=https://www.nngroup.com/articles/site-search-suggestions/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/site-search-suggestions/&amp;title=Site Search Suggestions&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/site-search-suggestions/&amp;text=Site Search Suggestions&amp;via=nngroup" data-share-type="Twitter">

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

</span>Useful search suggestions lead to relevant results and are visually distinct from the query text. If appropriate, they include scope, thumbnails, or categories.

</div>

<div class="article-body">

<p>Search suggestions (sometimes also called autocomplete or autosuggest) used to be an optional, nice-to-have feature for site search. (In this article, we use the term “site search” to refer to a website’s own search feature — that only <strong>searches within that single site’s content </strong>— as opposed to web-wide search engines like Google, Bing, or Baidu that search across multiple sites.)</p>

<blockquote>

<p><strong>Search suggestions </strong>are recommended queries that appear in a dropdown as users type in a search box. These recommendations appear beneath the search box and change as users type each letter of their query.</p>

</blockquote>

<p>In recent years, search suggestions have become an expected sign of a well-designed search feature. This change in expectations is likely a result of users’ frequent exposure to query suggestions on Google, which always sets the (unrealistic) standard of what a “good” search feature should be.</p>

<p>When your users select from search suggestions rather than typing in their own complete query, they benefit because they:</p>

<ul>

<li><strong>Pick an appropriate term, which will show them good results, </strong>rather than making up a query which might have no results or poor results </li>

<li><strong>Decrease </strong><a href="https://www.nngroup.com/articles/interaction-cost-definition/"><strong>interaction cost</strong></a>, because they can type less </li>

<li><strong>Avoid typos, </strong>because they don’t need to type out the entire query themselves </li>

<li><strong>Use less mental effort to search, </strong>because they can simply <a href="https://www.nngroup.com/articles/recognition-and-recall/">recognize</a> the right words or phrasing they want</li>

</ul>

<p>Interestingly, even though users expect this feature and sometimes comment on it when it isn’t available on a site, they don’t always actually use it. In our recent study on ecommerce websites, suggested queries were <strong>selected by users in only 23% of the instances </strong>where they were offered. (There were 31 suggestions selected out of 136 instances where suggestions were offered. The margin of error for this proportion is 7%.)</p>

<p>However, even when users didn’t actually choose from the list of query suggestions, the feature still had the potential to provide some benefits as a reference. Users could read the suggestions to see what’s available on the site, how to spell difficult terms, and what other users search for. In some cases, particularly when the query phrase is short, it is easier for users to just finish typing out the query themselves, rather than to reacquire their mouse or tap the screen.</p>

<p>For site search, search suggestions have the further benefit of informing users of the range of products or options offered by the site. Conversely, if something isn’t shown as a search suggestion after entering the first few characters of a product name, some users may conclude that the site doesn’t offer that product and abandon the site without even executing the search.</p>

<p>If you’re planning to implement or improve your site’s search suggestions, follow these tips to make them as helpful as possible.</p>

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

<a class="ga-article-toc-item" href="#toc-dont-suggest-bad-results-1">Don’t Suggest Bad Results</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-use-text-styling-to-differentiate-between-typed-query-text-and-suggested-terms-2">Use Text Styling to Differentiate Between Typed Query Text and Suggested Terms</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-include-scope-in-search-suggestions-3">Include Scope in Search Suggestions</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-consider-including-more-than-simple-query-recommendations-4">Consider Including More than Simple Query Recommendations</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-5">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-dont-suggest-bad-results-1">Don’t Suggest Bad Results</h2>

<p>Make sure every suggested query actually has good, relevant results. </p>

<p>One participant in a usability test was shopping for a new suitcase on JC Penney’s website. He typed “luggage” into the search box and saw the phrase “luggage sets clearance” in the suggested queries. </p>

<p>He selected the query and was taken to a results page that had no luggage sets at all — just two travel items for pets. </p>

<p>“That’s very weird,” he said. “The search was suggested to me, so I would think that clicking <em>luggage sets clearance </em>would take me to luggage on sale. So this is not great.”</p>

<div style="text-align:center">

<figure class="caption" style="display:inline-block"><img alt="/Users/kate/Dropbox/Reports/Ecommerce--Search/report-screenshots/jcpenney-luggage-sets-clearance.png" border="0" height="411" loading="lazy" src="https://media.nngroup.com/media/editor/2018/04/19/jcpenney-luggage-sets-clearance.png" width="721"/>

<figcaption><em>A user was annoyed when the suggested query returned irrelevant results.</em></figcaption>

</figure>

</div>

<p>Suggested terms that return zero results, or irrelevant results, are worse than unhelpful — they sidetrack users and are downright irritating.</p>

<h2 id="toc-use-text-styling-to-differentiate-between-typed-query-text-and-suggested-terms-2">Use Text Styling to Differentiate Between Typed Query Text and Suggested Terms</h2>

<p>Within a suggested search dropdown, each suggestion has two parts: the characters already typed by the user, and the characters suggested by the system to complete the query. </p>

<p style="text-align:center"><img alt="" border="0" height="250" loading="lazy" src="https://media.nngroup.com/media/editor/2018/04/19/suggest.png" width="500"/></p>

<p>It’s important to use different visual styles to show which characters fall into each category. You can use bolding, italics, color, or indenting to communicate the differences between these parts. Visual differentiation helps users understand why the suggestions are shown and scan the available options.</p>

<p>The type of suggestions your site offers should help you determine how to style the suggestions. </p>

<ul>

<li>If your suggested search feature only <strong>appends characters to the end </strong>of the user’s text to finish the query, then you should <strong>highlight the suggested characters</strong>. </li>

<li>If, instead, your suggested search feature will <strong>suggest popular queries that contain </strong>the user’s text anywhere in the query, it’s best to <strong>highlight the user’s query.</strong></li>

</ul>

<p>For example, one user typed his query, “basketball hoop,” on the website for Dick’s Sporting Goods. As he typed each letter, suggested search terms appeared in a dropdown. </p>

<p>Dick’s Sporting Goods uses the first type of suggestions — it only appends characters to the user’s text, in an effort to complete that query. The characters that matched what this particular user had already typed were shown in bold (“basketball h”) while the characters suggested to complete the query had a normal font weight. </p>

<div style="text-align:center">

<figure class="caption" style="display:inline-block"><img alt="/Users/kate/Dropbox/Reports/Ecommerce--Search/report-screenshots/Screen Shot 2017-08-22 at 4.40.29 PM.png" border="0" height="161" loading="lazy" src="https://media.nngroup.com/media/editor/2018/04/19/dicks-searchsuggestions.png" width="721"/>

<figcaption><em>DicksSportingGoods.com uses bold text to style the user’s typed characters in its search suggestions.</em></figcaption>

</figure>

</div>

<p>This approach clearly showed the difference between the two parts, but unfortunately placed the emphasis on the repetitive characters in each suggestion (the already-typed characters). So, it would’ve been better for Dick’s Sporting Goods to present the search suggestions like this, with the emphasis on the unique characters:</p>

<ul>

<li>basketball h<strong>oodie</strong></li>

<li>basketball h<strong>oop</strong></li>

<li>basketball h<strong>at</strong></li>

</ul>

<p>But if your feature suggests popular queries that contain the user’s text anywhere in the query, the opposite approach is better — you want to highlight the user’s query. </p>

<p>Using our basketball example, a system with this type of suggestions would return suggestions like “basketball hoodie,” but also things like “portable basketball hoop” and “kids basketball hat.” In this case, you should highlight the user’s query to help the user scan the suggestions and identify where the query text fits within each suggestion. For example:</p>

<ul>

<li><strong>basketball </strong><strong>h</strong>oodie</li>

<li>portable <strong>basketball </strong><strong>h</strong>oop</li>

<li>kids <strong>basketball </strong><strong>h</strong>at</li>

</ul>

<h2 id="toc-include-scope-in-search-suggestions-3">Include Scope in Search Suggestions</h2>

<p><a href="https://www.nngroup.com/articles/scoped-search/">Scoped search should only be used on some websites</a>, and even then, only if it can be implemented well. If your site scopes content, you’ll want to reflect that in the site’s search suggestions.</p>

<p>For scoped sites, each search suggestion can have three components:</p>

<ul>

<li>the characters already typed by the user</li>

<li>the characters suggested by the system to complete the query</li>

<li>the scope of that suggestion (if any)</li>

</ul>

<p style="text-align:center"><img alt="" border="0" height="250" loading="lazy" src="https://media.nngroup.com/media/editor/2018/04/19/suggest-2.png" width="500"/></p>

<p>Just like the other two parts, you’ll need to visually distinguish the scope from the rest of the suggestion. It’s important for users to know that the system will search for “basketball shorts” in the <em>Women’s </em>section of the site, rather than just searching for the terms “basketball shorts in Women’s.” Indenting scoped or category suggestions beneath the recommended query can communicate their relationship to the query. </p>

<p>One user’s search for “water bottle” on Amazon.com brought up two scoped suggestions: <em>in Home &amp; Kitchen </em>and <em>in Outdoor Recreation</em>. The text of these scoped suggestions was presented in a lighter gray color, and indented beneath the suggested query.</p>

<div style="text-align:center">

<figure class="caption" style="display:inline-block"><img alt="/Users/kate/Dropbox/Reports/Ecommerce--Search/report-screenshots/amazon-waterbottle.png" border="0" height="201" loading="lazy" src="https://media.nngroup.com/media/editor/2018/04/19/amazon_p14_search-waterbottle-2.png" width="720"/>

<figcaption><em>Amazon.com shows its scoped search suggestions by indenting the scope category beneath the query terms.</em></figcaption>

</figure>

</div>

<p>This approach worked well because all three levels were linked. The user could choose between three slightly different options:</p>

<ul>

<li>search for “water bottle” without any scope</li>

<li>search for “water bottle” in the Home &amp; Kitchen scoped category</li>

<li>search for “water bottle” in the Outdoor Recreation scoped category</li>

</ul>

<h2 id="toc-consider-including-more-than-simple-query-recommendations-4">Consider Including More than Simple Query Recommendations</h2>

<p>Beyond just completing a user’s query, the search suggestions dropdown can include links to other types of related content. For example, B&amp;H Photo Video uses a huge, full-width search suggestion dropdown that provided query suggestions, but also linked to:</p>

<ul>

<li>Category pages</li>

<li>Product-detail pages</li>

<li>Resources/articles</li>

</ul>

<div style="text-align:center">

<figure class="caption" style="display:inline-block"><img alt="" border="0" height="351" loading="lazy" src="https://media.nngroup.com/media/editor/2018/04/19/bhphoto.png" width="721"/>

<figcaption><em>B&amp;H Photo Video used a variety of rich content in its very large search suggestion dropdown.</em></figcaption>

</figure>

</div>

<p>Consider if this type of complex search-suggestion dropdown would be helpful for your users, or confusing overkill. If you do adopt this approach, your suggestion dropdown should be well organized and labeled. Users should be able to easily scan and understand all of the information presented.</p>

<p>In particular, providing links to related products in the dropdown can be a good shortcut for those who know what they were looking for. However, we found that it was rare for participants in our study to select a specific item from the rich suggestions. Instead, most users preferred to see the full list of results, so they could browse and compare. </p>

<p>If you decide to use rich search suggestions, use an adaptive approach to simplify the feature for mobile devices. On smaller devices, just offer simple text search suggestions.</p>

<div style="text-align:center">

<figure class="caption" style="display:inline-block"><img alt="" height="566" loading="lazy" src="https://media.nngroup.com/media/editor/2018/04/19/mobile-search-suggestions-1.png" width="700"/>

<figcaption><em>For mobile devices, Sur La Table (left) and Home Depot (right) reduce their rich search suggestions to display only simple text suggestions.</em></figcaption>

</figure>

</div>

<h2 id="toc-conclusion-5">Conclusion</h2>

<p>Prioritize scannability and ease of processing in your search suggestions. Remember that their primary purpose is to make it as easy as possible for your users to express their information need and to see helpful results.</p>

<p>(For more information, see the new 4th edition of our report on <a href="https://www.nngroup.com/reports/ecommerce-ux-search-including-faceted-search/">Ecommerce Search User Experience</a>, with 80 design guidelines.)</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Information Architecture" href="/courses/information-architecture/?lm=site-search-suggestions&amp;pt=article">

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

<li>

<a class="tile ga-article-related-course" data-course-title="Omnichannel Journeys and Customer Experience" href="/courses/cross-channel-user-experience/?lm=site-search-suggestions&amp;pt=article">

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

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Search,Ecommerce</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Search</span>

<a class="ga-article-related-topic" href="/topic/search/">Search</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/e-commerce/">Ecommerce</a>

</li>

</ul>

</div>

</div>

</div>

</div>