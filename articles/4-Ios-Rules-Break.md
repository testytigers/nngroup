# iOS Design Rules to Break - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">10</span>

<div class="article-header">

<h1 class="article-h1">4 iOS Rules to Break</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Amy Schade, Aurora Harley, Kara Pernice, Raluca Budiu</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/amy_schade_headshot.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Aurora-Harley-20190601SF.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/kara-2025.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/2023-04-portraits-raluca.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list">

Amy Schade,

<a class="ga-article-author" href="/articles/author/aurora-harley/">

Aurora Harley</a>,

<a class="ga-article-author" href="/articles/author/kara-pernice/">

Kara Pernice</a>, and

<a class="ga-article-author" href="/articles/author/raluca-budiu/">

Raluca Budiu</a></span>

<p class="publication-date">

July 19, 2015

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2015-07-19</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: 4 iOS Rules to Break&amp;body=https://www.nngroup.com/articles/4-ios-rules-break/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/4-ios-rules-break/&amp;title=4 iOS Rules to Break&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/4-ios-rules-break/&amp;text=4 iOS Rules to Break&amp;via=nngroup" data-share-type="Twitter">

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

</span>Page control (dots), Submit at top, and the Plus (+) and Move icons are 4 common iOS patterns that cause usability problems in testing.

</div>

<div class="article-body">

<p>Large software organizations (such as Apple, Microsoft, and Google) create design guidelines to help both users and designers.</p>

<ul>

<li>On the one hand, designers and developers can get a head start on creating interfaces that will hopefully be good, without needing to invent (and test) all-new UI elements.</li>

<li>On the other hand, users get a consistent look-and-feel across applications running on the same operating system if all designers comply with these guidelines.</li>

</ul>

<p>Following style guides is almost always recommended. But there are some cases where the official design does not work well in practice. Nonetheless, for reasons unknown — maybe the recommendation was a trade-off, it wasn't thoroughly researched, or it seemed to be the best possible a solution to a very difficult design challenge — it still made it in the style guide.</p>

<p>The following are 4 common iOS patterns that Apple has used extensively in its apps and that have been followed by many other designers. Some of them are part of the <a href="https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/MobileHIG/index.html">iOS human-interface guidelines</a>. Time and again, we have seen these designs cause usability problems. The Apple gods may strike us down with lightning, but we <strong>recommend against following these patterns </strong>because they fail in usability testing:</p>

<ol>

<li>Page control: dots to indicate pages</li>

<li>Form <em>Submit</em> button at the top</li>

<li><em>Plus</em> (+) icon</li>

<li><em>Move</em> icon</li>

</ol>

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

<a class="ga-article-toc-item" href="#toc-1-page-control-dots-to-indicate-pages-1">1. Page Control: Dots to Indicate Pages</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-2-form-submit-button-or-equivalent-at-the-top-2">2. Form Submit Button (or Equivalent) at the Top</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-3-plus-icon-3">3. Plus (+) Icon</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-4-move-icon-4">4. Move Icon</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-5">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-1-page-control-dots-to-indicate-pages-1">1. Page Control: Dots to Indicate Pages</h2>

<p>Many iOS users are familiar with the page control. The iOS page control is a <strong>line of horizontal dots that represent open views or pages</strong>. The currently selected page is represented with an opaque dot and the other pages are represented with translucent dots.</p>

<figure class="caption"><img alt="iOS home screen uses dots (page indicator) to indicate the current view" height="354" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/12/apps.png" width="200"/>

<figcaption><em>The iOS home screen uses dots (page control) to indicate the current view and the number of additional views (that is, additional pages of apps pages) available. Although this is one of the most recognized and common examples of the dots, it’s also one of the few cases where they work tolerably well, because users know that they have multiple screens full of a muddled mix of icons that people swipe through in the attempt to locate a desired application. (The overall UX of locating icons is not ideal, but the page dots are not the problem.)</em></figcaption>

</figure>

<p>Some apps and sites use this interface element to indicate that users can swipe through pages of content while others use it in a partial area of the page to show a carousel of content. It’s a popular pattern in both mobile-web and app design, but it is also one <strong>commonly overlooked by users</strong>. In usability testing, these dots are often <strong>too subtle in the interface</strong> to clearly indicate to users that there is another view of content available. As such, they should <strong>never be used for key functionality</strong>, such as navigating between features, or as the sole method for accessing information.</p>

<figure class="caption"><img alt="The app shows dots at the bottom of the screen to indicate the user should swipe." height="438" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/13/stockmarket_dots_tr_rs.png" width="500"/>

<figcaption><em>In the iOS app, Stock Market HD Stocks and Shares, the only apparent way to navigate between the </em>Watchlist, Wishlist, Sold, <em>and </em>My Holdings<em> views is to notice the dots at the bottom of the screen and swipe to discover the additional functionality.</em></figcaption>

</figure>

<p>While designers and developers can select what colors to use for the tint of the circles, it is difficult to make a small, subtle, and translucent design element stand out on a page. Many designs use these circles on top of busy images, which causes an already subtle design to further <strong>fade into the background</strong>. If using the dots, <strong>help users notice them by increasing the color contrast between the dots and background</strong> <strong>and placing the dots on a solid color background when possible</strong>.</p>

<figure class="caption"><img alt="Zappos dots are barely visible because the background image obscures them." height="438" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/13/zappos_carousel_tr_rs.png" width="500"/>

<figcaption><em>The Zappos iOS app uses dots to indicate multiple views of content in the top half of the page. The dots are barely visible on the background of the shoe in the first image and disappear completely into the background picture of the chair in the second image.</em></figcaption>

</figure>

<p>Some sites and apps take liberties even with the existing iOS conventions, using squares or other shapes or moving the dots around the page. Users struggle to locate and use these dots even when they follow the design conventions described by the iOS guidelines. Changing the elements to diverge from these standards makes them that much <strong>more difficult to identify and understand</strong>. If using the dots, <strong>center them and place them directly below the elements they control</strong>.</p>

<figure class="caption"><img alt="The Fab app for Android uses barely noticeable triple-dot indicator in the lower-middle-right of the screen, too close to the images." height="355" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/12/fab_dotscarousel.png" width="200"/>

<figcaption><em>The Fab app for Android borrows the iOS-inspired dots, but places them to the right side of the carousel rather than centering them.</em></figcaption>

</figure>

<p>Even if users do notice the dots, an essential usability problem remains. The dots <strong>allow only </strong><a href="/articles/direct-vs-sequential-access/"><strong>sequential access</strong></a> <strong>to content</strong>, and provide no indication of what the content is. Whether the dots indicate items in a carousel or stand for separate pages in a deck-of-cards pattern, the same <a href="/articles/designing-effective-carousels/">usability concerns</a> apply. In particular, carousels using symbols to represent pages limit users’ control over their experience. Users have no way to know what’s coming next and no way to navigate directly to content of interest.</p>

<h3><strong>Instead, we recommend:</strong></h3>

<ul>

<li>Consider if content should even be accessed via swiping. It may be better accessed via navigation or text links.</li>

<li>Cut off a piece of content (text or image) to visually indicate that users can swipe to reveal more information.</li>

</ul>

<figure class="caption"><img alt="iOS App Store avoids the use of dots and instead uses cut off " height="354" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/12/appstore_carousel.png" width="200"/>

<figcaption><em>The iOS App Store avoids the use of dots and instead uses cut off elements to show users that the navigational carousels are movable.</em></figcaption>

</figure>

<h2 id="toc-2-form-submit-button-or-equivalent-at-the-top-2">2. Form Submit Button (or Equivalent) at the Top</h2>

<p>On iOS, the <em>Done</em> button is often displayed in a navigation bar at the top of the page. Sometimes the form <em>Submit</em> button (whether called <em>Submit</em> or something else — for instance, <em>Place Order</em>) is also placed at the top of the form. This pattern has started to trickle into Android apps as well.</p>

<figure class="caption"><img alt="Add button that submits form is in the top right corner instead of being in line with the flow, at the bottom." height="433" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/13/calendar.png" width="500"/>

<figcaption><em>Calendar for iOS (left): The </em>Add<em> button that submits the form is placed in the top right corner, in the navigation bar. Todoist</em> <em>(a to-do–list app) for Android (right) borrows the iOS pattern and places the </em>Submit <em>button (the checkmark icon) in the top right corner. (Note also that the form fields violate <a href="/articles/mobile-input-checklist/">many of our guidelines</a>: the labels are inside the field, and can you guess what GMT-8:00 stands for?)</em></figcaption>

</figure>

<p>Even in iOS apps we recommend against following this pattern for the simple reason that it <strong>goes against the natural top–bottom workflow</strong> on the page. As users fill in the form, they usually do it top to bottom. When they get to the end of it, they expect to find a <em>Submit</em> button right there, next to the last field they have completed. Most of the time, when people don’t find it there, they get confused and start looking around, not knowing what to do.</p>

<p>In the examples below (Pinkberry and Nordstrom), the <em>Sign In</em> and <em>Place Order</em> buttons need to be pressed after the user has filled in the form. Placing these buttons at the top of the screen is against the natural flow of filling in the form: once done with all the fields of the form, users find themselves at the bottom of the page, left with nothing to do next. Even on a small mobile screen, looking for and finding the corresponding <em>Submit</em> button requires unnecessary extra effort that could be saved if that button was placed at the bottom of the page, under the last field, as it is customary on most forms on the desktop.</p>

<p>(The generally accepted design guideline for any GUI — mobile or not — is <a href="/articles/closeness-of-actions-and-objects-gui/">proximity between actions and objects</a>, not to place the action button as far away as possible from the data it acts upon.)</p>

<figure class="caption"><img alt="Two screenshots show buttons in the top-right corner instead of at the bottom of the user task flow." height="429" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/13/pinkberry-nordstrom.png" width="500"/>

<figcaption><em>The working area in Pinkberry for iPhone (left) and in Nordstrom for iPhone (right) is disconnected from the</em> Submit <em>buttons (labeled</em> Sign In <em>and</em> Place Order,<em> respectively), which are placed at the top of the screen.</em></figcaption>

</figure>

<p>One of the advantages of having the <em>Submit</em> button in the page header is that, because this header is sticky in iOS apps, users can access the button easily at all times — whether they have filled in all the form fields and reached the bottom of the list, or not. (For the Calendar app it may be reasonable to assume that users won’t bother with all fields, but for a login form it’s not.) In any case, if having the button accessible at all times is important for you, consider instead a sticky <em>Submit</em> button at the bottom of the page, like in the Hotel Tonight app. Yes, you will sacrifice some screen real estate, but in return you will gain a better, more usable interaction flow.</p>

<figure class="caption"><img alt="Hotel Tonight screenshot shows a screen-width Apple Pay button in white at the bottom of a dark screen." height="355" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/12/hoteltonight.png" width="200"/>

<figcaption><em>Hotel Tonight: The </em>Pay <em>button at the bottom of the page is persistent and accessible at all times. This allows users to interact with the page as much as necessary while having consistent access to the payment button, which appears in a predictable and logical location.</em></figcaption>

</figure>

<h3><strong>Instead, we recommend</strong>:</h3>

<p>Display the form <em>Submit</em> button (or equivalent) under the form fields rather than at the top of the page.</p>

<h2 id="toc-3-plus-icon-3">3. <em>Plus</em> (+) Icon</h2>

<p>Throughout many mobile apps, the <em>Plus</em> icon is used to represent a variety of functions. When placed within a top navigation bar, it most commonly means “Add,” but when placed within a table or list of items the icon can signify either adding that item to some sort of list or group, or expanding that list item for more detailed information. When multiple interpretations exist, it becomes <a href="/articles/icon-usability/">difficult for users to consistently understand an icon's meaning</a>.</p>

<figure class="caption"><img alt="My Fitness Pal uses a Plus icon conventionally, to add a new item" height="354" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/12/plusicon_example1-addnew_border.png" width="200"/>

<figcaption><em>When located in the top navigation bar, a Plus icon (top right corner) most commonly means to add a new item, as used in the MyFitnessPal app to allow adding a friend.</em></figcaption>

</figure>

<p>The usability of the <em>Plus</em> icon is highly dependent on where it is located within a UI. When found in a common place, such as a navigation bar, the meaning is usually correctly understood as long as adding new items makes sense for the type of content shown on that screen. However, when the <em>Plus</em> icon appears within the main content of an interface, it can have <strong>multiple meanings, which creates confusion</strong> for users.</p>

<p>For example, a previous version of the app Any.do displayed the <em>Plus</em> icon alongside the label of existing to-do lists. In this context, it is unclear whether tapping the <em>Plus</em> icon would expand the list to view the items it contained, or if it would trigger adding a new to-do item to the corresponding list. The current version of the app has solved this ambiguity by relocating the <em>Plus</em> to the navigation bar: however it is now used to add an entirely new to-do list.</p>

<figure class="caption"><img alt="Any.do app used Plus icons both to add an item and to expand a to-do list. " height="439" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/12/plusicon_example2-differentmeanings.png" width="500"/>

<figcaption><em>In a previous version of the Any.do iOS app (left), the meaning of the </em>Plus<em> icon was unclear, as it could be interpreted as either allowing the expansion of the list or adding an item to a specific list. In the current version (right), the </em>Plus<em> icon is part of the top navigation bar, and is now used to add an entirely new to-do list.</em></figcaption>

</figure>

<p>Leveraging the <em>Plus</em> icon to trigger actions is particularly harmful when the user misinterprets what will occur. Since the <em>Plus</em> icon is regularly used on the web and in mobile apps to communicate that a list can be expanded — together with the arrow (&gt;) and the caret (^) — users often do not expect that same <em>Plus</em> icon to actually perform some sort of action. In the LinkedIn mobile app, a <em>Plus</em> icon in a circle is used to <em>Follow</em> a company or <em>Join</em> a group depending on where it is located. In usability testing, several users were surprised when they accidentally joined groups they were intending to merely get more information about.</p>

<figure class="caption"><img alt="LinkedIn app reuses the same Plus icon throughout the app" height="355" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/12/plusicon_example3-follow.png" width="200"/>

<figcaption><em>The LinkedIn app reuses the same </em>Plus <em>icon throughout the app for a variety of functions. On the main home screen shown above, the </em>Plus <em>icon can be tapped to follow a company (without confirming this is what the user intended). When searching in the app, the </em>Plus <em>icon can also be used to quickly join groups. Thankfully the questionable icon is omitted from the search results for </em>People<em> or </em>Jobs<em>, as that could lead to some interesting consequences.</em></figcaption>

</figure>

<p>Avoid adding the <em>Plus</em> icon haphazardly throughout an app, as it can be interpreted in several different ways depending on its exact context within the interface.</p>

<h3><strong>Instead, we recommend:</strong></h3>

<ul>

<li>While the navigation bar is a fairly safe location, displaying the + icon in other areas in a design must be tested with users to ensure the meaning is correctly understood.</li>

<li>The only way to fully avoid the issue is to also avoid the icon, and to use an arrow or caret for expandable lists, and text labels for buttons triggering any action associated with a list item.</li>

</ul>

<h2 id="toc-4-move-icon-4">4. Move Icon</h2>

<figure class="caption"><img alt="move icon" height="53" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/12/move.png" width="55"/>

<figcaption><em>Move icon</em></figcaption>

</figure>

<p>Like many icons for mobile devices, the move icon does not clearly reveal what it does. By looking at it you probably will not recognize that this icon will move an item in a list. The 3 horizontal lines used for the <em>Move</em> icon may represent a list, or maybe, as one reader pointed out, "ridges preventing the finger from slipping off the item while dragging it." When this icon appears within a row of a list, users are supposed to tap the icon and hold it while dragging the related item to its rightful place in the list. There are a few usability issues with this pattern.</p>

<p>When items are movable in a list, users expect to tap directly on an item (word, button, etc.) and drag it. They don’t expect to need to touch a small, hard-to-decipher icon instead and drag that. The icon is a much smaller and harder to <a href="https://www.nngroup.com/articles/touch-target-size/">tap target</a> than the item in the list itself is. So it increases the <a href="/articles/interaction-cost-definition/">interaction cost</a> and makes users work harder to tap and drag than they should need to. Additionally, in list views, users expect all the elements in a row to be associated with the same action: in other words, they think that dragging the item or the icon should do the same thing.</p>

<figure class="caption"><img alt="app displays the shadow text of the item as it moves" height="436" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/12/yahoo-finance_before_drag_after.png" width="750"/>

<figcaption><em>YAHOO! Finance uses Apple’s iOS recommendation for moving items in a list. Tap the 3-horizontal-line icon on the right (left) and drag and move the selected item. The app displays the shadow text of the item as it moves (middle) and the change takes effect (right). The list items themselves are a much larger tap target, but tapping and dragging them does not work.</em></figcaption>

</figure>

<p>Finally, nearly the exact same icon recommended in the iOS style guide has come to mean something completely different on the mobile web and elsewhere: The hamburger icon looks incredibly similar to the move icon.</p>

<figure class="caption"><img alt="move and hamburger icons: both are 3 horizontal lines. Move lines are closer together." height="53" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/07/12/move_hamburger.png" width="129"/>

<figcaption><em>On the left is a Move icon, on the right is a hamburger menu.</em></figcaption>

</figure>

<p>It can be disconcerting and confusing to people when the same thing, or what is perceived to be the same thing, is used to invoke different commands. If the hamburger menu continues to gain traction, more users will learn that clicking three horizontal lines opens a menu (even if they may still overlook this feature more often than we would like). But this is not how the move icon works. This disagreement hurts users’ ability to <a href="/articles/recognition-and-recall/">recall</a> what the icons do after they have already used them.</p>

<h3><strong>Instead, we recommend:</strong></h3>

<ul>

<li>Make it possible to tap and drag items in place without needing to click a particular icon to do so.</li>

<li>Instead of the hamburger icon alone for a menu, display it with the word "Menu" to indicate that a menu will open, or use the word "Menu" alone.</li>

</ul>

<h2 id="toc-conclusion-5">Conclusion</h2>

<p>Deviating from well-researched interface patterns is usually not recommended. It is better to follow the probable best practices, knowing that consistency and knowledge transferred from use of other iOS apps will prime <a href="/articles/efficiency-vs-expectations/">users’ expectations</a>. With any guidelines or style guides, doing usability testing can demonstrate or disprove if the guideline works well in your own design. Through watching people use these designs, we have witnessed enough consistent issues to recommend against using these 4 patterns.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Mobile User Experience" href="/courses/usability-mobile-websites-apps/?lm=4-ios-rules-break&amp;pt=article">

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

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">ios,Mobile &amp; Tablet,Design Patterns,standards &amp; conventions,Visual Design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet</span>

<a class="ga-article-related-topic" href="/topic/mobile-and-tablet-design/">Mobile &amp; Tablet</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/design-patterns/">Design Patterns</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/visual-design/">Visual Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>