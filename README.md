# Evaluating the quality of LEC 2021 Spring split teams using graph theory
We construct a directed graph representing half of the games played in the LEC 2021 spring split. We then evaluate the teams using the PageRank and degree centrality and rank them from best to worst. We use the second half of the games to predict winners by using the rankings acquired from both centrality measures. The idea is that in every competitive league there are some upsets (theoretically better team losing versus a theoretically worse team) present. In any sport such a result can be seen as a fluke but it can also showcase potential strengths of the theoretically worse team. The PageRank centrality is a great way to take such implicit potential strengths into account. We compare the accuracy of both prediction approaches.

### PageRank accuracy: 51.1%
### Degree centrality accuracy: 48.8%

We can see that the predictions based on the PageRank centrality outperforms the predictions based on the degree centrality. Such a difference translates into only 1 correct prediction more but on a bigger sample of games this could mean a lot more correctly predicted games.
*All the credits for the data goes to: https://liquipedia.net/leagueoflegends/LEC/2021/Spring*
