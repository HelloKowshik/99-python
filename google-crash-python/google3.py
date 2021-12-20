
# for left in range(7):
#     for right in range(left, 7):
#         print(f"[{str(left)} | {str(right)}]", end=" ")
#     print()


teams = ["Dragons", "Wolves", "Pandas", "Unicorns"]


def match_fixture(team_list):
    for home_team in team_list:
        for away_team in team_list:
            if home_team != away_team:
                print(f"{home_team} VS {away_team}")


match_fixture(teams)
