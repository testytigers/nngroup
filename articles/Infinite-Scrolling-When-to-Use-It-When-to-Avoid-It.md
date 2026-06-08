# Infinite Scrolling: When to Use It, When to Avoid It

**Author:** Tim NeusesserTim NeusesserSeptember 4, 20222022-09-04

**Topics:** Design Patterns

**Source:** https://www.nngroup.com/articles/infinite-scrolling-tips/

---

September 4, 20222022-09-04

Share

Infinite scrollingis alisting-pagedesign approach which loads content continuously as the user scrolls down. It eliminates the need forpagination— breaking content up into multiple pages.

Since its invention in 2006, infinite scrolling experienced a steep growth in popularity. Today, it is mostly used on websites and apps with a flat structure, where content streams constantly and is equally relevant to the user — for example, social-media sites (e.g., TikTok, Instagram, Twitter) but also news or ecommerce websites (e.g., Apple News, Nike.com).What are the benefits and limitations of infinite scrolling?

Since its invention, some variations to classic infinite scrolling (as described above) have been developed. One variant requires the user to explicitly press aLoad MoreorSee Morebutton to see more content added to the bottom of a page. Another variant breaks down the infinite scroll into pages that serve as valuable landmarks for orientation and enable users to quickly navigate the content, as they can jump from one page to the next one.

Despite the benefits discussed above, infinite scrolling does have several drawbacks, which can impair the user experience:

Infinite scrolling results in a lack of landmarks to help users orient themselves. With pagination, users may remember the page that an item was on and that an item was close to the top of the page or towards the middle, butin an infinite list of items, it is hard to remember the location of any specific item and return to it.

This is especially disruptive for the user experience when websitesdo not save the user’s spot in the list duringpogo sticking. Frequently, users will click on an item in the infinite list or feed to go to its detail page and, when they come back, using theBackbutton, they will find themselves at the top of the list, having to scroll down through screenfuls and screenfuls of already seen content. In contrast, with pagination, users are returned to a single page of content. Even if they’re taken back to the top of the page, that reduced set of items is more manageable than on a page with infinite scrolling.

On some pages that use infinite scrolling without aLoad Morebutton, there can be anillusion of completeness: the user may assume that the end of the content stream has been reached as new content loads in the background, below the fold. Usually, this problem ariseswhen there is no indication that additional content is loadingas users reach the end of their preloaded content.

Infinite scrolling (without aLoad Morebutton) can make it impossible to access the footer of a website. The constant stream of content prevents users from reaching useful information usually hosted in the footer (e.g., contact information, return policies).

Infinite scrolling can cause additional problems for users withaccessibility needs. For keyboard-only users, infinite scrolling complicates navigating the web, due to the vast amount of content that can be placed on one page because such users have to “tab” through content link by link and therefore face a lengthy task if they want to navigate to the end of an infinite scroll. On the other hand, screen-reader users will only see the first “chunk” of the list, without being able to trigger the loading of new content.

However, in recent years there have been positive developments in supporting infinite scrolling for users with accessibility needs. For example, theARIA “feed” role, introduced by theWorld Wide Web Consortium (W3C), allows screen readers to scroll through a feed of infinitely scrolling content.  This role also enables keyboard users to move past the infinite feed to the first focusable element following it.

Sites with infinite scrolling often tend to take longer to load due to the infinite flood of new content. If sites try to do the right thing and keep track of users’ location on the page as users engage in pogo sticking (see above), then there could be a ton of content to be loaded whenever the user returns to a list.

The slow speed tends to be a problem for mobile users(due to the variable connectivity)or to any user in an area with low bandwidth or on limited data plans.

Some companies, like Facebook, attempt to overcome these page-load issues by launching “lite” versions of their products (e.g., Facebook lite and Instagram lite) that require less data to function. While this is a great approach to make products available to a wider range of users, it might not be feasible for smaller companies to develop an additional lite version of their product.

Last but not least,infinite scrolling can negatively impact the SEO performance of your website.This is because search engine crawlers cannot always access all the content that is hidden below the first section of your page and page speed (an important SEO factor) can be slowed down by infinite scrolling.

To avoid some of the drawbacks of infinite scrolling without returning to traditional pagination, many sites and apps implement a variation on the infinite-scrolling approach —infinite scrolling with aLoad Morebutton.Load Morebuttons have gained popularity recently, particularly in mobile sites and apps. This approach is not only used on ecommerce websites, but also on Google’s mobile search-result pages.

Adding aLoad Morebutton reduces some of the usability issues created by classic infinite scrolling.The main issues that aLoad Morebutton can resolve or decrease are:

One disadvantage ofLoad Morebuttons, compared to classic infinite scrolling, is that interaction cost increases — users have to click theLoad Morebutton to load more content. Even the small interruption of clickingLoad Moremight make users consume less content and cause them to switch tasks.

A new variant of classic infinite scrolling is infinite scrolling with integrated pagination. With this variant, as the user reaches the end of the first loaded content segment, a set of page indicators is displayed and then a new chunk of content is automatically loaded.

This approachhas the potential to reduce some of the usability issues created by classic infinite scrolling —in particular:

Even though integrated pagination might solve some of the usability issues caused by infinite scrolling, it can’t solve all of them. In particular, the inability to access the end of the page and an increased page load remain problems that make this design decision not feasible for websites that place relevant information in the footer section or websites that need to avoid long load times.

Moreover, this design pattern is so new that we don’t have user-testing data. Even though integrated pagination has the potential to improve classic infinite scrolling, itcould be that, at least for a while, it confuses more than helps users because of its low familiarity.

Because of the usability issues that infinite scrolling can cause, we do not recommend it when users will want to use the listing page’s content to:

Infinite scrolling is also not a good fit if you have a large user group from areas with low bandwidth or if your website is visited frequently by users with accessibility needs.

There is no solution (infinite scroll, pagination,Load More, or integrated pagination) that is overall superior and the perfect fit for every website.It always depends on the specific circumstances of your website and the goals that your users want to accomplish. To assess what is the best solution for your website consider the advantages and limitations of each of the four options. You should ask yourself questions like:

Infinite scrolling typicallyworks best for situations where users will want to scroll through homogeneous items with no particular task or goal in mind— for example, entertainment, news, or social media.

To explore new design trends and decide whether they’re right for your designs, check out our full-day courseEmerging Patterns in Web Design.

Kim, J. et al. 2016. Pagination versus Scrolling in Mobile Web Search.Proceedings of the 25th ACM International on Conference on Information and Knowledge Management.(2016).

Sharma, S. and Murano, P. 2020.A usability evaluation of Web user interface scrolling types. First Monday.25, 3 (2020).

Zhang, Y. et al. 2019.How do interruptions affect user contributions on social commerce? Information Systems Journal.30, 3 (2019), 535-565.

Strategically combine content, visuals, and interactive components to design successful web pages

Interaction

Trending UX patterns and their impact on the total user experience

Interaction

Essential UX design principles for small-screen websites and apps

Interaction