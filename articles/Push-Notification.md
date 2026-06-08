# Five Mistakes in Designing Mobile Push Notifications - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">7</span>

<div class="article-header">

<h1 class="article-h1">Five Mistakes in Designing Mobile Push Notifications</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Alita Kendrick</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/alita-kendrick.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/alita-kendrick/">

Alita Kendrick</a></span>

<p class="publication-date">

November 18, 2018

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2018-11-18</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Five Mistakes in Designing Mobile Push Notifications&amp;body=https://www.nngroup.com/articles/push-notification/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/push-notification/&amp;title=Five Mistakes in Designing Mobile Push Notifications&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/push-notification/&amp;text=Five Mistakes in Designing Mobile Push Notifications&amp;via=nngroup" data-share-type="Twitter">

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

</span>Provide value to users before asking them to receive your app’s notifications; tell them what the notifications will be about. Don’t send notifications in bursts; make it easy to turn them off.

</div>

<div class="article-body">

<p>When properly executed, mobile push notifications can provide users with relevant information to encourage them to engage with an app. However, when poorly implemented, notifications can deter users from interacting and, in severe circumstances, can prompt them to delete an app altogether.</p>

<p>In 2016, the average mobile phone user received <strong>56 notifications per day </strong>according to a study from Telefonica Research in Spain [Pielot 2018]. Today, maybe more? For sure, notifications need to be designed properly, or they can be highly detrimental to the user experience, given this barrage of notifications.</p>

<p><a href="https://www.nngroup.com/articles/indicators-validations-notifications/">Notifications</a> are generally not triggered by the user’s immediate actions. Nonetheless, they announce an event that (supposedly) has some significance to the user. There are two main types of notifications: action-required and passive. Action-required notifications, as the label suggests, require the user to act upon the information received in the notification. Passive notifications are purely informational. Most push notifications are passive.</p>

<p>Do you ever feel the need to read an email as soon as you get it? When the message is important or time-sensitive, this behavior is beneficial. However, if the message is unimportant, you may feel bad because you became distracted and wasted time reading it. Push notifications can be disruptive for the same reason.</p>

<p>Notifications can happen in almost any type of user interface. For example, in Windows 10, they usually appear either as a “toast” that slides up from the taskbar for a short time or as a small icon in the dedicated notification area of the taskbar. In auditory interfaces, notifications can be especially disruptive, if the system started speaking when you least expect it. In this article, we’ll focus on notifications on mobile devices. Mobile notifications have the potential to be particularly useful (when used right) since many people carry their mobile device most of the time and thus will be informed about an important event no matter when it occurs.</p>

<p>In this article, we discuss 5 push-notification mistakes that mobile apps make frequently:</p>

<ol>

<li>Asking users to enable notifications in the initial launch</li>

<li>Neglecting to tell users what information notifications will contain</li>

<li>Sending burst notifications</li>

<li>Sharing irrelevant content</li>

<li>Making it difficult to turn off notifications</li>

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

<a class="ga-article-toc-item" href="#toc-mistake-1-asking-users-to-enable-notifications-immediately-after-launching-an-app-for-the-first-time-1">Mistake #1: Asking Users to Enable Notifications Immediately After Launching an App for the First Time</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-mistake-2-neglecting-to-tell-users-what-information-notifications-will-contain-2">Mistake #2: Neglecting to Tell Users What Information Notifications Will Contain</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-mistake-3-sending-notifications-in-bursts-3">Mistake #3: Sending Notifications in Bursts</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-mistake-4-sharing-irrelevant-content-4">Mistake #4: Sharing Irrelevant Content</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-mistake-5-making-it-difficult-to-turn-off-notifications-5">Mistake #5: Making it Difficult to Turn Off Notifications</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-6">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-mistake-1-asking-users-to-enable-notifications-immediately-after-launching-an-app-for-the-first-time-1">Mistake #1: Asking Users to Enable Notifications Immediately After Launching an App for the First Time</h2>

<p>Users who have just downloaded your app do not necessarily have a clear understanding of the value the app will bring to them. At that point, the app has not yet gained their <a href="https://www.nngroup.com/articles/commitment-levels/">trust</a>, but it asks for permission to invade their screens. What will users get from the app’s notification?</p>

<p>This offense is so frequent that users barely read the message anymore. In many of our studies, the immediate response is to click <em>Don’t Allow</em>. Instead, apps should take advantage of the <a href="https://www.nngroup.com/articles/reciprocity-principle/">reciprocity principle</a> and offer users some value first. <strong>Allow them to experience the app</strong> and only in a later session ask them to accept notifications.</p>

<p><strong><img alt="" height="15" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/x-red-fill.png" style="width:15px;" width="15"/> DON'T</strong></p>

<figure class="caption"><img alt="" height="623" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/freeprints.PNG" width="350"/>

<figcaption><em>FreePrints, an app for ordering photos, greets first-time users with a simple splash screen which transitions into a Getting Started page. Before users get a chance to read the copy on this page, they’re interrupted with a message asking them to allow notifications. FreePrints has neglected to inform users of what type of notifications they will receive and why they will find the content valuable.</em></figcaption>

</figure>

<p><strong><img alt="" height="15" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/check-green-fill.png" style="width:15px;" width="15"/> DO</strong></p>

<figure class="caption"><img alt="" height="413" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/game-of-thrones.png" width="483"/>

<figcaption>The Conquest mobile game lets users experience the app before asking them to enable notifications. Game players complete multiple tasks to increase their stats and level up. Only after a player has leveled up for the first time does the game ask users to enable notifications.</figcaption>

</figure>

<h2 id="toc-mistake-2-neglecting-to-tell-users-what-information-notifications-will-contain-2">Mistake #2: Neglecting to Tell Users What Information Notifications Will Contain</h2>

<p>Consider the generic messaging that iOS sends users: <em>X company would like to send you notifications</em>. This message focuses on what the company wants from users, but not on what the user will gain from the company. For some apps (such as social-media or news apps) users can make reasonable guesses on the sort of information they will see in notifications. On the other hand, it’s harder to guess the content of the notifications sent by a retail or an entertainment app. Details about the nature of your notifications can make users understand whether they need them and can increase the perceived credibility and trustworthiness of your app (after all, you’re being honest and transparent about your notifications, rather than trying to fool your users into accepting them).</p>

<p><strong>Tell people</strong> <strong>what notifications will be about</strong> to increase the chance that they will accept your request.</p>

<p><strong><img alt="" height="15" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/x-red-fill.png" style="width:15px;" width="15"/> DON'T</strong></p>

<figure class="caption"><img alt="" height="623" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/tasty.PNG" width="350"/>

<figcaption><em>The Tasty app, which houses food videos and recipes, doesn’t provide users with an explanation of the information that will be in notifications. Users are stuck pondering why Tasty wants to send them notifications and whether it will be content that they want to see or not.</em></figcaption>

</figure>

<p><strong><img alt="" height="15" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/check-green-fill.png" style="width:15px;" width="15"/> DO</strong></p>

<figure class="caption"><img alt="" height="623" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/nightsky.jpg" width="350"/>

<figcaption><em>Night Sky, an AR planetarium app explains what notifications will be about (stargazing conditions, object rise times, etc.). By providing this information before asking users to enable notifications, the app allows users to make an informed decision.</em></figcaption>

</figure>

<h2 id="toc-mistake-3-sending-notifications-in-bursts-3">Mistake #3: Sending Notifications in Bursts</h2>

<p>Has someone ever rung your doorbell repeatedly? This is the effect that burst notifications can have within an interface. Receiving many notifications in a short interval can overwhelm and irritate users, causing them to turn off notifications (or worse, delete your app). Not to mention, repeated notifications may appear sloppy and unprofessional, perhaps even <a href="https://www.nngroup.com/articles/needy-design-patterns/">needy</a>, leaving a lasting negative impression on your users.</p>

<p>Instead of filling your user’s screen with several notifications, <strong>send fewer notifications in a meaningful way</strong>. If you have more than five notifications that you need to send at once, combine them into a single message. Shift the focus to quality over quantity and you will be sure to see increased user satisfaction.</p>

<p><strong><img alt="" height="15" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/x-red-fill.png" style="width:15px;" width="15"/> DON'T</strong></p>

<figure class="caption"><img alt="" height="623" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/wunderlist-notifications.PNG" width="350"/>

<figcaption><em>Wunderlist, a to-do–list app, sends notifications for every task that is due. Receiving reminders via notifications is helpful until it becomes overwhelming. If multiple items have the same due date, they will result in burst notifications.</em></figcaption>

</figure>

<p><strong><img alt="" height="15" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/check-green-fill.png" style="width:15px;" width="15"/> DO</strong></p>

<figure class="caption"><img alt="" height="623" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/instagram.png" width="350"/>

<figcaption><em>Instagram bundles notifications when several users like a photo that you’ve posted. In this case, rather than sending 11 separate notifications, Instagram sent one with the names of two users and a numeric count of the others. (Ideally, the two users named would be the ones of most salience to the user and not just the two most recent likes.)</em></figcaption>

</figure>

<p>Note: iOS 12 makes it easier to deal with burst notifications by grouping all notifications from one app into a single stack. However, combing through 10 similar notifications is overwhelming at worst and boring at best. Don’t rely on the operating system to deal with burst notifications for you.</p>

<figure class="caption"><img alt="" height="502" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/ios-notifications.png" width="483"/>

<figcaption><em>iOS 12 groups all the notifications from a single app under the same alert (left); tapping a stack shows the list of all notifications from that app (right).</em></figcaption>

</figure>

<h2 id="toc-mistake-4-sharing-irrelevant-content-4">Mistake #4: Sharing Irrelevant Content</h2>

<p>Any notification amounts to an interruption: it is meant to grab our attention and direct it to the notification. When the message is irrelevant to us, the interruption is irritating. Some people like to keep their inbox at zero unread messages, others like their phone’s lock screen clear of notifications. If you’re in the latter group, swiping away irrelevant notifications feels particularly time-consuming and bothersome.</p>

<p>Sending users notifications for every little thing that happens in your app is a big mistake. You don’t want to be the app that causes your users to roll their eyes any time a notification pops up on their screen. Nor should you justify this behavior by saying ‘Well, they can turn them off in settings.’ Instead, <strong>provide relevant content</strong> aimed to inform and engage.</p>

<p><strong><img alt="" height="15" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/x-red-fill.png" style="width:15px;" width="15"/> DON'T</strong></p>

<figure class="caption"><img alt="" height="623" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/venmo.PNG" width="350"/>

<figcaption><em>Venmo, an app that allows you to send money to people you know, sends users notifications when any transaction (even ones that do not involve the primary user) occurs. The app has a feed which shows when your friends send others money. When using the app, this feature isn’t bothersome (may be a little strange, but it’s not disruptive). But notifications with this type of content are irrelevant because they do not pertain to the main user.</em></figcaption>

</figure>

<p><strong><img alt="" height="15" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/check-green-fill.png" style="width:15px;" width="15"/> DO</strong></p>

<figure class="caption"><img alt="" height="622" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/redditasset-2.png" width="350"/>

<figcaption><em>Reddit sends users notifications when there is a trending post in a subreddit they follow. Notifications for popular posts within subreddits that users subscribed to are relevant and prompt users to open the app and explore further content.</em></figcaption>

</figure>

<p>Ideally, apps should allow users more control over both the frequency and relevancy of notifications. Maybe people could specify the maximum number of notifications they would want in any given time period, or maybe they could require some minimum importance for events that triggered a notification. The latter feature is difficult to make usable, but it would be very useful in domains where it’s easy for users to specify importance. However, research shows that <a href="https://www.nngroup.com/articles/customization-of-uis-and-products/">most users don’t bother customizing their systems</a>, even when customization would help them substantially in the long run. Thus, allowing users to modify their preference settings are no excuse for pushing too many (or too unimportant) notifications to the many users who stick with the default settings.</p>

<h2 id="toc-mistake-5-making-it-difficult-to-turn-off-notifications-5">Mistake #5: Making it Difficult to Turn Off Notifications</h2>

<p>There are many reasons why users decide to turn off notifications:</p>

<ul>

<li>They get too many notifications overall.</li>

<li>Your content is less relevant or important to them than it once was.</li>

<li>They find them distracting.</li>

</ul>

<p>No matter the reason, you should never try to hide this functionality from your users. This practice is deceptive, decreases trust in the company and application, and provides users with all the more reason to delete your app.</p>

<p>Turning off app notifications should be straightforward and quick. <strong>Allow users to edit their notification preferences within the app</strong>, so they are not forced to go to their phone’s native settings. Additionally, place this functionality in the <em>Settings</em> section of your app to meet users’ expectations and ensure <a href="https://www.nngroup.com/articles/navigation-ia-tests/">findability</a>.</p>

<p><strong><img alt="" height="15" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/x-red-fill.png" style="width:15px;" width="15"/> DON'T</strong></p>

<figure class="caption"><img alt="" height="492" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/econ-times.png" width="568"/>

<figcaption><em>The Economic Times, an app focused on providing news related to the economy, does not allow users to change notification settings within the app despite some deceiving language. Within the hamburger menu, there are two places where users may reasonably expect to change their notification settings: Notifications Hub (left) and Settings (right). The Notifications Hub contains no information about changing notifications. The Settings page does not allow users to edit notification preferences either. To change notifications, users are forced to go to their phone’s global-notification settings.</em></figcaption>

</figure>

<p><strong><img alt="" height="15" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/check-green-fill.png" style="width:15px;" width="15"/> DO</strong></p>

<figure class="caption"><img alt="" height="488" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/15/elevate.png" width="585"/>

<figcaption><em>The brain training app, Elevate, allows users to edit their notification preferences within the app. Users can navigate to the Settings page (left), then select Push Notifications and navigate to a page where they can change the toggle state for any type of push notification (right).</em></figcaption>

</figure>

<h2 id="toc-conclusion-6">Conclusion</h2>

<p>Notifications are disruptive and <a href="https://www.nngroup.com/articles/does-user-annoyance-matter/">annoy</a> users when they are irrelevant. Don’t risk inciting negative sentiment. Allow users to experience your app and understand its value proposition before asking permission to send push notifications. Tell them what type of notifications you will send. Ensure that users can easily find and edit your app’s notification settings. Avoid burst notifications and share content that is relevant to the user at hand.</p>

<p>For more on mobile notifications and related topics, read our report <a href="https://www.nngroup.com/reports/mobile-website-and-application-usability/">UX for Mobile Applications and Websites</a>.</p>

<p> </p>

<h3>Reference</h3>

<p>Martin Pielot, Amalia Vradi, and Souneil Park (2018): <a href="https://dl.acm.org/citation.cfm?doid=3229434.3229445">Dismissed!: a detailed exploration of how mobile phone users handle push notifications</a>, <em>Proceedings MobileHCI '18 Conference.</em></p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Mobile User Experience" href="/courses/usability-mobile-websites-apps/?lm=push-notification&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet,design mistakes,mobile web</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet</span>

<a class="ga-article-related-topic" href="/topic/mobile-and-tablet-design/">Mobile &amp; Tablet</a>

</li>

</ul>

</div>

</div>

</div>

</div>