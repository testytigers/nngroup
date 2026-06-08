# 3 Design Considerations for Effective Mobile-App Permission Requests - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">10</span>

<div class="article-header">

<h1 class="article-h1">3 Design Considerations for Effective Mobile-App Permission Requests</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Maria Rosala</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/20211213_Vegas-maria.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/maria-rosala/">

Maria Rosala</a></span>

<p class="publication-date">

April 28, 2019

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2019-04-28</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: 3 Design Considerations for Effective Mobile-App Permission Requests&amp;body=https://www.nngroup.com/articles/permission-requests/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/permission-requests/&amp;title=3 Design Considerations for Effective Mobile-App Permission Requests&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/permission-requests/&amp;text=3 Design Considerations for Effective Mobile-App Permission Requests&amp;via=nngroup" data-share-type="Twitter">

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

</span>Mobile permission requests are often poorly designed. Consider the content and timing of these requests, avoid dark patterns, and enable users to reverse their decision.

</div>

<div class="article-body">

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

<a class="ga-article-toc-item" href="#toc-what-are-permission-requests-and-why-have-them-1">What Are Permission Requests and Why Have Them?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-3-design-considerations-2">3 Design Considerations</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-1-permission-request-copy-3">1. Permission-Request Copy</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-2-the-timing-of-the-permission-request-4">2. The Timing of the Permission Request</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-3-decision-reversal-for-permissions-5">3. Decision Reversal for Permissions</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-avoid-dark-patterns-6">Avoid Dark Patterns</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-summary-7">Summary</a>

</li>

</ul>

</div>

</div><h2 id="toc-what-are-permission-requests-and-why-have-them-1">What Are Permission Requests and Why Have Them?</h2>

<p>An app must request permission before accessing resources such as the camera, current location, or microphone, on the user’s mobile device. The app sends (via the operating system) a request in the form of a <a href="https://www.nngroup.com/articles/modal-nonmodal-dialog/">modal dialog</a>, asking the user to grant or decline access.</p>

<figure class="caption"><img alt="An image of the permission requests from Google Translate on iOS and Android side-by-side. The permission request asks the user to allow Google Translate access the microphone to enable dictation." height="577" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/20/google_translate.png" width="692"/>

<figcaption><em>Google Translate requires access to the microphone to use the dictation feature; iOS (left) and Android (right) permission requests differ slightly.</em></figcaption>

</figure>

<p>There are slight differences in how these requests are presented across mobile operating systems. As you can see from the example above, in iOS the user is asked for access to the microphone, whereas in Android the user is asked for permission to record audio. Moreover, in iOS, the modal dialog contains what’s called a <a href="https://developer.apple.com/documentation/uikit/core_app/protecting_the_user_s_privacy/accessing_protected_resources">purpose string</a>, which describes why the app is requesting access. This type of information is not present in Android. <strong>It’s up to Android designers to ensure that the rationale behind the request is introduced before the modal dialog appears</strong>.</p>

<p><strong>Permission requests give users perceived and actual control </strong>over their personal (and potentially sensitive) data. The decision to allow access can be a significant one, as the app often retains access to the resource until users uninstall the app or deliberately revoke the permission in their device’s permission settings. As a result, users need to trust that the app won’t ever maliciously access resources.</p>

<p><strong>App permission requests are still often poorly designed, </strong>despite fairly extensive guidance from the iOS and Android development community. One reason could be that permission requests are often not considered to be part of UX design, because the UI component for the permission itself is dictated by the operating system. It may also be hard for UX designers and app developers to understand why permission requests are so important. After all, who wouldn’t want to give access to every resource so they may use all the excellent functionality?</p>

<p>However, <strong>app permission requests contribute to the overall user experience and should follow the same usability principles as other features.</strong> They should:</p>

<ul>

<li>be easy to use and <a href="https://www.nngroup.com/articles/plain-language-experts/">understand</a></li>

<li>fit the user’s <a href="https://www.nngroup.com/articles/mental-models/">mental model</a></li>

<li>promote genuine, informed choice</li>

<li>stand up to scrutiny from regulators</li>

</ul>

<p>When permission requests are designed well, they seem reasonable and nonintrusive; users barely think twice when dealing with them. On the other hand, <strong>when permission requests are designed poorly, users often feel uncomfortable, confused, and irritated</strong>. They may even consider uninstalling the app and looking to competitors, especially if the app’s brand isn’t strong and the functionality doesn’t provide great utility.</p>

<h2 id="toc-3-design-considerations-2">3 Design Considerations</h2>

<p>3 design considerations greatly affect the quality of a permission request. These are:</p>

<p style="margin-left:.5in">1. Permission-request copy</p>

<p style="margin-left:.5in">2. Timing</p>

<p style="margin-left:.5in">3. Decision reversal</p>

<h2 id="toc-1-permission-request-copy-3">1. Permission-Request Copy</h2>

<p>The best permission requests <strong>communicate the rationale behind the request.</strong> In one study of 15 mobile apps, Tan and his colleagues found that users were <strong>12% more likely to grant a permission</strong> request when they were given a reason for the request. This estimate came from randomly showing or removing the purpose string included with each request, as designed by its vendor, even when the explanation was fairly poor.</p>

<p>Of more interest, the researchers also tested a series of different reasons for requesting access to contacts in a party-planning app they had created. Here, the most compelling reason (<em>Let Party Planner use your contacts to autocomplete email addresses)</em> resulted in a whopping <strong>81% lift</strong> in granted requests compared to the least compelling reason (<em>Party Planner would like to access your address book to show you the cheapest attractions by your contacts’ location and other purposes</em>.). As we’ve said many times before, <a href="https://www.nngroup.com/articles/interface-copy-decision-making/">UX copy drives decision making</a>. It’s not at all surprising that the wording of a request came close to doubling the acceptance rate, because <a href="https://www.nngroup.com/courses/writing/">words are one of the most important elements of the user experience</a>.</p>

<p>When users read a permission request, they perform an implicit<strong> cost­–benefit analysis.</strong> They ask themselves how much benefit they will receive from granting this permission and how much they trust the app to allow it access. <strong>Designers must write understandable copy</strong>, especially when communicating the rationale for unexpected permission requests, so as not to alarm users and to help them understand why the app requires access to a resource on their device.</p>

<p>In order to assist users in making an informed choice:</p>

<ul>

<li><strong>write content that is free from </strong><a href="https://www.nngroup.com/articles/plain-language-experts/">technical jargon</a><strong> and </strong><a href="https://www.nngroup.com/articles/user-centric-language/">focus on user-oriented benefits, rather than system-oriented features</a></li>

<li>clearly <strong>communicate to users </strong><a href="https://www.nngroup.com/articles/reciprocity-principle/">what they’ll get in return</a></li>

<li><strong>don't request access to resources without providing any value to users</strong>, as they may become suspicious of your app and <a href="https://www.nngroup.com/articles/brand-experience-ux/">brand</a>, and such data collection can be deemed excessive by regulators</li>

</ul>

<figure class="caption"><img alt='An image of an iOS permission request from Instagram that reads: "Instagram" would like to access your photos. This lets you share photos from your library and save photos to your camera roll.' height="758" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/20/instagram_access_photos.png" width="350"/>

<figcaption><em>Instagram clearly indicates the benefits of allowing the app to access the user’s photo library: the user can share photos with others and save photos edited within the app locally.</em></figcaption>

</figure>

<figure class="caption"><img alt="An image of an iOS permission request from United Airlines' mobile app. Permission reads: United would like to access your camera. Camera usage and photo for scanning various Travel documents and Payment options." height="622" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/20/united-access-camera.png" width="350"/>

<figcaption><em>In the United Airlines iOS app, the purpose string reads more like placeholder text than informative description. It makes the app look clumsy and arouse suspicion. (The capitalization of the words </em>Travel<em> and </em>Payment<em> also seems random and reinforces the impression of unprofessionalism.) Moreover, the explanation doesn’t communicate to users the benefit of allowing access. For example, while scanning travel documents is a feature, an actual benefit could be that if users scan their passport, they won’t have to enter the details in manually.</em></figcaption>

</figure>

<p><strong>Write requests that focus on user benefits. </strong>Don’t just mention the features that depend on the permission; frame your requests in terms of what those features will do for your users. This information makes it easy for users to understand the request and to accept it.</p>

<p>Example:</p>

<p style="margin-left:40px"><strong>OK: </strong><em>Skyscanner would like to access your location for flight-search personalization.</em></p>

<p style="margin-left:40px"><strong>Better: </strong><em>Skyscanner would like to access your location, so that you can quickly select departure airports near you.</em></p>

<p>Example:</p>

<p style="margin-left:40px"><strong>OK: </strong><em>Allow Snapchat access to your camera for taking photos.</em></p>

<p style="margin-left:40px"><strong>Better: </strong><em>Allow Snapchat access to your camera, so you can take snaps in the app to share with friends.</em></p>

<p>Far too many Android apps neglect to provide explanations for the permission request and user benefits (while their iOS versions provide perfectly good explanations). <strong>UX teams designing for Android should consider providing additional screens to communicate the purpose before the permission request appears</strong>; otherwise, consent cannot be seen to be properly informed.</p>

<figure class="caption"><img alt="A gif of a productivity app on Android. The screen in the app says &quot;Never forget to call back. Any.do can remind you to call back. Never let an important call slip away. If the user selects the 'allow' button two Android permission requests appear asking for access to contacts and for the app to manage and make phone calls." height="700" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/20/anydo.gif" width="350"/>

<figcaption><em>Any.do, an Android productivity app, provides an intro page upon launch, explaining the benefits of allowing access to the user’s contacts: get reminded to return phone calls. When users select </em>Allow<em>, the usual Android permission request is triggered. Without this initial screen, the permission request alone would be unexpected and potentially alarming for Android users, as users could wonder why a productivity app would require access to their contacts. However, it may not be appropriate to introduce the feature immediately after the app was launched for the first time, as I’ll discuss later.</em></figcaption>

</figure>

<h3><strong>Writing Suggestions:</strong></h3>

<ul>

<li style="margin-left:.5in;">Write in the <strong>active voice</strong>.</li>

<li style="margin-left:.5in;">Use <strong>plain language</strong> that your users understand.</li>

<li style="margin-left:.5in;">Explain why the app requires access and convey the user benefits. Generally, a good content formula for permission requests goes like this: [app]<em> would like to access your</em> [resource] <em>so that you can</em> [benefit/task].</li>

<li style="margin-left:.5in;"><strong>Avoid vague phrases </strong>such as <em> to offer a better user experience</em> when explaining why the app requires access. (Users are highly skeptical of vague promises and often suspect that they cover nefarious schemes.)</li>

<li style="margin-left:.5in;"><strong>For Android,</strong> design additional screens for unexpected requests, so that the rationale and benefits can be communicated to users before the permission-request dialog appears. (And if you’re Google, redesign the permission API, to make it easy to include an explanation right when the request is made.)</li>

<li style="margin-left:.5in;"><strong>Test your permission requests</strong> with users to find out whether they understand the text.</li>

</ul>

<h2 id="toc-2-the-timing-of-the-permission-request-4">2. The Timing of the Permission Request</h2>

<p>The timing of permission requests is important, as it can result in users finding the request either normal or alarming.</p>

<p>There are two types of permission request: context-related and system-initiated. <strong>Context-related permission requests are less likely to cause surprise</strong>: users select an icon in the app (such as a camera or microphone symbol) or tap inside an address field (for location), and the system reacts with a permission request. The context of the users’ action and timeliness of the modal dialog help them to reason about the meaning of the request.</p>

<p>Conversely, <strong>system-initiated requests</strong>, which are programmed to request a permission at a specific time,<strong> often require additional context</strong>. An example of a system-initiated request is when the user opens an app for the first time and is greeted with a dialog asking for access to the current location. Because system-initiated requests can be programed to appear at any time, there’s more potential for them to occur at moments that are inopportune for the user.</p>

<figure class="caption"><img alt="An image of a permission request from Google Maps in iOS. The permission message appears after the user has selected their destination and is about to start navigating. The permission request reads: Google Maps would like to access Apple Music, your music and video activity, and your media library." height="622" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/20/googlemaps.PNG" width="350"/>

<figcaption><em>Google Maps for iOS: An unexpected system-initiated request to access the media library appears when the user is about to tap </em>Start<em> to navigate to a local hotel. The user is left wondering how Google Maps would use that permission (the answer is: to display the details of the currently playing song within the app). While this feature could enhance the user experience, it is brought up at the wrong time because users are likely to be task-focused, and possibly in a hurry when they start navigation. A better option would be to advertise new features when users open the app and then allow them to discover these new features when it is convenient.</em></figcaption>

</figure>

<figure class="caption"><img alt="A gif of a navigation app called Waze on Android. A microphone button is selected and a permission request appears reading: Allow Waze to record audio?" height="654" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/20/waze_audio.gif" width="350"/>

<figcaption><em>Waze for Android: When users press the red microphone button, the record-audio permission request appears. This is an example of a helpful and expected context-related permission request.</em></figcaption>

</figure>

<figure class="caption"><img alt="A gif showing 5 system-initiated requests from Viber on Android." height="700" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/20/ezgifcom-optimize.gif" width="350"/>

<figcaption><em>When users install Viber (a messaging app) on an Android device, they are greeted with 5 system-initiated permission requests in a row, inducing a serious case of request fatigue. These are to access the user’s contacts, photos, camera, microphone, and location. While the user can guess why Viber might need access to contacts, other requests are less intuitive. The timing of some of these requests could be improved: for example, the permission to access the photo library and camera should be requested when users try to upload a picture from their phone or take a picture in the app, respectively.</em></figcaption>

</figure>

<p>Interruptions at the start can be overwhelming and confusing. First impressions are formed when users install an app. Asking for all permissions (like Viber does on Android) is like <a href="https://www.nngroup.com/articles/donation-usability/">asking for a donation without telling people</a> anything about the charity. A better modus operandi is to ask only for core permissions (essential for the core functionality of the app) upon the first launch and ask for further permissions only when they are needed to offer the user additional functionality.</p>

<h3><strong>Suggestions for timing permission requests:</strong></h3>

<ul>

<li>Don’t show all permission requests at once. Avoid asking for all permissions upfront, when the app is first installed.</li>

<li>Whenever possible, initiate a permission request when the user selects a feature that requires that permission. This approach gives the request important context and the user a feeling of control, plus it’s more likely for users to understand why the app needs it and agree to it.</li>

<li>When users are completing a task in your app, don’t interrupt them with an unrelated system-initiated permission request, because <a href="https://www.nngroup.com/articles/most-hated-advertising-techniques/">unsolicited modal dialogs irritate users</a> and are quickly dismissed.</li>

<li>Provide value to the user before asking for noncritical permissions.</li>

</ul>

<h2 id="toc-3-decision-reversal-for-permissions-5">3. Decision Reversal for Permissions</h2>

<p>Sometimes users initially deny access to a resource and later want to reverse their decision. For example, they may deny access to the phone contacts for a messaging app, but later realize that adding contacts manually is too arduous and may wish to reverse their initial decision.</p>

<p>Rather than reporting an error when users try to access a feature that relies on a denied permission, <strong>clearly explain why that functionality can’t be used, and make it easy for them to grant access</strong>. Sometimes users don’t make the mental connection between a permission and a functionality, so providing this messaging helps users to form the right mental model of the app’s workings.</p>

<p>Secondly, <strong>provide a link to </strong>where they can toggle the permission on, in order to make sure that users will not get lost in their permission settings.</p>

<figure class="caption"><img alt="An image of a screen in the Venmo app in iOS when the app doesn't have permission to access the camera. The text reads: No camera access. To scan codes and take pictures for your profile, allow us to use your camera in Settings &gt; Privacy &gt; Camera. Open Settings." height="622" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/20/venmo.PNG" width="350"/>

<figcaption><em>Venmo for iOS, a cash app for sending and receiving money from friends, shows this screen to users after they’ve declined the permission to access their camera. The text communicates the existing state of access and provides a link to the exact place in the device’s settings where the user can toggle the permission on from off. The only thing that could be improved here is making the </em>Open Settings<em> link <a href="https://www.nngroup.com/articles/clickable-elements/">look more like a link</a>, as it could be easily mistaken for simply text.</em></figcaption>

</figure>

<h3><strong>Tips for designing for decision reversal:</strong></h3>

<ul>

<li style="margin-left:.5in;">When users try to access functionality in the app that requires a permission they initially declined, clearly describe the reason the functionality is not available.</li>

<li style="margin-left:.5in;">Provide a link to the exact place in the device’s settings where they can reverse their decision.</li>

</ul>

<h2 id="toc-avoid-dark-patterns-6">Avoid Dark Patterns</h2>

<p>Since the implementation of the GDPR requiring unambiguous consent for EU citizens, some app developers have begun implementing <a href="https://darkpatterns.org/">dark patterns</a> to nudge users to agree to their permission requests. In some cases, app developers try to couch a permission request as an informational dialogue (like in the WeChat example below). These requests can often pop up at times when the user is in the flow of a task. Sometimes designers make it deliberately difficult for users to deny the request. While these unscrupulous tactics may be successful in getting more users to accept permission requests, they are ethically and legally dubious. Moreover, they <strong>erode trust </strong>and<strong> may impact </strong><a href="https://www.nngroup.com/articles/communicating-trustworthiness/">user loyalty over time</a>.</p>

<figure class="caption"><img alt="A permission request shown in WeChat on iOS. The permission request reads: 'Find WeChat Friends. WeChat will upload your address book to its server to help you find out which mobile contacts are using WeChat. Your uploaded data is only used for matching contacts and won't be saved for other purposes'. The options for the user is to say 'OK' or 'Learn more'. 'OK' is labelled as 'Recommended'." height="758" loading="lazy" src="https://media.nngroup.com/media/editor/2019/03/20/wechat.PNG" width="350"/>

<figcaption><em>This notification from WeChat uses a dark pattern to disguise a permission request as an informational dialogue. The </em>OK<em> button is labeled </em>Recommended<em>, and there’s no option to directly decline the request. If users want to deny access to contacts, they have to pay a greater <a href="https://www.nngroup.com/articles/interaction-cost-definition/">interaction cost</a> because they’ll need to select </em>Learn more<em>, where yet more dark patterns make it difficult to find out how to decline the request.</em></figcaption>

</figure>

<p><strong>Avoid using dark patterns.</strong> Give your users enough information to make their own choice. Respect their decision. Remember, you can always support users to reverse their decision later.</p>

<h2 id="toc-summary-7">Summary</h2>

<p>App permission requests allow users to remain in control of their data. Users perform a cost–benefit analysis when deciding whether to accept a permission request. It’s important that designers think about how to communicate the benefits and when to make the request, so that users aren’t irritated or alarmed, and feel in control. Lastly, designers should avoid dark patterns, and instead present users with fair options and the ability to reverse their decision later.</p>

<p>For more on mobile notifications and related topics read our report <a href="https://www.nngroup.com/reports/mobile-website-and-application-usability/">UX for Mobile Applications and Websites</a>.</p>

<h3><strong>References:</strong></h3>

<p>Tan, J., Nguyen, K., Theodorides, M., Negrón-Arroyo, H., Thompson, C., Egelman, S. and Wagner, D. (2014). <a href="https://doi.org/10.1145/2556288.2557400">The effect of developer-specified explanations for permission requests on smartphone user behavior</a>. In<em>Proceedings of the 32nd annual ACM conference on Human factors in computing systems - CHI ’14</em> (Toronto, Ontario, Canada, 2014), 91–100.</p>

<p>Android developer guidance: <a href="https://material.io/design/platform-guidance/android-permissions.html">https://material.io/design/platform-guidance/android-permissions.html</a></p>

<p>iOS developer guidance: <a href="https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/requesting-permission/">https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/requesting-permission/</a></p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=permission-requests&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet,Application Design,privacy</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet</span>

<a class="ga-article-related-topic" href="/topic/mobile-and-tablet-design/">Mobile &amp; Tablet</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>