# Supporting Multiple-Location Users - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">2</span>

<div class="article-header">

<h1 class="article-h1">Supporting Multiple-Location Users</h1>

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

May 25, 2002

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2002-05-25</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Supporting Multiple-Location Users&amp;body=https://www.nngroup.com/articles/supporting-multiple-location-users/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/supporting-multiple-location-users/&amp;title=Supporting Multiple-Location Users&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/supporting-multiple-location-users/&amp;text=Supporting Multiple-Location Users&amp;via=nngroup" data-share-type="Twitter">

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

</span>About half of the users now access the Internet from more than one location. Despite the implications of this for service design, many systems assume that users remain bound to a single computer.

</div>

<div class="article-body">

<p>Deeply buried inside a <a class="out" href="http://www.ntia.doc.gov/ntiahome/dn/html/Chapter4.htm" title="'A Nation Online: How Americans are Expanding Their Use of the Internet,' National Telecommunications and Information Administration, U.S. Department of Commerce, February 2002"> recent report from the U.S. Department of Commerce</a> is an interesting data nugget with profound implications for the future of the Internet: In September 2001, 45% of U.S. Internet users accessed the Net from <em> both </em> their home and outside locations (typically work). By contrast, in 1998, only 20% of Internet users accessed the Net from more than one location.</p>

<p>In only three years, Internet use has <strong> changed from being overwhelmingly a single-location </strong> activity to being a <strong> multiple-location activity for almost half of all users</strong>. Given that the census data is already six months old, I wouldn't be surprised if the percentage of multi-location users had increased to more than half by now.</p>

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

<a class="ga-article-toc-item" href="#toc-putting-it-together-1">Putting It Together</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-design-implications-2">Design Implications</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-more-users-more-need-for-usability-3">More Users = More Need for Usability</a>

</li>

</ul>

</div>

</div><h2 id="toc-putting-it-together-1">Putting It Together</h2>

<p>I know people who <strong> synchronize their office and home PCs by keeping both synchronized to a brick </strong> they strap to their belt and carry back and forth. The brick may be called a Palm Pilot, but it's still as close to the Stone Age as you come with modern technology.</p>

<p><span style="font-size: 12px;">Both my Blackberry PDA and my main workstation have always-on Internet connections. So why is it that the only way I can keep their address books and calendars synchronized is to plop the Blackberry into a primitive cradle? Why not send updates between the machines when the network has spare capacity?</span></p>

<p>Multi-computer user interfaces require <strong> seamless and invisible device coordination</strong>. If we rely on users to take explicit action, we'll always encounter situations where they've forgotten to do so, and the resulting lack of synchronization will create odd behavior in the overall system.</p>

<p><a class="old" href="/articles/the-network-is-the-user-experience-microsofts-net-announcement/" title="Alertbox June 2000: The Network is the User Experience: Microsoft's .NET Announcement">The network is the user experience</a>, and we should begin designing individual components to fit into this larger whole. Right now, it comes as a big surprise each time a piece of technology -- whether hardware, software, website, or Intranet service -- has to work with more than one other piece.</p>

<h2 id="toc-design-implications-2">Design Implications</h2>

<p>The significant increase in users who access the Internet from multiple locations has several key implications for system design.</p>

<ul>

<li><strong>Recognize individuals</strong>, not computers. Cookies are not a long-term solution for personalization and simplified log-in.</li>

<li><strong>Preserve settings and preferences </strong> across computers and devices.</li>

<li><strong>Synchronize data </strong> automatically. Or, at a minimum, offer users synchronization features.</li>

<li><strong>Create a seamless task flow hand-off </strong> as the user moves from one access point to another. Users should be able to stop in the middle of a transaction and resume it from a different computer without having to redo the initial steps.</li>

<li><strong>Provide a scalable UI</strong>. Some interface elements should appear only on full-featured devices, like desktop PCs. Nonetheless, the user experience must be recognizably the same, even on mobile systems and other less-capable devices that support only a UI subset.</li>

<li><strong>Abandon the firewall fantasy</strong>. Users need to access sensitive files from their laptops and home computers, so they transfer these files to their local hard disks. High-level CIA officials have done this; you can bet that average business professionals in your company violate security as well -- or they wouldn't get any work done. We must move to a security model in which all information is encrypted at all times, except when displayed on the monitor and viewed by an authorized user (possibly authenticated through eye-scanning).</li>

</ul>

<h2 id="toc-more-users-more-need-for-usability-3">More Users = More Need for Usability</h2>

<p>Another interesting piece of data in the Department of Commerce report: An estimated <strong> 54% of the U.S. population used the Internet </strong> in September 2001. This is a dramatic increase from the 33% reported three years earlier.</p>

<p><span style="font-size: 12px;">At last, half of the people in the U.S. are online, and other rich countries are recording similar statistics. We are still far from having </span><em style="font-size: 12px;"> everybody </em><span style="font-size: 12px;"> online, of course, and we continue to face the problem of slower growth in poorer countries.</span></p>

<p>Basically, we now have the <strong> entire elite online </strong> : Almost all early adopters, technology enthusiasts, and highly educated people use the Internet. The next decade will bring the usability challenge of making the Internet sufficiently easy for the other half of the population to use. Making something easy for a college graduate is a piece of cake compared to making it <a class="new" href="/articles/writing-for-lower-literacy-users" title="Alertbox: Lower-Literacy Users"> easy for a high-school drop-out</a>, but that's both our challenge and opportunity in the days to come.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Customer Journey Management" href="/courses/customer-journey-management/?lm=supporting-multiple-location-users&amp;pt=article">

<h4 class="title heading-small">Customer Journey Management</h4>

<p id="customer-journey-management" class="description body-small">

Build a crossfunctional journey-centric design approach that scales

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-management" />

</svg>

<p class="ux-specialty ux-management">Management</p>

</div>

</div>

</a>

</li>

<li>

<a class="tile ga-article-related-course" data-course-title="UX Roadmaps" href="/courses/roadmaps/?lm=supporting-multiple-location-users&amp;pt=article">

<h4 class="title heading-small">UX Roadmaps</h4>

<p id="ux-roadmaps" class="description body-small">

Set a strategic, practical plan to align, prioritize, and communicate UX work

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-management" />

</svg>

<p class="ux-specialty ux-management">Management</p>

</div>

</div>

</a>

</li>

<li>

<a class="tile ga-article-related-course" data-course-title="Becoming a UX Coach" href="/courses/ux-coach/?lm=supporting-multiple-location-users&amp;pt=article">

<h4 class="title heading-small">Becoming a UX Coach</h4>

<p id="becoming-a-ux-coach" class="description body-small">

Empower and guide UX and product teams to reach their full potential

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-management" />

</svg>

<p class="ux-specialty ux-management">Management</p>

</div>

</div>

</a>

</li>

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet,Strategy</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet</span>

<a class="ga-article-related-topic" href="/topic/mobile-and-tablet-design/">Mobile &amp; Tablet</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/strategy/">Strategy</a>

</li>

</ul>

</div>

</div>

</div>

</div>