my @tab = ();
### Add new link at the beginning
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddswm9b-65b1eb6c-9821-44ec-a2fc-4f402eae590d.jpg/v1/fill/w_1280,h_859,q_75,strp/philae_21_03_2020_by_archiwyzard_ddswm9b-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODU5IiwicGF0aCI6IlwvZlwvNTQ4NTEyMjUtMTNlZC00OTk5LWJlMjgtODgzZTE0M2U0NjFjXC9kZHN3bTliLTY1YjFlYjZjLTk4MjEtNDRlYy1hMmZjLTRmNDAyZWFlNTkwZC5qcGciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.eiM5xs4QufTVncOuLNBj6SgBV7nLziyqPF_UoQMLZRA";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddstyp0-7618edb5-dad6-4a7f-850b-13a068e5650a.jpg/v1/fill/w_1280,h_1937,q_75,strp/eglise_montfort_l_amaury_by_archiwyzard_ddstyp0-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTkzNyIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRzdHlwMC03NjE4ZWRiNS1kYWQ2LTRhN2YtODUwYi0xM2EwNjhlNTY1MGEuanBnIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.TQ2SqUoZdwLwWyE-61AiIsUB3eXEa9nVAVmw30EO7sU";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddsdy4v-6b644944-35c4-4fe7-9792-d89c9dec6b72.jpg/v1/fill/w_1066,h_749,q_70,strp/tit_on_eletrical_cable_by_archiwyzard_ddsdy4v-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9Mjc3MCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRzZHk0di02YjY0NDk0NC0zNWM0LTRmZTctOTc5Mi1kODljOWRlYzZiNzIuanBnIiwid2lkdGgiOiI8PTM5NDEifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.qMEOAp_5f3C-LexBmnVQmIxJC6gwJCogSwKyyXMWP80";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddrkzpu-348d33e4-b66d-4dbc-8c5a-63621e4334c6.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRya3pwdS0zNDhkMzNlNC1iNjZkLTRkYmMtOGM1YS02MzYyMWU0MzM0YzYuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.egMrA5SZzFVSRxseMtAz43-PUHIOIm8kngCUwI1deDg";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddrfp3h-09fd17fe-2a0d-4e64-b032-a260fee75b39.jpg/v1/fill/w_1046,h_764,q_70,strp/daily_painting_29_02_2020_by_archiwyzard_ddrfp3h-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzExMyIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRyZnAzaC0wOWZkMTdmZS0yYTBkLTRlNjQtYjAzMi1hMjYwZmVlNzViMzkuanBnIiwid2lkdGgiOiI8PTQyNjEifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.7BTTpgl55mpsaIaHjCjaz31muyKIiseFxJ7d0GMhXnQ";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddrcwuy-a84208f8-6727-4dfb-98f9-07b9dc660ddb.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRyY3d1eS1hODQyMDhmOC02NzI3LTRkZmItOThmOS0wN2I5ZGM2NjBkZGIuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.Zy6R-YlAQPvJ4X3W2fPYUrPQVe3GIOIZRoxuDsYZ1SA";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddr72d3-dff29957-106f-46b2-9359-718561f7d669.jpg/v1/fill/w_1042,h_767,q_70,strp/daily_drawing_25_02_2020_by_archiwyzard_ddr72d3-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTg5OCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRyNzJkMy1kZmYyOTk1Ny0xMDZmLTQ2YjItOTM1OS03MTg1NjFmN2Q2NjkuanBnIiwid2lkdGgiOiI8PTI1NzkifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.VrwleCyPXkl01PgZWG2D-vKH4A6X6Q4eQcec5CqhdW4";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddr14y9-d798453c-7107-4ac3-bf79-9975d6a69fa7.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRyMTR5OS1kNzk4NDUzYy03MTA3LTRhYzMtYmY3OS05OTc1ZDZhNjlmYTcuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.FgPkMBPhHdF57VrVW15JWd8lpdL0JaJToEqL_ign74A";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddqjmvm-c8095b45-b491-430b-ae62-d0cb554f3f55.jpg/v1/fill/w_799,h_1000,q_70,strp/daily_drawing_16_02_2020_by_archiwyzard_ddqjmvm-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9Mjk3NCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRxam12bS1jODA5NWI0NS1iNDkxLTQzMGItYWU2Mi1kMGNiNTU0ZjNmNTUuanBnIiwid2lkdGgiOiI8PTIzNzkifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.8IiC1t0w7xTHOVlXMOmTdvu_FQQhHX54_lhoj6HqfVw";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddqfkxw-225ddbf6-a692-45cf-b84d-67fdebf01219.jpg/v1/fill/w_1110,h_720,q_70,strp/aerobatics_of_a_swallow_by_archiwyzard_ddqfkxw-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjE0NCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRxZmt4dy0yMjVkZGJmNi1hNjkyLTQ1Y2YtYjg0ZC02N2ZkZWJmMDEyMTkuanBnIiwid2lkdGgiOiI8PTMzMDUifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.XnFa9m-lO5eNXduydo3I6TFDs85skIuV2luhlbLLsIw";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddq01iv-bc6911cf-f4cb-4fff-9a36-6237e6880b0d.jpg/v1/fill/w_800,h_999,q_70,strp/daily_drawing_08_02_2020_by_archiwyzard_ddq01iv-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NDE3OSIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRxMDFpdi1iYzY5MTFjZi1mNGNiLTRmZmYtOWEzNi02MjM3ZTY4ODBiMGQuanBnIiwid2lkdGgiOiI8PTMzNDQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.ss2fi99gagdck47vc034yiz83A1hpjtV3ujJGOur_ec";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddpvjys-af7a5b75-80bf-4173-884d-c8b312fd215b.jpg/v1/fill/w_1096,h_729,q_70,strp/daily_drawing_06_02_2020_by_archiwyzard_ddpvjys-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzIwNSIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRwdmp5cy1hZjdhNWI3NS04MGJmLTQxNzMtODg0ZC1jOGIzMTJmZDIxNWIuanBnIiwid2lkdGgiOiI8PTQ4MTMifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.pRuWlUx91yg1jRscdsf6F2cNEK8lwYfwwRmhQJFqPyI";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddpjbnw-04283e6f-3bed-42af-a3b7-e2aede95c0a6.jpg/v1/fill/w_1159,h_690,q_70,strp/king_fisher_study_by_archiwyzard_ddpjbnw-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTIwMyIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRwamJudy0wNDI4M2U2Zi0zYmVkLTQyYWYtYTNiNy1lMmFlZGU5NWMwYTYuanBnIiwid2lkdGgiOiI8PTIwMjAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.AbsBtixLFs0RAjY9upsiwcUdmWgm8Q90D-7lYMkVtHo";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddpg6d7-1b112ff1-4c8d-4b33-97af-3c78a34d1e20.jpg/v1/fill/w_1034,h_773,q_70,strp/daily_drawing_31_01_by_archiwyzard_ddpg6d7-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI2MSIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRwZzZkNy0xYjExMmZmMS00YzhkLTRiMzMtOTdhZi0zYzc4YTM0ZDFlMjAuanBnIiwid2lkdGgiOiI8PTE2ODgifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.PzG462vCwxlgJVia2069lhTZR74zwphmNjY8_CIZIaY";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddpce5k-ba966a33-2d18-4e59-b819-13ba568f8a68.jpg/v1/fill/w_1106,h_723,q_70,strp/_tonight_work_by_archiwyzard_ddpce5k-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTEzMCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRwY2U1ay1iYTk2NmEzMy0yZDE4LTRlNTktYjgxOS0xM2JhNTY4ZjhhNjguanBnIiwid2lkdGgiOiI8PTE3MjgifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.9jJuO2nCc-bCh9Vo7FtoYwJfMMSI9EuTRDeKLCuIELc";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddp24an-71c94052-a418-4980-b211-0397c9e238c7.jpg/v1/fill/w_894,h_894,q_70,strp/painted_for_a_friend_by_archiwyzard_ddp24an-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTYwMCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRwMjRhbi03MWM5NDA1Mi1hNDE4LTQ5ODAtYjIxMS0wMzk3YzllMjM4YzcuanBnIiwid2lkdGgiOiI8PTE2MDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.llFxrx1UaPqLZcz3wlU3Cf-NzxRN0M3iDrbx-z0jI04";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddorcvv-fbf9228d-392d-46c3-962d-0f5a01cca6a2.jpg/v1/fill/w_1089,h_734,q_70,strp/a_fish__to_change_by_archiwyzard_ddorcvv-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI0NiIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRvcmN2di1mYmY5MjI4ZC0zOTJkLTQ2YzMtOTYyZC0wZjVhMDFjY2E2YTIuanBnIiwid2lkdGgiOiI8PTE4NDgifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.L5jWdIRkICkz3Mj8FpkOICayACJM4RJwRq9uKKwJ3k0";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddom4ou-c9a3097f-9edc-4c1b-a658-e545e1694fd0.jpg/v1/fill/w_894,h_894,q_70,strp/swallow_with_morikuni_style_by_archiwyzard_ddom4ou-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTIxNCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRvbTRvdS1jOWEzMDk3Zi05ZWRjLTRjMWItYTY1OC1lNTQ1ZTE2OTRmZDAuanBnIiwid2lkdGgiOiI8PTEyMTQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.htv-jDtQZmFQKhjmaMrJoBN32DRFHI4Gc9qunm-Yu9U";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddojkti-ff93dcfc-aaa6-4c70-beb7-28a18bd8323d.jpg/v1/fill/w_970,h_823,q_70,strp/well__another_bird_inspired_by_hokusai_by_archiwyzard_ddojkti-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODg1IiwicGF0aCI6IlwvZlwvNTQ4NTEyMjUtMTNlZC00OTk5LWJlMjgtODgzZTE0M2U0NjFjXC9kZG9qa3RpLWZmOTNkY2ZjLWFhYTYtNGM3MC1iZWI3LTI4YTE4YmQ4MzIzZC5qcGciLCJ3aWR0aCI6Ijw9MTA0MyJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.K_V9Ajsk2PgjxSmoEK_cezBzfN9EQOBlbZ8gP9oyTT0"; 
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddofah3-002da690-b594-4d0d-9b7d-28c8f145df18.jpg/v1/fill/w_1052,h_759,q_70,strp/inspired_by_hokusai_by_archiwyzard_ddofah3-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTM4NiIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRvZmFoMy0wMDJkYTY5MC1iNTk0LTRkMGQtOWI3ZC0yOGM4ZjE0NWRmMTguanBnIiwid2lkdGgiOiI8PTE5MjAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.4U0W-Ceocbd__lf0AtBZ_W4lCsO9Mn4N4Vq-cEj3Dz8";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddo79cg-6b6f06ce-251c-4587-8eae-6809dc5c092a.jpg/v1/fill/w_1020,h_783,q_70,strp/watercolor_according_to_hokusai_by_archiwyzard_ddo79cg-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQ0NCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRvNzljZy02YjZmMDZjZS0yNTFjLTQ1ODctOGVhZS02ODA5ZGM1YzA5MmEuanBnIiwid2lkdGgiOiI8PTE4ODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.P4CNc522u8fyBOT8y-qdWqxubSBgCbkoWKYBL-pYEFM";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddnnqxd-93b4f976-3982-4382-9e3d-f31b3dca2283.jpg/v1/fill/w_1009,h_792,q_70,strp/swirl_in_ocean_by_archiwyzard_ddnnqxd-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTg5NiIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRubnF4ZC05M2I0Zjk3Ni0zOTgyLTQzODItOWUzZC1mMzFiM2RjYTIyODMuanBnIiwid2lkdGgiOiI8PTI0MTUifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.bt94aapAjGhjKHJSqsRXRZ7TPcbVxsFzqpUL6bccCng";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddnl1nk-9221cd15-7616-4baf-a4a5-da31403fd7e7.jpg/v1/fill/w_1063,h_752,q_70,strp/first_drawing_of_2020_by_archiwyzard_ddnl1nk-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTg0MyIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRubDFuay05MjIxY2QxNS03NjE2LTRiYWYtYTRhNS1kYTMxNDAzZmQ3ZTcuanBnIiwid2lkdGgiOiI8PTI2MDcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.N13994a6tboRgdlZw-57KduFQhK1Cxgnb5sKg_agIfQ";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddmwogp-601e1d28-4f24-4eec-9bc1-96620c6dfa82.jpg/v1/fill/w_1156,h_691,q_70,strp/cherry_blossom_study_by_archiwyzard_ddmwogp-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTc0NiIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRtd29ncC02MDFlMWQyOC00ZjI0LTRlZWMtOWJjMS05NjYyMGM2ZGZhODIuanBnIiwid2lkdGgiOiI8PTI5MjAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.K5pgK-wnGNDLO7k_PM6HQZihbM-WcMv9SIhkmOIFgc4";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddmulwa-2e8e3a0b-6495-4413-b1e4-54f87436b8ac.jpg/v1/fill/w_983,h_813,q_70,strp/art_of_the_day_by_archiwyzard_ddmulwa-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTc1OSIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRtdWx3YS0yZThlM2EwYi02NDk1LTQ0MTMtYjFlNC01NGY4NzQzNmI4YWMuanBnIiwid2lkdGgiOiI8PTIxMjUifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.MEEb6y4clYc8xFRCPtKlU9VqF4sHum2P_OzgVATRKHg";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddlczc0-c2123f8f-b5c9-4b9e-96fe-58e10dd193a0.jpg/v1/fill/w_928,h_861,q_70,strp/daily_drawing_30_11_2019_by_archiwyzard_ddlczc0-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQzOCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRsY3pjMC1jMjEyM2Y4Zi1iNWM5LTRiOWUtOTZmZS01OGUxMGRkMTkzYTAuanBnIiwid2lkdGgiOiI8PTE1NTAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.gHtyA6t4XItA4la56Y35LEp2_LUzzr-4cgBUiv__rrU";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddl2faw-01f85de4-b23b-40ad-867e-8e48d991cf6e.jpg/v1/fill/w_1095,h_730,q_70,strp/magpie_sumi_e_by_archiwyzard_ddl2faw-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTYwMCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRsMmZhdy0wMWY4NWRlNC1iMjNiLTQwYWQtODY3ZS04ZTQ4ZDk5MWNmNmUuanBnIiwid2lkdGgiOiI8PTI0MDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.74F64E3SorHnLmBjgEX6iCMMPMRYj9rbbAk8NMe1jPQ";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddluioo-e3bc241d-dd6a-41b9-8c8d-1d05c6a627ca.jpg/v1/fill/w_1095,h_730,q_70,strp/zen_drawing_by_archiwyzard_ddluioo-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTYwMCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRsdWlvby1lM2JjMjQxZC1kZDZhLTQxYjktOGM4ZC0xZDA1YzZhNjI3Y2EuanBnIiwid2lkdGgiOiI8PTI0MDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.nMu0qhVhfTwYIDpqwxPI4r6MgLqcLd3lhQmH6P670g8";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddl04b7-53183511-4578-4594-b84a-7945504b01ed.jpg/v1/fill/w_1138,h_702,q_70,strp/swallow_and_cherry_blossom_by_archiwyzard_ddl04b7-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQ4MSIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRsMDRiNy01MzE4MzUxMS00NTc4LTQ1OTQtYjg0YS03OTQ1NTA0YjAxZWQuanBnIiwid2lkdGgiOiI8PTI0MDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.P5EHsPcOkPQ6ENDt-pmdv0MhUjp_0QpDH9epyii6ZxM";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddkwyfd-6d36f9c9-4a91-4c5d-8f43-c1c4b1c475ae.jpg/v1/fill/w_1059,h_754,q_70,strp/sumi_e_experimentation_by_archiwyzard_ddkwyfd-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTMxNiIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRrd3lmZC02ZDM2ZjljOS00YTkxLTRjNWQtOGY0My1jMWM0YjFjNDc1YWUuanBnIiwid2lkdGgiOiI8PTE4NDcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.IESdj1xzxsX1tiYTN0V9fGa3RDaDFgapZ3uwREQfdkk";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddkksb6-7f9c7630-3676-4d5f-9249-ee292d775f05.jpg/v1/fill/w_800,h_1000,q_70,strp/tree_sumi_e_style_by_archiwyzard_ddkksb6-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjAwMCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRra3NiNi03ZjljNzYzMC0zNjc2LTRkNWYtOTI0OS1lZTI5MmQ3NzVmMDUuanBnIiwid2lkdGgiOiI8PTE2MDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.Ru4fTV1Ky5dZOoWG0z9grh1m6y49_mrgxrlKZniNmHM";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddnlkh1-0fd3b697-2742-43d0-a7c3-121ee1f0c951.jpg/v1/fill/w_1136,h_703,q_70,strp/drawing_i_forgot_to_post_by_archiwyzard_ddnlkh1-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTMyMSIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRubGtoMS0wZmQzYjY5Ny0yNzQyLTQzZDAtYTdjMy0xMjFlZTFmMGM5NTEuanBnIiwid2lkdGgiOiI8PTIxMzQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.k2J5Mt6iMvXiZE8LDlCu0_fWsVIDSwRPe6zSLEWgAhc";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddjzi8p-19b5b518-b3d1-48a8-99cb-2dcc3552ae6e.jpg/v1/fill/w_1120,h_714,q_70,strp/daily_drawing_07_11_2019_by_archiwyzard_ddjzi8p-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTM1MyIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRqemk4cC0xOWI1YjUxOC1iM2QxLTQ4YTgtOTljYi0yZGNjMzU1MmFlNmUuanBnIiwid2lkdGgiOiI8PTIxMjIifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.Rm2xSPf5oXT5wp71Mvgq65_Xw_EG653jpP_EgFED6ZA";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddilrik-edb3426e-697c-4ba2-a421-f08b0ded04a5.jpg/v1/fill/w_808,h_989,q_70,strp/wind_tower_athens_by_archiwyzard_ddilrik-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzExNCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRpbHJpay1lZGIzNDI2ZS02OTdjLTRiYTItYTQyMS1mMDhiMGRlZDA0YTUuanBnIiwid2lkdGgiOiI8PTI1NDIifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.jce2sF16lmEKwQQwSvHQhDVNVGkALyP7XKsM1KmXvLI";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddijmv1-138b0277-e718-43fe-b768-71100dfc5e58.jpg/v1/fill/w_1128,h_708,q_70,strp/cariatides_by_archiwyzard_ddijmv1-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjQ3OCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRpam12MS0xMzhiMDI3Ny1lNzE4LTQzZmUtYjc2OC03MTEwMGRmYzVlNTguanBnIiwid2lkdGgiOiI8PTM5NDcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.V6wMRTsSATWc8vCCjFWHIglOi4B36-uRw9ihgKExAb4";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddnllx6-154acd04-cf9f-4e31-bd50-fc5cbfe2b9e9.jpg/v1/fill/w_833,h_960,q_70,strp/mushrooms_watercolor_by_archiwyzard_ddnllx6-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTgyNiIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRubGx4Ni0xNTRhY2QwNC1jZjlmLTRlMzEtYmQ1MC1mYzVjYmZlMmI5ZTkuanBnIiwid2lkdGgiOiI8PTE1ODUifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.qjmblSuKdEehLMKiFLWjBZr8umWEVC1IOy0_HWF_9ys";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddhvcvs-e6b9eb0d-4925-460c-ac72-c5f80db12004.jpg/v1/fill/w_876,h_913,q_70,strp/little_swallow_by_archiwyzard_ddhvcvs-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjcyMCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRodmN2cy1lNmI5ZWIwZC00OTI1LTQ2MGMtYWM3Mi1jNWY4MGRiMTIwMDQuanBnIiwid2lkdGgiOiI8PTI2MTAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.QRQjgjEXxx5wpM4goEx3X4-MWkdpNgiymUrm_SEw4OA";
push @tab, "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/dciq3l5-57befe6e-6a19-4d06-9970-93faefdb13e1.jpg/v1/fill/w_1024,h_706,q_75,strp/swallow_by_archiwyzard_dciq3l5-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NzA2IiwicGF0aCI6IlwvZlwvNTQ4NTEyMjUtMTNlZC00OTk5LWJlMjgtODgzZTE0M2U0NjFjXC9kY2lxM2w1LTU3YmVmZTZlLTZhMTktNGQwNi05OTcwLTkzZmFlZmRiMTNlMS5qcGciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.41-6A9056v7h_Sbaff6EHjKVm-ADHfHSllT7W2H9xcQ";

my @desc = ();
### Add new desc at the beginning
push @desc, "Temple Philae Grece";
push @desc, "Church Montfort L'Amaury";
push @desc, "tit aquarelle";
push @desc, "Tit painting aquarelle";
push @desc, "Bird ink quarelle";
push @desc, "temple japanese aquarelle ink";
push @desc, "Blue tits nature";
push @desc, "Bird japanese ink";
push @desc, "Tit on a tree branch, painted by ALexandre Proux";
push @desc, "Aerobatics of a swallow, painted by Alexandre Proux";
push @desc, "Bird and glycine inspired by japanese prints, painted by Alexandre Proux";
push @desc, "Sparrow landing on a tree branch, watercolor and ink painted by Alexandre Proux";
push @desc, "A king fisher painted with watercolor and ink inspired by japanese prints, painted by Alexandre Proux";
push @desc, "Watercolor and ink, a bird inspired by hokusai, painted by Alexandre Proux";
push @desc, "Watercolor painting of two sparrows eatings fruits, painted by Alexandre Proux";
push @desc, "Koi, watercolor, black ink, painted by Alexandre Proux";
push @desc, "Fish like morukuni, painted with chinese ink by Alexandre Proux";
push @desc, "Bird inspired by Morukuni, ink and watercolor, painted by Alexandre Proux";
push @desc, "Bird and flowers inspired by Hokusai, Gansai Tambi watercolor and waterproof ink, painted by Alexandre Proux";
push @desc, "Sparrow and tree flowers inspired by Hokusai, Gansai Tambi watercolor and waterproof ink, painted by Alexandre Proux";
push @desc, "Sparrow on a tree branch, inspired by Hokusai and Hiroshige, painted by Alexandre Proux";
push @desc, "Swirls in ocean inspired by horushige Naruto swirl, painted by Alexandre Proux";
push @desc, "2 sparrows on a tree branch painted with sennelier watercolor by Alexandre Proux";
push @desc, "Cherry Blossom tree branch, Schmincke watercolor, painted by Alexandre Proux";
push @desc, "King Fisher, by Alexandre Proux";
push @desc, "Proud little tits";
push @desc, "Proud little tits";
push @desc, "Sumi e cherry blossom";
push @desc, "Cherry Blossom and swallow";
push @desc, "Sumi e landscape";
push @desc, "Sumi e tree";
push @desc, "Sumi e sparrow";
push @desc, "Sparrow and berries";
push @desc, "Wind tower Athens";
push @desc, "Sumi e sparrow";
push @desc, "Mushrooms";
push @desc, "Swallows";
push @desc, "Sumi e magpie";


# Get path 
my @path_tab = split (" ", `pwd`);
my $path = $path_tab[0];
$path =~ s/pause-nature\/(.*)?/pause-nature\//g;
my $templatePath = $path."/templates";
my $cssPath = $path."/static/css/layouts";

######################################
### HTML part 
### To copy in HTML file 
######################################
open (FILEin, "$templatePath/galerie_peinture.html");
open (FILE, ">$templatePath/htmlfile.txt");
my $copy = 1;
while (!eof(FILEin))
{
    my $line = <FILEin>;
    chomp $line;
    print FILE $line."\n" if $copy == 1;
    if ($line =~ /end autogenerated/i)
    {
        $copy = 1;
        print FILE $line."\n"; # Copy the autogenerated end comment 
    }
    if ($line =~ /start autogenerated/i)
    {
        $copy = 0;    
        createPic();
    }
}

system("mv $templatePath/htmlfile.txt $templatePath/galerie_peinture.html");

close(FILE);
close(FILEin);

######################################
### auto generate CSS
######################################
my $nbrLines = int(scalar(@tab)/4)+1;
open (FILE, ">$cssPath/gallery_paintings1.css");
print FILE "* {
  box-sizing: border-box;
  -webkit-animation: fadeIn 0.5s;
          animation: fadeIn 0.5s;
}

.cover {object-fit: cover;}

.gallery {
    display: grid;
    justify-content: center;
    grid-template-columns: repeat(4, 300px);
    grid-gap: 20px;
    grid-template-rows: repeat($nbrLines, 300px);
}

\@media (max-width: 768px) {
  .gallery {
    grid-gap: 10px;
    grid-template-columns: repeat(auto-fit, 50px);
    grid-template-rows: repeat(auto-fit, 50px);
  }
}

.gallery__item {
  cursor: pointer;
  border-radius: 5px;
  grid-row: span 1;
  grid-column: span 1;
  transition: -webkit-transform 0.1s ease-in-out;
  transition: transform 0.1s ease-in-out;
  transition: transform 0.1s ease-in-out, -webkit-transform 0.1s ease-in-out;
}
.gallery__item:hover {
  -webkit-transform: scale(1.1) rotate(5deg);
          transform: scale(1.1) rotate(5deg);
}

.gallery__select {
  display: none;
}\n";

for (0..scalar(@tab)-1)
{
    my $nbr = $_+1;
    print FILE ".gallery__select:nth-of-type($nbr):checked ~ .gallery .gallery__item:nth-of-type($nbr) {\n";
    print FILE "  cursor: default;\n";
    print FILE "  display: grid;\n";
    print FILE "  align-items: center;\n";
    print FILE "  grid-row: 1/-1;\n";
    print FILE "  grid-column: 3;\n";
    print FILE "}\n";
    print FILE ".gallery__select:nth-of-type($nbr):checked ~ .gallery .gallery__item:nth-of-type($nbr):hover {\n";
    print FILE "  -webkit-transform: none;\n";
    print FILE "          transform: none;\n";
    print FILE "}\n";
    print FILE "\@media (max-width: 768px) {\n";
    print FILE "  .gallery__select:nth-of-type(1):checked ~ .gallery .gallery__item:nth-of-type(1) {\n";
    print FILE "    grid-row: 1/-3;\n";
    print FILE "    grid-column: 1/-1;\n";
    print FILE "  }\n";
    print FILE "}\n";
}
print FILE "\@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
\@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}\n";
close(FILE);

sub autoHTML
{
    my ($name, $index) = @_;
    open (FILE_sheet, ">$templatePath/sheet_$name.html");
        print FILE_sheet "<!doctype html>
<html lang=\"en\">
    <head>

        <script data-ad-client=\"ca-pub-4353004932795007\" async
                src=\"https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js\"></script>

        <meta name=\"google-site-verification\" content=\"9cZqCjgkf5l9r1cUe7kBRjXSj4Ru49PHJiXJmp96S7k\" />
        <meta name=\"msvalidate.01\" content=\"ADBE1D6C621C0EE7980A84478EED53ED\" />
        <meta charset=\"utf-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
        <link rel=\"stylesheet\" href=\"../static/css/layouts/pure-min.css\">
        <link rel=\"stylesheet\" href=\"../static/css/layouts/grids-responsive-min.css\">
        <link rel=\"stylesheet\" href=\"../static/css/layouts/blog.css\">

        <script type=\"application/ld+json\">{\"\@context\" : \"http://schema.org\",\"\@type\" : \"Article\",\"name\" : \"pictures\",\"author\" : {\"\@type\" : \"Person\",\"name\" : \"Amandine Poterala\"},\"articleSection\" : \"Pictures\"}</script>
        <meta name=\"description\" content=\"Amandine's pictures.\">    

    </head>
    
    <body>
       <div id=\"layout\" class=\"pure-g\">
            <div class=\"sidebar pure-u-1 pure-u-md-1-5\">
                <div class=\"header\">

                    <p><center>
                        <img width=\"140\" height=\"140\" alt=\"Alexandre Proux avatar\"

src=\"https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/54851225-13ed-4999-be28-883e143e461c/ddp24an-71c94052-a418-4980-b211-0397c9e238c7.jpg/v1/fill/w_894,h_894,q_70,strp/painted_for_a_friend_by_archiwyzard_ddp24an-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTYwMCIsInBhdGgiOiJcL2ZcLzU0ODUxMjI1LTEzZWQtNDk5OS1iZTI4LTg4M2UxNDNlNDYxY1wvZGRwMjRhbi03MWM5NDA1Mi1hNDE4LTQ5ODAtYjIxMS0wMzk3YzllMjM4YzcuanBnIiwid2lkdGgiOiI8PTE2MDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.llFxrx1UaPqLZcz3wlU3Cf-NzxRN0M3iDrbx-z0jI04\">
                    </center></p>

                    <h1 class=\"brand-title\">Pause nature</h1>
                    <h2 class=\"brand-tagline\">Nature, watercolor and photography</h2>
                    <h2 class=\"brand-tagline\"></h2>
                    <nav class=\"nav\">
                        <ul class=\"nav-list\">
                            <li class=\"nav-item\">
                                <a class=\"pure-button\" href=\"/home\">Home</a>
                            </li>
                            <li class=\"nav-item\">
                                <a class=\"pure-button\" href=\"/reviews\">Reviews</a>
                            </li>
                            <li class=\"nav-item\">
                                <a class=\"pure-button\" href=\"/galerie_peinture\">Paintings</a>
                            </li>
                            <li class=\"nav-item\">
                                <a class=\"pure-button\" href=\"/galerie_pictures\">Pictures</a>
                            </li>
                            <li class=\"nav-item\">
                                <a class=\"pure-button\" href=\"/about\">About</a>
                            </li>
                        </ul>
                    </nav>

                    <p><center>
                        <a href=\"https://www.instagram.com/archiwyzard/\"><img src=\"../static/img/common/logo_instagram.jpg\" alt=\"logo instagram\" height=\"30px\" width=\"30px\" /></a>
                        <a href=\"https://www.deviantart.com/archiwyzard/\"><img src=\"../static/img/common/logo_deviantart.jpeg\" alt=\"logo deviantart\" height=\"30px\" width=\"30px\" /></a>
                        <a href=\"https://pixabay.com/users/sinason-14315822/\"><img src=\"../static/img/common/logo_pixabay.jpg\" alt=\"logo pixabay\" height=\"30px\" width=\"30px\" /></a>
                    <center></p>
                </div>
            </div>
            
            
<div class=\"content pure-u-1 pure-u-md-3-4\">

    <header class=\"ScriptHeader\">
            <div class=\"col-rt-12\">
                    <div class=\"rt-heading\">
                    <h1>Bee Abeille Prunus Alpes Alps</h1>
                </div>
            </div>
    </header>
    
    <div class=\"photo-box pure-u-1 pure-u-md-1-1 pure-u-lg-1-1\">
    <img width=100% height=100% src=\"$tab[$index]\" alt=\"$desc[$index]\">
    </div>
    
<div> <!-- End div pure blabla -->
            
                        <div class=\"footer\">
                            <p>Copyright &copy; Alexandre Proux </p>
                        </div>
                </div>
            </div>
        </div>
    </body>
</html>\n";
    
    close(FILE_sheet);
}

sub createPic
{
    for (0..scalar(@tab)-1)
    {
        print FILE "     <input class=\"gallery__select\"  type=\"radio\" name=\"autogenerated\" id=\"".$_."\"/>\n";
    }
    print FILE "\n";
    print FILE "\n";
    print FILE "    <div class=\"gallery\">\n";
    for my $i (0..scalar(@tab)-1)
    {
        my $name = $i;
        if ($tab[$i] =~ /\/([\w\_\d]+_by_archiwyzard)/i)
        {
            $name = $1;
            $name .= "_".$i;    
        }
        print FILE "         <label class=\"gallery__item\" for=\"".$i."\">\n"; 
        print FILE "             <a href=\"/sheet_$name\" target=\"_blank\">\n";
        print FILE "             <img class=\"cover\" height=100% width=100% min-height=\"50px\" src=\"".$tab[$i]."\" alt=\"".$desc[$i]."\"></a>\n";
        print FILE "         </label>\n";
        
        #### Generate file HTML for picture
        autoHTML($name, $i);
    }
    print FILE "    </div> <!-- End div classe gallery -->\n";
}