
class Knight
  attr_reader :start_pos

  MOVES = [
    [-2, -1],
    [-2,  1],
    [-1, -2],
    [-1,  2],
    [ 1, -2],
    [ 1,  2],
    [ 2, -1],
    [ 2,  1]
  ]

  def valid_moves(pos)
    moves = []
    cur_x,cur_y = pos 
    MOVES.each do |dx,dy|
      new_pos = [cur_x + dx, cur_y + dy]
      if new_pos.all? {|coord| coord.between?(0,7)}
        moves << new_pos
      end 
    end 
    moves 
  end 

  