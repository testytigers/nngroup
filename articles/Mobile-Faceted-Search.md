# Mobile Faceted Search with a Tray : New and Improved Design Pattern - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">5</span>

<div class="article-header">

<h1 class="article-h1">Mobile Faceted Search with a Tray: New and Improved Design Pattern</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Kathryn Whitenton</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Kathryn_1.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/kathryn-whitenton/">

Kathryn Whitenton</a></span>

<p class="publication-date">

July 26, 2015

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2015-07-26</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Mobile Faceted Search with a Tray: New and Improved Design Pattern&amp;body=https://www.nngroup.com/articles/mobile-faceted-search/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/mobile-faceted-search/&amp;title=Mobile Faceted Search with a Tray: New and Improved Design Pattern&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/mobile-faceted-search/&amp;text=Mobile Faceted Search with a Tray: New and Improved Design Pattern&amp;via=nngroup" data-share-type="Twitter">

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

</span>Displaying faceted-search controls on mobile devices in a ‘tray’ overlay is a new effective solution to the challenge of showing both results and filters on small screens.

</div>

<div class="article-body">

<p>Recently, a few big brands have introduced a new method for displayed facet controls on mobile devices, by placing them in a ‘tray’ overlay on top of the actual results. This new design approach addresses a major shortcoming typical of many faceted search displays on mobile devices: the placement of facet controls on a separate screen, which forces users to work harder to understand how the facet controls affect the results set. But before understanding why this is the case, let’s go back to the basics of faceted search.</p>

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

<a class="ga-article-toc-item" href="#toc-what-makes-faceted-search-special-1">What Makes Faceted Search Special?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-challenges-of-displaying-search-facets-on-mobile-devices-2">Challenges of Displaying Search Facets on Mobile Devices</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-new-solution-tray-overlay-to-display-facet-controls-3">New Solution: ‘Tray’ Overlay to Display Facet Controls</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-design-pattern-elements-4">Design Pattern Elements</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-why-is-simultaneous-display-of-results-and-facet-controls-important-5">Why Is Simultaneous Display of Results and Facet Controls Important?</a>

</li>

</ul>

</div>

</div><h2 id="toc-what-makes-faceted-search-special-1">What Makes Faceted Search Special?</h2>

<p><a href="http://www.nngroup.com/articles/filters-vs-facets/">Faceted search</a> lets users refine a set of results by applying filters that comprehensively describe the search space. Such narrowing is invaluable for users who need to find something specific within a large content set. This type of search has become common for ecommerce and travel websites, as well as many different types of document and media collections. A faceted system includes two critical elements:</p>

<ol>

<li><strong>Simple controls to construct sophisticated searches</strong>: Providing familiar controls like drop-down menus and checkboxes with natural-language labels empowers ordinary users to narrow down a large set of results to a small set that meets their exact criteria—without any special knowledge of Boolean logic or query syntax.</li>

<li><strong>Simultaneous display of the facet controls and the results</strong>: Showing both the filters and the results at the same time makes it easier for users to understand the relationship between the two; ideally, this is reinforced by dynamically updating the results set as soon as the user selects a filter criteria.</li>

</ol>

<p>The simple filter controls are the most obvious component of a faceted system. However, the importance of simultaneous display should not be underestimated. Long before faceted search became popular, we had ‘advanced search’ screens with similar controls for creating complex search queries. The big difference introduced with the <a href="https://www.google.com/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;uact=8&amp;ved=0CCEQFjAA&amp;url=http%3A%2F%2Fflamenco.berkeley.edu%2F&amp;ei=8IKUVdvJNIPnsAWlqqjADg&amp;usg=AFQjCNG4vccHDKGytSpOmkdgQPlb91UnkQ&amp;bvm=bv.96952980,d.b2w">first faceted navigation system</a> was in displaying the <strong>facet</strong> <strong>controls and the results</strong> <strong>at the same time,</strong> which makes the effects of each filter instantly visible. This innovation embodies 2 of the <a href="http://www.nngroup.com/articles/ten-usability-heuristics/">10 usability heuristics</a>: provide rapid system feedback, and offer users control and freedom.</p>

<h2 id="toc-challenges-of-displaying-search-facets-on-mobile-devices-2">Challenges of Displaying Search Facets on Mobile Devices</h2>

<p>Faceted search was originally designed for desktop and laptop users. Translating this experience onto a mobile device is difficult, because the very thing that makes faceted search so helpful to users – being able to see the filters and the results at the same time – is difficult to achieve on a small screen. There simply isn't enough space to show a full set of facets and a decent number of detailed results simultaneously.</p>

<p>Until recently, most mobile designers haven’t even tried to display facets and results at the same time, instead opting to place them on separate screens. But this solution forces users to navigate to the facet-control screen, make their selections, then navigate back to the results set to see the effects of their selections. The istockphoto.com mobile website illustrates the typical approach to providing faceted search to mobile users. The results page includes an icon that users can tap to open the facet controls (assuming they can figure out what the icon means). Once the facet controls are displayed, users can select different filtering criteria, but it’s not obvious how the results will be affected by the facet selection because:</p>

<ul>

<li>None of the results are shown on this screen.</li>

<li>The number of files, displayed in the page header updates too slowly.</li>

<li>The header showing the number of files may not even be visible once a user has scrolled down to expand and select the facets below.</li>

</ul>

<p>Due to these limitations, users have to return to the previous screen in order to find out whether their filter selections were effective at targeting the best results and whether they have narrowed the results set down to a manageable size— or if perhaps they've applied such restrictive criteria that no results match.</p>

<div style="text-align:center">

<figure class="caption" style="display:inline-block"><img alt="Mobile search results and facet controls on iStockphoto.com" height="598" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/15/istockphoto_mobile_facets.png" width="700"/>

<figcaption><em>Left: Like many mobile search designs, iStockphoto.com does not display faceted search controls on the actual search results page. Instead it requires users to navigate to the facet controls, in this case via a cryptic icon composed of lines and circles on the right edge of the Search bar. Right: The facet controls take up the entire screen, and in order to see the effects of their selections, users must navigate back to the results screen.</em></figcaption>

</figure>

</div>

<h2 id="toc-new-solution-tray-overlay-to-display-facet-controls-3">New Solution: ‘Tray’ Overlay to Display Facet Controls</h2>

<p>Recently a new approach to providing faceted search for mobile users has appeared: showing the facet controls as a ‘push-out’ style tray on top of the search results. This design allows for <strong>continuous visibility of results</strong>: even while the facet controls are open, some information about the results is visible in the background. The Amazon iPhone application and eBay’s mobile website both now use an overlay to display facet controls on the same screen as the search results.</p>

<div style="text-align:center">

<figure class="caption" style="display:inline-block"><img alt="Mobile Facet Tray Overlay Examples" height="596" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/15/mobile-facet-trays-examples.png" width="700"/>

<figcaption><em>Amazon’s iPhone application (left) and eBay’s mobile website (right) both recently introduced an overlay to display search facet controls on the same screen as the search results. </em></figcaption>

</figure>

</div>

<h2 id="toc-design-pattern-elements-4">Design Pattern Elements</h2>

<p>Both the Amazon and eBay designs include several details that combine to create a good user experience:</p>

<ul>

<li>Once activated, facet controls appear in a vertical panel overlaid on top of the results screen.</li>

<li>The results are always visible in the background, and can be seen to change as the user makes her facet selections.  (However, in the case of eBay, users can hardly make out what the results are. Amazon’s design is better because users actually get useful information from the background.)</li>

<li>The total number of results is always visible, even if the user has scrolled down a long list of facets. (Amazon accomplishes this by fixing the header at the top of the screen so that it remains visible even as the list of facets scrolls up or down).</li>

<li>A translucent gray shadow slightly obscures the underlying results and ensures that the facet controls stand out.</li>

</ul>

<ul>

<li>The facet panel appears at the right edge of the screen, leaving the left edge of the results visible. (This is helpful because the left edge is more likely to have meaningful content; with Amazon you can actually see the product images.)</li>

</ul>

<p>(You may also notice that both Amazon and eBay use actual words – <em>Filter </em>and <em>Refine </em>– as the commands to access facets, rather than a special symbol.  Any of the labels commonly used for faceted navigation – <em>narrow your results, refine, </em>and <em>filter – </em>are far more understandable than cryptic <a href="http://www.nngroup.com/articles/icon-usability/">icons</a>, and definitely worth the extra space. )</p>

<h2 id="toc-why-is-simultaneous-display-of-results-and-facet-controls-important-5">Why Is Simultaneous Display of Results and Facet Controls Important?</h2>

<p>In usability testing, I am always amazed at how successful people are at immediately understanding and using faceted search screens, which tend to include many different elements and controls. As long as the controls are displayed properly, most people jump right in to creating and refining their queries. Instant results are an important part of the process because they allow users to see right away if they have applied the wrong filter, or applied overly narrow criteria that eliminates too many options. Both of those errors are very easy to recover from if you can instantly see the effects of your actions, but without this visibility users can end up in a tedious cycle of <a href="http://www.nngroup.com/articles/pogo-sticking/">pogo-sticking</a> between the results and the filters. </p>

<p>The facet ‘tray’ approach illustrated by Amazon and Ebay doesn’t provide complete visibility, since only a small part of the results screen is visible. But these creative solutions offer at least <em>some</em> visibility into the effects of applying a filter. Users may still find that they need to close and re-open the facet controls, but this approach feels more like expanding a part of the current page, rather than jumping back and forth between different pages.</p>

<p>Find out more about the best approaches for visual displays on smaller screens in our full-day courses about <a href="http://www.nngroup.com/courses/vis-mob-2/">Visual Design for Mobile and Tablet</a>.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Information Architecture" href="/courses/information-architecture/?lm=mobile-faceted-search&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet,Search,Visual Design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet</span>

<a class="ga-article-related-topic" href="/topic/mobile-and-tablet-design/">Mobile &amp; Tablet</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/search/">Search</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/visual-design/">Visual Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>