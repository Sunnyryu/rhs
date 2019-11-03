shoter = shotchartdetail.ShotChartDetail(league_id="00",team_id="0", player_id="201939", season_nullable="")
  # season_nullable을 ""로 하는 것은 전체 커리어를 보기 위해서 임
  shotframe = shoter.get_data_frames()
  shotdata = shotframe[0]
  with pd.option_context('display.max_columns', None):
      display(shotdata.head())

  sns.set_style("white")
  sns.set_color_codes()
  def draw_court(ax=None, color='black', lw=2, outer_lines=False):
      # 코트를 그리기 위한 함수
      if ax is None:
          ax = plt.gca()
      hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)

      backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)

      outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color,
                            fill=False)
      inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color,
                            fill=False)

      top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                           linewidth=lw, color=color, fill=False)
      bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                              linewidth=lw, color=color, linestyle='dashed')
      restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
                       color=color)
      corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw,
                                 color=color)
      corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)

      three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw,
                      color=color)
      center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                             linewidth=lw, color=color)
      center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                             linewidth=lw, color=color)
      court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                        bottom_free_throw, restricted, corner_three_a,
                        corner_three_b, three_arc, center_outer_arc,
                        center_inner_arc]

      if outer_lines:
          outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw,
                                  color=color, fill=False)
          court_elements.append(outer_lines)
      for element in court_elements:
          ax.add_patch(element)

      return ax

  draw_court(outer_lines=True)
  plt.xlim(-300,300)
  plt.ylim(-100,500)
  draw_court(outer_lines=True)
  plt.xlim(300,-300)
  draw_court()
  plt.xlim(-250,250)
  plt.ylim(422.5, -47.5)
  joint_shot_chart = sns.jointplot(shotdata.LOC_X, shotdata.LOC_Y, stat_func=None,
                                   kind='scatter', space=0, alpha=0.5)

  joint_shot_chart.fig.set_size_inches(12,11)
  ax = joint_shot_chart.ax_joint
  draw_court(ax)

  ax.set_xlim(-250,250)
  ax.set_ylim(422.5, -47.5)

  ax.set_xlabel('')
  ax.set_ylabel('')
  ax.tick_params(labelbottom='off', labelleft='off')

  # 차트 위에 타이틀 추가
  ax.set_title('career shot graph',
               y=1.2, fontsize=18)
  # 차트에 내용 추가
  ax.text(-250,445,'Data Source: nba_api'
          '\nAuthor: curry',
          fontsize=12)

  a=plt.show()
  cmap=plt.cm.YlOrRd_r
  joint_shot_chart = sns.jointplot(shotdata.LOC_X, shotdata.LOC_Y, stat_func=None,
                                   kind='kde', space=0, color=cmap(0.1),
                                   cmap=cmap, n_levels=50)

  joint_shot_chart.fig.set_size_inches(12,11)
  ax = joint_shot_chart.ax_joint
  draw_court(ax)
  ax.set_xlim(-250,250)
  ax.set_ylim(422.5, -47.5)
  ax.set_xlabel('')
  ax.set_ylabel('')
  ax.tick_params(labelbottom='off', labelleft='off')
  ax.set_title('career shot graph',
               y=1.2, fontsize=18)

  ax.text(-250,445,'Data Source: nba_api'
          ,
          fontsize=12)
  b=plt.show()

  cmap=plt.cm.gist_heat_r
  joint_shot_chart = sns.jointplot(shotdata.LOC_X, shotdata.LOC_Y, stat_func=None,
                                   kind='hex', space=0, color=cmap(.2), cmap=cmap)

  joint_shot_chart.fig.set_size_inches(12,11)

  ax = joint_shot_chart.ax_joint
  draw_court(ax)

  ax.set_xlim(-250,250)
  ax.set_ylim(422.5, -47.5)

  ax.set_xlabel('')
  ax.set_ylabel('')
  ax.tick_params(labelbottom='off', labelleft='off')


  ax.set_title('career shotchart', y=1.2, fontsize=14)

  ax.text(-250,445,'Data Source: nba_api', fontsize=12)
  c=plt.show()
