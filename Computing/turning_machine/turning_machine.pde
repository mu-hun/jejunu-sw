enum Mode { INITTAPE, INITPOS, EXECUTE, HALT, FAIL }
enum Step { STARTED, READ, WRITTEN, MOVED, HALTED, FAILED } 
enum Focus { NONE, TAPE, CELL, STEP, RESET, CYCLE, RUN }
final int gap = 50;
final int hCell = 100;
final int wCell = 60;
final int maxCells = 12;
final int wButton = 120;
final String stateLabel = "CONTROLLER STATE";
final String initLabel = "INIT";
final String startLabel = "START";
final String prevLabel = "PREV";
final String curLabel = "CUR";
final String haltLabel = "HALT";
final char BLANK = '*';
Mode curMode = Mode.INITTAPE;
String startState;
String haltState;
String curState;
String commNext;
char commOutput;
char commMove;
int startCell;
int prevCell;
int curCell;
boolean commExists;
boolean displayPrev;
boolean foundFocus;
Focus curFocus;
int focussedCell = -1;
Step curStep;
int inputIndex;
final color focusColor = color(250, 250, 0);
final color highlightColor = color(0, 255, 0);

char[] curTape, startTape, prevTape;
Table table;

void setup()
{
    size(990, 650);
    textSize(32);
    startTape = new char[maxCells];    
    prevTape = new char[maxCells];    
    curTape = new char[maxCells];    
    table = loadTable("turing_1.csv", "header");
    TableRow row = table.getRow(0);
    startState = row.getString("cur");
    haltState = row.getString("next");
    table.removeRow(0);
    reset();
}

void draw()
{
    background(240, 240, 230);
    if (curMode != Mode.INITTAPE) {
        displayControllerState();
        drawTape(startTape, startLabel, gap, 2 * gap + hCell);
        if (curMode == Mode.EXECUTE || curMode == Mode.HALT) {
            if (displayPrev)
                drawTape(prevTape, prevLabel, gap, 3 * gap + 2 * hCell);
            if (curState.equals(haltState))
                drawTape(curTape, haltLabel, gap, 4 * gap + 3 * hCell);
            else
                drawTape(curTape, curLabel, gap, 4 * gap + 3 * hCell);
        }
    } else
        drawInitTape();

    drawButtons();
}

void reset()
{
    curMode = Mode.INITTAPE;
    curState = startState;
    startCell = -1;
    prevCell = -1;
    curCell = 0;
    commExists = false;
    displayPrev = false;
    foundFocus = false;
    curFocus = Focus.NONE ;
    focussedCell = -1;
    curStep = Step.STARTED;
    inputIndex = 0;
}

void getCommand()
{
    commExists = true;
    for (TableRow comm : table.findRows(curState, "cur"))
        if (comm.getString("in").charAt(0) == curTape[curCell]) {
            commOutput = comm.getString("out").charAt(0);
            commMove = comm.getString("move").charAt(0);;
            commNext = comm.getString("next");
            return;
        }
    commExists = false;
}

void takeReadStep()
{
    fill(highlightColor);
    rect(gap + 3 * wCell, gap, 3 * wCell, hCell);
    text(curTape[curCell], gap + 4 * wCell, gap + hCell / 2);
    curStep = Step.READ;
}

void takeWriteStep()
{
    curTape[curCell] = commOutput;
    curStep = Step.WRITTEN;
}

void takeMoveStep()
{
    if (commMove == 'L')
        curCell--;
    else if (commMove == 'R')
        curCell++;
    curStep = Step.MOVED;    
}

void takeChangeStep()
{
    curState = commNext;
    if (curState.equals(haltState)) {
        curMode = Mode.HALT;
        curStep = Step.HALTED;
        commExists = false;
    } else {
        getCommand();
        if (!commExists) {
            curMode = Mode.FAIL;
            curStep = Step.FAILED;          
        }  else
            curStep = Step.STARTED;
    }
}

void displayControllerState()
{
    textAlign(LEFT, BASELINE);
    fill(0);
    text(stateLabel, gap, gap - 10);
    if (curStep == Step.STARTED)
        fill(highlightColor);
    else
        fill(255);
    rect(gap, gap, 3 * wCell, hCell);
    if (curStep == Step.READ)
        fill(highlightColor);
    else
        fill(255);
    rect(gap + 3 * wCell, gap, 2 * wCell, hCell);
    if (curStep == Step.WRITTEN)
        fill(highlightColor);
    else
        fill(255);
    rect(gap + 5 * wCell, gap, 2 * wCell, hCell);
    if (curStep == Step.MOVED)
        fill(highlightColor);
    else
        fill(255);
    rect(gap + 7 * wCell, gap, 2 * wCell, hCell);
    fill(255);
    rect(gap + 9 * wCell, gap, 3 * wCell, hCell);

    textAlign(CENTER, CENTER);
    fill(0);
    text(curState, gap + wCell * 3 / 2, gap + hCell / 2);
    if (commExists) {
        text(curTape[curCell], gap + 4 * wCell, gap + hCell / 2);
        text(commOutput, gap + 6 * wCell, gap + hCell / 2);
        text(commMove, gap + 8 * wCell, gap + hCell / 2);
        text(commNext, gap + wCell * 21 / 2, gap + hCell / 2);
    }
}

void drawInitTape()
{
    textAlign(LEFT, BASELINE);
    fill(0);
    text(initLabel, gap, 2 * gap + hCell - 10);
    fill(focusColor);
    rect(gap, 2 * gap + hCell, 12 * wCell, hCell);
    fill(0);
    textAlign(LEFT, CENTER);
    text(curTape, 0, inputIndex, gap + 20, 2 * gap + hCell * 3 / 2);
}

void drawTape(char[] tape, String title, float x, float y)
{
    textAlign(LEFT, BASELINE);
    fill(0);
    text(title, x, y - 10);
    fill(255);
    textAlign(CENTER, CENTER);
    for (int i = 0; i < maxCells; i++, x += wCell) {
        if (curMode == Mode.INITPOS && i == focussedCell)
            fill(focusColor);
        else if (title.equals(startLabel) && i == startCell
            || title.equals(prevLabel) && i == prevCell
            || title.equals(curLabel) && i == curCell
            || title.equals(haltLabel) && i == curCell)
            fill(highlightColor);
        else
            fill(255);
        rect(x, y, wCell, hCell);
        fill(0);
        text(tape[i], x + wCell / 2, y + hCell / 2);
    }
}

void drawButtons()
{
    textAlign(CENTER, CENTER);
    if (curMode != Mode.HALT && curMode != Mode.FAIL && curFocus == Focus.STEP)
        fill(focusColor);
    else
        fill(200);
    rect(2 * gap + 12 * wCell, gap, wButton, hCell);
    if (curFocus == Focus.RESET)
        fill(focusColor);
    else
        fill(200);
    rect(2 * gap + 12 * wCell, 2 * gap + hCell, wButton, hCell);
    if (curMode != Mode.HALT && curMode != Mode.FAIL && curFocus == Focus.CYCLE)
        fill(focusColor);
    else
        fill(200);
    rect(2 * gap + 12 * wCell, 3 * gap + 2 * hCell, wButton, hCell);
    if (curMode != Mode.HALT && curMode != Mode.FAIL && curFocus == Focus.RUN)
        fill(focusColor);
    else
        fill(200);
    rect(2 * gap + 12 * wCell, 4 * gap + 3 * hCell, wButton, hCell);
    fill(0);
    text("STEP", 2 * gap + 12 * wCell + wButton / 2, gap + hCell / 2);
    text("RESET", 2 * gap + 12 * wCell + wButton / 2, 2 * gap + 3 * hCell / 2);
    text("CYCLE", 2 * gap + 12 * wCell + wButton / 2, 3 * gap + 5 * hCell / 2);
    text("RUN", 2 * gap + 12 * wCell + wButton / 2, 4 * gap + 7 * hCell / 2);
}

void copyTape(char[] dest, char[] src)
{
    for (int i = 0; i < maxCells; i++)
        dest[i] = src[i];
}

boolean isOnRESET()
{
    if (mouseX >= 2 * gap + 12 * wCell && mouseX <= 2 * gap + 12 * wCell + wButton
        && mouseY >= 2 * gap + hCell && mouseY <= 2 * gap + 2 * hCell)
        return true;
    return false;
}

boolean isOnSTEP()
{
    if (mouseX >= 2 * gap + 12 * wCell && mouseX <= 2 * gap + 12 * wCell + wButton
        && mouseY >= gap && mouseY <= gap + hCell)
        return true;
    return false;
}

boolean isOnCYCLE()
{
    if (mouseX >= 2 * gap + 12 * wCell && mouseX <= 2 * gap + 12 * wCell + wButton
        && mouseY >= 3 * gap + 2 * hCell && mouseY <= 3 * gap + 3 * hCell)
        return true;
    return false;
}

boolean isOnRUN()
{
    if (mouseX >= 2 * gap + 12 * wCell && mouseX <= 2 * gap + 12 * wCell + wButton
        && mouseY >= 4 * gap + 3 * hCell && mouseY <= 4 * gap + 4 * hCell)
        return true;
    return false;
}

void mouseMoved()
{
    curFocus = Focus.NONE;
    if (isOnRESET())
        curFocus = Focus.RESET;
    else if (curMode == Mode.INITPOS) {
        if (mouseX >= gap && mouseX <= gap + 12 * wCell
            && mouseY >= 2 * gap + hCell && mouseY <= 2 * gap + 2 * hCell) {
            curFocus = Focus.CELL;
            focussedCell = (mouseX - gap) / wCell;
        } else {
            curFocus = Focus.NONE;
            focussedCell = -1;
        }
    } else if (curMode == Mode.EXECUTE) {
        if (!commExists)
            curFocus = Focus.NONE;
        else if (isOnSTEP())
            curFocus = Focus.STEP;
        else if (curStep == Step.STARTED) {
            if (isOnCYCLE())
                curFocus = Focus.CYCLE;
            else if (isOnRUN())
                curFocus = Focus.RUN;
        }       
    }
}

void mouseClicked()
{
    if (curFocus == Focus.NONE)
        return;
    if (curFocus == Focus.CELL) {
        startCell = curCell = focussedCell;
        if (mouseButton == LEFT) {
            curMode = Mode.EXECUTE;
            curStep = Step.STARTED;
        }
        getCommand();
    } else if (curFocus == Focus.STEP) {
        displayPrev = true;
        if (curStep == Step.STARTED) {
            takeReadStep();
            copyTape(prevTape, curTape);
            prevCell = curCell;
        } else if (curStep == Step.READ)
            takeWriteStep();
        else if (curStep == Step.WRITTEN)
            takeMoveStep();
        else 
            takeChangeStep();
    } else if (curFocus == Focus.RESET) {
        reset();
    } else if (curFocus == Focus.CYCLE) {
        displayPrev = true;
        copyTape(prevTape, curTape);
        prevCell = curCell;
        takeReadStep();
        takeWriteStep();
        takeMoveStep();
        takeChangeStep();        
    } else if (curFocus == Focus.RUN) {
        displayPrev = false;
        while (curMode == Mode.EXECUTE) {
            takeReadStep();
            takeWriteStep();
            takeMoveStep();
            takeChangeStep();
        }
    } 
}

void keyReleased()
{
    if (curMode == Mode.INITTAPE) {
        if (key == BACKSPACE) {
            if (inputIndex > 0)
                inputIndex--;
        } else if (key == ENTER && inputIndex > 0) {
            curMode = Mode.INITPOS;
            int t = (maxCells - inputIndex) / 2;
            if (t > 0) {
                int i;
                for (i = maxCells - 1; i >= inputIndex + t; i--)
                    curTape[i] = BLANK;
                for ( ; i >= t; i--)
                    curTape[i] = curTape[i - t];
                for ( ; i >= 0; i--)
                    curTape[i] = BLANK;
            }
            copyTape(startTape, curTape); 
        } else if (inputIndex < maxCells) {
            curTape[inputIndex] = key;
            inputIndex++;
        }
    }
}