import pandas as pd

# Load the matches data
matches = pd.read_csv('data/serie_a_matches_cleaned.csv')

# Initialize the league table
league_table = pd.DataFrame({
    'team': matches['homeTeam'].unique(),
    'points': 0,
    'played': 0,
    'goalScored': 0,
    'goalConceded': 0,
    'goalDifference': 0,
    'wins': 0,
    'draws': 0,
    'losses': 0,
    'leaguePosition': 0,
    'homeLeaguePosition': 0,
    'awayLeaguePosition': 0,
    'homePerformance': 0,
    'awayPerformance': 0,
    'recentForm': 0,
    'goalsPerMatch': 0,
    'homeGoalsScored': 0,
    'homeGoalsConceded': 0,
    'homeGoalDifference': 0,
    'awayGoalsScored': 0,
    'awayGoalsConceded': 0,
    'awayGoalDifference': 0,
})

# Update the league table based on match results
for index, game in matches.iterrows():
    if game['status'] == 'FINISHED':
        home_team = game['homeTeam']
        away_team = game['awayTeam']
        home_goals = game['ft_home']
        away_goals = game['ft_away']
        
        league_table.loc[league_table['team'] == home_team, 'goalScored'] += home_goals
        league_table.loc[league_table['team'] == away_team, 'goalScored'] += away_goals
        league_table.loc[league_table['team'] == home_team, 'goalConceded'] += away_goals
        league_table.loc[league_table['team'] == away_team, 'goalConceded'] += home_goals
        
        league_table.loc[league_table['team'] == home_team, 'homeGoalsScored'] += home_goals
        league_table.loc[league_table['team'] == away_team, 'awayGoalsScored'] += away_goals
        league_table.loc[league_table['team'] == home_team, 'homeGoalsConceded'] += away_goals
        league_table.loc[league_table['team'] == away_team, 'awayGoalsConceded'] += home_goals
        
        if game['winner'] == 0:  # Home team wins
            league_table.loc[league_table['team'] == home_team, 'wins'] += 1
            league_table.loc[league_table['team'] == away_team, 'losses'] += 1
        elif game['winner'] == 1:  # Draw
            league_table.loc[league_table['team'] == home_team, 'draws'] += 1
            league_table.loc[league_table['team'] == away_team, 'draws'] += 1
        elif game['winner'] == 2:  # Away team wins
            league_table.loc[league_table['team'] == away_team, 'wins'] += 1
            league_table.loc[league_table['team'] == home_team, 'losses'] += 1
        
        league_table.loc[league_table['team'] == home_team, 'played'] += 1
        league_table.loc[league_table['team'] == away_team, 'played'] += 1

# Calculate additional metrics
league_table['points'] = league_table['wins'] * 3 + league_table['draws']
league_table['goalDifference'] = league_table['goalScored'] - league_table['goalConceded']
league_table['homeGoalDifference'] = league_table['homeGoalsScored'] - league_table['homeGoalsConceded']
league_table['awayGoalDifference'] = league_table['awayGoalsScored'] - league_table['awayGoalsConceded']
league_table['goalsPerMatch'] = league_table['goalScored'] / league_table['played']

# Sort the league table by points
league_table = league_table.sort_values(by=['points', 'goalDifference'], ascending=[False, False]).reset_index(drop=True)

# Update league position
league_table['leaguePosition'] = league_table.index + 1

# Save the league table to a CSV file
league_table.to_csv('data/serie_a_league_table.csv', index=False)