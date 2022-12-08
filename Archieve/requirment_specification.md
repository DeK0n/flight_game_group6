<h1>Requirment specification</h1>
<h2>Introduction</h2>
<p>In this document, we are going to give a thorough description of the flight game we are developing. Firstly, we are going to share our vision about the game, what is the main idea behind it and how does it work. Secondly, we will discuss the main gameplay components and everything the player can do in this game. We will also define the functional and quality requirements which are relevant to the game’s performance and players’ comfort. This document is mainly targeted towards developers of the game for the purpose of keeping track that the game is being developed in the right direction, as well as towards the person responsible for evaluating this project.</p>
<h2>Vision</h2>
<p>The main goal of the game is to visit given number of countries and spend as few credits as possible to get in "top budjet travellers ranking". </p>
<h2>Functional requirements:</h2>
<p> At the beginning, player has 10 000 credits on account.</br>
Credits are to a) fly, in related proportion to distance between airports</br>
b)to request weather forecast</br>
c)other functions may ne added later.</br>
The game session has no time limits but ends as soon as player visits definite number countries.(numer is told in the beginning) At this point final score is calculated and is written to top chart players table.</br>
d) flight price is calculated as 1cr=1km, weather forecast request cost 50cr(can be modified to balance)
Special features: </br>
a)if player has flown to airport and it is closed - player gets some penalty(define penalty for balance, and actions - return to arrival airport - or move to another.)</br>
b)other features may be added or changed</br>
c)player can get information about visited countries, current position, current score, and list of airport codes in any country without charging points</br>
d)NOT CONFIRMED IN BASE VERSION player can request distance information between airports using their codes for some charge </p>
<h2>Quality requirements</h2>
<p>Player must be able in any stage of the game to know their status, position, airports info etc.</br>
</p>
<h2>Boundary conditions from the task</h2>
<p>1) game is played by keyboard 2) use given databases, althout they can be modified 3) concrete goal and good game experience 4)sustainability  5) game etiquette (12+)</p>
