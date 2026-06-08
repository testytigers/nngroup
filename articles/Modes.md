# Modes in User Interfaces: When They Help and When They Hurt Users - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">8</span>

<div class="article-header">

<h1 class="article-h1">Modes in User Interfaces: When They Help and When They Hurt Users</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Page Laubheimer</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/2022-portrait-page-3.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list">

Page Laubheimer

</span>

<p class="publication-date">

April 14, 2019

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2019-04-14</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Modes in User Interfaces: When They Help and When They Hurt Users&amp;body=https://www.nngroup.com/articles/modes/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/modes/&amp;title=Modes in User Interfaces: When They Help and When They Hurt Users&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/modes/&amp;text=Modes in User Interfaces: When They Help and When They Hurt Users&amp;via=nngroup" data-share-type="Twitter">

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

</span>In a modal interface, the same user action can have different results depending on the state of the system. Poorly signaled modes can easily trigger user errors with disastrous consequences.

</div>

<div class="article-body">

<p>Modes are a frequently misunderstood UI concept: they are often confused with different visual representations of the same data, or features located in a separate part of an application.  Even UX practitioners who understand what modes are argue about their appropriate use, with many famous UXers <a href="https://www.oreilly.com/library/view/humane-interface-the/0201379376/">advocating for modeless interfaces</a>. However, modes can be beneficial and helpful, if implemented carefully and thoughtfully.</p>

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

<a class="ga-article-toc-item" href="#toc-definition-1">Definition</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-why-modes-are-useful-2">Why Modes Are Useful</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-common-mode-errors-and-usability-problems-3">Common Mode Errors and Usability Problems</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-discoverability-problems-and-modes-4">Discoverability Problems and Modes</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-what-modes-arent-5">What Modes Aren’t</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-summary-6">Summary</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-references-7">References</a>

</li>

</ul>

</div>

</div><h2 id="toc-definition-1">Definition</h2>

<p style="margin-left:.5in"><strong>Definition: </strong>Modes are different interpretations of the user input by the system, depending on the state which is active. Same input, different results.</p>

<p>The most classic example of a mode is the use of the <em>Caps Lock</em> key on a typical keyboard:  With the <em>Caps Lock</em> key off, pressing the key for the letter <em>a </em>in a text editor will display lower-case <em>a</em>.  With<em> Caps Lock</em> on, the same action will result in an upper-case <em>A</em>. Thus, the <em>Caps</em> <em>Lock</em> key is a mode switcher.</p>

<figure class="caption"><img alt="A text editor window with all caps text" height="795" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/06/textedit.png" width="918"/>

<figcaption><em>An example of a mode: in Mac TextEdit, the </em>Caps Lock<em> key turns the same user input into different outputs.</em></figcaption>

</figure>

<p>A system is <strong>modeless</strong> if the same user input will always have the same result, regardless of the system state.</p>

<h2 id="toc-why-modes-are-useful-2">Why Modes Are Useful</h2>

<p>Modes become useful when we have too many different options that we want to make available to users, and not enough available types of input to accommodate them all (in a usable, discoverable, and sensible way). </p>

<p>For example, in an image-editing application like Photoshop, it’s useful for the standard mouse click to have many different functions, because being able to point to specific parts of the image is critical for these functions — other input types (like keyboard commands) would not be sensible. Therefore, mode-switching tools (such as the marquee, pen, magic wand, eraser, and all the other toolbar icons) are used to change the result of a left mouse click.</p>

<figure class="caption"><img alt="Two photoshop windows, showing the difference in cursor appearance with different tool modes selected" height="2617" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/06/psd-modes-icons.png" width="1461"/>

<figcaption><em>In Photoshop, the </em>Brush<em> tool (top) and the </em>Quick Select<em> tool (bottom) are different modes: if </em>Brush<em> is selected, a left mouse click adds a colored patch to the screen; if </em>Quick Select<em> is active, the system selects whatever it perceives as an object in the photo (for example, the sky in this screenshot). Photoshop indicates which mode is active in several ways: the cursor icon changes, the icon in the toolbar corresponding to the active mode is darkened, and the contextual panel at the top of the window displays options relevant to the active mode.</em></figcaption>

</figure>

<p> </p>

<h2 id="toc-common-mode-errors-and-usability-problems-3">Common Mode Errors and Usability Problems</h2>

<p>Modes can cause a range of usability problems, including <strong>mode <a href="https://www.nngroup.com/articles/slips/">slips</a></strong> (occurring when the user is not aware of the currently active mode) and <strong>low discoverability</strong> of mode-specific features.</p>

<p>Mode slips happen because the system doesn’t clearly <a href="https://www.nngroup.com/articles/visibility-system-status/">indicate its status</a> to the user, violating the very first of the <a href="https://www.nngroup.com/articles/ten-usability-heuristics/">10 usability heuristics</a>.  Mode errors have been a longstanding problem in our discipline, and, especially in complex systems, can have deadly consequences.  Famously, in 1991, <a href="https://www.aviationtoday.com/2004/09/01/human-factors-in-avionics-certification/">a plane crashed into a mountain due to a mode error</a> — in different modes, the same control could be used for either the degree or the speed of descent, but it was not sufficiently clear which mode was currently active.  Tragically, the pilot’s intention of a 3.3-degree descent angle was interpreted by the system as a negative vertical descent of 3,300 feet per minute — all because the same control was used to enter these numbers and the dashboard didn’t have a clear mode indicator. </p>

<p>Another, far more common mode error involves email, and is unfortunately still present in every email application I’ve ever encountered: the dreaded <em>Reply All</em> instead of <em>Reply </em>to sender. This mode slip has been around since the invention of email, and yet remains unsolved, despite the fact that it causes embarrassment to users everywhere (and inspires advice articles <a href="https://www.nytimes.com/2019/01/17/smarter-living/crowdwise-reply-all-embarrassment-email-etiquette.html">on how to handle this disastrous slip</a>). If you want to do truly impactful UX work, come up with a design that solves the <em>Reply All</em> error once and for all. You will save literally billions of hours of human lifespan.</p>

<p>Mode slips can be reduced with a few key design considerations:</p>

<ul>

<li><strong>Clear visibility of the current active mode.</strong> Use strong visual signals such as different backgrounds, emphasis on active-mode indicators (such as high-contrast highlighting or borders), or changing the cursor to indicate which mode is active. Redundancy in indicators is a wise idea: we strongly recommend at least two visual indicators (such as the combination of highlighting on mode-selector controls combined with a cursor change) for which mode is active, to ensure that users are aware of the currently active mode even when they are not fully paying attention.</li>

<li><strong>Indication of the effects of the mode. </strong>Clearly named modes, text labels for mode-selector icons, and tooltips that help establish what happens when that mode is active help users to understand what the mode does.</li>

<li><strong>Avoiding modes entirely when mode slips can have unsafe outcomes</strong> (such as accidental loss of work, deletion of data, <a href="https://www.nngroup.com/articles/embarrassment/">embarrassment</a>, or physical-safety consequences).  Even if two features are conceptually similar (such as the aforementioned plane’s descent controls), if accidentally mixing them up can cause real harm, go for other design alternatives — like two separate controls.</li>

<li><strong><a href="https://www.nngroup.com/articles/error-message-guidelines/">Constructive error messages</a></strong> when you can deduce that a certain user action was most likely intended for a different mode than the one that’s currently active. A classic example is password entry while <em>Caps Lock</em> is active: the user may type the password in all-capital letters without realizing it in systems that <a href="https://www.nngroup.com/articles/stop-password-masking/">mask password entry</a>. However, the system knows that upper- and lower-case characters were swapped during text entry and can warn the user to deactivate <em>Caps Lock</em> and try again (or even prevent the error by showing a symbol indicating that the <em>Caps Lock</em> key is active while typing).</li>

<li><strong><a href="https://www.nngroup.com/articles/confirmation-dialog/">Confirmation dialogs</a></strong> that clearly explain what the computer is about to do, while possibly mentioning the current mode. As always, confirmations should be used sparingly, or they won’t do any good because the user will unthinkingly answer <em>Yes</em> if you ask them to confirm too many times. But confirmation dialogs can be a last chance to save the user in cases where usability testing, analytics, or other data indicate that people are likely to forget what mode they’re in.</li>

</ul>

<figure class="caption"><img alt="A table with a row in edit mode that is clearly visually signaled" height="472" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/06/edit-mode.png" width="974"/>

<figcaption><em>Telerik uses several clear mode indicators in this table to redundantly show the row that is in </em>Edit<em> mode: the row’s background has a different color, the data is represented as form fields, the action buttons change position and color. </em></figcaption>

</figure>

<p>An alternative to modes are <a href="https://www.nngroup.com/articles/spring-loaded-modes/">spring-loaded modes</a> (also known as <em>quasimodes)</em>; such modes are active only while a modifier is engaged.  For example, holding down the <em>Shift</em> key on a keyboard is the spring-loaded equivalent of the <em>Caps Lock</em> key — the quasimode is only active while the <em>Shift </em>key is being pressed. Quasimodes prevent mode slips, but make it less likely that the users will discover the features associated to these modes. (Also, of course, spring-loaded modes are less efficient in cases where the user wants to remain in the mode for an extended set of actions. THAT SAID, HOW OFTEN DO YOU REALLY WANT TO TYPE AN ENTIRE SENTENCE OF ALL-CAPS TEXT, WHICH IS THE MAIN CASE WHEN <em>CAPS LOCK</em> IS MORE EFFICIENT THAN THE SPRING-LOADED <em>SHIFT</em> KEY.)</p>

<h2 id="toc-discoverability-problems-and-modes-4">Discoverability Problems and Modes</h2>

<p>Modes also make it tough for new users to find and remember where certain features or commands are. If a feature or command is only available to users in one mode, the likelihood that a user will encounter it naturally (known as <em>discoverability)</em> or be able to locate it later (known as<em> findability</em>) is much lower than if that feature were always available. </p>

<p>For example, I have a pair of Bluetooth earphones that block out most outside sound when I’m wearing them.  They have a useful toggle that allows me to selectively pass through <em>some</em> outside sound for situational awareness when I need it, such as when I am walking down a busy street. I toggle this mode by double-tapping the button on the earphones while I’m listening to music, and it turns it off or on, with a nice short beep as audible feedback.</p>

<p>This ambient-awareness feature also comes in handy when making a phone call, as it reduces the odd feeling of talking but hearing your own voice very muffled. However, when there’s a loud noise around while I’m on a call (I live in NYC, where there are often loud noises around), I’ve often wanted to switch this feature off for a bit.  Unfortunately, the double-tap control doesn’t work while you’re in phone call mode – double-tapping the button does nothing in this case except make the audible-feedback beep.  As it usually happens when I’m distracted (by focusing my attention on the conversation, not on the UI of the headphones), it took me forever to understand what was happening – I was running into a major findability problem related to my headphones’ mode.</p>

<h3>Modals: a Special Case of Modes</h3>

<p><a href="https://www.nngroup.com/articles/modal-nonmodal-dialog/">Modal windows</a> are a specific type of mode; they present as popups or slide-over panels and they restrict the user’s ability to interact with the content behind the modal, even though that content will remain visible (and typically darkened). Modal windows or dialogs demand that users interact with them before returning to whatever they were doing before. A modal restricts user input to its window until it is dismissed. If the user taps or clicks on the background behind the modal (attempting to interact with the content), the modal can be either dismissed or nothing may happen. Therefore, a modal window moves the interface into a special mode where the same input (clicking on a link in the background) produces different results depending on whether the modal is active.</p>

<figure class="caption"><img alt="A website with a modal popup covering content behind it" height="827" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/06/wired-modal.png" width="974"/>

<figcaption><em>Wired.com shows a classic modal window — the user can still see, but cannot interact with the content below the popup. Clicking on the darkened background area has no effect (and does not dismiss the modal window).  </em></figcaption>

</figure>

<p>Importantly, not all popups are modal — if a user can still interact with the content below it, the window is not modal (many <a href="https://eugdpr.org/">GDPR</a>-compliance popups are nonmodal, which at least makes them slightly less annoying). Modals are a heavyweight design choice that are only appropriate when users truly <em>must</em> interact with them in order to continue their current task.</p>

<figure class="caption"><img alt="A non modal popup on a website" height="833" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/06/tnw-non-modal.png" width="860"/>

<figcaption><em>TheNextWeb.com features a GDPR-compliance popup (“Have a cookie”) that is nonmodal, as users can still interact with the background content while that popup remains visible.</em></figcaption>

</figure>

<h2 id="toc-what-modes-arent-5">What Modes Aren’t</h2>

<h3>Not Different Views of the Data Space</h3>

<p>Modes are not different ways of looking at the same data. For example, in the Mac Finder, the list view and the icon view take the same data (the files and folders stored on the computer) and present them differently, with the list view showing additional metadata absent in the icon view.  However, the same user input has the same effect in both cases: clicking on an object highlights it, double-clicking on it opens it. The same input has the same effect in both cases, so the icon and list views should not be considered different modes, just different views of the data space.</p>

<figure class="caption"><img alt="Two Mac Finder windows shoing the same folder structure in two different views (which are not modes)" height="1209" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/06/finder-imagesfirst-finder-mode-image.png" width="1214"/>

<figcaption><em>These two views of the same data in the Mac Finder are <strong>not</strong> different modes, even though the icon view (top) does not display all of the metadata that is visible in the list view (bottom). The same user input (a click on one of the items) produces the same effect in both views: selecting and highlighting that item. </em></figcaption>

</figure>

<p>However, even this simple interface also includes access to a mode. Normally, typing a letter in either of the views will highlight other items, based on their names. However, if you click on the text label once, after that item is already selected and highlighted, the name of the item flips into edit mode.  At this point, typing will change the name of the item. So, even though the icon and list views themselves are not modes (just different views of the data), they both include access to other modes (navigate and edit, respectively). </p>

<h2 id="toc-summary-6">Summary</h2>

<p>Modes are useful for managing a large number of features that would all benefit from using the same input control. If either the total number of input controls is limited, such as on physical devices with a limited number of buttons, or if several actions are best signaled by the same input (e.g., both scrolling and drawing are well signified by dragging a finger on a touchscreen), using modes will be an appropriate design choice.  However, the currently active mode must be clearly indicated, with a strong visual differentiation, and modes should not be used in critical scenarios where mode errors can produce disastrous consequences.  </p>

<p>Learn more in our full-day <a href="https://www.nngroup.com/courses/application-ux/">Application Design for Web and Desktop</a> course.</p>

<h2 id="toc-references-7">References</h2>

<p><em>The Humane Interface, </em>Jef Raskin, 2000</p>

<p>Asaf Degani. “<a href="https://pdfs.semanticscholar.org/39aa/1c4b755c9ed709850e31cbd630486654ec62.pdf?_ga=2.24516601.2116285835.1594750950-470849997.1594750950">Modeling Human-Machine Systems: On Modes, Error, and Patterns of Interaction.</a>” Ph.D. Thesis, School of Industrial and Systems Engineering, Georgia Institute of Technology, 1996.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Interaction Design,Human Computer Interaction,interfaces,mental models</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Interaction Design</span>

<a class="ga-article-related-topic" href="/topic/interaction-design/">Interaction Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

</ul>

</div>

</div>

</div>

</div>