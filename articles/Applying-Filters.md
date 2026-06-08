# User Intent Affects Filter Design - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">7</span>

<div class="article-header">

<h1 class="article-h1">User Intent Affects Filter Design</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Katie Sherwin</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Katie_Sherwin_portrait.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/katie-sherwin/">

Katie Sherwin</a></span>

<p class="publication-date">

February 7, 2016

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2016-02-07</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: User Intent Affects Filter Design&amp;body=https://www.nngroup.com/articles/applying-filters/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/applying-filters/&amp;title=User Intent Affects Filter Design&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/applying-filters/&amp;text=User Intent Affects Filter Design&amp;via=nngroup" data-share-type="Twitter">

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

</span>Results pages that refresh too soon or shift the page position disrupt the filtering process. Design filters and facets to offer a smooth user experience.

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

<a class="ga-article-toc-item" href="#toc-when-to-apply-the-filters-2">When to Apply the Filters</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-scrolling-the-new-results-into-view-3">Scrolling the New Results into View</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-4">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-introduction-1">Introduction</h2>

<p>Filters are among the top web innovations since, well, the Internet. These controls allow us to quickly find the needle in the haystack on information-rich sites, such as travel sites or ecommerce sites. Brands have built their reputations for their ability to narrow results efficiently. Filters eliminate items that do not satisfy specific criteria, and facets <a href="/articles/search-navigation/">turn search into navigation</a> by suggesting categories and attributes users might want (but might not otherwise think of on their own). Filters and facets have become standard for refining large results sets.</p>

<p>However, while filters may look similar on many sites (e.g., they are typically placed on the left), their behaviors vary widely. In this article we focus on two dimensions of filter implementation:</p>

<ol>

<li><strong>When to apply the filters.</strong> Can the user adjust multiple filters before the results of the compound query are returned (<strong>batch</strong> <strong>filters</strong>), or are the results returned after each filter value is specified (<strong>interactive</strong> <strong>filters</strong>)? Or, can the results be computed and displayed quickly enough that this dimension is irrelevant?</li>

<li><strong>Whether the new results should be scrolled into view.</strong> Once the query is submitted, does the page scroll back to the top to show the results or is the current position on the page preserved to allow users to continue specifying more filters without distraction?</li>

</ol>

<p>Both these dimensions inform the <strong>continuity of the user experience</strong>. The overarching theme in selecting an implementation should be to<strong> not fragment the user experience,</strong> and let users smoothly progress towards their goals while maintaining a sense of UI stability and <a href="/articles/ideologies-of-web-design/">user mastery</a>.</p>

<h2 id="toc-when-to-apply-the-filters-2">When to Apply the Filters</h2>

<p>Continuing <a href="/articles/ux-learn-in-restaurants/">our restaurant UX analogy</a>, think about how you might order appetizers at a restaurant. Say you want to order three appetizers for the table, but as soon as you name the first one, the waiter snatches the menu out of your hands and walks back to the kitchen to get the chefs started on cooking that dish. Instead, a good waiter understands that you’re still in the process of ordering and knows to give you more time before taking away the menu. A good waiter <strong>allows you time to</strong> <strong>make a batch decision</strong>, even if that might slightly delay the delivery of the first item ordered. (However, sometimes the waiter may take the appetizer order, and then give you more time to decide on the main course. A good waiter is flexible and adapts to the needs of the customers.)</p>

<p>Just like it would be disruptive for the waiter to immediately walk away every time you named an item from the menu, for users who intend to select more than one facet, it’s disruptive and tiresome to refresh the page every single time they make a selection, especially if the site is slow.</p>

<p>Choosing between a batch and an interactive filter implementation will depend on both <strong>user intent</strong> (does the user plan to specify multiple filtering criteria or just one) and <strong>site speed</strong> (how fast the results are presented to the user).</p>

<h3>User Intent</h3>

<p>Intelligent filtering mechanisms <strong>recognize when users are still thinking</strong> and do not refresh the page until the user is done making selections. The big problem then is how can the system know if users are ready to see the updated results? How can a system be like a good waiter?</p>

<p>The first question to ask is whether users are in an exploratory mode or they have clear search parameters in mind. Users who do not have a clear search goal still need to <a href="/articles/search-not-enough/">learn about the structure of the search space</a> and the possible options that are available to them. These users will benefit most from <strong>interactive</strong> filtering. They make one selection, and the system updates the results. After looking through the updated results, they get an idea for another filter, select it, and the system updates the results again, and so on.</p>

<p>Interactive filtering is usually associated with facets: as soon as users have selected a new possible facet, the results are displayed along with the set of new applicable facets (e.g., once the user has selected <em>Refrigerators</em>, new range-specific facets such as <em>Freezer volume</em> will be displayed). Often, facets also show the number of elements available under each filter, and thus help users avoid zero-search results.</p>

<p>Alternatively, users who already have multiple criteria in mind will benefit from <strong>batch</strong> filtering. For example, a customer shopping for a “little black dress” might go to a <em>Dresses</em> category and immediately look to the filters to refine by color, length, style, and size. For these shoppers, the experience will be smoothest if the system waits for them to finish making selections before it loads the new results set. The biggest disadvantage of batch filtering is that there is a risk that users will select a combination of criteria that leads to zero results. Delaying the presentation of results makes it difficult to give users continuous feedback about which filters are available or disabled and how many results there are for each filter. The advantage is however that it saves users extra wait time between queries, and that instead of waiting through multiple queries (one for each attribute) they can only wait for one.</p>

<p>For designers, it is <strong>difficult to accurately predict users’ mindset while they are filtering</strong>. Here are some rules of thumb to help you figure out the users’ goals:</p>

<ul>

<li><strong>Let users tell you when they’re done selecting filters.</strong> This essentially means to err on the side of batch filtering and include an <em>Apply</em> button in your filter design. Users can click on that button once they’ve indicated all the filter values that they are interested in. This is the recommended approach on mobile devices, <a href="/articles/mobile-faceted-search/">even with the new tray design pattern</a>. However, this method implies that you’re failing your exploratory users, who may not be sure of what attributes they are interested in.</li>

<li><strong>Detect activity around the filters. </strong>Look for user movement via mouse hover or keyboard focus. If users are moving the mouse around the filters (or using the keyboard to tab between them), they may be on their way to make another selection. Conversely, if the mouse leaves the filter area and moves to main results, it’s a good sign that users are ready for the results. Note that even if there is some movement, this works best when a time limit is used as a fallback (see #3 in this list).</li>

<li><strong>Update results based on the time since the last selection. </strong>If a user hasn’t made another selection or moved the mouse after a certain amount of time (1–2 seconds), then display the new results. Of course, the system should still give immediate feedback (e.g. a <a href="/articles/progress-indicators/">progress indicator</a>) to acknowledge that the first selection was received.</li>

</ul>

<div class="captioned">

<video controls="" preload="" src="https://media.nngroup.com/media/editor/2016/02/03/houseoffrasercouk-batch-filters.mp4" width="100%"> </video>

<div class="caption"><em>Houseoffraser.co.uk: An example of effective batch filtering. The system allows users to keep making selections while users are active in the filter area. After a few moments of user inactivity, the system displays the results with all the filters applied.</em> <em>(In most browsers, hover over the video to display the controls if they're not already visible.)</em></div>

</div>

<h3>Site Speed</h3>

<p>The other variable that influences the choice between interactive and batch filtering is <strong>the speed of the site</strong>: how fast you can produce the results. If you expect the queries to be instantaneous (and the new results to be <a href="/articles/response-times-3-important-limits/">shown less than one second</a> after each filter has been specified) then interactive filtering will be less offensive even to users in search mode. If however your site is likely to be slow at least occasionally, then the batch filtering can save users some wait time. That is the main reason for which, on mobile devices, we recommend batch filtering — page loads are often slow on the go, and having to wait for four page loads for a complex query involving four filter values increases <a href="/articles/interaction-cost-definition">interaction cost</a> too much for the user.</p>

<h3>Continuous Feedback: A Warning</h3>

<p>Interactive filtering has another disadvantage: continuous updates can be visually distracting, even if they are fast and don’t scroll the page. Any time items in a results list update, the flicker of an image swap will attract attention (though it probably will not be clear what exactly changed). Flickering in the peripheral vision is annoying and may also cause the user to waste time looking at the preliminary results. That said, visual cues are necessary so that users are aware that a change has occurred (i.e., to prevent <a href="/articles/change-blindness/">change blindness</a>).</p>

<p>To balance the advantages of continuous feedback without distracting users’ peripheral vision, many effective faceted navigation systems dim the results set and show a progress indicator before displaying the new results. This way, the change that users detect is a single dimmed area (instead of individual items seemingly flashing on and off the screen).</p>

<figure class="caption"><img alt="Results dim while updating" height="361" loading="lazy" src="https://media.nngroup.com/media/editor/2016/02/03/dimmed-filter-results.png" width="720"/>

<figcaption><em>Net-a-porter.com: The moment between when a facet is selected (in this case, </em>Black<em>) and the new results are displayed minimizes visual distractions; the entire results area dims and an animated spinner shows progress. Even with a fast system, designs should avoid visual changes that happen too quickly, becoming annoying and distracting.</em></figcaption>

</figure>

<h2 id="toc-scrolling-the-new-results-into-view-3">Scrolling the New Results into View</h2>

<p>Remember that our goal is to achieve a smooth user experience. What happens to the page view once users apply the filters is the second stage of this experience. This stage also depends on correctly recognizing user intent. Unfortunately, many sites fragment the experience during this part of the interaction.</p>

<p>For example, Houseoffraser.co.uk disappoints after the filters are applied: the page scrolls back to the top of the results. This will usually cause users who are still looking at the filters to lose their place on the page and become disoriented. But worst of all, it increases the chances of an accidental click on the wrong category if users are in the process of selecting a filter and the page scrolls at the same time.</p>

<div class="captioned">

<video controls="" preload="" src="https://media.nngroup.com/media/editor/2016/02/03/houseoffrasercouk-filters-scroll-to-top.mp4" width="100%"> </video>

<div class="caption"><em>Houseoffraser.co.uk: Jumping the results page to top can cause users to accidentally select unintended facets. (In most browsers, hover over the video to display the controls if they're not already visible.)</em></div>

</div>

<p>On the other hand, scrolling to the top of the page has some benefits as well. First, the best results will appear at the top of the list: if relevance or popularity declines dramatically with results lower down on the page, then users will see the best options sooner if they are taken to the top of the page. Second, after filtering, there may be too few results and the page might refresh to a blank screen next to the filters. In both these situations, it is better to send users to the top of the page so that they can see the changes.</p>

<figure class="caption"><img alt="New results are not visible without scrolling up" height="400" loading="lazy" src="https://media.nngroup.com/media/editor/2016/02/03/results-dont-scroll-into-view.jpg" width="675"/>

<figcaption><em>Kayak.com: After adjusting the price filter to show flights up to $500, the page refreshes the results to the current page position. Unfortunately, no results are visible at this view, because only six matching flights were found. The empty screen can be interpreted as the system still working, or as zero results. It would be better to refresh the page to the top of the results list.</em></figcaption>

</figure>

<p>Note that the main problem here is, again, failing to recognize the user intent — namely that the user is still engaged with the filters area. The same techniques that we describe in the first section of the article can be successfully applied to determine whether it’s safe to scroll up or you should wait a few more seconds until the users are done with interacting with the filters.</p>

<h2 id="toc-conclusion-4">Conclusion</h2>

<p>By detecting users’ intent to select additional filters, sites can offer a smoother, more efficient filtering experience. Use interactive filters if your users are exploratory in their search. Use batch filtering when your users have clear refinement criteria, or you know that your site will be slow at least occasionally (e.g., on mobile devices).</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Omnichannel Journeys and Customer Experience" href="/courses/cross-channel-user-experience/?lm=applying-filters&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Ecommerce,Interaction Design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Ecommerce</span>

<a class="ga-article-related-topic" href="/topic/e-commerce/">Ecommerce</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/interaction-design/">Interaction Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>