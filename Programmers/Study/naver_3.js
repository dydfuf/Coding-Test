function solution(block,board) {
    var answer = -1;

    let available = []
    switch(block){

        case 0:
            available = case_0(board)
            break
        case 1:
            available = case_1(board)
            break
        case 2:
            available = case_2(board)
            break
        case 3:
            available = case_3(board)
            break
        case 4:
            available = case_4(board)
            break
        case 5:
            available = case_5(board)
            break
        default:
            break
    }
    let clear_lines = []
    for(let i = 0; i < available.length; i+=1){
        let temp_board = JSON.parse(JSON.stringify( board ))
        let put_block_board = putBlock(available[i], block, temp_board)
        console.log(clear_row(put_block_board))
        clear_lines.push(clear_row(put_block_board))
    }
    answer = Math.max(...clear_lines)
    return answer;
}

//* 0번 블록일때 놓을 수 있는 위치 찾기
function case_0(board){
    let arr = []
    for(let i = 0; i < board.length; i += 1){
        for(let j = 0; j < board.length; j += 1){
            if(board[i][j] === 0){
                if(board[i+1] !== undefined && board[i+2] !== undefined){
                    if(board[i+1][j] === 0 && board[i+2][j] === 0){
                        arr.push([i,j])
                    }
                }
            }
        }
    }
    return arr
}

//* 1번 블록일때 놓을 수 있는 위치 찾기
function case_1(board){
    let arr = []
    for(let i = 0; i < board.length; i += 1){
        for(let j = 0; j < board.length; j += 1){
            if(board[i][j] === 0){
                if(board[i][j+1] === 0 && board[i][j+2] === 0){
                    arr.push([i,j])
                }
            }

        }
    }
    return arr
}

//* 2번 블록일때 놓을 수 있는 위치 찾기
function case_2(board){
    let arr = []
    for(let i = 0; i < board.length; i += 1){
        for(let j = 0; j < board.length; j += 1){
            if(board[i][j] === 0){
                if(board[i+1] !== undefined){
                    if(board[i+1][j] === 0 && board[i+1][j+1] === 0){
                        arr.push([i,j])
                    }
                }

            }

        }
    }
    return arr
}

//* 3번 블록일때 놓을 수 있는 위치 찾기
function case_3(board){
    let arr = []
    for(let i = 0; i < board.length; i += 1){
        for(let j = 0; j < board.length; j += 1){
            if(board[i][j] === 0){
                if(board[i+1] !== undefined){
                    if(board[i+1][j] === 0 && board[i+1][j-1] === 0){
                        arr.push([i,j])
                    }
                }

            }

        }
    }
    return arr
}

//* 4번 블록일때 놓을 수 있는 위치 찾기
function case_4(board){
    let arr = []
    for(let i = 0; i < board.length; i += 1){
        for(let j = 0; j < board.length; j += 1){
            if(board[i][j] === 0){
                if(board[i+1] !== undefined){
                    if(board[i][j+1] === 0 && board[i+1][j+1] === 0){
                        arr.push([i,j])
                    }
                }

            }

        }
    }
    return arr
}

//* 5번 블록일때 놓을 수 있는 위치 찾기
function case_5(board){
    let arr = []
    for(let i = 0; i < board.length; i += 1){
        for(let j = 0; j < board.length; j += 1){
            if(board[i][j] === 0){
                if(board[i+1] !== undefined){
                    if(board[i+1][j] === 0 && board[i][j+1] === 0){
                        arr.push([i,j])
                    }
                }

            }

        }
    }
    return arr
}

//* 블록 놓기 @return 놓아진 board
function putBlock(index, blockType, board){
    let i = index[0]
    let j = index[1]
    switch(blockType){
        case 0:
            board[i][j] = 1
            board[i+1][j] = 1
            board[i+2][j] = 1
            break
        case 1:
            board[i][j] = 1
            board[i][j+1] = 1
            board[i][j+2] = 1
            break
        case 2:
            board[i][j] = 1
            board[i+1][j] = 1
            board[i+1][j+1] = 1
            break
        case 3:
            board[i][j] = 1
            board[i+1][j] = 1
            board[i+1][j-1] = 1
            break
        case 4:
            board[i][j] = 1
            board[i][j+1] = 1
            board[i+1][j+1] = 1
            break
        case 5:
            board[i][j] = 1
            board[i][j+1] = 1
            board[i+1][j] = 1
            break
        default:
            break
    }
    return board
}

//* 몇줄이 사라지는지 구하는 함수 @return number
function clear_row(board){
    let rows = 0
    for(let i = 0; i < board.length; i+= 1){
        let sum = 0
        for(let j = 0; j <board.length; j += 1){
            sum += board[i][j]
        }
        if(sum === board.length){
            rows += 1
        }
    }
    return rows
}