# Multivariate vs. A/B Testing: Incremental vs. Radical Changes - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">5</span>

<div class="article-header">

<h1 class="article-h1">Multivariate vs. A/B Testing: Incremental vs. Radical Changes</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Aurora Harley</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Aurora-Harley-20190601SF.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/aurora-harley/">

Aurora Harley</a></span>

<p class="publication-date">

April 8, 2018

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2018-04-08</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Multivariate vs. A/B Testing: Incremental vs. Radical Changes&amp;body=https://www.nngroup.com/articles/multivariate-testing/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/multivariate-testing/&amp;title=Multivariate vs. A/B Testing: Incremental vs. Radical Changes&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/multivariate-testing/&amp;text=Multivariate vs. A/B Testing: Incremental vs. Radical Changes&amp;via=nngroup" data-share-type="Twitter">

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

</span>Radical redesigns are best tested using an A/B experiment, while multivariate tests indicate how various UI elements interact with each other and support incremental improvements to a design.

</div>

<div class="article-body">

<p>In the world of design-optimization methods, A/B testing gets all the attention. Multivariate testing is its less understood alternative, often deemed too time-consuming to be worth the wait. While this method has its limitations, they are counterbalanced by its benefits, which cannot be easily achieved using A/B testing alone.</p>

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

<a class="ga-article-toc-item" href="#toc-multivariate-testing-mvt-1">Multivariate Testing (MVT)</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-difference-between-multivariate-testing-and-ab-testing-2">Difference Between Multivariate Testing and A/B Testing</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-mvt-measures-interactions-between-elements-3">MVT Measures Interactions Between Elements</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-limitations-of-mvt-4">Limitations of MVT</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-use-mvt-to-refine-a-design-not-completely-change-it-5">Use MVT to Refine a Design, Not Completely Change It</a>

</li>

</ul>

</div>

</div><h2 id="toc-multivariate-testing-mvt-1">Multivariate Testing (MVT)</h2>

<p>Let’s assume you wanted to optimize the design of a live product-detail page in order to maximize <a href="https://www.nngroup.com/articles/conversion-rates/">conversions</a> for adding the item to the user’s cart. You are considering several possible changes:</p>

<ul>

<li>Using a video of a product instead of an image</li>

<li>Changing the label of the main call-to-action button from <em>Buy Now </em>to <em>Add to Cart</em></li>

</ul>

<p>A <strong>multivariate test can help you decide which combination of these design choices</strong> would optimize conversions.</p>

<p>Let’s first clarify some terminology:</p>

<ul>

<li>

<p><strong>Variable:</strong> A UI element (such as an image or headline) with multiple possible design versions</p>

<p>In our ecommerce example, the variables are the visual representation of the product and the label of the call-to-action button.</p>

</li>

<li>

<p><strong>Variant:</strong> Each design version of a variable</p>

<p>The product image and the product video represent the two variants for the visual-representation variable; the <em>Add to Cart </em>and the <em>Buy Now </em>labels are the variants of the call-to-action.</p>

</li>

<li>

<p><strong>Variation:</strong> The resulting design containing a variant of each variable, to be compared with other variations</p>

<p>In our example, there would be 4 design variations, corresponding to all the possible combinations of the variables’ variants: image × <em>Add to Cart</em>, image × <em>Buy Now, </em>video × <em>Add to Cart, </em>video × <em>Buy Now</em>.</p>

</li>

</ul>

<blockquote style="padding-top:0;margin-top:1.25rem;">

<p>Definition: A multivariate test (MVT) is a design-optimization method in which <strong>multiple variants of specified variables</strong> are tested in a user interface, with the goal of maximizing conversions (either major conversions like completing an order, or <a href="https://www.nngroup.com/articles/micro-conversions/">micro conversions</a> like interacting with a feature on a page). This method determines which combination of the variants results in the highest performing design (in terms of the conversion goal specified).</p>

</blockquote>

<figure class="caption"><img alt="Diagram showing UI with 2 variants for 2 variables identified." loading="lazy" src="https://media.nngroup.com/media/editor/2018/03/16/mvt.png"/>

<figcaption><em>In a multivariate test, 2 or more design elements (the variables) are tested. Each of these variables could have multiple variants. For example, in the above page we could test 2 variables: visual representation for a product (with 2 variants: an image or a video) and label for the main call-to-action (with 2 variants: </em>Buy Now<em> or </em>Add to Cart<em>).</em></figcaption>

</figure>

<h2 id="toc-difference-between-multivariate-testing-and-ab-testing-2">Difference Between Multivariate Testing and A/B Testing</h2>

<p>Multivariate testing is often regarded as a type of<a href="https://www.nngroup.com/articles/putting-ab-testing-in-its-place/"> A/B testing</a>, although its setup and strengths are somewhat different. Here are the similarities and differences between them:</p>

<ul>

<li>Both methods test design variations against each other by dividing live site (or application) traffic across variations.</li>

<li>Both measure which design alternative (i.e., variation) leads to the highest rate of conversions for specified goals.</li>

<li>In an A/B test, the variations being tested could be completely different from each other, and not the result of manipulating a small set of variables. For instance, you could have two pages with completely different layouts, different copy, different navigation, different visual design, and so on. The result of the A/B test will indicate that one variation performs better than the other, but you will not know whether it’s because your copy is better, your visual design is better, or your layout is better (or the combination).</li>

</ul>

<p>In contrast, if you use MVT, you will usually be able to assign credit to one particular variant or combination of variants. Thus, you may, for example, find out that a product video makes a much bigger difference in your conversions than changing the button label, which can give you further strategy and design insights (for instance, it may tell you that it’s worthwhile to invest in producing good product videos).</p>

<h2 id="toc-mvt-measures-interactions-between-elements-3">MVT Measures Interactions Between Elements</h2>

<p>Let’s come back to our original ecommerce example. You may wonder whether two sequential A/B tests would produce the same result as an MVT.  Specifically, let’s pretend that you’d first run an A/B test to compare the video vs. the image — assume that the video wins. Next, on the winning variation (i.e., video), you’d do another A/B test between the two possible button labels, and the <em>Buy Now </em>label proved better. Wouldn’t this result be equivalent with the MVT test?</p>

<p>The answer is: not necessarily. It may be the case that the optimal combination is image × <em>Buy Now</em>, but you won’t have tested that version.</p>

<p>The main advantage of running a multivariate test rather than an A/B test is the <strong>ability to determine how various elements on a page interact</strong> with one another. Only by testing each combination of various variants can you not only figure out that visual A performs better than visual B, and that button C performs better than button D, but you can also <strong>discover the best combination </strong>of these overall.</p>

<h2 id="toc-limitations-of-mvt-4">Limitations of MVT</h2>

<p>The variations generated from every combination of the variants multiply like rabbits. Even our fairly simple ecommerce example has 4 design variations to compare, corresponding to all the possible combinations between the 2 variables. Adding 1 more variant for the call-to-action variable (e.g., <em>Purchase</em>) would create 2 more variations — generated by combining this variant with the other 2 variants of the visual-representation variable. (In general, the number of variations will be obtained by multiplying number of variants for each variable; so if you had 2 variables, one with 2 and the other with 3 variants, you’ll get 2×3=6 variations.)</p>

<figure class="caption"><img alt="Diagram showing 4 combinations of the variants" loading="lazy" src="https://media.nngroup.com/media/editor/2018/03/16/4variations.png"/>

<figcaption><em>Two variables that have each 2 variants leads to 4 design variations in a multivariate experiment, to represent all the possible combinations of these variants.</em></figcaption>

</figure>

<p>The large number of variations that need to be tested in a multivariate test leads to this method’s greatest limitation: much <strong>more traffic is typically required to run a multivariate test</strong> compared to an A/B test, in order to reach statistical significance. This is because each variation added to the comparison causes the live traffic to be divided into smaller pieces, and thus it also can take a long time to gather enough data points for each design alternative. (However, keep in mind that the time needed to run the test is dependent not only on the overall traffic, but also on the expected change in conversion rate for the experiment goal, because bigger improvements are easier to measure than tiny differences.) In general, splitting the live traffic among more variations leads to longer-running experiments.</p>

<p>Another limitation of MVT is that<strong> all combinations of the variants must make sense</strong> together. For example, when testing variants of an image and of a headline on a page, don’t write headlines that refer to details of an image variant (such as “Great Spa Vacations” vs. “Great Beach Vacations” with corresponding photos), because each headline will accompany each image in a variation for the test. That type of experiment would be better set up as an A/B test, so the combinations could be more controlled.</p>

<h2 id="toc-use-mvt-to-refine-a-design-not-completely-change-it-5">Use MVT to Refine a Design, Not Completely Change It</h2>

<p>Multivariate testing is a great way to <strong>make incremental improvements to a design</strong>, rather than dramatic redesigns. Because it requires that you identify certain elements of interest on a page to test multiple variants of that variable, you cannot easily compare radical changes across variations.</p>

<figure class="caption"><img alt="Diagram showing A/B test for radical page redesigns compared to MVT for incremental improvements." height="761" loading="lazy" src="https://media.nngroup.com/media/editor/2018/03/16/whentousewhich.png" width="1384"/>

<figcaption><em>For major redesigns, run an A/B test between the original and the proposed new version to find which is better. Then, refine various elements of the winning design using multivariate tests. Always keep iterating!</em></figcaption>

</figure>

<p>If your goal is to move towards a substantial redesign (such as major layout redesign), an A/B test to compare this new design against the current one is more appropriate than an MVT. <strong>Once the higher-performing design is discovered, use multivariate tests to further refine specific elements</strong> in the winning layout.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Analytics and User Experience" href="/courses/analytics-and-user-experience/?lm=multivariate-testing&amp;pt=article">

<h4 class="title heading-small">Analytics and User Experience</h4>

<p id="analytics-and-user-experience" class="description body-small">

Study your users’ real-life behaviors and make data-informed design decisions

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-research" />

</svg>

<p class="ux-specialty ux-research">Research</p>

</div>

</div>

</a>

</li>

<li>

<a class="tile ga-article-related-course" data-course-title="Measuring UX and ROI" href="/courses/measuring-ux/?lm=multivariate-testing&amp;pt=article">

<h4 class="title heading-small">Measuring UX and ROI</h4>

<p id="measuring-ux-and-roi" class="description body-small">

Use metrics from quantitative research to demonstrate value

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-research" />

</svg>

<p class="ux-specialty ux-research">Research</p>

</div>

</div>

</a>

</li>

<li>

<a class="tile ga-article-related-course" data-course-title="Personas: Turn User Data Into User-Centered Design" href="/courses/personas/?lm=multivariate-testing&amp;pt=article">

<h4 class="title heading-small">Personas: Turn User Data Into User-Centered Design</h4>

<p id="personas-turn-user-data-into-user-centered-design" class="description body-small">

Create, maintain, and utilize personas throughout the UX design process

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-research" />

</svg>

<p class="ux-specialty ux-research">Research</p>

</div>

</div>

</a>

</li>

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">a/b testing,Analytics &amp; Metrics,Research Methods</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Analytics &amp; Metrics</span>

<a class="ga-article-related-topic" href="/topic/analytics-and-metrics/">Analytics &amp; Metrics</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/research-methods/">Research Methods</a>

</li>

</ul>

</div>

</div>

</div>

</div>