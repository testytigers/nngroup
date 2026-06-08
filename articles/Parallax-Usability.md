# What Parallax Lacks - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">7</span>

<div class="article-header">

<h1 class="article-h1">What Parallax Lacks</h1>

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

January 20, 2019

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2019-01-20</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: What Parallax Lacks&amp;body=https://www.nngroup.com/articles/parallax-usability/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/parallax-usability/&amp;title=What Parallax Lacks&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/parallax-usability/&amp;text=What Parallax Lacks&amp;via=nngroup" data-share-type="Twitter">

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

</span>Parallax-scrolling effects add visual interest, but they often create usability issues, such as content that is slow to load or hard to read. Consider if the benefits are worth the cost.

</div>

<div class="article-body">

<p>Several years ago, a colleague and I ventured out to test a new design trend that was winning web-design awards and earning praise on designer forums. That trend was parallax scrolling. We were not impressed. More importantly, neither were users (for reasons I’ll explain below). After a short couple of years, the parallax trend slowly faded away, likely because those early adopters saw the same results we did: harm to the user experience or lukewarm user reactions, at best. The outcomes didn’t justify the work that went into creating and maintaining elaborate parallax-scrolling effects, and so the trend dwindled in popularity. For a while.</p>

<p>Fast forward to today. Just when we thought the web was safe, parallax scrolling is making a comeback. Like a sequel to a movie, our testing today reveals a familiar cast and storyline: unimpressed users and a range of usability issues. In this sequel, however, parallax scrolling is more restrained than the original. If the earlier parallax implementations were a horror show of usability issues, the modern version is closer to a PG-13 family comedy: not particularly entertaining, but also not likely to send people screaming to close the tab.</p>

<blockquote>

<p>The <strong>parallax animation </strong>effect is created by two or more layers of an interface moving at different speeds or in different directions in order to produce an impression of depth.</p>

</blockquote>

<p>(To understand why parallax design induces this illusion, try this experiment: hold up both of your hands in front of your face, with one hand as far away as you can stretch your arm, and the other hand halfway between the first hand and your eyes. Now move your head from left to right while holding your hands steady: it’ll look as if the two hands are moving relative to each other, particularly if you close one eye so that you get a 2D view.)</p>

<p>The animated GIF below shows an example of parallax scrolling on a restaurant’s website.</p>

<figure class="caption"><img alt="Animated GIF of parallax animation on a restaurant website" height="398" loading="lazy" src="https://media.nngroup.com/media/editor/2018/09/28/parallax_example.gif" width="692"/>

<figcaption><em>RestaurantLeDuc.com: In this example of parallax scrolling, the fish and the white menu boxes move at different speed than the scrolling background, creating the impression of being layered on the screen.</em></figcaption>

</figure>

<p>In this article, we’ll discuss why parallax is a popular trend, why it can be problematic, and how it can still sometimes be used to enhance user experience.</p>

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

<a class="ga-article-toc-item" href="#toc-why-designers-use-parallax-1">Why Designers Use Parallax</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-4-problems-with-parallax-2">4 Problems with Parallax</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-make-it-work-use-restraint-and-put-users-in-control-3">Make It Work: Use Restraint and Put Users in Control</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-4">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-why-designers-use-parallax-1">Why Designers Use Parallax</h2>

<p>If you ever played early video games, you may remember the parallax effect. Game designers moved objects in the foreground and background separately, to add depth to the game universe and make players feel immersed in it. The same desire to offer an “immersive” experience on the web often motivates the use of parallax effects by website designers, who assume that such effects make for a creative, unique branding statement and a memorable design.</p>

<p>Another reason for using parallax is to call attention to certain page elements. The velocity of motion is a <strong>preattentive trait</strong>: an object that moves at different speed than everything else in a scene stands out like a cheetah sprinting through open grasslands; people will notice it without making any explicit effort to search for it.</p>

<p>Unfortunately, <strong>parallax effects come with some costs</strong>. Designers need to know what their risks and benefits are.</p>

<h2 id="toc-4-problems-with-parallax-2">4 Problems with Parallax</h2>

<p>For sites considering adopting (or readopting) this trend, let’s look at some of the top UX issues with the parallax scrolling effect.</p>

<ol>

<li><strong>Parallax-presented content can be difficult to control.</strong> While parallax is supposed to draw attention to the animated elements, often these elements end up being ignored. Most users in our testing don’t wait for parallax effects to load: they scroll quickly, scanning for keywords of interest. Because this effect takes time, goal-oriented users looking for specific information may miss important content presented using parallax.

<p><strong>Pages can take longer to load</strong> when parallax animations are used. On the Apple site, some users scrolled and saw almost nothing on the screen, because the parallax effects hadn’t animated yet. Blank screens are not what designers intended, nor are they what users came to see.</p>

<div>

<figure class="caption"><img alt="Slow-loading parallax effects resulted in three near-blank screens on an iPhone" height="393" loading="lazy" src="https://media.nngroup.com/media/editor/2018/09/28/applecom_mob_parallax-blankscrolls.png" width="692"/>

<figcaption><em>Apple.com: A study participant encountered screens of blank space, because the parallax-animated text and images hadn’t loaded as quickly as he had scrolled down. The user had to keep scrolling to get the content to appear, then he scrolled back up to the start of each section so that he could read the text and look at the images.</em></figcaption>

</figure>

</div>

<p>But too fast parallax can be a problem, too: when the animation is tied to users’ scrolling speed, people may not get a chance to read animated text if they scroll too fast. One user scrolling on the <em>New York </em>Times mobile site noticed a panel of text scroll up and past the graph she was reading. She commented, “Oh, that happened so quickly I didn’t even get to read it.” The effect delayed her ability to interpret the graph and feel in control of the experience.</p>

<div>

<figure class="caption"><img alt="A block of parallax-animated text scrolled quickly off the screen" height="686" loading="lazy" src="https://media.nngroup.com/media/editor/2018/09/29/nytimescom_parallax_quickscroll.gif" width="350"/>

<figcaption><em>NYTimes app for iPhone: A fast-scrolling user caused parallax-animated text to scroll so quickly over and then off the user’s screen that she didn’t have time to read it.</em></figcaption>

</figure>

</div>

</li>

<li><strong>Too much movement, especially of text, can be dizzying.</strong> Using parallax to animate many different page elements and blocks of text <a href="https://www.nngroup.com/articles/scroll-animations/">makes reading hard</a> and can even cause people to feel sick. If this sounds exaggerated, remember that in 2013, Apple released an update to <a href="https://www.nngroup.com/articles/ios-7/">iOS 7</a> that allowed users to <em>Reduce Motion</em>, because the parallax animations for task switching caused many people to feel symptoms of vertigo, nausea, and dizziness. Having learned from that mistake, let’s hope future parallax <a href="https://www.nngroup.com/articles/distracted-driving-ux/">doesn’t cause harm</a>.</li>

<li><strong>Parallax effects might be missed entirely.</strong> By now, users have learned that many advertisers use motion to attract attention. Some people purposefully ignore movement on a page because of the association with unwanted advertisements. On mobile, subtle parallax effects are easily missed because the user’s hand can block animations that appear underneath. Overlooking the parallax effects may not be harmful to the experience (as long as the content doesn’t go away), but designers should consider whether these effects are worth the effort to build and maintain.</li>

<li><strong>Parallax is just <em>not that impressive to users</em>.</strong> The people most likely to appreciate parallax effects? Other designers or developers. When you know what goes in to building something complex like long-scrolling parallax pages, you can appreciate the work. But, to put it bluntly, average users could care less. Today, users’ reaction is the same as five years ago: indifference. They aren’t “wowed.” User-testing participants don’t stop to comment on how cool the effects are; they don’t scroll up and down for fun, to watch the effects bring the page to life. They don’t pause to watch each effect smoothly transition into the main content area. Instead, the vast majority of <strong>people are focused on content</strong>, and so the animation effects are an afterthought, if they’re noticed at all. The question to designers, then, becomes: is parallax the best way to impress users or make a brand statement?</li>

</ol>

<p>(A note about doing user research on the impact of parallax or other animations: if you prompt users to talk about the animation on scroll, you might hear comments that praise the interaction design. Use caution before celebrating such comments: sometimes users say one thing, but their behavior shows a completely different reality. As soon as you’ve directed users’ attention to a feature, you’ve biased their interpretation of that feature. For example, at the very end of two testing sessions in which one participant struggled to control the parallax-animated text blocks and the other did not notice them, we asked people about any movement they saw on the page. That was when they gave praise, with comments like “Oh that’s so cool” or “That’s so cute how it appears as you go down the page.” But we shouldn’t forget what really happened when they were trying to find an answer or read an article: they struggled or ignored the parallax.)</p>

<h2 id="toc-make-it-work-use-restraint-and-put-users-in-control-3">Make It Work: Use Restraint and Put Users in Control</h2>

<p>As I said at the beginning of this article, the latest iteration of parallax is subtler than five years ago. This is a good thing. Remember that parallax is a form of animation, and, <a href="https://www.nngroup.com/articles/animation-usability/">for most animations, less is more</a>.</p>

<p><strong>No task, no problem. </strong>Parallax is safest in environments where users are browsing for leisure, without a specific goal or task in mind. In those cases, parallax can be used to support a narrative or to contribute to a brand’s identity. If you’re not sure whether your use case fits this category, you can always refer to <a href="https://www.nngroup.com/videos/3-bs-design-trends/">the 3 Bs Test</a> to see if parallax is a good choice for your business and your users.</p>

<p><strong>If users have a task, put content first. </strong>The ultimate test of parallax usability is whether users can easily and quickly complete their task. To start, here are some suggestions:</p>

<ul>

<li><a href="https://www.nngroup.com/articles/in-page-links/">Provide in-page navigation links</a> on long scrolling parallax pages, so that scrolling isn’t the only way to navigate down the page. Use noticeable navigation UI, not just small vertical dots, which are likely to be missed (and have poor <a href="https://www.nngroup.com/articles/information-scent/">information scent</a>).</li>

<li>Save parallax effects for background or peripheral images, so that they are easy to ignore and don’t detract from the content.</li>

<li>Once users have scrolled down the page and triggered all the parallax effects on the way down, leave those objects in their final positions, instead of reanimating each object on scroll up or scroll down. In a goal-oriented context, once users begin to go up and down a page, it’s because they’re looking for information. Forcing people to rewatch parallax effects delays their access to that information and can quickly become tedious and irritating. It’s like listening to the same joke again and again. Show restraint here, and your users will benefit.</li>

</ul>

<p>In the following example, parallax scrolling animations are used to circle key descriptions of an iPad. The animations are subtle, but they call attention to key features about the device. They also remain in place — the keywords remain circled — as users scroll up or down the page. (Note that this is the same page that suffered slow page-load times caused by the larger parallax effects of iPad images sliding into view. The smaller subtler effects are not likely to cause such delays).</p>

<p> </p>

<figure class="caption"><img alt="Parallax animations circle and underline keywords as a user scrolls" height="398" loading="lazy" src="https://media.nngroup.com/media/editor/2018/09/28/parallax_ipad.gif" width="692"/>

<figcaption><em>On the iPad product page, users didn’t notice the subtle parallax animations, for example underlining or circling callout text. But the effects did not interfere with users’ ability to read the page. The markup-style animation also reinforced some of the page content, by showcasing the possibilities of using the Apple pencil with the tablet.</em></figcaption>

</figure>

<p> </p>

<h2 id="toc-conclusion-4">Conclusion</h2>

<p>Trends may come and go, but human behavior remains largely unchanged. The risks of parallax effects remain the same as years ago, because people are still focused on their goals and they are impatient with slow-loading sites. Fortunately, we can learn from past mistakes. If your team is considering parallax, make sure that it won’t intrude on users, slow them down, or take away their ability to quickly and easily find what they came for.</p>

<h3>Reference:</h3>

<p>Healey, C.G., <em>Perception in visualization</em> Department of Computer Science, North Carolina State University, available at: <a href="https://www.csc2.ncsu.edu/faculty/healey/PP/">https://www.csc2.ncsu.edu/faculty/healey/PP/</a></p>

<p> </p>

<p> </p>

<p> </p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=parallax-usability&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">animation,Visual Design,scrolling,readability</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Visual Design</span>

<a class="ga-article-related-topic" href="/topic/visual-design/">Visual Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>