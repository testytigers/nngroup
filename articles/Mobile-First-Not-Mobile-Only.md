# Mobile First Is NOT Mobile Only  - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">9</span>

<div class="article-header">

<h1 class="article-h1">Mobile First Is NOT Mobile Only </h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Raluca Budiu, Kara Pernice</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/2023-04-portraits-raluca.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/kara-2025.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/raluca-budiu/">

Raluca Budiu</a> and

<a class="ga-article-author" href="/articles/author/kara-pernice/">

Kara Pernice</a></span>

<p class="publication-date">

July 24, 2016

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2016-07-24</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Mobile First Is NOT Mobile Only &amp;body=https://www.nngroup.com/articles/mobile-first-not-mobile-only/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/mobile-first-not-mobile-only/&amp;title=Mobile First Is NOT Mobile Only &amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/mobile-first-not-mobile-only/&amp;text=Mobile First Is NOT Mobile Only &amp;via=nngroup" data-share-type="Twitter">

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

</span>Mobile-navigation patterns make navigation unusable on the desktop and decrease the use of this important UI element. Porting an unchanged UI to a different platform hurts UX.

</div>

<div class="article-body">

<p>In a <a href="https://www.nngroup.com/articles/hamburger-menus/">recent study</a>, we found that hiding navigation under a menu significantly decreases the use of the navigation and also degrades the overall user experience both on desktop and on mobile.</p>

<p>While hiding navigation under an expandable menu can be a necessity on a small mobile device, it is not a practice that is native to the desktop; rather, it is a trend inspired by mobile and reinforced by <a href="https://www.nngroup.com/articles/responsive-web-design-definition/">responsive design</a>, a technology that allows the same content and functionality to be present on different screen sizes, but rearranged in layouts that are appropriate to the available screen spaces. Many responsive sites use a mobile-first approach to designing for multiple devices: they start with a design that is optimized for mobile and then port it to the desktop, under the assumption that simple is better across all devices, and a design that is simple and condensed enough so that it works for small screens will also provide a good user experience on large ones.</p>

<p>In this article we examine the consequences of porting mobile-first designs to the desktop, with a focus on navigation.</p>

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

<a class="ga-article-toc-item" href="#toc-about-our-study-1">About Our Study</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-navigation-usage-more-on-mobile-than-on-desktop-2">Navigation Usage: More on Mobile than on Desktop?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-design-patterns-borrowed-from-mobile-3">Design Patterns Borrowed from Mobile</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-optimize-for-each-device-4">Optimize for Each Device</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-porting-user-interfaces-creates-terrible-user-experience-5">Porting User Interfaces Creates Terrible User Experience</a>

</li>

</ul>

</div>

</div><h2 id="toc-about-our-study-1">About Our Study</h2>

<p>NN/g partnered with international remote-usability-testing firm, <a href="http://whatusersdo.com/?utm_campaign=nng_hamburger_sidebar&amp;utm_medium=referral&amp;utm_source=ext_article">WhatUsersDo</a>, to test 3 different types of navigation: hidden, visible, and a combination of hidden and visible navigation. As described in the <a href="https://www.nngroup.com/articles/hidden-navigation-methodology/">study methodology</a>, 179 users participated in our study; they completed tasks on 6 different websites, on desktops and smartphones:</p>

<ul>

<li>7digital (music, e-commerce)</li>

<li>BBC (news)</li>

<li>Bloomberg Business (business news)</li>

<li>Business Insider UK (business news)</li>

<li>Supermarket HQ (e-commerce)</li>

<li>Slate (news)</li>

</ul>

<p>For each site, we designed two types of tasks that involved finding specific content:</p>

<ol>

<li><strong>A navigation-optional task, </strong>which could be accomplished without using the navigation or search on the site, by simply selecting an item on the homepage</li>

<li><strong>A navigation-required task, </strong>which could only be accomplished through the use of navigation (or search — so even these tasks could be done without navigation)</li>

</ol>

<p>All the sites in our study were responsive, with the exception of Business Insider UK. By looking at the patterns that all of these sites employed, whether responsive or not, (e.g., the use of hidden navigation, repeating the navigation at the bottom of the page, using a search icon instead of a search box), we also surmise that most if not all of these sites were designed using mobile-first principles.</p>

<p>As discussed in our other articles, we collected several metrics; here, we focus on one of them: navigation use. This measure captured whether participants clicked on the navigation options during their tasks.</p>

<h2 id="toc-navigation-usage-more-on-mobile-than-on-desktop-2">Navigation Usage: More on Mobile than on Desktop?</h2>

<p>When we look at the differences between mobile and desktop navigation use, it is highly surprising that, on the sites that we included in our study, the <strong><a href="https://www.nngroup.com/articles/find-navigation-mobile-even-hamburger">navigation was used a lot more on mobile</a> <a href="https://www.nngroup.com/articles/find-navigation-desktop-not-hamburger/">than on desktop</a></strong>. (This difference was statistically significant with a paired t-test, p &lt;0.05.) Not only that, but comparing the navigation use on each site, on 5 out of the 6 sites, the navigation was used significantly more on mobile than on the desktop. (These differences were significant by N-1 2 proportion tests.) The exception was 7Digital, where we also recorded more navigation use on mobile but the difference was not statistically significant, and thus may just have been random.</p>

<figure class="caption"><img alt="" border="0" height="444" loading="lazy" src="https://media.nngroup.com/media/editor/2016/07/11/navuse.PNG" width="700"/>

<figcaption><em>Navigation usage was higher on the mobile versions of the sites than on the desktop versions of the sites.</em></figcaption>

</figure>

<p>This result is unexpected for several reasons:</p>

<ul>

<li>Making navigation <strong>easy to access</strong> is a notoriously hard task on mobile. Mobile pages are long and often as soon as users scroll down the first screenful, navigation placed at the top of the page is no longer visible. If they want to access it, they have to scroll back. (Sticky navigation or back-to-top buttons are sometimes used to alleviate this problem, but they often get ignored by users.)</li>

<li>Making navigation <strong>discoverable</strong> is also notoriously difficult on mobile. Lucky sites that only have 4–5 options in their main navigation can afford to make these options visible at the top of the screen, but the majority of sites must hide at least some of the navigation under an expandable menu. Because these menus hide a wide variety of items, by necessity, they have vague labels such as <em>Menu </em>or <em>Browse </em>with low <a href="https://www.nngroup.com/articles/information-scent/">information scent</a>. Users must actively think about turning to them as a problem-solving strategy when they are in trouble; they are not <a href="https://www.nngroup.com/articles/priming/">primed</a> by a label that resembles the content that they are looking for. As a result, people often ignore these menus, and sometimes they forget about them even after they’ve used them once within the same session.</li>

</ul>

<p>So how is it possible that on this platform with hard-to-use navigation, the navigation is still used a lot more than on the desktop? Did the mobile sites in our sample have exceptionally good navigation designs? If you look at the individual sites, you’ll see that they were not much different from the many navigation implementations on countless other mobile sites: either the much reviled hamburger menu or an homologue, plus, in some cases, a number of visible navigation links.</p>

<p>No. The proper way of describing our findings is not that these sites had discovered the secret of <a href="https://www.nngroup.com/articles/mobile-navigation-patterns/">mobile navigation</a> or that there was more navigation on mobile (in fact, the overall navigation usage on mobile was only a modest 63%), but, rather, that there was <strong>less navigation on the desktop</strong>. While these two statements are logically the same, the twist in perspective allocates the guilt where it belongs: to the desktop user interfaces, which were not up to the demands of this platform.</p>

<p>And why were the desktop designs worse? Because they were ported from a different platform — mobile. In other words, all of these sites were likely built to be mobile-first: they were optimized for mobile, and as a result the desktop user experience suffered significantly.</p>

<p>You can perhaps think of another possible explanation for why the navigation was used more on mobile. Because the mobile screen is too small and shows only a little content at the time, users have to scroll more to get the same amount of content that is displayed on a desktop screen. (That is indeed, a consequence of the fact that the <a href="https://www.nngroup.com/articles/scaling-user-interfaces">mobile–user communication channel is narrower in capacity</a>, and it’s also the reason why <a href="https://www.nngroup.com/articles/mobile-content-is-twice-as-difficult/">comprehension is poorer on mobile</a>). So maybe mobile users got tired of scrolling, so they decided to use navigation instead of fishing around for information on the page. That may be true; however, remember that our study included both navigation-required and navigation-optional tasks. If people were simply tired of scrolling on mobile, you’d expect to see more navigation use on mobile for the navigation-optional tasks that could be accomplished by clicking on a link on the homepage. But there should be no difference between mobile and desktop for the navigation-required tasks, that required the use of navigation to be completed.</p>

<p>But our data says otherwise: we found statistically significant differences for mobile and desktops for each type of tasks, both navigation-dependent and navigation independent. In other words, the reason why people used navigation less on the desktop was <em>not </em>that they didn’t need it; even in those situations where they couldn’t accomplish the task without the navigation, they used it in only 54% of the times, compared to 77% on mobile.</p>

<figure class="caption"><img alt="" border="0" height="418" loading="lazy" src="https://media.nngroup.com/media/editor/2016/07/11/bytask.PNG" width="700"/>

<figcaption><em>Navigation usage was higher on mobile irrespective of task type. Navigation-dependent tasks that required the use of navigation to be completed had an overall higher rate of navigation use. However, the navigation usage was still higher on mobile than on desktop even for these tasks.</em></figcaption>

</figure>

<h2 id="toc-design-patterns-borrowed-from-mobile-3">Design Patterns Borrowed from Mobile</h2>

<p>Which were some of the more important mobile-design patterns that the sites in our study borrowed for the desktop?</p>

<p><strong>Hidden navigation</strong>. Perhaps the expandable navigation menu (such as the hamburger menu) was the biggest offender and certainly the mobile-inspired pattern most relevant to our study. We’ve seen from many qualitative studies that <a href="https://www.nngroup.com/articles/killing-global-navigation-one-trend-avoid/">it doesn’t work on the desktop</a>, but sites still insist on using it.</p>

<p><strong>Repeated navigation at the bottom of the screen. </strong>One of the sites (7Digital) in our study has an expandable navigation menu at the top of the page and also repeats the navigation options at the bottom of the screen. This practice is often used on mobile to prevent users from having to scroll back to the top of the page to access the navigation positioned there.</p>

<p><strong>Sticky navigation at the top of the page. </strong>Some desktop sites (e.g., Bloomberg, Business Insider UK) chose to make the navigation sticky: that is, it remained present at the top of the page as users scrolled down or when they started to scroll up.</p>

<p><strong>Navigation in the top right corner. </strong>One of the desktop sites (Slate) placed the navigation in a highly nonstandard position for the desktop: the top right corner. This placement for the hamburger menu is a lot more common on mobile (where, in apps, the top left corner is often reserved for the <em>Back </em>button).</p>

<p><strong>Search icon instead of search box.</strong> Many of the sites also got rid of the search box on the desktop and preferred to use a search icon instead. We generally <a href="https://www.nngroup.com/articles/magnifying-glass-icon/">recommend against this practice on the desktop</a>; we’ve heard countless users complaining about having to locate a tiny icon on a large screen.</p>

<figure class="caption"><img alt="" border="0" height="644" loading="lazy" src="https://media.nngroup.com/media/editor/2016/07/11/slate-better-res.png" width="700"/>

<figcaption><em>Slate desktop (left) and mobile (right): the desktop site used a hamburger menu at the top of the right rail, in the top right corner of the page, a position highly nonstandard for desktop but fairly common on mobile. It also displayed a search icon instead of the traditional search box that people expect on the desktop.</em></figcaption>

</figure>

<figure class="caption"><img alt="" border="0" height="569" loading="lazy" src="https://media.nngroup.com/media/editor/2016/07/11/bbc.png" width="700"/>

<figcaption><em>BBC desktop (left) and mobile (right): The desktop site used a navigation bar with a </em>More<em> tab — similar with the </em>More<em> tab used to fit extra tabs in the iOS tab bar.</em></figcaption>

</figure>

<figure class="caption"><img alt="" border="0" height="582" loading="lazy" src="https://media.nngroup.com/media/editor/2016/07/11/businessins.png" width="700"/>

<figcaption><em>Business Insider desktop (left) and mobile (right): The desktop site used a hamburger menu for the desktop global navigation. The top blue bar was sticky: it stayed at the top of the page as the user scrolled down. Other mobile-inspired featured were the image-based, information-depleted layout and the search icon instead of a search box.</em></figcaption>

</figure>

<p>None of these patterns are either common or particularly usable or useful on desktop, yet they often work or are necessary on mobile. These sites found them valuable for their small-screen designs, and thought they should apply them to the desktop. Little did they know that they were throwing the baby out with the bath water: the desktop user experience suffered, and they created unnecessary problems.</p>

<h2 id="toc-optimize-for-each-device-4">Optimize for Each Device</h2>

<p>In our world of many interconnected devices, it is imperative to design for all of them. Agreed, it seems wasteful to have separate designs for every single device. But, different devices have different capabilities of interaction and different screen sizes. The amount of information that can be displayed on each of these devices at a time varies wildly and the same design will have a very different <a href="https://www.nngroup.com/articles/content-chrome-ratio">content-to-chrome ratio</a> on two different devices. For example, on a small mobile screen, a hamburger icon may be noticeable enough, but if you move the same icon to a large 27” screen, it will easily get lost.</p>

<p>Granted, you could make the hamburger bigger, like in the image below, which shows Slate’s homepage if the hamburger icon were sized to take the same fraction of the desktop screen as it does on an iPhone 6S. But we don’t advise you to use a design like this for several reasons:</p>

<ol>

<li><a href="https://www.nngroup.com/articles/logo-placement-brand-recall/">Right-aligned logos work worse than left-aligned logos</a> (but we retained the right-alignment here for the sake of comparison).</li>

<li>Icons this huge may still be overlooked due to <a href="https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/">banner blindness</a>.</li>

<li>If you do allocate this much space to navigation, you might as well show the links.</li>

</ol>

<figure class="caption"><img alt="Mockup of desktop homepage, magnifying the navigation icons to take up the same proportion of screen space on a 27-inch desktop monitor as they do on a smartphone screen" height="411" loading="lazy" src="https://media.nngroup.com/media/editor/2016/07/11/slate-big-icons-both.png" width="720"/>

<figcaption><em>Slate desktop homepage, as tested (left) and with icons resized to take up the same percentage of the screen on a 27-inch monitor as they do on an iPhone 6 screen (right). Since a good 27-inch monitor costs $180, it’s currently a typical purchase for business users.</em></figcaption>

</figure>

<p>We cannot ignore these differences when scaling user interfaces. We must take advantage of individual device strengths in order to produce designs that work across all screen sizes.</p>

<h2 id="toc-porting-user-interfaces-creates-terrible-user-experience-5">Porting User Interfaces Creates Terrible User Experience</h2>

<p>The history of user interface design has many examples of people replying on the shortcut of porting a UI from one platform to another. It never works:</p>

<ul>

<li>1980s: Taking a DOS program and porting it to Windows translates into a miserable user experience, as the resulting software doesn’t integrate GUI direct-manipulation features properly.</li>

<li>1990s: Taking a Windows program and porting it to Macintosh results in a substandard user experience, as the application doesn’t feel like a native Mac program. The look-and-feel is simply wrong, and the Apple magazines of the day rightfully savaged such ports in their reviews.</li>

<li>2000s: Taking a brochure or other print collateral and making it into a website results in a sluggish user experience, with little use of interactive features and impoverished navigation. Porting print content to online by making it into a <a href="https://www.nngroup.com/articles/pdf-unfit-for-human-consumption/">PDF blob</a> is even worse.</li>

<li>Late 2000s: Taking a website optimized for desktop use and offering it to mobile users results in an almost unusable user experience, as people get lost in overly elaborate menus and content that doesn’t fit the small screen.</li>

<li>2010: Taking a magazine designed for paper and <a href="https://www.nngroup.com/articles/ipad-usability-first-findings/">porting it to the iPad</a> results in a dreadful user experience, with users stuck into a nonhyperlinked world and crushed by the print metaphor.</li>

<li>Late 2010s: Taking a website optimized for mobile use and offering it to desktop users results in a degraded user experience, as we have seen in this article.</li>

<li>2020? Taking a mobile app and cramming it onto a <a href="https://www.nngroup.com/articles/smartwatch/">watch will also be terrible</a>. Let’s hope that history won’t repeat itself, though it surely will.</li>

</ul>

<p>Tempting as it may be to design once and use twice, it can result in a subpar user experience for one of the platforms, and maybe for both of them. Providing content and feature parity across devices is a great goal, but it doesn’t mean that all the UI elements and the design must also stay exactly the same. Each UI platform has different capabilities leading to different design requirements for an optimized user experience. Serving users on multiple platforms requires a multiplatform design strategy.</p>

<p> </p>

<h3>Other Articles Related to the NN/g Hidden-Navigation Study</h3>

<p><a href="https://www.nngroup.com/articles/hamburger-menus/">Hamburger Menus and Hidden Navigation Hurt UX Metrics</a></p>

<p><a href="https://www.nngroup.com/articles/hidden-navigation-methodology/">Hidden- and Visible-Navigation Study: Methodology</a></p>

<p><a href="http://www.nngroup.com/articles/find-navigation-mobile-even-hamburger/">How to Make Navigation (Even Hamburger) Discoverable on Mobile</a></p>

<p><a href="http://www.nngroup.com/articles/find-navigation-desktop-not-hamburger/">Beyond the Hamburger: How to Make Navigation Discoverable on Desktops</a></p>

<p> </p>

<p>Learn more about scaling user interfaces across different devices in our full-day <a href="https://www.nngroup.com/courses/scaling-responsive-design/">course</a>.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Mobile User Experience" href="/courses/usability-mobile-websites-apps/?lm=mobile-first-not-mobile-only&amp;pt=article">

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

<li>

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=mobile-first-not-mobile-only&amp;pt=article">

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

<li>

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=mobile-first-not-mobile-only&amp;pt=article">

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

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">hamburger,mobile navigation,Mobile &amp; Tablet,Navigation,Web Usability</span>

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

<a class="ga-article-related-topic" href="/topic/web-usability/">Web Usability</a>

</li>

</ul>

</div>

</div>

</div>

</div>