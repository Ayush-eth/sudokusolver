for(char k='1';k<='9';k++){
    if(isSafe(board,i,j,k)){
        board[i][j]=k;                   
        if(solve(board)){
            return true;
        }
        else{
            board[i][j]='.';
        }
    }
}