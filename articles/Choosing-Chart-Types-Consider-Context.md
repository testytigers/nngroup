# Choosing Chart Types: Consider Context

**Author:** Kate MoranKate MoranJanuary 30, 20222022-01-30

**Topics:** Visual Design

**Source:** https://www.nngroup.com/articles/choosing-chart-types/

---

January 30, 20222022-01-30

Share

Quantitative UX datacan be incredibly powerful. It can help us make decisions, end arguments, or even prove the value of our work. However, I often find that many UX professionals struggle to present their data. In particular, they rarely put together compelling, easy-to-interpret charts.

You don’t have to have extensivevisual-designskills to create good charts from your analytics data or other quantitative UX data.  Simply apply the same user-centered–design approach that you would use when designing an interface.

Considerone key questionbefore you begin designing your chart:What is your goal?

In other words, what point are you trying to make? What do you want your audience to understand when they look at your chart? What action do you want them to take?

Once you’ve answered that question, tailor your chart to fit that goal (while not misrepresenting or falsifying the data, of course).

This article focuses on explanatory data visualizations — communicating a finding to teammates, stakeholders, or clients. You will likely need to create different types of charts to explore your data during the analysis process.

Also, this article discusses charts, notinfographics, which usually combine multiple visuals and data visualizations to tell a story. In addition, this article doesn’tcover dashboarddesigns.

The 3 Cs are an easy way to remember the most important aspects of any good chart:

We explore each of these factors ina three-part series.This article discusses the importance of context in data visualization and how context can help you decide which type of chart to create.

Numbers are meaningless without context. If I told you that the completion rate for checking out in an ecommerce app was 24%, what would that mean? Nothing, unless I also told you that the completion rate had been 17% in the previous year.People need to compare a number against another number in order to interpret it.

In UX, we often compare data points collected at differenttimes.For example, we could compare our completion rate for this year against our completion rate for the past 3 years. Or, we could look at completion time for an important task before and after a redesign.

Sometimes, instead of comparing two versions of the same product at different times, wecompare similar products, features, content, or user groups. For example:

When comparing numerical data, it’s important tobe familiar with at least the basics ofexperimental designand statistics— particularly confidence intervals and statistical significance. Our full-day courseHow to Interpret UX Numberscovers how these concepts apply to UX research.

There are many of different types of charts, but, for most UX purposes, we recommend the basics: bar charts, line charts, or scatter plots. Choose the chart that best suits your goal and the context you’re presenting.

For most of these common UX comparisons, thebar chart(sometimes called a column chart) works well. Researchers have found that bar charts are much easier for people to comprehend than other types of charts (like pie charts). This is because bar charts make it easy for people to quickly and accurately perceive the differences between values.

Apaired bar chartshows two data series side by side — for example, data about two different user groups, designs, or devices.

Let’s imagine we recently redesigned a website that sells home furniture. We have two primary user groups — people who buy furniture for their own homes (Consumers) and people who buy furniture for their clients (InteriorDesigners). We collect the average order value (AOV) for each group before and after the redesign; essentially, this number shows how much money we make from the average purchase.

In this case, we have two variables (user group and time) with two levels each, resulting in four datapoints we want to compare:

This is a great opportunity for a paired bar chart, but we have to decide how to group the data. We can either group the bars by time (before vs. after) or by user group (Consumersvs.InteriorDesigners).

Many people would opt to group them by time. (In one of my training courses, attendees often pick this grouping in a similar activity.) However, it’d be a mistake to group the bars by time in this case. To see why, take a look at the chart below.

Think about our objective in this example — to show the differences before and after the redesign for each user group.What comparison do you want people to make?Put those things close together, so your viewers easily see them side by side and understand your main point. In the above chart, the easiest comparison is between consumers and interior designers: it’s very clear that the professionals buy more than the amateurs. But this isn’t the most important point.

In a case like this one, we could simplify the chart even more by showing only the percent increase in order value for each user type. The result would be a simple bar chart with a single series. This approach does more of the work for the viewers — they don’t have to visually estimate those differences on their own.

Ahorizontal bar chartis a good option when you’re working with long labels — for example, feature names or task descriptions. The horizontal orientation allows you to display the labels without abbreviating or rotating them, as would be necessary with a vertical bar chart.

Another popular variation is thestacked bar chart. I often see this option used fortask-success levels. For example, such a chart could show, for each task, the breakdown of users who were successful on their own, successful with help from the facilitator, or failed the task.

In the previous horizontal bar chart example, we showed only the success rates for each task. Now, let’s include success with help and failures in a stacked bar chart.

The example above illustrates one of the key problems with the stacked bar chart. It’s easy to compare theSuccessbars shown in green, because all four bars are aligned on the x-axis at 0%. (Similarly, it’s reasonably easy to compare theFailbars, which are all right-aligned.) However, it’s much harder to compare theSuccess with Helpbars in yellow, because they don’t have the same starting point.

Also, notice that the stacked bar charts don’t allow you to showconfidence intervals(or any other type of error bars) — which are important for making sound numerical comparisons.

Research shows that stacked bar charts are in fact very hard to understand — they are among the charts with the highest error rates. That is why we strongly recommend that you stay away from them. Simply use a series of 3 bar charts instead (or even 3 different charts if you want to emphasize, for instance, that one task benefits from facilitator intervention than others.)

If you want to show a data trend over time, aline chartwill work better than a bar chart. For line charts, use data-point markers to clarify where in the timeline you collected data.

Finally, ascatterplotcan work in situations where you want to show the relationship between two variables. Scatterplots look like line charts, but the points are not connected with lines.

For example, to show that a few of the features in an app are used most frequently by the majority of users, we might show each feature as a dot plotted against the percentage of accounts that use each feature (x-axis) and the average amount of times the feature is used by each user in a month (y-axis).

Researchers have found that bar charts, line charts, and scatter plots are easiest to understand.

Other chart types require users to visually assess angle, area, or volume to understand the data. These tend to be much more challenging for people to process and include:

Just because they’re trickier to read, that doesn’t mean you can't ever use them. But before choosing one of these, go back to your goal: What are you trying to communicate? Is one of these more-complex visualizations adding value to your message? If your goal can be achieved with one of the basic charts, opt for them.

For example, many analytics and information-architecture testing tools use dendrograms to illustrate navigation flows. Those charts are good for indicating clusters of objects; the same information would be challenging to present with a bar or line chart.  Also, typically those tools use dendrograms for exploring data and conducting analysis — not for presenting findings or recommendations to stakeholders.)

Provide context for your data points by including relevant comparisons. Decide which type of chart to use based on the data type you’re working with and the comparison you’d like to present.

Thenext articlein series explainshow to keep your charts clean and focusedby removing unnecessary elements.

The following books and websites are good references on how to design great charts. These books provided inspiration for this article series.

Better Data Visualizations: A Guide for Scholars, Researchers, and Wonksby Jonathan Schwabish

Schwabish’s book provides concrete guidance on when to use each type of chart (from basic charts like bar charts to more obscure options like violin charts and treemaps). He provides detailed advice on how to design each type. Schwabish’s book is written in plain language and should be approachable for all experience levels.

Storytelling with Data: A Data Visualization Guide for Business Professionalsby Cole Nussbaumer Knaflic

Nussbaumer Knaflic’s guide advocates for applying a design mindset to your data visualizations — starting from a clear understanding of your audience and your objective. The book goes beyond data visualization to consider the story you build around your data.

The Visual Display of Quantitative Informationby Edward R. Tufte

As a data visualization classic, Tufte’s book elevates this “boring” topic to an art form. Tufte assembles a diverse collection of data-visualization examples from a variety of fields, countries, and centuries. While this book may be less practical and applicable than the others listed here, I highly recommend it to anyone deeply interested in data visualization.

For more inspiration, explore the websites of these organizations that excel (pun very much intended) at communicating quantitative data.

Pew Research Center

Pew conducts large-scale surveys and publishes reports. Each of Pew’s charts focuses on clearly communicating a single finding from their enormous data sets.

FiveThirtyEight

Every article on politics, economics, or sports that FiveThirtyEight publishes contains at least one chart, and some of them are interactive.

The Washington Post

This American newspaper’s site often provides innovating interactive data visualizations focusing on current events.

The Economist

You don’t have to know much about economics to appreciate these brilliant charts. (Unfortunately, you do have to be a paying Economist subscriber.)

Wired Magazine

Wired publishes interesting charts on variety of technology-adjacent topics. If you happen to have a Wired or Apple News+ subscription, check out theChartgeistcolumn in the magazine, which features comedic charts (they’re funnier than they sound).

Nussbaumer Knaflic, C., 2015.Storytelling with Data: A Data Visualization Guide for Business Professionals,Wiley.

Tufte, E., 1983.The Visual Display of Quantitative Information,Graphics Press.

Heer, J. and Bostock, M. and Ogievetsky V., 2010. A Tour Through the Visualization Zoo,ACM.

Schwabish J., 2021.Better Data Visualizations: A Guide for Scholars, Researchers, and Wonks,Columbia University Press.

Cleveland W. and McGill, R., 1984. Graphical Perception and Graphical Methods for Analyzing Scientific Data, Journal of the American Statistical Association.

Use metrics from quantitative research to demonstrate value

Research

Calculate, interpret, and report the numbers from your quantitative UX studies

Research