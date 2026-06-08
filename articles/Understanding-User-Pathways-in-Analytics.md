# Understanding User Pathways in Analytics

**Author:** Page LaubheimerPage LaubheimerOctober 16, 20222022-10-16

**Topics:** Analytics & Metrics, Customer Journeys

**Source:** https://www.nngroup.com/articles/analytics-pathways/

---

October 16, 20222022-10-16

Share

Understandingusers’ journeysis one of the key insights that UX practitioners seek: if we know how our users move through our websites and what steps they take to satisfy their goals, we can better support them. Analytics tools often promise to reveal user journeys and offer dedicated tools for displaying how users move through a website.

However, understanding theuser’s journey requires more datathan analytics alone can provide — analytics cannot tell us each user’s specific goals or expectations and certainly cannot provide us with the richqualitativedetails like their thoughts and feelings that make journey mapping such a valuable exercise. But, while you wouldn’t make a whole meal from just garlic, garlic certainly is a valuable ingredient; so, too, is analytics a key ingredient in understanding common user journeys.

What type of information does analytics provide? Analytics can reveal the most commonpathwaysbetween pages — in other words, it can show us where most people start in our product or app and the pages or screens (or even features) they interact with next. These pathways are usually visualized in a Sankey diagram.

Definition: ASankey diagramis made up ofnodes(usually corresponding to pages, screens, or use of a feature) connected throughlinksthat indicate how people move from one node to the next. The width of the link indicates the amount of traffic that moves between those nodes.

While Sankey diagrams may look overwhelming, the basic concept is simple: they flow from left to right, showing a sequence of steps in columns, with each successive column representing the first, second, third (and so on) node viewed.

In each column, the nodes are ordered according to the traffic they get — with the highest one at the top. At the bottom of the column, the diagram indicates the number of dropoffs (users who exited the site or application). From each node, there are links connecting it to the next node that users viewed. The width of each link visualizes the number of users that traveled between those nodes, so that you can quickly identify common pathways.

One important point is that these user-flow diagrams aggregate (often dissimilar) traffic data. While many analytics platforms will allow you to dive into specific users’ sessions to some degree, the tools are built to present large-scale data. Theyshow trends rather than individual-user’s movementthrough the site. That is, they reveal the most common first steps, second steps, and so on. They compile users who may have had different intentions, goals, and information needs. Therefore, they do not represent realuserjourneys.

Since analytics cannotdirectly observe what’s going on in users’ heads, we haveno reliable way to segment this traffic by what the user was interested in.Two people with the exact same behavior may have had wildly different experiences. For example, on a search-results page two people may exit the site without clicking on any of the result links; one may have left out of frustration with the irrelevant results, the other may have got an answer to their question without clicking any links (an example ofgood abandonment). These two wildly different experiences will look identical in path reports, because we don’t know what each user was trying to achieve.

Because Sankey diagrams can be challenging to interpret, here are a few suggestions for how to analyze them effectively.

Because flow diagrams display a large amount of data, it can be overwhelming to make sense of what is happening. A key recommendation is to filter this data down into meaningful chunks to make the interpretation process easier.

If you were to watch all the traffic in a city moving at the same time, it’d very hard to see patterns unless you focused in on a single stream of traffic and paid attention to the details. How many people entered the highway via a specific ramp during rush hour? Where did they come from before merging onto the highway? If we follow them for a bit, where do they exit the highway? Was there a big traffic jam when a bunch of entering traffic met up with a bunch of traffic trying to leave in the same few exits? A transportation engineer will take that traffic data to investigate how to solve congestion problems. In user experience, while we don’t manage traffic jams very often, we are trying to get people to their destination with the lowest amount of effort (in terms ofcognitive load,working memory load, andinteraction cost), so knowing those common connections is still absolutely vital.

Since there are so many journeys all superimposed in these diagrams, you can’t typically reviewallof them. So, instead, focus on key pages or screens as your starting point for analysis. Make liberal use of the feature that allows you to hide everything except traffic flowing through a specific page. This feature allows you to highlight one node and see where users came from when they arrived at that node and then where they went afterwards.

It’s also worth taking the time to filter this data by usersegments. Are the common pathways different on mobile vs desktop? How about for users that have completed key goals, such as conversions, purchases, or even important feature usage? What do the pathways look like for users that interacted with your search as compared to those that didn’t, for example?

Review the first nodes that users encounter.While a lot of traffic will start on the homepage, many of your users’ first impressions are on internal pages. Take a look at those popular internal pages — do they clearly indicate the purpose of the site and do they feature understandableorientation, navigation, and wayfindingoptions to other key areas? Do these pages surface up links to key offerings, content, and features? Is thedropoff ratefrom any of these landing pages higher than from others? That’s an indication that there may be issues with the content of that page.

Examine each of the common non-homepage starting pages individually and where users went next. You can use this information to make hypotheses about what information needs users had; just be aware that this exercise will often have relatively obvious insights — most users will follow prominent links on the page.

Investigate which nodes are encountered at users’ second step.Look for patterns such as a high dropoff rate after the second interaction. Such data could be the only sign you get of problems such as the lack ofdeep linkingafter a login page. For example, a user of a meal-kit delivery service might get a weekly email reminder to choose their recipes. They click that link and are asked to log into their account before proceeding. After logging in, they are unceremoniously redirected back to the homepage with no obvious way to get to the promised customized content from the email. The user sighs with frustration and proceeds to close the browser tab, rather than hunt around for the page offered up in the email.

Compare related links to actual next paths.Looking at the list of next steps can also identify places where algorithmically generatedrelated-content linksorpersonalizedinformationaren’t really relevantto users. To do this, however, you’ll need to compare the related links on each of those nonhomepage starting pages to the pages where usersactuallywent next. If there’s a big difference, ask yourself why.

Review hub pages.Hub pagesare nodes with a lot of traffic coming into and out of them; they are typically routing pages that function like a form of navigation. Look forpogo sticking: places where users come back to the same hub page over and over. This pattern can indicate a frustrating experience while the user is trying to locate a known item, but it can also be a sign of high engagement and enjoyable exploration. Consider using the path report to identify pogo-sticking locations and do some qualitative user testing to find out why it’s occurring.

Another technique for investigating pathways is to begin your analysis by looking at theendof the flow, not at the beginning. (However, not all analytics tools may have this capability.) Start from a key goal you have for users — such as signing up for a service, purchasing something, filling out a lead-generation form, or interacting with a feature meant for power users. Then move backwards to see how users made their way to that goal. This approach can reveal howdiscoverableadvanced features are and howpersuasiveconversion-supportive content is.

This analysis technique can also help you to do a postmortem on less desirable outcomes. What are the last few features users typically interact with before deleting their account? Perhaps those interactions can help identify signs of dissatisfaction with the site or product, so that later on you can look more closely into the needs of those users who exhibit those signs (e.g., throughintercept recruiting) and try to address them.

User-path reports are an exploratory tool for understanding common ways that users move through a site. While helpful in understanding aspects of users’ journeys, they are not a replacement for qualitative research that seeks to understand the thoughts, feelings, and expectations of users as they use a product.

To learn more about the role that user-path reports have in UX work, take our full-day seminarAnalytics & User Experience.

Study your users’ real-life behaviors and make data-informed design decisions

Research

Capture and communicate UX insights across complex interactions

Research

Build a crossfunctional journey-centric design approach that scales

Management