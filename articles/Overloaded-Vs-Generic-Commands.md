# Overloaded vs. Generic Commands - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">3</span>

<div class="article-header">

<h1 class="article-h1">Overloaded vs. Generic Commands</h1>

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

December 18, 2011

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2011-12-18</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Overloaded vs. Generic Commands&amp;body=https://www.nngroup.com/articles/overloaded-vs-generic-commands/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/overloaded-vs-generic-commands/&amp;title=Overloaded vs. Generic Commands&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/overloaded-vs-generic-commands/&amp;text=Overloaded vs. Generic Commands&amp;via=nngroup" data-share-type="Twitter">

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

</span>Overloading different outcomes on similar commands can be confusing. Using the same command for multiple actions enhances usability if the results are conceptually the same.

</div>

<div class="article-body">

<p>One way to manage interaction design complexity is to have <strong> commands serve double duty</strong>. There are two ways of doing this, with different usability implications:</p>

<ul>

<li><strong>Generic commands </strong> use the same command in <strong> different contexts </strong> to achieve conceptually the <strong> same outcome</strong>, even though details of the specific effects might differ.</li>

<li><strong>Overloaded commands </strong> use variants of the same command to achieve <strong> different outcomes </strong> — sometimes depending on the context and other times depending on where the command appears on the screen.</li>

</ul>

<p>I <a class="old" href="/articles/generic-commands/" title="Alertbox: Generic Commands"> discussed generic commands in depth</a> in an earlier article. The most famous generic command these days is the <strong> pinch-zoom gesture </strong> , which works in most touchscreen user interfaces. In fact, the command is so pervasive that users expect it to work universally — and are sorely disappointed when they encounter an application that doesn't support it. Pinching outward sometimes enlarges text and other times enlarges pictures. Users don't know or care about the differences; they simply rely on the gesture as a generic command when they encounter stuff that's too small and want to make it bigger.</p>

<p><strong>Generic commands increase usability</strong>, because they allow users to learn one thing and use it many times. As further discussed in our training course on <a class="new" href="http://www.nngroup.com/courses/human-mind/" title="Nielsen Norman Group: detailed outline for training course"> The Human Mind and Usability: How Your Customers Think</a>, memories are strengthened by repeated activation, so the more places the command works, the better users will learn it.</p>

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

<a class="ga-article-toc-item" href="#toc-overloaded-commands-often-confusing-1">Overloaded Commands: Often Confusing</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-effective-command-reuse-2">Effective Command Reuse</a>

</li>

</ul>

</div>

</div><h2 id="toc-overloaded-commands-often-confusing-1">Overloaded Commands: Often Confusing</h2>

<p>You might think that overloaded commands are good as well. Having the same command achieve different (but similar) results sounds like an equally sound idea.</p>

<p>In practice, however, command overloading often confuses users:</p>

<ul>

<li>If a single command has different results depending on context, users often overlook the context and don't understand why they get different outcomes when doing the "same" thing.</li>

<li>When a single screen has multiple instances of what seems to be the same command, users often assume that the design is redundant and that all instances of the command will have the same effect. Or, when users simply grab onto the first instance they see, they often fail to notice that the command actually appears multiple times.</li>

</ul>

<p>A classic example of overloaded commands is websites with <strong> multiple search fields</strong>. I can't count how many times we've seen users issue a query in the wrong search on such sites. (However, there is an exception to the guideline to avoid multiple search fields: <a class="old" href="/articles/employee-directory-search-resolving-conflicting-usability-guidelines/" title="Alertbox: Employee Directory Search: Resolving Conflicting Usability Guidelines"> people finders on intranets</a>.)</p>

<p>We saw several examples of confusing command overloading in our recent <a class="old" href="/articles/kindle-fire-usability-findings/" title="Alertbox: Kindle Fire Usability Findings"> Kindle Fire user testing</a>. For example, the Condé Nast magazine app has one "home" button at the top of the screen that takes users to the list of magazines and another "home" button that takes users to the Kindle home screen:</p>

<p style="text-align: center; "><img alt="Two Kindle Fire screenshots, from different pages within Vanity Fair." height="132" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/conde-nast-overloaded-home.png" width="600"/><br/>

<em>Two home buttons in Condé Nast's Kindle Fire app. </em></p>

<p>These two buttons have different icons and appear in different locations, but they're still confusing.</p>

<p>Even worse, the "back" button has many different interpretations across different Kindle Fire apps:</p>

<ul>

<li>In many apps, "back" means "back to the previous screen" (which is the recommended use).</li>

<li>In ESPN, "back" means "back to home screen" (and should thus be a "home" button).</li>

<li>In <cite> The New York Times </cite> , "back" sometimes means "one step back" and sometimes means "two steps back." (When our users did a search and clicked through to an article, tapping "back" didn't return them to the search listing, but rather bounced them back one step further.)</li>

</ul>

<p>For a decade, one of the primary <a class="old" href="/articles/113-design-guidelines-homepage-usability/" title="113 Design Guidelines for Homepage Usability"> homepage usability guidelines</a> has been to designate a <strong> single page as the one and only official homepage </strong> for any given website. Users are confused when several pages are referred to as "home." In other words, don't use "home" as an overloaded command within a website. The main page for a subsite should be called something else, such as "foobar main page," "foobar overview," or — if you must — "foobar home" (within the site's foobar section).</p>

<p>For mobile apps, it's usually a good idea to have an "application home" that users can return to as a safe base after exploring the apps various areas. This is particularly important for content-rich apps, such as magazines or newspapers. Used this way, the "home" button serves as a generic command: conceptually, it always does the same thing, even though the specific place users return to differs in different apps.</p>

<p>In contrast, offering many different "homes" within the same site or app makes "home" an overloaded command, which is confusing.</p>

<p>A final example of the risks from overloaded command is the <a class="old" href="/articles/ipad-usability-year-one/" title="Alertbox: iPad Usability Year One"> swipe ambiguity we found in our iPad user testing</a>. When the same command (a swipe gesture) has different outcomes, depending on exactly where and how the user swipes, confusion results, unless the distinctions are clearer than they were in the apps we tested.</p>

<h2 id="toc-effective-command-reuse-2">Effective Command Reuse</h2>

<p>As these examples show, it can be a bit tricky to determine whether command reuse should count as a generic command (usually good) or an overloaded command (usually bad). There are two key deciding factors:</p>

<ul>

<li>Do people recognize that <strong> two contexts are different? </strong> For example, two different websites are usually so different that users wouldn't expect the two sites' "home" buttons to lead to identical destinations. In contrast, the context for two search boxes on the same screen is similar, even if the labels (which users rarely read) are different.</li>

<li>Do people view the <strong> outcomes as similar or different? </strong> For example, returning to the previous screen is a strong enough concept that users will view "back" commands as conceptually similar, even though the previously screens will usually differ.</li>

</ul>

<p>Both criteria depend on <strong> how users interpret </strong> the user interface. How can you know what they'll think? Well, you could analyze it yourself and try to judge the strength of the similarities and differences. But empirical testing is safer.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=overloaded-vs-generic-commands&amp;pt=article">

<h4 class="title heading-small">Application Design for Web and Desktop</h4>

<p id="application-design-for-web-and-desktop" class="description body-small">

Components, design patterns, workflows, and ways of interacting with complex data

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Application Design,Mobile &amp; Tablet</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Application Design</span>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/mobile-and-tablet-design/">Mobile &amp; Tablet</a>

</li>

</ul>

</div>

</div>

</div>

</div>