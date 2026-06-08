# Cookie Permissions 101

**Author:** Samhita TankalaSamhita TankalaNovember 10, 20232023-11-10

**Topics:** Design Patterns, Analytics & Metrics

**Source:** https://www.nngroup.com/articles/cookie-permissions/

---

November 10, 20232023-11-10

Share

With the increase in regulation arounddata protection, companies must give users more control over data privacy by providing options for cookie permissions. The question becomes how to effectively give users clear and simple choices without confusing or frustrating them. To answer this question, we conducted a study to observe how users interact with a variety of cookie-permission designs.

Cookies are small data files that are sent and stored in an individual’s browser by a website. They record data about user preferences, browsing history, and other interactions. Cookies are often used to identify users over time. Here are some of the common reasons why companies use cookies:

Legislation such as GDPR, CCPA, and VCDPA grants users the right to control how data is collected about them by websites. As a result, websites mustobtain users’ consentbefore they store, retrieve, or use data stored on individual devices. Cookie permissions involve the process of obtaining that consent.

Cookie permissions are a requirement if your company has users in areas where cookie regulations apply. These laws give users the right to choose whether to allow cookies from different categories such as analytics, marketing, and third-party separately.

In addition, GDPR also demands that users actively opt into these cookies, rather than opt-out. What that means is that cookies other thanstrictly necessaryones cannot be used until the user actively selects them. If the user ignores the cookie-permission request, then that action counts as opting out and only strictly necessary cookies can be used.

(You should always check with your company’s legal team to determine how to comply with the laws that govern your users.)

Although cookies may provide benefits to users, there is a significant level of skepticism among many users regarding the data collected and how it is used. Many users feel uneasy about being tracked by websites through cookies, and the unclear options provided do not alleviate their concerns.

And can you blame them? Often cookie-permission designs don’t respect users’ choices. They can be confusing, difficult to use, or might rely on manipulative tactics to encourage users to opt in for cookies. These practices do not help build trust. Companies must find a balance between collecting data for personalized user experiences and upholding ethical practices. Merely having a cookie-permission box is insufficient.

Cookie permissions can be presented in two primary formats:

Some websites give users the ability to accept different types of cookies. Others may not provide users with options at all and, instead, inform users that the site uses cookies. Local laws will dictate how granular the cookie-permission request needs to be.

To understand the user experience of cookie-permission UIs, we conducted a qualitative usability study on mobile and desktop. The study involved 10 participants from all over the world. We explored a range of cookie-permission designs from live websites. Some of these were powered cookie-permission vendors, which are third-party services that allow companies to customize templates that comply with different regulations like GDPR.

We learned in our study that users’ willingness to share data and how they interact with cookie permission box options varied pretty drastically. These behaviors sometimes would vary depending on the situation. For example, some users said that they select theAccept alloptiononly when they are in a rush, but in other situations, they look through options in more detail. Here are common user types that we discovered during the study:

Understanding the range of how users interact with cookie permissions gives you an idea of whom your design might alienate. For example, only oneAcceptalloption might alienate users who are less willing to share their data.

Our study participants found cookie-permission designs annoying regardless of how willing they were to share their data. The degree of annoyance varied depending on the size, placement, options presented, and other UI elements of the cookie-permission design.

The following guidelines are based on research insights that emerged from the study. There are five main design considerations in cookie-permission requests:

1. Provide users with clearly marked, low-granularityoptionsfor cookie selection, including:Accept all,Denyall/Select strictly necessary only, and Manage settings.

Cookie-permission options give users autonomy over their data. Companies need to understand that not providing options for users who care about their data privacy can be just as risky as having users opt out of cookies. By not including options, sites lose their users’ trust. As a result, they may leave the site or clear cookies right after using it.

Website cookie permissions are becoming common, and users notice when options are not provided. During the study, a participant encountered a cookie-permission box with only anAcceptalloption. He said:

I am kind of used to opt out options. It doesn't seem to give the option to reject it or to tailor the cookies and the provisions to me, which […]  makes me feel a bit uneasy.

By not including multiple options, you may alienate users who care about what happens to their data.

2. Make cookie options immediately available rather than forcing users to click into extra pages for additional options.

On the Harper’s Bazaar website, you can’t deny cookies until you selectLearn more.The buttonLearn morehas lowinformation scentand doesn’t indicate whether there will be additional options available. Users might assume thatAccept allis their only option andLearn moreis just an explanation of the cookies used by the site.

Users prefer that options likeAcceptall,Managesettings,andDenyorStrictlynecessaryonlyare immediately available rather than hidden on secondary pages. This design builds trust and shows that the site does not try to force them toAccept all.It also supports quick access to the site content.

Having cookie options immediately available is particularly helpful on mobile devices, where screen space is limited, and it saves users from having to scroll or click around extensively.

3. Do not use deceptive UI patterns that trick users into opting into cookies.

Some companies use UI designs that trick users into accepting all cookies.

Here are some deceptive UI elements that you should avoid:

Many users can see through these deceptive tactics. One user came across a high-contrast button and said:

It’s obviously very leading because the Accept is darkened out. Like it kind of leads you to just click on that one, which for me is fine, but for other people, it may not be.

For these reasons, we recommend that you stay away from these problematic design patterns. If you decide to include aClosebutton in your cookie-permissions overlay, make sure that it amounts toAccept only strictly necessary.

4. Useplain language.

Sometimes websites use cookie options that are vague or too similar with each other. Users should be able to quickly scan the different options and decide which one is right for them.

5. Usebullet pointsto describe each cookie.

There are users who go through cookie settings every time to decide which to allow. ManyManageSettingspages provide long descriptions of each cookie. Bullet points with short descriptions make information scannable.

6. Minimize the size of cookie overlays to avoid obscuring page content.

Our study participants preferred small cookie-permission overlays that didn’t block access to the page content. Sites with big cookie overlays were viewed as intrusive and annoying. Some users wanted to know more about the site before deciding whether to accept cookies.

One study participant explained:

The simpler the better. I don’t want [the cookie-permissions overlay] to be intrusive. I don’t want it to cover my page. I definitely don’t want it to cover the page when I can’t even see what the page is, [I want] to decide before I have to accept.

A different participant who was on a website with a large cookie banner at the bottom of the screen said,I don’t like it when I can’t see [the website]. I don’t know that I want to accept their cookies before I know what the site is.

However, this same participant was okay with the UK government’s large cookie-permission banner, which was placed at the top of the page. He said,It’s big but it’s not actually covering up the rest of the site. It just kind of pushes the site down so I can still see what the site is and make a decision.

DHL took an alternate approach and useda modalcookie banner that allowed users to scroll the landing page but prevented them from clicking on anything before making a decision about cookies.

Some companies place the cookie-permission overlay in the middle of the screen or make it large and salient because they want to ensure that users make an informed decision. Other companies, who use a third-party cookie service, may not have a say in the placement or size of the cookie overlay.

Whatever the reason, if your content overlay is big and intrusive, give users clear and multiple options immediately to allow them to decide which permissions they will grant and then move on to the site.  A large cookie permission overlay is more frustrating when the cookie-permission options are unclear.

7. Do not include multiple competing overlays that show up immediately when a user lands on your site.

When multiple overlays (such as cookie permissions,newslettersignups, coupons, or chat features) compete for attention,the experience quickly deteriorates.

Users are getting more accustomed to cookie-permission overlays and expect to see them despite finding them annoying. But when sites add several popups or other disruptive elements, they run the risk of annoying users or even turning them away. Consider alternative locations (e.g., footer for newsletter signups) or wait to show certain overlays until after the user has accepted cookies.

Cookie-permission overlays shouldn’t be only a compliance requirement. They are an opportunity to build trust and foster a positive website experience for users. Ultimately, what we aim to do is respect users’ privacy while finding ways to enhance their experience on your website. These design guidelines will help you develop long-term relationships with your users and improve brand loyalty.

Anon. 2019. Cookies, the GDPR, and the ePrivacy directive. (May 2019). Retrieved August 31, 2023 fromhttps://gdpr.eu/cookies/

Lorenzo Porcelli, Massimo Ficco, and Francesco Palmieri. 2023. Mitigating user exposure to dark patterns in cookie banners through Automated Consent.Computational Science and Its Applications – ICCSA 2023 Workshops14105 (2023), 145–159. DOI:http://dx.doi.org/10.1007/978-3-031-37108-0_10

Study your users’ real-life behaviors and make data-informed design decisions

Research

Use metrics from quantitative research to demonstrate value

Research

Calculate, interpret, and report the numbers from your quantitative UX studies

Research