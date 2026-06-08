# Overuse of Overlays: How to Avoid Misusing Lightboxes - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">14</span>

<div class="article-header">

<h1 class="article-h1">Overuse of Overlays: How to Avoid Misusing Lightboxes</h1>

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

May 25, 2015

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2015-05-25</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Overuse of Overlays: How to Avoid Misusing Lightboxes&amp;body=https://www.nngroup.com/articles/overuse-of-overlays/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/overuse-of-overlays/&amp;title=Overuse of Overlays: How to Avoid Misusing Lightboxes&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/overuse-of-overlays/&amp;text=Overuse of Overlays: How to Avoid Misusing Lightboxes&amp;via=nngroup" data-share-type="Twitter">

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

</span>Poorly implemented overlays and lightboxes are not only frustrating for users, but can also be disastrous for conversion and task completion. Use the five W’s – Who, What, When, Where, and Why – to determine whether an overlay is truly the most appropriate design solution, and how you should implement it.

</div>

<div class="article-body">

<p>When lightboxes and overlays first appeared a few years ago, they provided an elegant solution to a tricky interaction-design challenge: how to convey important information without losing the context of the current screen, while minimizing some of the problems created by pop-ups and dialog boxes. We even recognized the lightbox as the application-design <a href="http://www.nngroup.com/articles/10-best-application-uis/">technique of the year</a> in 2008.</p>

<blockquote>

<p>Definition: An <strong>overlay</strong> refers to a content box that is displayed on top of another page. The overlay box is usually noticeably smaller than the underlying page. Often the rest of the background page is obscured, leading to the use of the term ‘lightbox’ to describe this visual effect of heightened focus on the overlay content.    </p>

</blockquote>

<p>Since this technique first appeared, designers have adopted lightboxes with a vengeance. Only last week at our <a href="http://www.nngroup.com/training">Usability Week conference</a>, a designer approached me to ask, ‘is it ok to use anchor links within a lightbox?’ The overlay in question had so much content that it required a scrollbar, and getting all the way to the bottom required a LOT of scrolling. In order to minimize the need to scroll, the team was now considering adding anchor links – with a side benefit of creating link targets so that other pages could send users directly to the overlay content. In case you’re having trouble visualizing this, here’s an example of a similar design, in the <em>Support </em>section of Apple.com. </p>

<p><img alt="Screenshot of the support overlay window for delayed email on Apple.com" height="593" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/apple-mobile-me-support-overlay.png" width="802"/></p>

<p><em>Apple’s MobileMe support section used to present help content in an overlay window, including a link to another help article about spam and a scrollbar to access lower-level content. </em></p>

<p>Scrolling and anchor links make sense on very long web pages. But if you find yourself adding <strong>multiple navigation mechanisms within an overlay</strong>, it’s time to <strong>stop</strong> and reevaluate your approach. Apple has since modified its design to completely eliminate the overlay, and instead simply display the content as a (new) full page. As a result, the viewable content area is much larger and uses the normal browser scrollbar, allowing users all the standard controls they're used to. The standalone page also allows users to easily save and share links to this content — a very important usage scenario for help content. Apple has even avoided using an overlay for a survey invitation, and instead shows it in a feature box at the top of the page. </p>

<p><img alt="Screenshot of Apple.com email delay support page with no overlay" height="583" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/apple-mobile-me-support-no-overlay.png" width="787"/></p>

<p><em>The current version of Apple’s email-delay support content completely eliminates the overlay and instead displays support information as a new page. </em></p>

<p>Overlays are sometimes appropriate, but as illustrated in the example above, all too often they are <strong>overused or misused</strong>. Sometimes this happens with the best of intentions: designers want to provide quick access to important information. In other cases, lightboxes appear to be used purely for the designer’s convenience, as a way to provide more features or content without having to create a new page or modify the navigation.</p>

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

<a class="ga-article-toc-item" href="#toc-considerations-when-using-overlays-1">Considerations When Using Overlays</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-who-is-the-target-audience-2">WHO Is the Target Audience?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-what-action-is-the-user-supposed-to-take-3">WHAT Action Is The User Supposed To Take?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-when-will-the-overlay-appear-and-will-it-interrupt-an-important-task-4">WHEN Will the Overlay Appear, and Will It Interrupt an Important Task?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-where-will-the-overlay-appear-on-the-page-5">WHERE Will the Overlay Appear on the Page?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-why-does-this-content-need-to-be-in-an-overlay-instead-of-being-within-a-page-6">WHY Does This Content Need to Be in an Overlay Instead of Being Within a Page?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-7">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-considerations-when-using-overlays-1">Considerations When Using Overlays</h2>

<p>Many designers are familiar with a few standard <strong>guidelines for using overlays</strong>, such as:</p>

<ul>

<li>Provide a <strong>visible ‘close’</strong> command to allow users to return to the underlying page.</li>

<li>Ensure that the overlay box is visually<strong> distinct from the background</strong> page by making it smaller and using translucent shading to obscure the background (which indicates that the underlying content isn’t currently interactive, and also lets the user know that they haven’t actually navigated to a new page).</li>

<li>Make overlay content <strong>accessible</strong> to keyboard users (by allowing the <em>Escape</em> key to close the overlay, and by providing keyboard access to content and fields within the overlay).</li>

</ul>

<p>But you can follow all of these rules and still end up with a frustrating experience — sometimes one that is so bad that users are not just annoyed, but literally prevented from accessing content and completing tasks. To avoid these situations, use a systematic process to analyze your design problem and make sure an overlay is the most appropriate solution.  Just because you <strong>can </strong>use an overlay doesn’t mean you <strong>should. </strong></p>

<p>When considering an overlay, lightbox, or modal window, ask yourself the following questions:</p>

<ul>

<li><strong>Who </strong>is the target audience?</li>

<li><strong>What </strong>action is the user supposed to take?</li>

<li><strong>When </strong>will the overlay appear, and will it be an interruption?</li>

<li><strong>Where </strong>will the overlay appear on the page?</li>

<li><strong>Why</strong> does this need to be in an overlay instead of within a page?</li>

</ul>

<h2 id="toc-who-is-the-target-audience-2">WHO Is the Target Audience?</h2>

<p>If your users are on a mobile device, showing them an overlay designed for a large desktop screen is at best disorienting; at worse, it can completely block users from accessing your content.</p>

<ul>

<li><strong>Disorientation</strong>.  The Viafoura.com website illustrates the disorienting effect of overlay conversion forms for mobile users; after clicking a button named <em>Request a Free Trial</em>, the next screen may show just a small portion of the form. Users have to immediately zoom out to understand what is being displayed.

<p><img alt="Screenshot of Viafoura.com free trial overlay" height="667" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/viafoura-overlay-zoomed-in-and-zoomed-out.png" width="820"/></p>

<p><strong><em>Left</em></strong><em>: what users actually see after clicking ‘</em>Request a Free Trial<em>’ on viafoura.com; <strong>Right</strong>: the full overlay form, visible after closing the keyboard and zooming the screen out. </em></p>

</li>

<li><strong>Blocking access to content</strong>. Another all-to-common – and much more severe – problem occurs when either an incorrect implementation or a bug <strong>disables the scrolling and zooming features</strong> needed to dismiss an overlay. You’ve probably experienced this before: you visit a page using a mobile device, only to find that there’s an overlay blocking the page content, and the controls to dismiss the overlay are located off the screen. In this situation the user literally cannot access the underlying page content. In some cases, the page rendering even prevents pinching and zooming, or makes it so difficult that it is nearly impossible to expand the page enough to access the overlay controls.</li>

</ul>

<p>If users on mobile devices are an important part of your audience, think long and hard before putting important content in an overlay. If you do go with an overlay, prepare for both an initial and ongoing investment in testing and QA, to ensure the design works properly at different screen resolutions and in different device orientations.</p>

<p>Accessibility is another factor to consider when evaluating who will be using your overlay. Low-vision users with full-sized monitors often employ screen magnifiers to vastly enlarge the screen content. After zooming in, the user can only see a small part of the page, so overlays can create the same disorienting effects for screen-magnifier users as they do for mobile-device users.</p>

<h2 id="toc-what-action-is-the-user-supposed-to-take-3">WHAT Action Is The User Supposed To Take?</h2>

<p>In order to create a good overlay, you need to first clearly articulate the purpose: what are users supposed to do in response to the content? Should they just glance at a short message, or should  they browse through a large set of images or read lengthy text? Do they need to make a decision between different options, or simply acknowledge the receipt of the information? Or do you need people to actually input content through the lightbox —and if so, what kind of content, and how much?</p>

<p>Experiences that feel quick and simple to users are usually <strong>not</strong> the result of a quick and simple design process. Instead, creating a design that feels easy to your audience means taking the time to clearly articulate the purpose, circumstances, and desired outcomes.</p>

<p>Overlays are typically intended to get users to <strong>view content</strong>, <strong>complete a form</strong>, or <strong>make a decision</strong>.</p>

<p><strong>Read text or view images</strong>: If the sole function of the modal window is to present a brief status message, a simple overlay with a single button for users to acknowledge and dismiss the notification may work very well. But anything more than a sentence or two creates complexity:</p>

<ol>

<li>If the content is too long to fit into a small lightbox, will you add a scrollbar? If so, consider disabling the browser scrollbar to prevent users from mistakenly scrolling the background page instead of the lightbox. (Though disabling the browser scrollbar can have unintended consequences, especially for mobile users, if they are unable to scroll enough to see the overlay controls.)</li>

<li>Will users want to bookmark the overlay content or share it? When an overlay contains actual content rather than a simple status message, users are more likely to want to do things with that content – like bookmark it for future reference, or share the link with others. You may need to do extra design work, to create special <em>save </em>and <em>share </em>functions.</li>

<li>Will the content be presented better if you had a larger window (like the full-size browser window)? If users have to scroll a lot more to read the content just because it’s in an overlay, you’re <a href="http://www.nngroup.com/articles/utilize-available-screen-space/">wasting screen space</a>.</li>

</ol>

<p><strong>Complete a form:</strong> Overlays that include form fields make it possible to provide access to the form from any screen, without needing to load a new page. This is a very attractive option for things like login and subscription forms. But keep in mind, any bugs can make it impossible for users to access these essential functions. Again, either plan for both initial and ongoing testing (across browsers, operating systems, and devices) or stick to the tried and true login screen. Some issues to look for:</p>

<ol>

<li>Overlays that ask users to provide input, even if it is just a single field, need an <strong>explicit ‘Cancel’ option</strong>. Too often designers assume that users will know they can just click outside of the modal to dismiss it. In fact, many users won’t know that; others (especially those using touchscreens) may dismiss the overlay accidentally. In the Bluefly example below, even clicking the gray area of the screen had no effect. The only way to dismiss this overlay was to click the black Shop Now button, but the placement of this button implies that it will submit the form—not dismiss it.

<p><img alt="Screenshot of Bluefly.com subscription overlay" height="694" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/bluefly-overlay.png" width="800"/></p>

<p><em>The only way to dismiss the Bluefly’s overlay is to click the black ‘</em>Shop Now’ <em>button. </em></p>

</li>

<li>To help users recover from accidentally closing the overlay, the field inputs <strong>should be saved</strong> and the overlay should be <strong>easy to reactivate</strong>.</li>

</ol>

<p><strong>Make a decision:</strong> Overlays are also commonly used to confirm user actions or to help users make simple selections. This is problematic because we’ve been trained by the many <a href="http://www.nngroup.com/articles/making-hated-design-elements-work/">pop-ups</a> and unimportant overlays we encounter on other websites to dismiss a modal window as soon as it appears. When we actually run into one that is important and useful, we may dismiss it automatically, before even reading the contents. This tendency is exacerbated by action buttons with generic labels, like US Airways’ payment-confirmation buttons labeled simply ‘<em>OK’ </em>and ‘<em>Cancel’. </em></p>

<p><img alt="Screenshot of USAirways purchase confirmation overlay" height="546" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/usairways-confirmation-overlay.png" width="800"/></p>

<p><em>US Airways uses an overlay to confirm before a credit card charge, but the action button labels don’t specifically state what action you are confirming. </em></p>

<p>To help users avoid dismissing a lightbox without understanding the consequences of their actions, use <strong>an explicit  button label</strong> that states exactly what will happen when the user clicks it, as LinkedIn does with their <em>‘Yes, Remove them’ </em>confirmation button on the lightbox to confirm deleting a contact.</p>

<p><img alt="Screenshot of Linkedin.com remove contacts confirmation overlay" height="477" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/linkedin-confirmation-overlay.png" width="800"/></p>

<p><em>LinkedIn uses the specific button label ‘Yes, remove them’ to confirm deleting a contact. </em></p>

<p>You should also consider what will happen if the user decides NOT to complete any of your target actions. Of course you should include an explicit way to dismiss the lightbox, but another common user strategy is to click the browser’s <em>Back </em>button in an attempt to revert to the underlying screen. By default, web browsers don’t treat overlays like separate pages, so the <em>Back </em>button takes users not to the underlying screen, but to whatever page preceded that screen. If your analytics show users clicking <em>Back </em>after reaching an overlay, consider adjusting the <em>Back </em>button so that when an overlay is displayed, the <em>Back </em>button closes the lightbox instead of navigating to the previous page in browser history.</p>

<h2 id="toc-when-will-the-overlay-appear-and-will-it-interrupt-an-important-task-4">WHEN Will the Overlay Appear, and Will It Interrupt an Important Task?</h2>

<p>One of the biggest challenges with overlays is that they interrupt users from whatever they were doing before the overlay appeared. How can this interruption be avoided?</p>

<p>One strategy is to present overlays during times when users are less likely to be immersed in a task. For example, many applications use overlays for <a href="http://www.nngroup.com/articles/mobile-instructional-overlay/">introductory instructions</a> or tips for using an interface. Users may have a specific task in mind when launching an application, but this intrusion at least comes at the beginning the task, rather than right in the middle. The overlay format is especially helpful on small screens, where there is not enough room to show the tips anywhere but on top of the underlying screen.  </p>

<p><img alt="Screenshot of Zappos iphone app help overlay" height="525" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/zappos-help-overlay.png" width="350"/></p>

<p><em>The Zappos iPhone application uses an introductory overlay to explain the meaning of their icons. </em></p>

<ol>

<li> <strong>User-initiated overlays</strong>  can be a great way to implement <a href="http://www.nngroup.com/articles/progressive-disclosure/">progressive disclosure</a>: giving people more information or options exactly at the time when they need those options. Often these types of overlays are closely related to the user’s current task, which takes advantage of the main benefit of overlays: the ability to<strong> maintain the context of the current screen</strong> while providing some additional content or features. For example, the Facebook iPhone application uses an overlay treatment to display various options for sharing content. This is actually just a modified visual treatment for a drop-down menu, which increases visual emphasis on the active workflow while maintaining the task context. When deciding how you want to share content it’s helpful to have the title of that piece of content   visible in the background – especially if you have just returned to the screen after an interruption.

<p><img alt="Screenshot of Facebook sharing options overlay" height="621" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/facebook-sharing-overlay.png" width="350"/></p>

<p><em>Facebook shows ‘share’ options as an overlay on top of an article; being able to see the article title ‘behind’ the overlay can help users remember what they were about to share if they are interrupted in the middle of sharing. </em></p>

</li>

<li><strong>Overlays that are not user initiated</strong>, however, are an entirely different story. When the website unexpectedly obscures the page someone was viewing, the experience ranges from distracting to obnoxious. Sometimes these notifications contain critical information that actually justifies the interruption, but more often these types of overlays are deliberate attempts to entice the user to take some action that benefits the organization (such as subscribing to a newsletter).  (Many web marketers seem to operate under the ‘ends justify the means’ principle, and believe that the benefit of increasing your subscriber base outweighs the negative consequences of annoying your users. If you attempt this strategy, make sure to follow up and measure whether those extra subscribers are actually qualified leads. Do they really end up buying your products? If not, you may be aggravating your true audience for no reason at all.)

<p>Sometimes, overlays that are not user initiated seem to be more benign, but due to inappropriate timing can end up being just as irritating as the pushy subscription pitches.  Randomly timed <em>Help </em>chat windows are a frequent offender in this category. On the Bank of the West screen shown below, the <em>Live Chat Support </em>overlay indiscriminately appears on every page – even on forms where the user is actually in the middle of completing a form to open an account. In this case the overlay is actually making it <strong>more difficult </strong>for users to convert, by requiring them to click through the overlay before they can proceed to the next form field.</p>

<p><img alt="Scerenshot of Bank of the West Chat overlay" height="837" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/bank-of-the-west-chat-overlay.png" width="800"/></p>

<p><em>The Bank of the West website interrupts users who are attempting to complete the form to open an account with an overlay offering chat support. </em></p>

<p>The safest strategy is to restrict overlays to only user-initiated actions, or truly urgent messages, and to use alternate means (like in-page feature boxes in the Apple.com example) for less-critical content. If you do decide to interrupt users with lightboxes, at the very least experiment with timing and target pages to ensure that you minimize the interruption—for example, by presenting the overlays only when users are ready to leave the site, like  DigitalMarketer.com does with  their ‘free gift’ offer. </p>

<p><img alt="Screenshot of digital Marketer exit overlay" height="703" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/digital-marketer-exit-overlay.png" width="800"/></p>

<p><em>This overlay on the DigitalMarketer.com website avoids interrupting visitors by waiting until they are about to navigate away from the site before displaying this overlay.</em></p>

</li>

</ol>

<h2 id="toc-where-will-the-overlay-appear-on-the-page-5">WHERE Will the Overlay Appear on the Page?</h2>

<p>Too often, overlays appear too low on the page. This is especially prevalent on mobile devices, but also happens on full-size screens. When planning your design, remember that many users have browser toolbars installed, and the available browser viewing area may be much shorter than what you preview in a browser with no toolbars. The <strong>lightbox content should appear directly in the users’ line of sight</strong>, or err on the side of being higher on the page. On Verizon’s mobile broadband page below, most of the lightbox content is not visible.  </p>

<p><img alt="Screenshot of Verizon Mobile Broadband overlay" height="469" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/mobile-broadband-overlay.png" width="800"/></p>

<p><em>The overlay on Verizon’s mobile broadband site is centered on the page, but due to the user’s browser toolbars, the lower section of the lightbox isn’t visible. </em></p>

<p>Placing your overlay nearer to the top of the page (rather than in the exact center) minimizes the risk of having it cut off at the bottom, and keeping the browser scrollbar available ensures that even in very small browser windows, users will still be able to scroll down to view the entire lightbox. </p>

<p><img alt="Screenshot of USPS overlay" height="546" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/usps-overlay.png" width="800"/></p>

<p><em>On USPS, the overlay is closer to the top of the page, increasing the likelihood that the full contents will be immediately visible. </em></p>

<p>Another important consideration, especially for larger lightboxes, is <strong>where the controls and content should be placed</strong> within the overlay. Sometimes advertising overlays will deliberately place controls in unusual locations (apparently to force users to spend more time interacting with the ad content) as if tormenting customers is a way to engender warm feelings toward a brand. But you also often see control placement that is just poorly laid out. This can be especially challenging if a single standardized overlay design is used to present content with varying dimensions. In the example below, American Furniture Warehouse presents the content (a photograph of a desk) at the top of the lightbox, while the button to close the lightbox appears at the bottom, leaving a vast amount of empty space that users must scroll through in order to dismiss the overlay. </p>

<p><img alt="Screenshot of American Furniture Warehouse overlay" height="960" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/american-furniture-warehouse-overlay.png" width="800"/></p>

<p><em>American furniture warehouse has the ‘</em>Close<em>’ control at bottom and overlay is so big it might as well be a whole page.</em></p>

<h2 id="toc-why-does-this-content-need-to-be-in-an-overlay-instead-of-being-within-a-page-6">WHY Does This Content Need to Be in an Overlay Instead of Being Within a Page?</h2>

<p>Last but definitely not least: don’t use an overlay unless you have a clear, compelling case for why this content should not be presented within a regular page. Good reasons for using an overlay could include:</p>

<ul>

<li>The user is about to take an action that has <strong>serious consequences</strong> and is difficult to reverse.</li>

<li>It’s <strong>essential to collect</strong> a small amount of information before letting users proceed to the next step in a process.</li>

<li>The content in the overlay is <strong>urgent</strong>, and users are more likely to notice it in an overlay.</li>

</ul>

<p>The first instance – using an overlay to confirm user actions – should be used with restraint, and only when it truly is difficult to reverse an action. Even then, you may want to offer users a ‘<em>Don’t ask me this again’ </em>option, in case it is an action they need to repeat many times.</p>

<p>Quickly collecting essential information with an overlay is aptly illustrated by the Chase.com screen below. The user has requested auto-loan rates, but the site can’t display the correct rates without knowing the user’s location. </p>

<p><img alt="Screenshot of Chase Zipcode overlay" height="444" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/chase-zip-code-form-overlay.png" width="800"/></p>

<p><em>Chase.com appropriately uses an overlay to collect critical information that is required to complete a user-requested action, which needs to be explained to the user</em></p>

<p>The last condition – giving users urgent information – is the most open to interpretation. ‘Urgent’ can mean different things to different people, after all. What seems urgent to a marketer interested in promoting a new product may seem completely irrelevant to a user who just wants to get to the search box to look for a completely different product.</p>

<p>It’s easiest to determine urgency (and to communicate it to your audience) when the organization’s interests and the users’ interests are closely aligned. For example, back in December, the Environmental Defense Fund website presented incoming visitors with an overlay soliciting donations and explaining that donations made prior to an upcoming deadline would be matched by a sponsor. Given the timing, this information would probably be considered urgent by many site visitors, especially those interested in making their end-of-the-year tax-deductible charitable gifts. But what about the second example? This overlay, presented in April, does not reference any specific deadline, and appears to be simply a generic sales pitch. <a href="http://www.nngroup.com/articles/donation-usability/">Collecting donations</a> is still urgent for the organization, but is much less likely to be considered urgent by visitors. </p>

<p><img alt="Screenshot of Environmental Defense Fund overlay 1" height="586" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/environmental-defense-fund-1.png" width="800"/></p>

<p><em>The Environmental Defense Fund used an overlay to convey time-sensitive information.</em></p>

<p><img alt="Screenshot of no deadline Environmental Defense Fund overlay" height="626" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/12/environmental-defense-fund-2.png" width="800"/></p>

<p><em>The Environmental Defense Fund's call to action is much less relevant to the user when the urgency is not convincingly communicated. </em></p>

<p>Notice that our list of good reasons to use an overlay does not include ‘so we won’t have to set up a new page template’. (If setting up a new page is so difficult that you find yourself sticking content into overlays, perhaps it’s time to reconsider your website platform.) Recruiting user-research participants is also not included. As much as we value user research, the number of sites bombarding incoming visitors with survey invitations is reaching near-epidemic proportions. Surely there are less intrusive ways to collect user feedback.</p>

<h2 id="toc-conclusion-7">Conclusion</h2>

<p>Overlays can be effective in certain contexts, but too often they are used without enough planning, as a convenient way to insert additional content that may or may not be appropriate. They frequently break on mobile or on smaller browser windows, create confusion and annoyance, cause people to work harder to achieve the same task, and make content hard to access at later times. In other words, the overlay benefits are often overwhelmed by disadvantages. </p>

<p>In many cases presenting the content within a page instead of an overlay can get around these problems.  Before considering an overlay, carefully investigate your motivations and think about the five Ws. If you still think that overlays are the right design solution for you, proceed with care. Test repeatedly on a variety of browsers and devices to make sure that your design does not break.</p>

<p>Learn more about how to effectively present content and facilitate task workflows in our full-day seminar on <a href="http://www.nngroup.com/courses/web-ux-design-guidelines/">Top Web UX Design Guidelines</a></p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=overuse-of-overlays&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=overuse-of-overlays&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Web Usability</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Web Usability</span>

<a class="ga-article-related-topic" href="/topic/web-usability/">Web Usability</a>

</li>

</ul>

</div>

</div>

</div>

</div>