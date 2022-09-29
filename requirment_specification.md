<p>https://www.markdownguide.org/basic-syntax/ Markdown syntax</p>
<h2>The requirement specification document must contain at least the following chapters:</h2>
<ol>
  <li>Introduction</li>
  <li>Vision</li>
  <li>Functional requirements</li>
  <li>Quality requirements</li>
</ol>
<h1>Requirment specification</h1>
<h2>Introduction</h2>
<p>In this document, we are going to give a thorough description of the flight game we are developing. Firstly, we are going to share our vision about the game, what is the main idea behind it and how does it work. Secondly, we will discuss the main gameplay components and everything the player can do in this game. We will also define the functional and quality requirements which are relevant to the game’s performance and players’ comfort. This document is mainly targeted towards developers of the game for the purpose of keeping track that the game is being developed in the right direction, as well as towards the person responsible for evaluating this project.</p>
<h2>Vision</h2>
<p>The main goal of the game is to spend as few points as possible to get in top chart of players. During the game player tries to visit all countries in region (predifined by program), "flying" between airports.</br> Points are collected by a)flying, in related proportion to distance between airports b)by making requests to dispatcher database to check flight avalibility c)other functions may ne added later.</br>The game session has no time limits but ends as soon as player visits all countries. At this point points are finally calculated and are written down in top chart players table. </br>Special features: a) from current airport "A" player can choose airport "B" and fly there,not all airports are always available to fly to, player can request weather conditions there, or rely on luck and fly without checking weather. If the airport("B") is not available for landing and player flew to it anyway, player is not allowed to land and is automatically directed to another airport("C") by programm (random, but in the same country as airport "B" gets some ponts as price of dispathcing) b)other features may be added or changed c)player can get information about visited countries, current position, current score, and list of airport codes in any country without charging points d) player can request distance information between airports using their codes for some charge </p>
<h2>Functional requirements</h2>
<p>Here we write Functional requirements</p>
<h2>Quality requirements</h2>
<p>Here we write Quality requirements</p>

