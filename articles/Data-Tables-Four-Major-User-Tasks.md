# Data Tables: Four Major User Tasks

**Author:** Page LaubheimerPage LaubheimerApril 3, 20222022-04-03

**Topics:** Application Design, Human Computer Interaction

**Source:** https://www.nngroup.com/articles/data-tables/

---

April 3, 20222022-04-03

Share

If you have lots of data, there’s a strong likelihood that you will end up displaying it in a table. Tables are present in manyworkplace applicationsprecisely because they are a compact way of showing a large multivariate dataset. However, big tables present challenges to both designers and users.

This article is part of a series that covers various aspects of designing usable tables:

Note: this article is primarily concerned with large data tables used in the workplace rather than withproduct-comparison tables(common on ecommerce websites).

Tables are not usually winners of a UI beauty contest — they are a utilitarian part of our designs. To embrace their functional advantages over other, perhaps more aesthetically pleasing, forms of multivariate-data displays (such as collections ofcardsordashboardswith variousinformation visualizationsanddata charts), we need to understand when to use tables and what kinds of user tasks are suited to them.

The primary advantages of a data table over other data-presentation options are:

While the specific tasks carried out on a table will vary depending on applications or even users, the following 4 tasks are frequently performed and can be considered the core tasks to be supported by a table design:

When users engage in this type of task, they may seek a specific item (whose name or other pertinent details they already know) or may look for several items that meet a few criteria they have in mind.

This process might involve filtering, sorting, using a search feature (or using the browser’s built-inCTRL-Ffeature on the page), or simplyvisually scanningdown the table. The reasons users will choose one of those interactions can be hard to predict and it’s based on the specifics of the data table, as well as on their expectations of what will be the least effortful way to find what they’re looking for.

Designing to support this task involves a few different things:

Tables are most effective when they allow users to easily compare data — whether this data is in two or more records or in different columns. Often, these comparisons aim to detect relationships between different variables or records, data ranges for a column, outliers or to simply explore what is typical for one or more variables.

There are two common issues that users encounter when performing comparisons in complex, big tables:

The primary design solutions ensure that:

Here are some specific guidelines related to these two principles.

Another common task in tables involves viewing, creating, or editing a single record. For all three cases, a tabular presentation of a single record can be challenging to read (and even more so to edit), especially when the table is wide and the user will have to scroll horizontally in order to access all the fields.

There are a variety of ways to present a single record as a complete unit, optimized for readability and editability. Each has different tradeoffs to consider:

Another important task in a table is to take action on one or multiple records (beyond editing the record itself) — for example, deleting, sharing, or performing some other data-specific action (like sending out invoices, changing deadlines, etc.).

Traditionally, there are two ways to implement this task:single-record actionsandbatch actions.

Placing thesingle-record actionsinline within a table row can work if you just have one or two actions, but, when there are more, screen space becomes an issue. As a result, multiple single-record actions end up either:

Batch actionsusually involve a mechanism for selecting records (e.g., acheckboxfor each record) and then a series of action buttons or menus above or below the table. This type of design allows for a space-efficient presentation of multiple options. If applying the same action to the full data set is a common need, it’s a convenient shortcut to have a single-click option toSelect All.

Compared to modular presentations such as card-based displays, tables are space efficient and well suited for comparing records and for detecting patterns in the data.

Data tables must support the following frequent user tasks:

Components, design patterns, workflows, and ways of interacting with complex data

Interaction