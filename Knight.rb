
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

  def self.valid_moves(pos)
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

  def initialize(start_pos)
    @start_pos = start_pos
    @considered = [start_pos]
    build_move_tree
  end 

  def find_path(end_pos)
    end_node = root_node.dfs(end_pos)
    trace_path_back(end_node).reverse.map(&:value)
  end

  private
  attr_accessor :root_node, :considered

  def build_move_tree 
    self.root_node = PolyTreeNode.new(start_pos)
    nodes = [root_node]
    until nodes.empty?
      current_node = nodes.shift
      current_pos = current_node.val 
      new_move_positions(current_pos).each do |next_pos|
        next_node = PolyTreeNode.new(next_pos)
        current_node.add_child(next_node)
        nodes << next_node
      end 
    end  
  end

  def new_move_positions(pos)
    Knight.valid_moves(pos)
    .reject {|new_pos| considered.include?(new_pos)}
    .each { |new_pos| considered << new_pos}
  end 

  def trace_path_back(end_node)
    nodes = []
    current_node = end_node
    until current_node.nil?
      nodes << current_node
      current_node = current_node.parent
    end 
    return nodes
  end 